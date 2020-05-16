import pytest
import os
import feedwork.utils.FileHelper as fileu


def test_linecount():
    filepath = "/tmp/xxx"
    ftext = f"\nlksdjf\n88888888\n "
    fileu.write(filepath, ftext)
    assert fileu.linecount(filepath) == 4


def test_size():
    filepath = "/tmp/xxx"
    fileu.write(filepath, "ftext\r\n")
    assert fileu.size(filepath) == 7
    assert fileu.size(filepath, readable=True) == f"{7 / 1024:.2f} KB"

    ftext = ""
    n_line = 1024  # 生成的文件的行数
    for i in range(1024):
        ftext += f"{i:10d}\n"  # 每行11个字符
    text_size = 11 * n_line
    fileu.write(filepath, ftext)
    assert fileu.size(filepath) == text_size
    assert fileu.size(filepath, readable=True) == f"{text_size / 1024:.2f} KB"


def test_write():
    filepath = "/tmp/xxx1"
    fileu.write(filepath, "")
    assert os.path.exists(filepath)

    fileu.write(filepath, "1\n ", append=True)
    fileu.write(filepath, " \n", append=True)

    with open(filepath) as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0] == "1\n"
        assert lines[1] == "  \n"
