<#
  gen-image.ps1 — AI image generation for Friedman Team reports.

  TWO ENGINES:
    -Engine pollinations   (DEFAULT) — 100% free, no key, no billing.
                           Flux-schnell quality: good for atmospheric
                           backgrounds / concept art. Weak at baked-in
                           text + logos. Text-to-image only (no -Ref).
    -Engine gemini         gemini-2.5-flash-image. Top quality, supports
                           -Ref reference photos. NOT free — needs a
                           billing-enabled Google key (~$0.03-0.04/image).
                           Reads GEMINI_API_KEY from scripts/.env.

  USAGE (free):
    powershell -File scripts/gen-image.ps1 `
      -Prompt "Wide 16:9 editorial banner, ..." `
      -Out "properties/8303-bellona/generated/section-tax.png"

  USAGE (gemini, needs billing):
    powershell -File scripts/gen-image.ps1 -Engine gemini `
      -Prompt "..." -Ref "brand-assets/logo.png","properties/8303-bellona/photos/front.jpg" `
      -Out "properties/8303-bellona/generated/hero.png"

  PARAMS:
    -Prompt / -PromptFile   the prompt (text or a .txt path)
    -Out                    output .png/.jpg path (folders auto-created)
    -Engine                 pollinations (default) | gemini
    -Ref                    0-4 local image paths (gemini only)
    -Width / -Height        default 1792 x 1024 (16:9)
    -Model                  override the model id
#>

[CmdletBinding()]
param(
  [string]$Prompt,
  [string]$PromptFile,
  [Parameter(Mandatory = $true)][string]$Out,
  [ValidateSet("pollinations", "gemini")][string]$Engine = "pollinations",
  [string[]]$Ref = @(),
  [int]$Width = 1792,
  [int]$Height = 1024,
  [string]$Model
)

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot  = Split-Path -Parent $scriptDir
function Resolve-RepoPath([string]$p) {
  if ([System.IO.Path]::IsPathRooted($p)) { return $p } else { return (Join-Path $repoRoot $p) }
}

if ($PromptFile) { $Prompt = Get-Content (Resolve-RepoPath $PromptFile) -Raw }
if (-not $Prompt) { Write-Error "Provide -Prompt or -PromptFile." }

$outPath = Resolve-RepoPath $Out
$outDir  = Split-Path -Parent $outPath
if ($outDir -and -not (Test-Path $outDir)) { New-Item -ItemType Directory -Force -Path $outDir | Out-Null }

# ======================================================================
if ($Engine -eq "pollinations") {
  if ($Ref.Count -gt 0) { Write-Warning "-Ref is ignored on the free pollinations engine (text-to-image only)." }
  if (-not $Model) { $Model = "flux" }
  $full = "$Prompt. Wide horizontal composition. Correctly spelled text. No watermark."
  $enc  = [System.Uri]::EscapeDataString($full)
  if ($enc.Length -gt 1800) { Write-Warning "Prompt is long; pollinations may truncate it." }
  $seed = Get-Random -Minimum 1 -Maximum 999999
  $uri  = "https://image.pollinations.ai/prompt/$enc`?width=$Width&height=$Height&model=$Model&nologo=true&enhance=true&seed=$seed"
  $ok = $false
  for ($attempt = 1; $attempt -le 3; $attempt++) {
    try {
      Invoke-WebRequest -Uri $uri -OutFile $outPath -TimeoutSec 180 -UseBasicParsing
      if ((Get-Item $outPath).Length -gt 3000) { $ok = $true; break }
      Write-Warning "Attempt $attempt returned a tiny/empty file; retrying..."
    } catch {
      Write-Warning "Attempt $attempt failed ($($_.Exception.Message)); retrying in 15s..."
    }
    Start-Sleep -Seconds 15
  }
  if (-not $ok) { Write-Error "Pollinations did not return a usable image after 3 tries." }
  $kb = [math]::Round((Get-Item $outPath).Length / 1KB)
  Write-Output "OK  $outPath  ($kb KB, engine: pollinations/$Model)"
  return
}

# ======================================================================
# Engine: gemini  (needs a billing-enabled key)
$key = $env:GEMINI_API_KEY
$envFile = Join-Path $scriptDir ".env"
if (-not $key -and (Test-Path $envFile)) {
  Get-Content $envFile | ForEach-Object {
    if ($_ -match '^\s*GEMINI_API_KEY\s*=\s*(.+?)\s*$') { $key = $matches[1].Trim('"').Trim("'") }
  }
}
if (-not $key) { Write-Error "gemini engine needs GEMINI_API_KEY in scripts/.env" }
if (-not $Model) { $Model = "gemini-2.5-flash-image" }

$fullPrompt = "$Prompt`n`nOutput a single wide 16:9 horizontal image. All visible text spelled correctly. No watermark."
$parts = @( @{ text = $fullPrompt } )
$mimeByExt = @{ ".jpg"="image/jpeg"; ".jpeg"="image/jpeg"; ".png"="image/png"; ".webp"="image/webp" }
$refCount = 0
foreach ($r in $Ref) {
  if ($refCount -ge 4) { Write-Warning "Ignoring 5th+ reference '$r'."; continue }
  $rp = Resolve-RepoPath $r
  if (-not (Test-Path $rp)) { Write-Error "Reference not found: $rp" }
  $ext = [System.IO.Path]::GetExtension($rp).ToLower()
  $mime = $mimeByExt[$ext]; if (-not $mime) { Write-Error "Unsupported ref type '$ext'." }
  $b64 = [Convert]::ToBase64String([System.IO.File]::ReadAllBytes($rp))
  $parts += @{ inline_data = @{ mime_type = $mime; data = $b64 } }
  $refCount++
}
$body = @{ contents = @( @{ parts = $parts } ); generationConfig = @{ responseModalities = @("TEXT","IMAGE") } } |
  ConvertTo-Json -Depth 12 -Compress
$uri = "https://generativelanguage.googleapis.com/v1beta/models/$Model`:generateContent?key=$key"

$resp = $null
for ($attempt = 1; $attempt -le 2; $attempt++) {
  try { $resp = Invoke-RestMethod -Uri $uri -Method Post -ContentType "application/json" -Body $body -TimeoutSec 180; break }
  catch {
    $code = $_.Exception.Response.StatusCode.value__
    if (($code -eq 429 -or $code -eq 503) -and $attempt -eq 1) { Write-Warning "HTTP $code; retry in 30s..."; Start-Sleep 30; continue }
    throw
  }
}
$imgPart = $null; $textParts = @()
foreach ($p in $resp.candidates[0].content.parts) {
  if ($p.inlineData -and $p.inlineData.data) { $imgPart = $p.inlineData } elseif ($p.text) { $textParts += $p.text }
}
if (-not $imgPart) { Write-Error ("No image returned. Model said: " + ($textParts -join " ")) }
[System.IO.File]::WriteAllBytes($outPath, [Convert]::FromBase64String($imgPart.data))
$kb = [math]::Round((Get-Item $outPath).Length / 1KB)
Write-Output "OK  $outPath  ($kb KB, engine: gemini, refs: $refCount)"
