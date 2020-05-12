import os
import sys

import feedwork.utils.Constant as const

# 命令行下进行整天测试时，不希望显示print的内容，执行方式为：
# PYTHONPATH=$PWD UNIT_TEST=false python3 test/utils/ConstantTest.py
UNIT_TEST = os.getenv("UNIT_TEST", "true")

# ==== 单元测试代码开始 ====
const.NAME = "fd"
const.VALUE = 5

print(f"const.NAME={const.NAME}") if UNIT_TEST == "true" else None

# 不能使用未定义过的常量
try:
    a = const.a
except AttributeError as ex:
    pass

# 不能使用小写的常量
try:
    const.val = 15
except const.ConstError as ex:
    pass

assert const.NAME == "fd"
assert const.VALUE == 5

# ==== 单元测试代码结束 ====
print(f"[TEST] {os.path.basename(sys.argv[0]):20s}>> passed.")
