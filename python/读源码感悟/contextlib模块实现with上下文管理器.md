# contextlib模块实现with上下文管理器
```python
import contextlib


@contextlib.contextmanager
def open_file(file_name):
    print("将要打开文件")
    yield {}
    print('关闭文件')


with open_file('aaa.txt') as f:
    print("正在处理文件")

```