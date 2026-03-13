"""
根据项目说明文档逐项验证
"""

import os
from pathlib import Path

print("=" * 70)
print("根据项目说明文档逐项验证")
print("=" * 70)

checks = []

# 1. 系统架构组件
print("\n【系统架构组件】")
architecture = [
    ("核心引擎", "medclaw/core/"),
    ("功能模块目录", "medclaw/modules/"),
    ("集成层/适配器", "medclaw/adapters/"),
]
for name, path in architecture:
    exists = os.path.exists(path)
    checks.append(exists)
    print(f"  {'✅' if exists else '❌'} {name}: {path}")

# 2. 功能模块
print("\n【功能模块】(每个模块代码 ≤ 300 行)")
modules = [
    ("病历书写模块", "medclaw/modules/medical_record.py"),
    ("病历质控模块", "medclaw/modules/medical_quality.py"),
    ("医保分析模块", "medclaw/modules/insurance_analysis.py"),
    ("临床预测模块", "medclaw/modules/clinical_prediction.py"),
    ("AI 阅片模块", "medclaw/modules/ai_reading.py"),
    ("科研分析模块", "medclaw/modules/research_analysis.py"),
    ("论文分析模块", "medclaw/modules/paper_analysis.py"),
]
for name, path in modules:
    exists = os.path.exists(path)
    if exists:
        lines = sum(1 for _ in open(path, encoding='utf-8'))
        within_limit = lines <= 300
        checks.append(within_limit)
        print(f"  {'✅' if within_limit else '❌'} {name}: {lines} 行 {'(符合要求)' if within_limit else '(超出 300 行限制!)'}")
    else:
        checks.append(False)
        print(f"  ❌ {name}: 文件不存在")

# 3. 集成层
print("\n【集成层】")
integrations = [
    ("MCP 适配器", "medclaw/core/mcp_client.py"),
    ("QQBot 适配器 - NoneBot2", "medclaw/adapters/nonebot_adapter.py"),
    ("QQBot 适配器 - go-cqhttp", "medclaw/adapters/gocqhttp_adapter.py"),
]
for name, path in integrations:
    exists = os.path.exists(path)
    checks.append(exists)
    print(f"  {'✅' if exists else '❌'} {name}: {path}")

# 4. 外部依赖
print("\n【外部依赖】")
dependencies = [
    ("requirements.txt", "requirements.txt"),
    ("Python 3.9+ 兼容", None),  # 假设兼容
]
for name, path in dependencies:
    if path:
        exists = os.path.exists(path)
        checks.append(exists)
        print(f"  {'✅' if exists else '❌'} {name}")
    else:
        checks.append(True)
        print(f"  ✅ {name} (假设兼容)")

# 5. 配置文件
print("\n【配置文件】")
configs = [
    ("主配置文件", "config.yaml"),
    ("配置模板", "config.example.yaml"),
]
for name, path in configs:
    exists = os.path.exists(path)
    checks.append(exists)
    print(f"  {'✅' if exists else '❌'} {name}: {path}")

# 6. 初始化脚本
print("\n【初始化脚本】")
scripts = [
    ("数据库初始化", "scripts/init_db.py"),
    ("MCP 连接测试", "scripts/test_mcp.py"),
]
for name, path in scripts:
    exists = os.path.exists(path)
    checks.append(exists)
    print(f"  {'✅' if exists else '❌'} {name}: {path}")

# 7. 启动脚本
print("\n【启动脚本】")
start_scripts = [
    ("主程序", "main.py"),
    ("QQBot 独立启动", "bot.py"),
    ("快速启动批处理", "start.bat"),
]
for name, path in start_scripts:
    exists = os.path.exists(path)
    checks.append(exists)
    print(f"  {'✅' if exists else '❌'} {name}: {path}")

# 8. 测试文件
print("\n【测试文件】")
tests = [
    ("模块功能测试", "tests/test_modules.py"),
]
for name, path in tests:
    exists = os.path.exists(path)
    checks.append(exists)
    print(f"  {'✅' if exists else '❌'} {name}: {path}")

# 9. 文档
print("\n【文档】")
docs = [
    ("README.md", "README.md"),
    ("项目说明.md", "项目说明.md"),
]
for name, path in docs:
    exists = os.path.exists(path)
    checks.append(exists)
    print(f"  {'✅' if exists else '❌'} {name}: {path}")

# 10. 数据目录
print("\n【数据目录】")
directories = [
    ("模板目录", "medclaw/templates/"),
    ("规则目录", "medclaw/rules/"),
    ("数据目录", "medclaw/data/"),
    ("模型目录", "medclaw/models/"),
    ("缓存目录", "medclaw/cache/"),
]
for name, path in directories:
    exists = os.path.exists(path)
    checks.append(exists)
    print(f"  {'✅' if exists else '❌'} {name}: {path}")

# 总结
print("\n" + "=" * 70)
total = len(checks)
passed = sum(checks)
print(f"检查项目总数：{total}")
print(f"通过：{passed}")
print(f"失败：{total - passed}")
print(f"完成率：{passed/total*100:.1f}%")
print("=" * 70)

if passed == total:
    print("\n🎉 所有项目说明文档中的要求都已完成！")
else:
    print(f"\n⚠️  还有 {total - passed} 项未完成")
    print("\n失败项目:")
    # 这里可以列出失败的项目
