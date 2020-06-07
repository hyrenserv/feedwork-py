# feedwork
python 项目的公共包。

| 包            | 工具类  | 功能           | 详细说明                                |
| -------------- | ---------- | ---------------- | ------------------------------------------- |
| utils | logger     | 日志处理     | from feedwork.utils import logger <br> logger.debug("......") |
| utils | Constant   | 定义程序中的常量 | import feedwork.utils.Constant as const <br> const.NAME = "fd" # 定义了一个常量 |
| utils | DateHelper | 日期时间处理 | import feedwork.utils.DateHelper as dateu <br> dateu.sys_date()  # 得到系统当前日期 |
| utils | FileHelper | 文件处理 | import feedwork.utils.FileHelper as fileu <br> fileu.linecount()  # 得到文件行数 |
| utils | System | 操作系统环境处理 | import feedwork.utils.System as sysu <br> PATH = sysu.env("PATH", str)  # 得到PATH环境变量 |

## 安装
### 开发环境的安装方式
```shell
python3 -m pip install -U git+http://139.9.126.19:38111/FdcoreHyren/feedwork-py.git
```

### 部署发布的安装方式

1. 构建模块：python3 setup.py build。完成后会多出来一个build目录
2. 生成发布压缩包：python3 setup.py sdist。完成后会在dist目录下生成一个gz压缩文件
3. 把该gz文件上传需安装的主机，解压文件并进入解压目录，执行：python3 setup.py install

## 源码测试
1. 安装pytest： python3 -m pip install pytest
2. 运行测试用例
  * 命令行方式： pytest xxx.py（不指定文件则运行所有测试用例）
  * PyCharm方式： File -> setting -> Python Integrated Tools - Default test runner 的下拉框中选 pytest
