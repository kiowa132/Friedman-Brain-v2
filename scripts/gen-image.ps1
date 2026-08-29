<#
  gen-image.ps1 — AI image generation for Friedman Team reports.

  ENGINES:
    -Engine openai        (RECOMMENDED) gpt-image-1. Best at baked-in text,
                          logos, infographics, prompt adherence. ~$0.04/image
                          at -Quality medium. Supports -Ref reference images
                          (logo / property photo / headshot). Needs
                          OPENAI_API_KEY in scripts/.env (billing on).
    -Engine pollinations  (DEFAULT) 100% free, no key. Flux-schnell — fine
                          for atmospheric background art only. No text, no
                          logos, ~1000px, no -Ref.
    -Engine gemini        gemini-2.5-flash-image. Strong on reference photos
                          and faces. ~$0.03/image, needs a billing-enabled
                          GEMINI_API_KEY. (Free tier is limit:0 for images.)

  USAGE (openai — the one to use):
    powershell -File "Friedman Brain/scripts/gen-image.ps1" -Engine openai `
      -Prompt "Wide 16:9 editorial banner ..." `
      -Ref "brand-assets/logo.png","brand-assets/swatch.png" `
      -Out "properties/8303-bellona/generated/hero.png"

  PARAMS:
    -Prompt / -PromptFile   prompt text, or a path to a .txt prompt
    -Out                    output .png path (folders auto-created)
    -Engine                 openai | pollinations (default) | gemini
    -Ref                    0-4 local image paths (openai + gemini)
    -Quality                low | medium (default) | high   (openai only;
                            ~$0.01 / ~$0.04 / ~$0.17 per landscape image)
    -Size                   openai: 1536x1024 (default) | 1024x1024 | 1024x1536
    -Width / -Height        pollinations only (default 1792x1024)
    -Model                  override the model id
#>

[CmdletBinding()]
param(
  [string]$Prompt,
  [string]$PromptFile,
  [Parameter(Mandatory = $true)][string]$Out,
  [ValidateSet("openai", "pollinations", "gemini")][string]$Engine = "pollinations",
  [string[]]$Ref = @(),
  [ValidateSet("low", "medium", "high")][string]$Quality = "medium",
  [string]$Size = "1536x1024",
  [int]$Width = 1792,
  [int]$Height = 1024,
  [string]$Model,
  [string]$CropAspect   # e.g. "3:1", "21:9", "16:9" — center-crops the result to a thinner banner
)

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot  = Split-Path -Parent $scriptDir
function Resolve-RepoPath([string]$p) {
  if ([System.IO.Path]::IsPathRooted($p)) { return $p } else { return (Join-Path $repoRoot $p) }
}
function Read-EnvKey([string]$name) {
  $v = [Environment]::GetEnvironmentVariable($name)
  if (-not $v) {
    $envFile = Join-Path $scriptDir ".env"
    if (Test-Path $envFile) {
      Get-Content $envFile | ForEach-Object {
        if ($_ -match "^\s*$name\s*=\s*(.+?)\s*$") { $v = $matches[1].Trim('"').Trim("'") }
      }
    }
  }
  return $v
}
$mimeByExt = @{ ".jpg" = "image/jpeg"; ".jpeg" = "image/jpeg"; ".png" = "image/png"; ".webp" = "image/webp" }

function Invoke-CenterCrop([string]$path, [string]$aspect) {
  if (-not $aspect) { return }
  $parts = $aspect -split "[:x/]"
  if ($parts.Count -ne 2) { Write-Warning "Bad -CropAspect '$aspect'; skipping crop."; return }
  $tr = [double]$parts[0] / [double]$parts[1]
  Add-Type -AssemblyName System.Drawing
  $bytes = [IO.File]::ReadAllBytes($path)
  $ms = New-Object IO.MemoryStream(, $bytes)
  $img = [System.Drawing.Image]::FromStream($ms)
  $sw = $img.Width; $sh = $img.Height; $sr = $sw / $sh
  if ($sr -gt $tr) { $nw = [int]([math]::Round($sh * $tr)); $nh = $sh } else { $nw = $sw; $nh = [int]([math]::Round($sw / $tr)) }
  $x = [int](($sw - $nw) / 2); $y = [int](($sh - $nh) / 2)
  $bmp = New-Object System.Drawing.Bitmap($nw, $nh)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $g.DrawImage($img, (New-Object System.Drawing.Rectangle(0, 0, $nw, $nh)), (New-Object System.Drawing.Rectangle($x, $y, $nw, $nh)), [System.Drawing.GraphicsUnit]::Pixel)
  $img.Dispose(); $ms.Dispose()
  $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
  $g.Dispose(); $bmp.Dispose()
  Write-Output "    cropped to $aspect -> ${nw}x${nh}"
}

if ($PromptFile) { $Prompt = Get-Content (Resolve-RepoPath $PromptFile) -Raw }
if (-not $Prompt) { Write-Error "Provide -Prompt or -PromptFile." }
$outPath = Resolve-RepoPath $Out
$outDir  = Split-Path -Parent $outPath
if ($outDir -and -not (Test-Path $outDir)) { New-Item -ItemType Directory -Force -Path $outDir | Out-Null }

# ======================================================================
# Engine: openai  (gpt-image-1)
# ======================================================================
if ($Engine -eq "openai") {
  $key = Read-EnvKey "OPENAI_API_KEY"
  if (-not $key) { Write-Error "openai engine needs OPENAI_API_KEY in scripts/.env" }
  if (-not $Model) { $Model = "gpt-image-1" }
  $headers = @{ Authorization = "Bearer $key" }
  $full = "$Prompt`n`nWide 16:9 horizontal composition. Every visible word spelled correctly. No watermark."

  $refPaths = @()
  foreach ($r in $Ref) {
    if ($refPaths.Count -ge 4) { Write-Warning "Ignoring 5th+ reference '$r'."; continue }
    $rp = Resolve-RepoPath $r
    if (-not (Test-Path $rp)) { Write-Error "Reference not found: $rp" }
    if (-not $mimeByExt[[System.IO.Path]::GetExtension($rp).ToLower()]) { Write-Error "Unsupported ref type: $rp" }
    $refPaths += $rp
  }

  if ($refPaths.Count -eq 0) {
    # ---- text-to-image: POST /v1/images/generations (JSON) ----
    $body = @{ model = $Model; prompt = $full; size = $Size; quality = $Quality; n = 1 } | ConvertTo-Json -Depth 6
    $resp = Invoke-RestMethod -Uri "https://api.openai.com/v1/images/generations" -Method Post `
      -Headers $headers -ContentType "application/json" -Body $body -TimeoutSec 300
  }
  else {
    # ---- with references: POST /v1/images/edits (manual multipart) ----
    $boundary = [Guid]::NewGuid().ToString()
    $LF = "`r`n"
    $ms = New-Object System.IO.MemoryStream
    function Write-Str($s) { $b = [Text.Encoding]::UTF8.GetBytes($s); $ms.Write($b, 0, $b.Length) }
    function Add-Field($n, $v) { Write-Str "--$boundary$LF"; Write-Str "Content-Disposition: form-data; name=`"$n`"$LF$LF"; Write-Str "$v$LF" }
    Add-Field "model"   $Model
    Add-Field "prompt"  $full
    Add-Field "size"    $Size
    Add-Field "quality" $Quality
    Add-Field "n"       "1"
    foreach ($rp in $refPaths) {
      $bytes = [IO.File]::ReadAllBytes($rp)
      $fn = [IO.Path]::GetFileName($rp)
      $mime = $mimeByExt[[IO.Path]::GetExtension($rp).ToLower()]
      Write-Str "--$boundary$LF"
      Write-Str "Content-Disposition: form-data; name=`"image[]`"; filename=`"$fn`"$LF"
      Write-Str "Content-Type: $mime$LF$LF"
      $ms.Write($bytes, 0, $bytes.Length)
      Write-Str $LF
    }
    Write-Str "--$boundary--$LF"
    $resp = Invoke-RestMethod -Uri "https://api.openai.com/v1/images/edits" -Method Post `
      -Headers $headers -ContentType "multipart/form-data; boundary=$boundary" -Body $ms.ToArray() -TimeoutSec 300
    $ms.Dispose()
  }

  $b64 = $resp.data[0].b64_json
  if (-not $b64) { Write-Error ("No image in response: " + ($resp | ConvertTo-Json -Depth 6)) }
  [IO.File]::WriteAllBytes($outPath, [Convert]::FromBase64String($b64))
  Invoke-CenterCrop $outPath $CropAspect
  $kb = [math]::Round((Get-Item $outPath).Length / 1KB)
  Write-Output "OK  $outPath  ($kb KB, engine: openai/$Model $Quality, refs: $($refPaths.Count))"
  return
}

# ======================================================================
# Engine: pollinations  (free)
# ======================================================================
if ($Engine -eq "pollinations") {
  if ($Ref.Count -gt 0) { Write-Warning "-Ref is ignored on pollinations (text-to-image only)." }
  if (-not $Model) { $Model = "flux" }
  $full = "$Prompt. Wide horizontal composition. Correctly spelled text. No watermark."
  $enc  = [Uri]::EscapeDataString($full)
  $seed = Get-Random -Minimum 1 -Maximum 999999
  $uri  = "https://image.pollinations.ai/prompt/$enc`?width=$Width&height=$Height&model=$Model&nologo=true&enhance=true&seed=$seed"
  $ok = $false
  for ($attempt = 1; $attempt -le 3; $attempt++) {
    try {
      Invoke-WebRequest -Uri $uri -OutFile $outPath -TimeoutSec 180 -UseBasicParsing
      if ((Get-Item $outPath).Length -gt 3000) { $ok = $true; break }
      Write-Warning "Attempt $attempt returned a tiny file; retrying..."
    } catch { Write-Warning "Attempt $attempt failed ($($_.Exception.Message)); retry in 15s..." }
    Start-Sleep -Seconds 15
  }
  if (-not $ok) { Write-Error "Pollinations gave no usable image after 3 tries." }
  Invoke-CenterCrop $outPath $CropAspect
  $kb = [math]::Round((Get-Item $outPath).Length / 1KB)
  Write-Output "OK  $outPath  ($kb KB, engine: pollinations/$Model)"
  return
}

