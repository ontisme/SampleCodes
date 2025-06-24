# 檔案路徑: configure_system_settings.ps1
# 自動提升管理員權限

# 檢查是否以管理員身分執行
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{
    Write-Host "需要管理員權限，正在重新啟動..." -ForegroundColor Yellow
    Start-Process PowerShell -Verb RunAs "-File `"$PSCommandPath`""
    exit
}

Write-Host "正在設定 Windows 系統設定..." -ForegroundColor Green

# 取消增強指標的準確性（滑鼠加速）
Write-Host "設定滑鼠設定..." -ForegroundColor Yellow
Set-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name "MouseSpeed" -Value "0"
Set-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name "MouseThreshold1" -Value "0"
Set-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name "MouseThreshold2" -Value "0"

# 設定鍵盤重複延遲為最短（0 = 最短，3 = 最長）
# 設定鍵盤重複速率為最快（31 = 最快，0 = 最慢）
Write-Host "設定鍵盤設定..." -ForegroundColor Yellow
Set-ItemProperty -Path "HKCU:\Control Panel\Keyboard" -Name "KeyboardDelay" -Value "0"
Set-ItemProperty -Path "HKCU:\Control Panel\Keyboard" -Name "KeyboardSpeed" -Value "31"

# 設定螢幕關閉時間為永不（0 = 永不）
Write-Host "設定電源管理..." -ForegroundColor Yellow
powercfg /change monitor-timeout-ac 0
powercfg /change monitor-timeout-dc 0

# 設定睡眠時間為永不（0 = 永不）
powercfg /change standby-timeout-ac 0
powercfg /change standby-timeout-dc 0

# 設定 UAC 為不要通知（0 = 永不通知）
Write-Host "設定 UAC..." -ForegroundColor Yellow
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "EnableLUA" -Value 0 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "ConsentPromptBehaviorAdmin" -Value 0 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "ConsentPromptBehaviorUser" -Value 0 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "PromptOnSecureDesktop" -Value 0 -Type DWord

Write-Host "設定完成。請重新啟動電腦以使所有變更生效。" -ForegroundColor Green
Read-Host "按 Enter 鍵繼續..."
