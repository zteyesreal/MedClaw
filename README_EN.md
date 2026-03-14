# MedClaw Medical Intelligence Assistant

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/your-org/medclaw)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

**MedClaw** is an intelligent task execution system designed specifically for medical scenarios, built on the OpenClaw framework. It provides standardized task templates for 9 major medical professional scenarios and dynamic task adjustment capabilities.

---

## 🌟 Core Features

- **🏥 9 Major Medical Professional Scenarios**: Covering clinical, quality control, insurance, imaging, pharmacy, research, nursing, emergency, and rehabilitation
- **📋 21 Standard Task Templates**: Professional workflows compliant with medical standards
- **⚡ Dynamic Task Adjustment**: Support for skipping, inserting, and modifying steps
- **🔌 Standardized Interfaces**: REST API + WebSocket real-time communication
- **🧪 Complete Test Suite**: Mock data support, testable without real interfaces
- **📚 Comprehensive Documentation**: API docs, architecture guides, usage manuals

---

## 🏗️ System Architecture

```
MedClaw/
├── medclaw/
│   ├── core/                      # Core Engine
│   │   ├── task_engine.py         # Task Execution Engine
│   │   ├── medical_ui_openclaw.py # Web UI and API
│   │   └── ...
│   ├── task_framework.py          # Task Framework and Template Definitions
│   └── ...
├── tests/                         # Test Suite
│   ├── mock_data.py               # Mock Medical Data
│   ├── mock_executor.py           # Mock Executor
│   └── test_all_functions.py      # Complete Functionality Tests
├── docs/                          # Documentation
│   └── API_DOCUMENTATION.md       # API Interface Documentation
└── README.md                      # This File
```

---

## 🚀 Quick Start

### 1. Requirements

- Python 3.8+
- Dependencies: FastAPI, Pydantic, Uvicorn

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Service

```bash
# Method 1: Start MedClaw Medical Mode
python -m uvicorn medclaw.core.medical_ui_openclaw:app --host 0.0.0.0 --port 8001

# Method 2: Use Startup Script
python start_openclaw_mode.py
```

### 4. Access System

- **Web UI**: http://localhost:8001
- **API Docs**: See `docs/API_DOCUMENTATION.md`

---

## 📊 Function Modules

### 9 Major Medical Professional Scenarios

| Profession | Module ID | Task Count | Core Functions |
|------------|-----------|------------|----------------|
| 👨‍⚕️ Clinician | `clinician` | 3 | Outpatient reception, inpatient rounds, emergency rescue |
| ✅ Quality Controller | `quality_controller` | 2 | Running medical record QC, final medical record review |
| 💰 Insurance Auditor | `insurance_auditor` | 2 | DRG grouping audit, fee compliance check |
| 🖼️ Radiologist | `radiologist` | 2 | CT report writing, emergency imaging consultation |
| 💊 Clinical Pharmacist | `clinical_pharmacist` | 2 | Prescription review, antimicrobial drug review |
| 📊 Researcher | `researcher` | 2 | Clinical data extraction, statistical analysis |
| 👩‍⚕️ Nurse | `nurse` | 2 | Admission assessment, order execution |
| 🚑 Emergency Physician | `emergency_physician` | 3 | Emergency triage, CPR, trauma assessment |
| ♿ Rehabilitation Physician | `rehabilitation_physician` | 3 | Rehabilitation assessment, exercise therapy, occupational therapy |

**Total: 21 Professional Task Templates**

---

## 🔧 Core Functions

### 1. Task Template System

Each professional scenario has predefined standard task templates:

```python
from medclaw.task_framework import PROFESSION_TASK_TEMPLATES

# Get clinician task templates
templates = PROFESSION_TASK_TEMPLATES["clinician"]
for template in templates:
    print(f"{template.name}: {template.description}")
```

### 2. Dynamic Task Adjustment

Support for runtime task step adjustments:

```python
# Skip step
task.steps[2]['skipped'] = True

# Insert step
new_step = {"action": "extra_check", "params": {}}
task.steps.insert(2, new_step)

# Modify step parameters
task.steps[0]['params']['patient_id'] = 'P999'
```

### 3. Standardized API Interface

**Get Module List**
```bash
curl http://localhost:8001/api/modules
```

**Get Task Templates**
```bash
curl http://localhost:8001/api/tasks
```

**Execute Task**
```bash
curl -X POST http://localhost:8001/api/execute_task \
  -H "Content-Type: application/json" \
  -d '{
    "id": "task_001",
    "name": "Outpatient Reception",
    "profession": "clinician",
    "goal": "Complete outpatient reception for patient Zhang San",
    "steps": [...]
  }'
```

See [API Documentation](docs/API_DOCUMENTATION.md) for details

---

## 🧪 Testing

### Run Complete Test Suite

```bash
python tests/test_all_functions.py
```

**Test Results Example:**
```
================================================================================
                         MedClaw Complete Functionality Tests
================================================================================

Test Summary:
  Total Tests: 13
  Passed: 13 (100.0%)
  Failed: 0 (0.0%)
  Total Time: 7.57 seconds

✅ Profession Template Loading Test
✅ Clinician Task Test
✅ Quality Controller Task Test
✅ Insurance Auditor Task Test
✅ Radiologist Task Test
✅ Clinical Pharmacist Task Test
✅ Researcher Task Test
✅ Nurse Task Test
✅ Emergency Physician Task Test
✅ Rehabilitation Physician Task Test
✅ Dynamic Adjustment - Skip Step
✅ Dynamic Adjustment - Insert Step
✅ Dynamic Adjustment - Modify Step
```

