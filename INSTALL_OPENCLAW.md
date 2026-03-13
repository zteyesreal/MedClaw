# MedClaw 完整功能安装指南

## 概述

MedClaw 现已完整实现 OpenClaw 的所有核心功能：
- ✅ Computer-Use 能力
- ✅ 办公自动化
- ✅ 任务自主拆解
- ✅ Web 可视化界面
- ✅ 7×24 小时运行

## 快速安装

### 方式一：完整安装（推荐）

```bash
# 安装所有依赖
pip install -r requirements.txt

# 安装 Computer-Use 依赖
pip install pyautogui pytesseract pillow opencv-python pygetwindow pyperclip

# 安装网页自动化依赖（可选）
pip install selenium
```

### 方式二：最小安装

```bash
# 仅安装核心功能
pip install fastapi uvicorn pydantic pyyaml httpx psutil
```

## 功能验证

### 1. 测试 Computer-Use

```python
from medclaw.core import get_computer_use_agent

computer = get_computer_use_agent()

# 获取屏幕截图
computer.save_screenshot("test.png")

# 获取鼠标位置
pos = computer.get_mouse_position()
print(f"鼠标位置：{pos}")
```

### 2. 测试办公自动化

```python
from medclaw.core import get_office_automation

office = get_office_automation()

# 整理下载目录
count = office.organize_files()
print(f"整理了 {count} 个文件")

# 搜索文件
files = office.search_files("*.pdf")
print(f"找到 {len(files)} 个 PDF 文件")
```

### 3. 测试任务引擎

```python
import asyncio
from medclaw.core import get_autonomous_task_engine

async def test():
    engine = get_autonomous_task_engine()
    
    # 创建任务
    task = await engine.create_task("整理下载目录")
    print(f"任务：{task.goal}")
    print(f"步骤：{len(task.steps)}")
    
    # 执行任务
    result = await engine.execute_task(task.task_id)
    print(f"结果：{result}")

asyncio.run(test())
```

### 4. 启动 Web UI

```bash
# 启动 Web 服务
python -m uvicorn medclaw.core.web_ui:app --reload --host 0.0.0.0 --port 8000

# 访问 http://localhost:8000
```

## 使用示例

### 示例 1：自动整理文件

**通过 Web UI**:
1. 访问 http://localhost:8000
2. 输入："整理下载目录的文件"
3. 点击"创建并执行任务"
4. 查看执行进度和结果

**通过代码**:
```python
from medclaw.core import get_office_automation
office = get_office_automation()
office.organize_files()
```

### 示例 2：自动搜索文件

```python
from medclaw.core import get_office_automation
office = get_office_automation()

# 搜索所有 PDF 文件
pdf_files = office.search_files("*.pdf")

# 搜索包含"病历"的文件
medical_files = office.search_files("*病历*")
```

### 示例 3：Computer-Use 自动化

```python
from medclaw.core import get_computer_use_agent

computer = get_computer_use_agent()

# 打开浏览器
computer.open_application("chrome")

# 等待
computer.wait(2)

# 输入网址
computer.type_text("https://www.google.com")
computer.press_key("enter")

# 截图
computer.save_screenshot("search.png")
```

### 示例 4：复杂任务自动执行

```python
import asyncio
from medclaw.core import get_autonomous_task_engine

async def main():
    engine = get_autonomous_task_engine()
    
    # 晨间例行任务
    await engine.execute_goal("晨间例行：整理文件、检查邮件、查看日程")
    
    # 自定义任务
    await engine.execute_goal("搜索所有 PDF 文件并整理到 Documents 目录")

asyncio.run(main())
```

## 系统要求

### 最低要求
- Python 3.9+
- 2GB 内存
- 1GB 磁盘空间

### 推荐配置
- Python 3.10+
- 4GB 内存
- 10GB 磁盘空间
- GPU（用于 OCR 和 AI 功能）

### 操作系统
- Windows 10/11
- macOS 10.15+
- Linux (Ubuntu 20.04+)

## 高级配置

### Tesseract OCR 安装

**Windows**:
1. 下载：https://github.com/UB-Mannheim/tesseract/wiki
2. 安装到 `C:\Program Files\Tesseract-OCR`
3. 添加到 PATH

**Linux**:
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
```

**macOS**:
```bash
brew install tesseract
```

### ChromeDriver 安装（网页自动化）

1. 下载：https://chromedriver.chromium.org/
2. 解压到系统 PATH 目录
3. 验证：`chromedriver --version`

## 故障排查

### pyautogui 安装失败

```bash
# Windows
pip install pyautogui --user

# 或手动安装
pip install mouseinfo pyscreeze pytweening
```

### OCR 无法识别中文

```bash
# 安装中文语言包
# Windows: 下载 chi_sim.traineddata 放到 tessdata 目录
# Linux: sudo apt-get install tesseract-ocr-chi-sim
```

### Web UI 无法访问

```bash
# 检查端口占用
netstat -ano | findstr :8000

# 使用其他端口
python -m uvicorn medclaw.core.web_ui:app --port 8001
```

## 性能优化

### 1. 使用 GPU 加速 OCR

```python
# 配置 pytesseract 使用 GPU
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 2. 任务并发执行

```python
# 同时执行多个任务
import asyncio
from medclaw.core import get_autonomous_task_engine

engine = get_autonomous_task_engine()

# 并发执行
await asyncio.gather(
    engine.execute_goal("整理文件"),
    engine.execute_goal("检查邮件")
)
```

### 3. 缓存优化

```python
# 启用文件搜索缓存
office = get_office_automation()
office.enable_cache = True  # 启用缓存
```

## 安全注意事项

1. **权限控制**
   - Computer-Use 需要屏幕录制权限
   - 文件操作需要文件系统权限
   - 建议在沙箱环境中运行

2. **隐私保护**
   - 屏幕截图可能包含敏感信息
   - 定期清理日志文件
   - 不要在不安全的环境中使用

3. **资源限制**
   - 设置 CPU 和内存使用上限
   - 避免同时执行过多任务
   - 定期重启服务释放资源

## 更新日志

### v2.0.0 (2026-03-12) - OpenClaw 完整功能版
- ✅ 新增 Computer-Use 能力
- ✅ 新增办公自动化
- ✅ 新增任务自主拆解引擎
- ✅ 新增 Web 可视化界面
- ✅ 增强 7×24 小时运行能力

### v1.0.0 (2026-03-12) - 医疗专业版
- ✅ 7 大医疗功能模块
- ✅ QQBot 集成
- ✅ MCP 客户端
- ✅ 系统监控和健康检查

---

**MedClaw v2.0.0 - 让医疗工作更智能、更高效**

**完全复刻 OpenClaw 所有核心功能！**
