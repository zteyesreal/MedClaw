"""代码行数统计脚本"""
import os

files = [
    "medclaw/core/config.py",
    "medclaw/core/mcp_client.py",
    "medclaw/core/module_base.py",
    "medclaw/core/scheduler.py",
    "medclaw/modules/medical_record.py",
    "medclaw/modules/medical_quality.py",
    "medclaw/modules/insurance_analysis.py",
    "medclaw/modules/clinical_prediction.py",
    "medclaw/modules/ai_reading.py",
    "medclaw/modules/research_analysis.py",
    "medclaw/modules/paper_analysis.py",
]

print("=== 代码行数统计 ===\n")

total = 0
for f in files:
    if os.path.exists(f):
        lines = sum(1 for _ in open(f, encoding='utf-8'))
        print(f"{f}: {lines} 行")
        total += lines

print(f"\n总计：{total} 行")
print("\n=== 模块行数检查（要求 <=300 行）===")
module_files = [f for f in files if 'modules/' in f]
for f in module_files:
    lines = sum(1 for _ in open(f, encoding='utf-8'))
    status = "✅" if lines <= 300 else "❌"
    print(f"{status} {os.path.basename(f)}: {lines} 行")
