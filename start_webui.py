"""
启动 MedClaw Web UI
"""

import uvicorn
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    print("=" * 60)
    print("MedClaw Web UI 启动中...")
    print("=" * 60)
    print()
    print("访问地址：http://localhost:8000")
    print()
    print("按 Ctrl+C 停止服务")
    print("=" * 60)
    
    uvicorn.run(
        "medclaw.core.web_ui:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )
