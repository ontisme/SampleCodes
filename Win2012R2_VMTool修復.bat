@echo off
:: 設定下載連結和檔名
set "url1=https://download.microsoft.com/download/2/1/E/21E26FC4-27A2-4330-90D0-938F87CD7C5D/Windows8.1-KB2975061-x64.msu"
set "url2=https://download.microsoft.com/download/D/B/1/DB1F29FC-316D-481E-B435-1654BA185DCF/Windows8.1-KB2919355-x64.msu"
set "file1=Windows8.1-KB2975061-x64.msu"
set "file2=Windows8.1-KB2919355-x64.msu"

:: 檢查並下載檔案1
if not exist "%file1%" (
    echo 正在下載 %file1% ...
    powershell -Command "Try { Invoke-WebRequest -Uri '%url1%' -OutFile '%file1%' -UseBasicParsing } Catch { Exit 1 }"
    if %errorlevel%==0 (
        echo %file1% 下載完成！
    ) else (
        echo %file1% 下載失敗，請檢查網路連線或 URL 是否正確。
        exit /b
    )
) else (
    echo %file1% 已存在，略過下載。
)

:: 檢查並下載檔案2
if not exist "%file2%" (
    echo 正在下載 %file2% ...
    powershell -Command "Try { Invoke-WebRequest -Uri '%url2%' -OutFile '%file2%' -UseBasicParsing } Catch { Exit 1 }"
    if %errorlevel%==0 (
        echo %file2% 下載完成！
    ) else (
        echo %file2% 下載失敗，請檢查網路連線或 URL 是否正確。
        exit /b
    )
) else (
    echo %file2% 已存在，略過下載。
)

:: 安裝檔案
echo 開始安裝...
wusa.exe "%file1%" /quiet /norestart
wusa.exe "%file2%" /quiet /norestart
echo 安裝完成！
pause
