import os
import sys
import time

import pytest

import feedwork.utils.DateHelper as dateu


def test_sys_date():
    ft = "%Y%m%d"
    date = time.strftime(ft, time.localtime(time.time()))
    assert date == dateu.sys_date()

    ft = "%Y-%m-%d"
    date = time.strftime(ft, time.localtime(time.time()))
    assert date == dateu.sys_date(ft)


def test_sys_time():
    ft = "%H%M%S"
    date = time.strftime(ft, time.localtime(time.time()))
    assert date == dateu.sys_time()

    ft = "%H:%M:%S"
    date = time.strftime(ft, time.localtime(time.time()))
    assert date == dateu.sys_time(ft)


def justshow():
    print(f"date={dateu.sys_date()}")
    print(f"time={dateu.sys_time()}")

    print(f"""date={dateu.sys_date("%y-%m-%d")}""")
    print(f"""time={dateu.sys_time("%H:%M:%S")}""")


if __name__ == "__main__":
    pytest.main(["-q", os.path.basename(sys.argv[0])])
