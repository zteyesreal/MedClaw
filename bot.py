"""
QQBot 独立启动脚本
用于单独启动 QQ 机器人服务
"""

import asyncio
import logging
import yaml
from pathlib import Path

from medclaw.core import ConfigManager
from medclaw.adapters import NoneBotAdapter, GoCQHTTPAdapter

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MedClawBot:
    """MedClaw QQBot 服务"""
    
    def __init__(self, config_path: str = "config.yaml"):
        self.config_manager = ConfigManager(config_path)
        self.config = None
        self.adapter = None
    
    def load_config(self):
        """加载配置"""
        self.config = self.config_manager.load()
        logger.info(f"配置加载成功：{self.config.app.name}")
    
    def initialize_adapter(self):
        """初始化适配器"""
        if not self.config:
            raise RuntimeError("配置未加载")
        
        qqbot_type = self.config.qqbot.type
        
        if qqbot_type == "nonebot":
            self.adapter = NoneBotAdapter(
                config={
                    "driver": self.config.qqbot.driver,
                    "host": self.config.qqbot.host,
                    "port": self.config.qqbot.port,
                },
                medclaw_core=None
            )
            logger.info("NoneBot 适配器初始化成功")
        elif qqbot_type == "go-cqhttp":
            self.adapter = GoCQHTTPAdapter(
                config={
                    "websocket": self.config.qqbot.websocket,
                },
                medclaw_core=None
            )
            logger.info("go-cqhttp 适配器初始化成功")
        else:
            raise ValueError(f"不支持的 QQBot 类型：{qqbot_type}")
    
    async def run(self):
        """运行服务"""
        try:
            self.load_config()
            self.initialize_adapter()
            
            logger.info("=" * 50)
            logger.info("MedClaw QQBot 启动成功!")
            logger.info(f"QQBot 类型：{self.config.qqbot.type}")
            if self.config.qqbot.type == "nonebot":
                logger.info(f"监听地址：{self.config.qqbot.host}:{self.config.qqbot.port}")
            else:
                logger.info(f"WebSocket: {self.config.qqbot.websocket}")
            logger.info("=" * 50)
            logger.info("发送 '/帮助' 查看可用命令")
            logger.info("=" * 50)
            
            await self.adapter.start_listening()
            
        except KeyboardInterrupt:
            logger.info("收到中断信号，正在关闭...")
        except Exception as e:
            logger.error(f"运行错误：{e}", exc_info=True)
        finally:
            if self.adapter and hasattr(self.adapter, 'disconnect'):
                await self.adapter.disconnect()


if __name__ == "__main__":
    bot = MedClawBot()
    asyncio.run(bot.run())
