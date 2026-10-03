@echo off
REM Harvest the Singapore consolidated Acts inside the 03:00-07:00 SGT window
REM that SSO's Terms of Use cl.13(d)(i) requires. Driven by the Windows
REM scheduled task "canon-sso-harvest"; safe to run by hand as well.
REM
REM pdftotext ships with Git for Windows but is not on the Task Scheduler PATH,
REM so it is added here explicitly. Without it the script exits immediately.
setlocal
set "PATH=%PATH%;C:\Program Files\Git\mingw64\bin"
cd /d "C:\Users\micha\canon"

if not exist "logs" mkdir "logs"
set "LOG=logs\sso-harvest-%DATE:~-4%%DATE:~4,2%%DATE:~7,2%.log"

echo ==== run started %DATE% %TIME% ==== >> "%LOG%"
"C:\Python312\python.exe" -u "tools\fetch-sso-corpus.py" ^
    --manifest "tools\sso-acts-manifest.json" ^
    --out "subjects\singapore" >> "%LOG%" 2>&1
set RC=%ERRORLEVEL%
echo ==== run finished %DATE% %TIME% exit=%RC% ==== >> "%LOG%"
exit /b %RC%
