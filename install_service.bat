@echo off
chcp 65001 >nul
echo ================================================
echo MedClaw 服务安装脚本 (Windows)
echo ================================================
echo.

set SERVICE_NAME=MedClaw
set SERVICE_PATH=%cd%\daemon.py
set PYTHON_PATH=python

echo 正在创建 Windows 服务...
echo 服务名称：%SERVICE_NAME%
echo 服务路径：%SERVICE_PATH%
echo.

:: 使用 NSSM 创建服务（需要先下载 nssm.exe）
if exist "nssm.exe" (
    nssm install %SERVICE_NAME% "%PYTHON_PATH%" "%SERVICE_PATH%" start
    nssm set %SERVICE_NAME% DisplayName MedClaw 医学自动化助手
    nssm set %SERVICE_NAME% Description 7x24 小时运行的医学自动化助手服务
    nssm set %SERVICE_NAME% Start SERVICE_AUTO_START
    nssm set %SERVICE_NAME% ObjectName LocalSystem
    nssm set %SERVICE_NAME% Type SERVICE_WIN32_OWN_PROCESS
    echo ✅ 服务创建成功!
    echo.
    echo 启动服务：net start %SERVICE_NAME%
    echo 停止服务：net stop %SERVICE_NAME%
    echo 查看状态：sc query %SERVICE_NAME%
) else (
    echo ❌ 未找到 nssm.exe
    echo.
    echo 请从 https://nssm.cc/download 下载 nssm.exe 并放到此目录
    echo.
    echo 或者使用以下方式手动启动守护进程:
    echo   python daemon.py start
)

pause
