@echo off
REM Drag a FOLDER of photos onto this file in File Explorer.
REM It writes web-ready ~1-3 MB JPEGs to a "web" subfolder next to them.
REM Then upload that "web" folder through /admin.

if "%~1"=="" (
  echo.
  echo   Drag a folder of photos onto this .bat file.
  echo.
  pause
  exit /b 1
)

set PY=C:\Users\kylej\AppData\Local\Python\bin\python.exe
"%PY%" "%~dp0compress-photos.py" "%~1"
echo.
pause
