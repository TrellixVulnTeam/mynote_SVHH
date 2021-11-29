# \_\_bool\_\_()方法
Python中有很多关于真假性的定义。参考手册中列举了许多和False等价的值：0、''、()、[]和{}。其他大部分的对象都是和True等价。
通常，我们会用下面的语句来测试一个对象是否“非空”。
```python
if some_object:
    process(some_object)
```
默认情况下，这个是内置的bool()函数的逻辑。这个函数依赖于一个给定对象的__bool__()方法。
默认的\_\_bool\_\_()方法返回True。我们可以通过下面代码来验证。
```python
>>> x = object()
>>> bool(x)
True
```
对大多数类来说，这是完全正确的。大多数对象都不应该和False等价。但是，对于集合，这样的行为并不总是正确的。一个空集合应该和False等价。
```python
class Person:
    def __init__(self,*args):
        self.args = list(args)

    def __repr__(self):
        if len(self.args) >0:
            return '{__class__.__name__}{args!r}'.format(__class__= self.__class__, **self.__dict__)
        else:
            return '{__class__.__name__}[]'.format(__class__= self.__class__)

if __name__ == '__main__':
    p = Person('张三','李四')
    print(p)
    print(bool(p))
    
```
输出结果：
```text
Person['张三', '李四']
True
```
以上代码的逻辑是说的通的，p对象里面有两个人名，bool函数的结果也是为True的。如果p对象里面没有人名，那bool函数的结果会是False吗？
```python
class Person:
    def __init__(self,*args):
        self.args = list(args)

    def __repr__(self):
        if len(self.args) >0:
            return '{__class__.__name__}{args!r}'.format(__class__= self.__class__, **self.__dict__)
        else:
            return '{__class__.__name__}[]'.format(__class__= self.__class__)


if __name__ == '__main__':
    p = Person()
    print(p)
    print(bool(p))
```
输出结果：
```text
Person[]
True
```
可见在实例化时传入空值，得到的对象用bool函数检查结果一样为True。这就不合理了。
想要在实例化传入空值时，bool函数结果为False，就需要用到__bool__()方法。下面我们对Person类进行修改：
```python
class Person:
    def __init__(self,*args):
        self.args = list(args)

    def __repr__(self):
        if len(self.args) >0:
            return '{__class__.__name__}{args!r}'.format(__class__= self.__class__, **self.__dict__)
        else:
            return '{__class__.__name__}[]'.format(__class__= self.__class__)

    def __bool__(self):
        if len(self.args) > 0:
            return True
        else:
            return False

if __name__ == '__main__':
    p1 = Person('张三','李四')
    print(p1)
    print(bool(p1))
    print('-'*10)
    p2 = Person()
    print(p2)
    print(bool(p2))
```
输出结果：
```text
Person['张三', '李四']
True
----------
Person[]
False
```