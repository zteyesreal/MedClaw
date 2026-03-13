# MedClaw 医疗智能助手

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/your-org/medclaw)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

**MedClaw** 是一个专为医疗场景设计的智能任务执行系统，基于 OpenClaw 框架构建，提供 9 大医疗职业场景的标准化任务模板和动态任务调整能力。

---

## 🌟 核心特性

- **🏥 9 大医疗职业场景**：覆盖临床、质控、医保、影像、药学、科研、护理、急诊、康复
- **📋 21 个标准任务模板**：符合医疗规范的专业流程
- **⚡ 动态任务调整**：支持跳过、插入、修改步骤
- **🔌 标准化接口**：REST API + WebSocket 实时通信
- **🧪 完整测试套件**：Mock 数据支持，无需真实接口即可测试
- **📚 完善文档**：API 文档、架构说明、使用指南

---

## 🏗️ 系统架构

```
MedClaw/
├── medclaw/
│   ├── core/                      # 核心引擎
│   │   ├── task_engine.py         # 任务执行引擎
│   │   ├── medical_ui_openclaw.py # Web UI 和 API
│   │   └── ...
│   ├── task_framework.py          # 任务框架和模板定义
│   └── ...
├── tests/                         # 测试套件
│   ├── mock_data.py               # Mock 医疗数据
│   ├── mock_executor.py           # Mock 执行器
│   └── test_all_functions.py      # 完整功能测试
├── docs/                          # 文档
│   └── API_DOCUMENTATION.md       # API 接口文档
└── README.md                      # 本文件
```

---

## 🚀 快速开始

### 1. 环境要求

- Python 3.8+
- 依赖包：FastAPI, Pydantic, Uvicorn

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 启动服务

```bash
# 方式 1：启动 MedClaw 医疗模式
python -m uvicorn medclaw.core.medical_ui_openclaw:app --host 0.0.0.0 --port 8001

# 方式 2：使用启动脚本
python start_openclaw_mode.py
```

### 4. 访问系统

- **Web UI**: http://localhost:8001
- **API 文档**: 见 `docs/API_DOCUMENTATION.md`

---

## 📊 功能模块

### 9 大医疗职业场景

| 职业 | 模块 ID | 任务数 | 核心功能 |
|------|---------|--------|----------|
| 👨‍⚕️ 临床医生 | `clinician` | 3 | 门诊接诊、住院查房、急诊抢救 |
| ✅ 病历质控员 | `quality_controller` | 2 | 运行病历质控、终末病历评审 |
| 💰 医保审核员 | `insurance_auditor` | 2 | DRG 分组审核、费用合规性检查 |
| 🖼️ 放射科医师 | `radiologist` | 2 | CT 报告书写、急诊影像会诊 |
| 💊 临床药师 | `clinical_pharmacist` | 2 | 处方审核、抗菌药物专项点评 |
| 📊 科研人员 | `researcher` | 2 | 临床数据提取、统计分析 |
| 👩‍⚕️ 护士 | `nurse` | 2 | 入院评估、执行医嘱 |
| 🚑 急诊科医师 | `emergency_physician` | 3 | 急诊分诊、心肺复苏、创伤评估 |
| ♿ 康复科医师 | `rehabilitation_physician` | 3 | 康复评估、运动疗法、作业疗法 |

**总计：21 个专业任务模板**

---

## 🔧 核心功能

### 1. 任务模板系统

每个职业场景都有预定义的标准任务模板：

```python
from medclaw.task_framework import PROFESSION_TASK_TEMPLATES

# 获取临床医生任务模板
templates = PROFESSION_TASK_TEMPLATES["clinician"]
for template in templates:
    print(f"{template.name}: {template.description}")
```

### 2. 动态任务调整

支持运行时调整任务步骤：

```python
# 跳过步骤
task.steps[2]['skipped'] = True

# 插入步骤
new_step = {"action": "extra_check", "params": {}}
task.steps.insert(2, new_step)

# 修改步骤参数
task.steps[0]['params']['patient_id'] = 'P999'
```

### 3. 标准化 API 接口

**获取模块列表**
```bash
curl http://localhost:8001/api/modules
```

**获取任务模板**
```bash
curl http://localhost:8001/api/tasks
```

**执行任务**
```bash
curl -X POST http://localhost:8001/api/execute_task \
  -H "Content-Type: application/json" \
  -d '{
    "id": "task_001",
    "name": "门诊接诊",
    "profession": "clinician",
    "goal": "为患者张三完成门诊接诊",
    "steps": [...]
  }'
```

详见 [API 文档](docs/API_DOCUMENTATION.md)

---

## 🧪 测试

### 运行完整测试套件

```bash
python tests/test_all_functions.py
```

**测试结果示例：**
```
================================================================================
                         MedClaw 完整功能测试
================================================================================

测试汇总:
  总测试数: 13
  通过: 13 (100.0%)
  失败: 0 (0.0%)
  总耗时: 7.57 秒

✅ 职业模板加载测试
✅ 临床医生任务测试
✅ 病历质控员任务测试
✅ 医保审核员任务测试
✅ 放射科医师任务测试
✅ 临床药师任务测试
✅ 科研人员任务测试
✅ 护士任务测试
✅ 急诊科医师任务测试
✅ 康复科医师任务测试
✅ 动态调整 - 跳过步骤
✅ 动态调整 - 插入步骤
✅ 动态调整 - 修改步骤
```

