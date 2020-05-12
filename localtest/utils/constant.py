import os
import sys

import feedwork.utils.constant as const

# 命令行下进行整天测试时，不希望显示print的内容，执行方式为：
# UNIT_TEST
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

print(f"[TEST] {os.path.basename(sys.argv[0]):15s}>> passed.")
