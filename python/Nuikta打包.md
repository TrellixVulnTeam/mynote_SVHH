# Nuikta打包
Python源码：
```Python
def printer():
    print('hello niutka')

if __name__ == '__main__':
    printer()
```
打包命令：
```cmd
nuitka --mingw64 --standalone --show-progress --show-memory  --output-dir=out .\hello.py
```
生成的hello.dist目录25M，将整个目录拷贝到没有Python环境的电脑可以运行。
将编译后的hello.exe二进制文件在自己电脑上随意移动也可以运行。
Python源码：
```python
import numpy as np
print(np.array([1,2,3]))
```
打包命令：
```cmd
nuitka --mingw64 --standalone --show-progress --show-memory  --nofollow-import-to=numpy --plugin-enable=numpy --output-dir=out .\hello.py
```
打包后需要把依赖的numpy包复制到hello.exe同级目录下。
生成的hello.dist目录85M，将整个目录拷贝到没有Python环境的电脑可以运行。
Python源码：
```python
import pandas as pd
df = pd.DataFrame([[1,2,3],[4,5,6]],index=['a','b'],columns=['one','two','three'])
print(df)
```
打包命令：
```cmd
nuitka --mingw64 --standalone --show-progress --show-memory  --nofollow-import-to=pandas --plugin-enable=numpy --output-dir=out .\hello.py
```
打包后执行hello.exe根据提示将依赖的三方库拷贝到hello.exe同级目录下。
Python源码：
```python
from need import mdl

mdl.my_module()
```
目录结构
.
├── __init__.py
├── main.py
└── need
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc
    │   └── mdl.cpython-39.pyc
    └── mdl.py

打包命令：
  ```cmd
nuitka --mingw64 --standalone --show-progress --show-memory --follow-import-to=need  --output-dir=../out .\main.py
  ```