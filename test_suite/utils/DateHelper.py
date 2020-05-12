import os
import sys

import feedwork.utils.DateHelper as dtime

# 命令行下进行整天测试时，不希望显示print的内容，执行方式为：
# PYTHONPATH=$PWD UNIT_TEST=false python3 test/utils/Constant.py
UNIT_TEST = os.getenv("UNIT_TEST", "true")

# ==== 单元测试代码开始 ====

print(f"date={dtime.getSysDate()}")
print(f"time={dtime.getSysTime()}")

print(f"""date={dtime.getSysDate("%y-%m-%d")}""")
print(f"""time={dtime.getSysTime("%H:%M:%S")}""")

# ==== 单元测试代码结束 ====
print(f"[TEST] {os.path.basename(sys.argv[0]):20s}>> passed.")