# ======================================================================
# Engine: gemini  (needs billing)
# ======================================================================
$key = Read-EnvKey "GEMINI_API_KEY"
if (-not $key) { Write-Error "gemini engine needs GEMINI_API_KEY in scripts/.env" }
if (-not $Model) { $Model = "gemini-2.5-flash-image" }
$fullPrompt = "$Prompt`n`nOutput a single wide 16:9 horizontal image. All visible text spelled correctly. No watermark."
$parts = @( @{ text = $fullPrompt } )
$refCount = 0
foreach ($r in $Ref) {
  if ($refCount -ge 4) { Write-Warning "Ignoring 5th+ reference '$r'."; continue }
  $rp = Resolve-RepoPath $r
  if (-not (Test-Path $rp)) { Write-Error "Reference not found: $rp" }
  $mime = $mimeByExt[[IO.Path]::GetExtension($rp).ToLower()]; if (-not $mime) { Write-Error "Unsupported ref type." }
  $parts += @{ inline_data = @{ mime_type = $mime; data = [Convert]::ToBase64String([IO.File]::ReadAllBytes($rp)) } }
  $refCount++
}
$body = @{ contents = @( @{ parts = $parts } ); generationConfig = @{ responseModalities = @("TEXT", "IMAGE") } } |
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
[IO.File]::WriteAllBytes($outPath, [Convert]::FromBase64String($imgPart.data))
Invoke-CenterCrop $outPath $CropAspect
$kb = [math]::Round((Get-Item $outPath).Length / 1KB)
Write-Output "OK  $outPath  ($kb KB, engine: gemini, refs: $refCount)"
