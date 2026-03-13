"""
项目完整性检查脚本
根据项目说明文档逐项检查
"""

import os
from pathlib import Path

print("=" * 70)
print("MedClaw 项目完整性检查")
print("=" * 70)

checks = {
    "核心引擎": [
        "medclaw/__init__.py",
        "medclaw/core/__init__.py",
        "medclaw/core/config.py",
        "medclaw/core/mcp_client.py",
        "medclaw/core/module_base.py",
        "medclaw/core/scheduler.py",
    ],
    "功能模块": [
        "medclaw/modules/__init__.py",
        "medclaw/modules/medical_record.py",
        "medclaw/modules/medical_quality.py",
        "medclaw/modules/insurance_analysis.py",
        "medclaw/modules/clinical_prediction.py",
        "medclaw/modules/ai_reading.py",
        "medclaw/modules/research_analysis.py",
        "medclaw/modules/paper_analysis.py",
    ],
    "适配器": [
        "medclaw/adapters/__init__.py",
        "medclaw/adapters/nonebot_adapter.py",
        "medclaw/adapters/gocqhttp_adapter.py",
    ],
    "配置文件": [
        "config.yaml",
        "config.example.yaml",
    ],
    "脚本工具": [
        "main.py",
        "bot.py",
        "scripts/init_db.py",
        "scripts/test_mcp.py",
    ],
    "测试": [
        "tests/test_modules.py",
    ],
    "文档": [
        "README.md",
        "requirements.txt",
    ],
    "数据目录": [
        "medclaw/data/",
        "medclaw/models/",
        "medclaw/cache/",
        "medclaw/rules/",
        "medclaw/templates/",
    ],
}

all_passed = True

for category, files in checks.items():
    print(f"\n{category}:")
    print("-" * 70)
    for file_path in files:
        full_path = Path(file_path)
        exists = full_path.exists()
        status = "✅" if exists else "❌"
        print(f"  {status} {file_path}")
        if not exists:
            all_passed = False

print("\n" + "=" * 70)
if all_passed:
    print("✅ 所有文件检查通过！")
else:
    print("❌ 有文件缺失，请检查！")
print("=" * 70)

# 检查模块导入
print("\n模块导入测试:")
print("-" * 70)
try:
    from medclaw.core import ConfigManager, MCPClient, ModuleBase, TaskScheduler
    print("  ✅ 核心模块导入成功")
except Exception as e:
    print(f"  ❌ 核心模块导入失败：{e}")
    all_passed = False

try:
    from medclaw.modules import (
        MedicalRecordModule,
        MedicalQualityModule,
        InsuranceAnalysisModule,
        ClinicalPredictionModule,
        AIReadingModule,
        ResearchAnalysisModule,
        PaperAnalysisModule,
    )
    print("  ✅ 功能模块导入成功")
except Exception as e:
    print(f"  ❌ 功能模块导入失败：{e}")
    all_passed = False

try:
    from medclaw.adapters import NoneBotAdapter, GoCQHTTPAdapter
    print("  ✅ 适配器模块导入成功")
except Exception as e:
    print(f"  ❌ 适配器模块导入失败：{e}")
    all_passed = False

print("\n" + "=" * 70)
print("项目完成度检查:")
print("=" * 70)

# 根据项目说明文档检查功能点
features = [
    ("病历书写模块", os.path.exists("medclaw/modules/medical_record.py")),
    ("病历质控模块", os.path.exists("medclaw/modules/medical_quality.py")),
    ("医保分析模块", os.path.exists("medclaw/modules/insurance_analysis.py")),
    ("临床预测模块", os.path.exists("medclaw/modules/clinical_prediction.py")),
    ("AI 阅片模块", os.path.exists("medclaw/modules/ai_reading.py")),
    ("科研分析模块", os.path.exists("medclaw/modules/research_analysis.py")),
    ("论文分析模块", os.path.exists("medclaw/modules/paper_analysis.py")),
    ("MCP 客户端", os.path.exists("medclaw/core/mcp_client.py")),
    ("QQBot 适配器 (NoneBot)", os.path.exists("medclaw/adapters/nonebot_adapter.py")),
    ("QQBot 适配器 (go-cqhttp)", os.path.exists("medclaw/adapters/gocqhttp_adapter.py")),
    ("配置文件", os.path.exists("config.yaml")),
    ("数据库初始化脚本", os.path.exists("scripts/init_db.py")),
    ("MCP 测试脚本", os.path.exists("scripts/test_mcp.py")),
    ("模块测试脚本", os.path.exists("tests/test_modules.py")),
    ("主程序", os.path.exists("main.py")),
    ("QQBot 启动脚本", os.path.exists("bot.py")),
    ("依赖文件", os.path.exists("requirements.txt")),
    ("README 文档", os.path.exists("README.md")),
]

completed = sum(1 for _, exists in features if exists)
total = len(features)

for feature, exists in features:
    status = "✅" if exists else "❌"
    print(f"{status} {feature}")

print("\n" + "=" * 70)
print(f"完成度：{completed}/{total} ({completed/total*100:.1f}%)")
print("=" * 70)

if completed == total and all_passed:
    print("\n🎉 项目已全部完成！")
else:
    print(f"\n⚠️  还有 {total - completed} 项未完成")
