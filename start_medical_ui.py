"""
启动 MedClaw 医疗专用 Web UI
"""

import uvicorn
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    print("=" * 60)
    print("MedClaw 医疗专用 Web UI 启动中...")
    print("=" * 60)
    print()
    print("访问地址：http://localhost:8001")
    print()
    print("功能模块:")
    print("  📝 病历书写    ✅ 病历质控    💰 医保分析")
    print("  🔮 临床预测    🖼️ AI 阅片     📊 科研分析")
    print("  📄 论文分析")
    print()
    print("按 Ctrl+C 停止服务")
    print("=" * 60)
    
    uvicorn.run(
        "medclaw.core.medical_ui:app",
        host="0.0.0.0",
        port=8001,
        reload=False,
        log_level="info"
    )