### Mock 数据测试

无需真实医疗系统接口，使用 Mock 数据即可完整测试：

```python
from tests.mock_executor import MockTaskExecutor
from medclaw.task_framework import Task, PROFESSION_TASK_TEMPLATES

# 创建 Mock 执行器
executor = MockTaskExecutor()

# 创建任务
template = PROFESSION_TASK_TEMPLATES["clinician"][0]
task = Task(
    id="test_001",
    name=template.name,
    profession="clinician",
    goal="测试任务",
    steps=template.default_steps
)

# 执行
result = await executor.execute_task(task)
```

---

## 📖 文档

| 文档 | 路径 | 描述 |
|------|------|------|
| API 接口文档 | [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) | 完整的 REST API 和 WebSocket 接口说明 |
| 架构对比分析 | [MedClaw_vs_OpenClaw 深度对比分析.md](MedClaw_vs_OpenClaw%20深度对比分析.md) | MedClaw 与 OpenClaw 的详细对比 |
| 操作差异详解 | [MedClaw_vs_OpenClaw_操作差异详解.md](MedClaw_vs_OpenClaw_操作差异详解.md) | 实际操作层面的差异分析 |
| 可靠性分析 | [为什么规范化的 MedClaw 更可靠.md](为什么规范化的%20MedClaw%20更可靠.md) | 规范化设计的优势分析 |
| 模块一致性验证 | [模块一致性验证报告.md](模块一致性验证报告.md) | 前后端模块一致性验证 |

---

## 💡 使用示例

### 示例 1：执行门诊接诊任务

```python
import asyncio
from medclaw.task_framework import Task, PROFESSION_TASK_TEMPLATES
from tests.mock_executor import MockTaskExecutor

async def main():
    # 获取模板
    template = PROFESSION_TASK_TEMPLATES["clinician"][0]
    
    # 创建任务
    task = Task(
        id="outpatient_001",
        name=template.name,
        profession="clinician",
        goal="为患者张三完成门诊接诊，生成规范病历",
        steps=template.default_steps.copy()
    )
    
    # 执行
    executor = MockTaskExecutor()
    result = await executor.execute_task(task)
    
    print(f"任务状态: {result['status']}")
    print(f"执行步骤: {result['success_steps']}/{result['total_steps']}")

asyncio.run(main())
```

### 示例 2：动态调整任务

```python
# 跳过某个步骤
task.steps[2]['skipped'] = True

# 插入新步骤
new_step = {
    "action": "extra_examination", 
    "params": {"type": "心电图"}
}
task.steps.insert(3, new_step)

# 修改参数
task.steps[0]['params']['patient_id'] = 'P002'
```

### 示例 3：通过 API 调用

```python
import requests

# 获取所有模块
modules = requests.get("http://localhost:8001/api/modules").json()

# 获取任务模板
templates = requests.get("http://localhost:8001/api/tasks").json()

# 执行任务
result = requests.post(
    "http://localhost:8001/api/execute_task",
    json={
        "id": "task_001",
        "name": "门诊接诊",
        "profession": "clinician",
        "goal": "为患者张三完成门诊接诊",
        "steps": [...]
    }
).json()
```

---

## 🏥 真实医疗场景参数

测试脚本中使用的参数基于真实医疗场景：

| 职业 | 参数示例 | 真实场景 |
|------|----------|----------|
| 病历质控员 | `department`: "心内科", `record_count`: 15 | 质控心内科15份运行病历 |
| 医保审核员 | `month`: "2026-03", `case_count`: 50 | 审核3月份50个病例的DRG分组 |
| 放射科医师 | `body_part`: "胸部", `count`: 10 | 书写10例胸部CT报告 |
| 临床药师 | `department`: "呼吸科", `prescription_count`: 30 | 审核呼吸科30张处方 |
| 科研人员 | `disease`: "高血压", `sample_size`: 100 | 提取100例高血压患者的临床数据 |
| 护士 | `patient_name`: "张三" | 为张三完成入院护理评估 |

---

## 🔍 项目亮点

### 1. 规范化设计
- 预定义标准任务模板
- 符合医疗行业规范
- 可预测的执行结果

### 2. 高可靠性
- 100% 测试通过率
- 稳定的执行流程
- 完善的错误处理

### 3. 易于扩展
- 模块化架构
- 清晰的接口定义
- 完善的文档支持

### 4. 无需真实数据
- Mock 数据支持完整测试
- 无需对接真实医疗系统
- 适合开发和演示环境

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 开发流程

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

---

## 📄 许可证

本项目采用 [MIT](LICENSE) 许可证

---

## 📞 联系方式

- 项目主页：[GitHub](https://github.com/your-org/medclaw)
- 问题反馈：[Issues](https://github.com/your-org/medclaw/issues)
- 文档地址：[Docs](docs/)

---

**MedClaw v1.0.0** - 让医疗工作更智能、更规范、更可靠

*基于 OpenClaw 框架构建，专为医疗场景优化*
