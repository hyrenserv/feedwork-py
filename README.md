# feedwork
python 项目的公共包

## 安装
### 开发环境的安装方式
```shell
python3 -m pip install git+http://139.9.126.19:38111/hyren/feedwork-py.git
```

### 部署发布的安装方式

1. 构建模块：python3 setup.py build。完成后会多出来一个build目录
2. 生成发布压缩包：python3 setup.py sdist。完成后会在dist目录下生成一个gz压缩文件
3. 把该gz文件上传需安装的主机，解压文件并进入解压目录，执行：python3 setup.py install
