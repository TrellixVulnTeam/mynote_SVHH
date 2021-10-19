# python模块发布

## 目录结构
```bash
❯ ls
data  __init__.py  LICENSE  README.md  setup.cfg  setup.py  src  tests
❯ tree
.
├── data
│   └── example.csv
├── __init__.py
├── LICENSE
├── README.md
├── setup.cfg
├── setup.py
├── src
│   ├── checkfilecode.py
│   ├── dataintodatabase.py
│   ├── __init__.py
│   └── __main__.py
└── tests

3 directories, 10 files
```

## 打包命令
```bash
python3 -m build
```
或者
```bash
python3 setup.py sdist bdist_wheel
```
开发时为了避免重复安装写好的wheel包，可以使用下面命令直接链接到新写的包
```python
python setup.py develop
```
删除链接
```python
python setup.py develop -u
```
## 在家目录创建.pypirc文件
创建完该文件后用twine上传模块就不需要输入用户名密码了
```bash
❯ cat .pypirc
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = qinxuan
password = 123qwe*90OP
```
## 打包好的模块上传到pypi
```bash
twine upload dist/*
```

## cython编译模块
setup.py文件
```python
from distutils.core import setup
from Cython.Build import cythonize

setup(name='nokia',
      ext_modules=cythonize("nokiaOmcQuery.pyx"))
```
执行
```python
python setup.py build_ext --inplacecd
```