### Mock Data Testing

Testable without real medical system interfaces using Mock data:

```python
from tests.mock_executor import MockTaskExecutor
from medclaw.task_framework import Task, PROFESSION_TASK_TEMPLATES

# Create Mock executor
executor = MockTaskExecutor()

# Create task
template = PROFESSION_TASK_TEMPLATES["clinician"][0]
task = Task(
    id="test_001",
    name=template.name,
    profession="clinician",
    goal="Test task",
    steps=template.default_steps
)

# Execute
result = await executor.execute_task(task)
```

---

## 📖 Documentation

| Document | Path | Description |
|----------|------|-------------|
| API Documentation | [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) | Complete REST API and WebSocket interface documentation |
| Architecture Comparison | [MedClaw_vs_OpenClaw_Deep_Comparison.md](MedClaw_vs_OpenClaw_Deep_Comparison.md) | Detailed comparison between MedClaw and OpenClaw |
| Operational Differences | [MedClaw_vs_OpenClaw_Operational_Differences.md](MedClaw_vs_OpenClaw_Operational_Differences.md) | Operational level differences analysis |
| Reliability Analysis | [Why_Standardized_MedClaw_is_More_Reliable.md](Why_Standardized_MedClaw_is_More_Reliable.md) | Advantages of standardized design |
| Module Consistency Verification | [Module_Consistency_Verification_Report.md](Module_Consistency_Verification_Report.md) | Frontend-backend module consistency verification |

---

## 💡 Usage Examples

### Example 1: Execute Outpatient Reception Task

```python
import asyncio
from medclaw.task_framework import Task, PROFESSION_TASK_TEMPLATES
from tests.mock_executor import MockTaskExecutor

async def main():
    # Get template
    template = PROFESSION_TASK_TEMPLATES["clinician"][0]
    
    # Create task
    task = Task(
        id="outpatient_001",
        name=template.name,
        profession="clinician",
        goal="Complete outpatient reception for patient Zhang San, generate standard medical record",
        steps=template.default_steps.copy()
    )
    
    # Execute
    executor = MockTaskExecutor()
    result = await executor.execute_task(task)
    
    print(f"Task Status: {result['status']}")
    print(f"Executed Steps: {result['success_steps']}/{result['total_steps']}")

asyncio.run(main())
```

### Example 2: Dynamic Task Adjustment

```python
# Skip a step
task.steps[2]['skipped'] = True

# Insert new step
new_step = {
    "action": "extra_examination", 
    "params": {"type": "ECG"}
}
task.steps.insert(3, new_step)

# Modify parameters
task.steps[0]['params']['patient_id'] = 'P002'
```

### Example 3: Call via API

```python
import requests

# Get all modules
modules = requests.get("http://localhost:8001/api/modules").json()

# Get task templates
templates = requests.get("http://localhost:8001/api/tasks").json()

# Execute task
result = requests.post(
    "http://localhost:8001/api/execute_task",
    json={
        "id": "task_001",
        "name": "Outpatient Reception",
        "profession": "clinician",
        "goal": "Complete outpatient reception for patient Zhang San",
        "steps": [...]
    }
).json()
```

---

## 🏥 Real Medical Scenario Parameters

Parameters used in test scripts are based on real medical scenarios:

| Profession | Parameter Example | Real Scenario |
|------------|-------------------|---------------|
| Quality Controller | `department`: "Cardiology", `record_count`: 15 | QC 15 running medical records in Cardiology |
| Insurance Auditor | `month`: "2026-03", `case_count`: 50 | Audit DRG grouping for 50 cases in March |
| Radiologist | `body_part`: "Chest", `count`: 10 | Write 10 chest CT reports |
| Clinical Pharmacist | `department`: "Respiratory", `prescription_count`: 30 | Review 30 prescriptions in Respiratory department |
| Researcher | `disease`: "Hypertension", `sample_size`: 100 | Extract clinical data for 100 hypertension patients |
| Nurse | `patient_name`: "Zhang San" | Complete admission nursing assessment for Zhang San |

---

## 🔍 Project Highlights

### 1. Standardized Design
- Predefined standard task templates
- Compliant with medical industry standards
- Predictable execution results

### 2. High Reliability
- 100% test pass rate
- Stable execution workflow
- Comprehensive error handling

### 3. Easy to Extend
- Modular architecture
- Clear interface definitions
- Comprehensive documentation support

### 4. No Real Data Required
- Mock data supports complete testing
- No need to connect to real medical systems
- Suitable for development and demonstration environments

---

## 🤝 Contribution Guide

Welcome to submit Issues and Pull Requests!

### Development Workflow

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

---

## 📄 License

This project uses [MIT](LICENSE) License

---

## 📞 Contact

- Project Homepage: [GitHub](https://github.com/your-org/medclaw)
- Issue Feedback: [Issues](https://github.com/your-org/medclaw/issues)
- Documentation: [Docs](docs/)

---

**MedClaw v1.0.0** - Making Medical Work Smarter, More Standardized, and More Reliable

*Built on OpenClaw framework, optimized for medical scenarios*
