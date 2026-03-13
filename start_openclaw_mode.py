"""
启动 MedClaw - OpenClaw 任务执行模式
"""

import uvicorn

if __name__ == "__main__":
    print("=" * 60)
    print("MedClaw - OpenClaw 任务执行模式")
    print("=" * 60)
    print()
    print("访问地址：http://localhost:8001")
    print()
    print("职业场景:")
    print("  👨‍⚕️ 临床医生    ✅ 病历质控员    💰 医保审核员")
    print("  🖼️ 放射科医师   💊 临床药师      📊 科研人员")
    print("  👩‍⚕️ 护士")
    print()
    print("任务执行模式:")
    print("  1. 选择职业场景")
    print("  2. 选择任务模板")
    print("  3. 自主执行任务")
    print("  4. 查看执行结果")
    print()
    print("按 Ctrl+C 停止服务")
    print("=" * 60)
    
    uvicorn.run(
        "medclaw.core.medical_ui_openclaw:app",
        host="0.0.0.0",
        port=8001,
        reload=False,
        log_level="warning"
    )
