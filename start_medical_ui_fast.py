"""
启动 MedClaw 医疗专用 Web UI - 快速启动版
"""

import uvicorn

if __name__ == "__main__":
    print("=" * 60)
    print("MedClaw 医疗专用 Web UI 启动中...")
    print("=" * 60)
    print()
    print("访问地址：http://localhost:8001")
    print()
    print("启动优化：")
    print("  ✓ 精简 HTML 模板")
    print("  ✓ 减少初始化模块")
    print("  ✓ 优化加载速度")
    print()
    print("按 Ctrl+C 停止服务")
    print("=" * 60)
    
    uvicorn.run(
        "medclaw.core.medical_ui:app",
        host="0.0.0.0",
        port=8001,
        reload=False,
        log_level="warning"
    )
