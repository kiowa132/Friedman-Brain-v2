# keep-image.ps1 — promote a generated image to the committed final/ folder
# as a compressed JPEG, and log how it was made.
#
# Use only for images that shipped in a deliverable. generated/ is scratch.
#
#   powershell -File "Friedman Brain/scripts/keep-image.ps1" `
#     -From "properties/8303-bellona/generated/report-cover.png" `
#     -Property "8303-bellona" -As "sell-vs-rent-cover" `
#     -Prompt "the exact prompt used" -Note "sell-vs-rent Gamma cover"

param(
  [string]$From,
  [string]$Property,
  [string]$As,
  [int]$MaxW = 1600,
  [int]$Quality = 85,
  [string]$Prompt = "",
  [string]$Note = ""
)
$ErrorActionPreference = "Stop"
if (-not $From) { throw "Pass -From <generated image path>." }

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot  = Split-Path -Parent $scriptDir
$src = if ([IO.Path]::IsPathRooted($From)) { $From } else { Join-Path $repoRoot $From }
if (-not (Test-Path $src)) { throw "Not found: $src" }

if ($Property) { $finalDir = Join-Path $repoRoot ("properties/" + $Property + "/final") }
else { $finalDir = Join-Path (Split-Path -Parent (Split-Path -Parent $src)) "final" }
if (-not (Test-Path $finalDir)) { New-Item -ItemType Directory -Force $finalDir | Out-Null }

if (-not $As) { $As = [IO.Path]::GetFileNameWithoutExtension($src) }
$dst = Join-Path $finalDir ($As + ".jpg")

Add-Type -AssemblyName System.Drawing
$raw = [IO.File]::ReadAllBytes($src)
$mem = New-Object IO.MemoryStream(, $raw)
$img = [System.Drawing.Image]::FromStream($mem)
$w = $img.Width; $h = $img.Height
if ($w -gt $MaxW) { $nw = $MaxW; $nh = [int][math]::Round($h * $MaxW / $w) } else { $nw = $w; $nh = $h }
$bmp = New-Object System.Drawing.Bitmap($nw, $nh)
$gfx = [System.Drawing.Graphics]::FromImage($bmp)
$gfx.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$gfx.DrawImage($img, 0, 0, $nw, $nh)
$img.Dispose(); $mem.Dispose(); $gfx.Dispose()

$jpg = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
$prm = New-Object System.Drawing.Imaging.EncoderParameters(1)
$prm.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]$Quality)
$bmp.Save($dst, $jpg, $prm)
$bmp.Dispose()

$log = Join-Path (Split-Path -Parent $finalDir) "image-log.md"
if (-not (Test-Path $log)) { Set-Content -Path $log -Value "# Image log" -Encoding UTF8 }
$block = "`n## $As.jpg  (" + (Get-Date -Format "yyyy-MM-dd") + ")"
if ($Note)   { $block += "`n- Use: $Note" }
if ($Prompt) { $block += "`n- Prompt: $Prompt" }
Add-Content -Path $log -Value $block -Encoding UTF8

$kb = [math]::Round((Get-Item $dst).Length / 1KB)
Write-Output ("KEPT  " + $dst + "  (" + $kb + " KB, " + $nw + "x" + $nh + ")   logged -> " + $log)
