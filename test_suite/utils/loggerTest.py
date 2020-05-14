import os
import sys
import datetime
from feedwork.utils import logger

UNIT_TEST = os.getenv("UNIT_TEST", "true")

# ==== 单元测试代码开始 ====

logger.debug(f"调试 {datetime.datetime.now()}")
logger.info(f"信息提示 {datetime.datetime.now()}")
logger.error(f"错误 !!!!!!  {datetime.datetime.now()}")

# ==== 单元测试代码结束 ====
print(f"[TEST] {os.path.basename(sys.argv[0]):20s}>> passed.")
