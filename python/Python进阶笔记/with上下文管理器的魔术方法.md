# with上下文管理器的魔术方法
```python
class WithTest:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print('do somthing')


if __name__ == '__main__':
    with WithTest() as wt:
        wt.do_something()
```

自定义的类中只要实现了__enter__ __exit__两个魔术方法，该类便可以使用上下文管理器方式访问