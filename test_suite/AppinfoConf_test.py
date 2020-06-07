"""
设置HRS_RESOURCES_ROOT为 fdconfig 的父目录才能执行本用例！
HRS_RESOURCES_ROOT=$PWD/resources pytest AppinfoConf_test.py
"""
import os
import sys
import time

import pytest

from feedwork.AppinfoConf import appinfo as prjInfo


def test_usable():
    assert prjInfo.project_name == "test fdcore"
    assert prjInfo.version == None
    assert prjInfo['global'] == "world"
    assert prjInfo.nums == 10
    assert prjInfo.money == -0.30
    assert prjInfo.flag == True
    assert prjInfo.show == False

    assert prjInfo.info.fetch_size == 200
    assert prjInfo.info.max_result_rows == -1
    assert prjInfo.info.show_conn_time == True

    assert prjInfo.databases[0]['name'] == "default"


if __name__ == "__main__":
    pytest.main(["-q", os.path.basename(sys.argv[0])])
