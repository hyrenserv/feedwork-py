import os
import sys

import pytest
import datetime
from feedwork.utils import logger

logger.debug(f"调试 {datetime.datetime.now()}")
logger.info(f"信息提示 {datetime.datetime.now()}")
logger.error(f"错误 !!!!!!  {datetime.datetime.now()}")


@logger.catch
def func(x, y, z):
    return 1 / (x + y + z)


func(1, -1, 0)

if __name__ == "__main__":
    pytest.main(["-q", os.path.basename(sys.argv[0])])
