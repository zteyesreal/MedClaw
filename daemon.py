"""
守护进程启动脚本
支持后台运行、自动重启、日志记录
"""

import os
import sys
import time
import signal
import logging
from datetime import datetime
from pathlib import Path

# 配置日志
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir / f"medclaw_{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class Daemon:
    """守护进程类"""
    
    def __init__(self, pid_file='medclaw.pid', max_restarts=5):
        self.pid_file = Path(pid_file)
        self.max_restarts = max_restarts
        self.restart_count = 0
        self.running = True
        
        # 注册信号处理
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """信号处理"""
        logger.info(f"收到信号 {signum}，正在关闭...")
        self.running = False
    
    def is_running(self):
        """检查是否已在运行"""
        if self.pid_file.exists():
            with open(self.pid_file, 'r') as f:
                pid = int(f.read().strip())
            try:
                os.kill(pid, 0)
                return True
            except ProcessLookupError:
                self.pid_file.unlink()
        return False
    
    def write_pid(self):
        """写入 PID 文件"""
        with open(self.pid_file, 'w') as f:
            f.write(str(os.getpid()))
    
    def remove_pid(self):
        """删除 PID 文件"""
        if self.pid_file.exists():
            self.pid_file.unlink()
    
    def run(self):
        """运行守护进程"""
        if self.is_running():
            logger.error("MedClaw 已在运行中")
            return
        
        logger.info("=" * 60)
        logger.info("MedClaw 医学自动化助手 - 守护进程启动")
        logger.info("=" * 60)
        
        while self.running and self.restart_count < self.max_restarts:
            try:
                self.write_pid()
                logger.info(f"MedClaw 主程序启动 (PID: {os.getpid()})")
                
                # 导入并运行主程序
                from main import MedClawCore
                import asyncio
                
                core = MedClawCore()
                
                try:
                    # 加载配置
                    core.load_config()
                    logger.info("配置加载成功")
                    
                    # 初始化 MCP
                    asyncio.run(core.initialize_mcp())
                    
                    # 初始化模块
                    core.initialize_modules()
                    logger.info(f"已加载 {len(core.modules)} 个模块")
                    
                    # 初始化 QQBot
                    core.initialize_qqbot()
                    logger.info(f"QQBot 适配器已初始化：{core.config.qqbot.type}")
                    
                    # 启动 QQBot
                    logger.info("开始监听 QQ 消息...")
                    asyncio.run(core.start_qqbot())
                    
                except KeyboardInterrupt:
                    logger.info("收到中断信号")
                except Exception as e:
                    logger.error(f"运行错误：{e}", exc_info=True)
                    self.restart_count += 1
                    logger.warning(f"程序异常退出，将在 5 秒后重启 (第 {self.restart_count}/{self.max_restarts} 次)")
                    time.sleep(5)
                finally:
                    # 清理资源
                    asyncio.run(core.shutdown())
                    
            except Exception as e:
                logger.error(f"守护进程错误：{e}", exc_info=True)
                self.restart_count += 1
                if self.restart_count < self.max_restarts:
                    logger.warning(f"将在 10 秒后重启 (第 {self.restart_count}/{self.max_restarts} 次)")
                    time.sleep(10)
                else:
                    logger.error("达到最大重启次数，停止重启")
                    break
            finally:
                self.remove_pid()
        
        if self.restart_count >= self.max_restarts:
            logger.error("MedClaw 因多次异常退出已停止运行，请检查日志")
        else:
            logger.info("MedClaw 已正常关闭")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='MedClaw 守护进程')
    parser.add_argument('command', choices=['start', 'stop', 'restart', 'status'],
                       help='操作命令')
    
    args = parser.parse_args()
    
    daemon = Daemon()
    
    if args.command == 'start':
        daemon.run()
    elif args.command == 'stop':
        if daemon.is_running():
            with open(daemon.pid_file, 'r') as f:
                pid = int(f.read().strip())
            os.kill(pid, signal.SIGTERM)
            logger.info(f"已发送停止信号到进程 {pid}")
            time.sleep(2)
            if daemon.pid_file.exists():
                daemon.pid_file.unlink()
        else:
            logger.info("MedClaw 未运行")
    elif args.command == 'restart':
        if daemon.is_running():
            logger.info("正在停止 MedClaw...")
            with open(daemon.pid_file, 'r') as f:
                pid = int(f.read().strip())
            os.kill(pid, signal.SIGTERM)
            time.sleep(3)
        logger.info("正在启动 MedClaw...")
        daemon.run()
    elif args.command == 'status':
        if daemon.is_running():
            with open(daemon.pid_file, 'r') as f:
                pid = f.read().strip()
            logger.info(f"MedClaw 正在运行 (PID: {pid})")
        else:
            logger.info("MedClaw 未运行")


if __name__ == "__main__":
    main()
