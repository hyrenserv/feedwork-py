import os
import sys

import pytest

import feedwork.utils.System as sysu


def test_env():
    PATH = sysu.env("PATH", str)
    assert "/bin" in PATH
    assert "/usr/bin" in PATH
    assert "/usr/sbin" in PATH

    HRS_NUMS = sysu.env("HRS_NUMS_XXX", int)
    assert HRS_NUMS is None
    HRS_NUMS = sysu.env("HRS_NUMS_XXX", int, 0)
    assert HRS_NUMS == 0


if __name__ == "__main__":
    pytest.main(["-q", os.path.basename(sys.argv[0])])
