# 下載 Build Tool：https://aka.ms/vs/17/release/vs_BuildTools.exe
# CMD 執行
vs_buildtools.exe --norestart --passive --downloadThenInstall --includeRecommended --add Microsoft.VisualStudio.Workload.NativeDesktop --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Workload.MSBuildTools

# PowerShell 腳本
$client = new-object System.Net.WebClient
$client.DownloadFile('https://aka.ms/vs/17/release/vs_BuildTools.exe', 'vs_BuildTools.exe')
.\vs_buildtools.exe --norestart --passive --downloadThenInstall --includeRecommended --add Microsoft.VisualStudio.Workload.NativeDesktop --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Workload.MSBuildTools
