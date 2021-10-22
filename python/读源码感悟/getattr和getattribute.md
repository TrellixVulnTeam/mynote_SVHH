## __getattr__ 和__getattribute__
这两个魔术方法可以控制对象的属性访问，如果实现了__getattr__方法，当访问一个不存在的对象时会被调用
如果重写了__getattribute__方法，所有的属性访问都会由它处理接收
```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        if item == 'Name':
            return self.name
        else:
            return '没找到%s属性' % item

    def __getattribute__(self, item):
        return '入口在我这里'


if __name__ == '__main__':
    user = User('qinxuan', 30)
    print(user.name)
    print(user.Name)
```