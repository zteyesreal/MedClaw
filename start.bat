@echo off
chcp 65001 >nul
echo ================================================
echo MedClaw 医学自动化助手 - 快速启动脚本
echo ================================================
echo.

:menu
echo 请选择要执行的操作:
echo.
echo 1. 安装依赖
echo 2. 初始化数据库
echo 3. 测试 MCP 连接
echo 4. 运行模块测试
echo 5. 启动 MedClaw 主服务
echo 6. 启动 QQBot (NoneBot)
echo 7. 退出
echo.
set /p choice=请输入选项 (1-7): 

if "%choice%"=="1" goto install
if "%choice%"=="2" goto initdb
if "%choice%"=="3" goto testmcp
if "%choice%"=="4" goto testmodules
if "%choice%"=="5" goto startmain
if "%choice%"=="6" goto startqqbot
if "%choice%"=="7" goto end
goto menu

:install
echo.
echo 正在安装依赖...
pip install -r requirements.txt
echo 依赖安装完成!
pause
goto menu

:initdb
echo.
echo 正在初始化数据库...
python scripts/init_db.py
echo 数据库初始化完成!
pause
goto menu

:testmcp
echo.
echo 正在测试 MCP 连接...
python scripts/test_mcp.py
pause
goto menu

:testmodules
echo.
echo 正在运行模块测试...
python tests/test_modules.py
echo 测试完成!
pause
goto menu

:startmain
echo.
echo 正在启动 MedClaw 主服务...
python main.py
pause
goto menu

:startqqbot
echo.
echo 正在启动 QQBot...
python bot.py
pause
goto menu

:end
echo.
echo 感谢使用 MedClaw!
echo.
exit
