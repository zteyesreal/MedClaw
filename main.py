"""
MedClaw 主程序
医学自动化助手核心服务
"""

import asyncio
import logging
from typing import Any, Dict, Optional
from pathlib import Path

from medclaw.core import (
    ConfigManager, MCPClient, ModuleBase, TaskScheduler,
    SystemMonitor, HealthChecker, get_monitor, get_health_checker
)
from medclaw.modules import (
    MedicalRecordModule,
    MedicalQualityModule,
    InsuranceAnalysisModule,
    ClinicalPredictionModule,
    AIReadingModule,
    ResearchAnalysisModule,
    PaperAnalysisModule,
)
from medclaw.adapters import NoneBotAdapter, GoCQHTTPAdapter

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MedClawCore:
    """MedClaw 核心类"""
    
    def __init__(self, config_path: str = "config.yaml"):
        """
        初始化 MedClaw 核心
        
        Args:
            config_path: 配置文件路径
        """
        self.config_manager = ConfigManager(config_path)
        self.config = None
        self.mcp_client: Optional[MCPClient] = None
        self.modules: Dict[str, ModuleBase] = {}
        self.scheduler = TaskScheduler()
        self.qqbot_adapter = None
        self.monitor = get_monitor()
        self.health_checker = get_health_checker()
    
    def load_config(self):
        """加载配置"""
        self.config = self.config_manager.load()
        logger.info(f"配置加载成功：{self.config.app.name}")
    
    async def initialize_mcp(self):
        """初始化 MCP 客户端"""
        if self.config:
            self.mcp_client = MCPClient(
                server_url=self.config.mcp.server_url,
                api_key=self.config.mcp.api_key,
                timeout=self.config.mcp.timeout
            )
            
            connected = await self.mcp_client.connect()
            if connected:
                logger.info("MCP 客户端连接成功")
            else:
                logger.warning("MCP 客户端连接失败，将使用基础功能")
    
    def initialize_modules(self):
        """初始化功能模块"""
        if not self.config:
            raise RuntimeError("配置未加载")
        
        module_classes = {
            "medical_record": MedicalRecordModule,
            "medical_quality": MedicalQualityModule,
            "insurance_analysis": InsuranceAnalysisModule,
            "clinical_prediction": ClinicalPredictionModule,
            "ai_reading": AIReadingModule,
            "research_analysis": ResearchAnalysisModule,
            "paper_analysis": PaperAnalysisModule,
        }
        
        enabled_modules = self.config.modules.enabled
        
        for module_name in enabled_modules:
            if module_name in module_classes:
                module_config = getattr(self.config.modules, module_name, {})
                
                module = module_classes[module_name](
                    config=module_config,
                    mcp_client=self.mcp_client
                )
                
                self.modules[module_name] = module
                logger.info(f"模块初始化成功：{module_name}")
                
                # 注册健康检查
                self.health_checker.register_check(
                    name=f"module_{module_name}",
                    check_func=lambda m=module_name: module_name in self.modules,
                    recovery_func=lambda m=module_name: logger.warning(f"模块 {m} 需要恢复")
                )
    
    def initialize_qqbot(self):
        """初始化 QQBot 适配器"""
        if not self.config:
            raise RuntimeError("配置未加载")
        
        qqbot_type = self.config.qqbot.type
        
        if qqbot_type == "nonebot":
            self.qqbot_adapter = NoneBotAdapter(
                config={
                    "driver": self.config.qqbot.driver,
                    "host": self.config.qqbot.host,
                    "port": self.config.qqbot.port,
                },
                medclaw_core=self
            )
            logger.info("NoneBot 适配器初始化成功")
        elif qqbot_type == "go-cqhttp":
            self.qqbot_adapter = GoCQHTTPAdapter(
                config={
                    "websocket": self.config.qqbot.websocket,
                },
                medclaw_core=self
            )
            logger.info("go-cqhttp 适配器初始化成功")
        else:
            logger.warning(f"未知的 QQBot 类型：{qqbot_type}")
    
    def get_module(self, module_name: str) -> Optional[ModuleBase]:
        """
        获取模块实例
        
        Args:
            module_name: 模块名称
            
        Returns:
            模块实例
        """
        return self.modules.get(module_name)
    
    async def execute_module(self, module_name: str, **kwargs) -> Any:
        """
        执行模块
        
        Args:
            module_name: 模块名称
            **kwargs: 模块参数
            
        Returns:
            执行结果
        """
        if module_name not in self.modules:
            raise ValueError(f"模块 {module_name} 不存在")
        
        module = self.modules[module_name]
        return await module.execute(**kwargs)
    
    async def start_qqbot(self):
        """启动 QQBot"""
        if not self.qqbot_adapter:
            logger.warning("QQBot 适配器未初始化")
            return
        
        if isinstance(self.qqbot_adapter, NoneBotAdapter):
            await self.qqbot_adapter.initialize()
            self.qqbot_adapter.run()
        elif isinstance(self.qqbot_adapter, GoCQHTTPAdapter):
            await self.qqbot_adapter.start_listening()
    
    async def shutdown(self):
        """关闭服务"""
        logger.info("正在关闭 MedClaw 服务...")
        
        if self.mcp_client:
            await self.mcp_client.disconnect()
        
        if self.qqbot_adapter and isinstance(self.qqbot_adapter, GoCQHTTPAdapter):
            await self.qqbot_adapter.disconnect()
        
        logger.info("MedClaw 服务已关闭")


async def main():
    """主函数"""
    core = MedClawCore()
    
    try:
        core.load_config()
        
        await core.initialize_mcp()
        
        core.initialize_modules()
        
        core.initialize_qqbot()
        
        # 打印系统状态
        core.monitor.print_status()
        
        logger.info("=" * 50)
        logger.info("MedClaw 医学自动化助手启动成功！")
        logger.info("=" * 50)
        logger.info("已加载模块:")
        for module_name in core.modules.keys():
            logger.info(f"  - {module_name}")
        logger.info("运行模式：7×24 小时守护")
        logger.info("日志目录：logs/")
        logger.info("=" * 50)
        
        # 启动健康检查
        health_task = asyncio.create_task(core.health_checker.start())
        
        # 定期保存状态报告
        async def save_status_periodically():
            while True:
                await asyncio.sleep(3600)  # 每小时保存一次
                core.monitor.save_report()
        
        status_task = asyncio.create_task(save_status_periodically())
        
        await core.start_qqbot()
        
        # 清理任务
        health_task.cancel()
        status_task.cancel()
        
    except KeyboardInterrupt:
        logger.info("收到中断信号")
    except Exception as e:
        logger.error(f"启动失败：{e}", exc_info=True)
    finally:
        await core.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
