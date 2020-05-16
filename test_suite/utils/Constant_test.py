import os
import sys

import pytest

import feedwork.utils.Constant as const

const.NAME = "fd\n"
const.VALUE = 5


def test_assign_val():
    assert const.NAME == "fd\n"
    assert const.VALUE == 5


def test_non_const():
    with pytest.raises(AttributeError):
        # 不能使用未定义过的常量
        a = const.NEWVAL
    with pytest.raises(const.ConstError):
        # 不能使用小写的常量
        const.val = 1


if __name__ == "__main__":
    pytest.main(["-q", os.path.basename(sys.argv[0])])
