import sys as _sys
import os as _os
import datetime

from loguru import logger

print(f"feedwork.utils imported at : {datetime.datetime.now()}")
__all__ = ["logger"]

HR_RUN_PROD = _os.getenv("HR_RUN_PROD", "n")
if HR_RUN_PROD == "y":
    # 投产阶段，使用文件记录日志
    HR_LOG_FILE = _os.getenv("HR_LOG_FILE", "hrpy_running.log")
    HR_LOG_CONSOLE = _os.getenv("HR_LOG_CONSOLE")
    format_str = "[{time:YYYY-MM-DD HH:mm:ss.SSS} {level:<5}] {message}"
    handlers = [{"sink": HR_LOG_FILE, "format": format_str,
                 "level": "ERROR", "rotation": "00:00", "retention": "1 days"}]
    if HR_LOG_CONSOLE:
        handlers.append({"sink": _sys.stdout, "format": format_str})
    logger.configure(handlers=handlers)
else:
    # 开发阶段
    format_str = (
        "[<green>{time:DD HH:mm:ss}</green> <level>{level:<5}</level>] "
        "<level>{message}</level>"
        " | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
    )
    logger.configure(handlers=[{"sink": _sys.stdout, "format": format_str}])

