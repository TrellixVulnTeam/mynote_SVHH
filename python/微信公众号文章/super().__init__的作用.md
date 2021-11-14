# super().__init__的作用
Python面向对象编程时，当一个class继承了另一个class时候，经常会看到在子类的init方法中有一句super().__init__代码，这句代码有什么作用呢，下面我们举例说明下。
## 不使用super().\_\_init__
```python
class Person:
    def __init__(self):
        self.x = '父类的属性'

    def func(self):
        print("父类的方法")


class Student(Person):
    def __init__(self):
        self.y = '子类的属性'


if __name__ == '__main__':
    s = Student()
    print(s.y)
    s.func()
    print(s.__dict__)
```
以上代码执行时输出结果为：
```text
子类的属性
父类的方法
{'y': '子类的属性'}
```
当我要打印出父类的属性x时，就会报错
```python
print(s.x)
```
```text
AttributeError: 'Student' object has no attribute 'x'
```
从上面打印s.__dict__的结果我们也看到了Student对象确实没有x这个属性。但在日常编码中我们经常会用到父类的属性值的情况，这个时候就需要super().__init__登场了。。。
## 使用super().\_\_init__
```python
class Person:
    def __init__(self):
        self.x = '父类的属性'

    def func(self):
        print("父类的方法")


class Student(Person):
    def __init__(self):
        super().__init__()
        self.y = '子类的属性'


if __name__ == '__main__':
    s = Student()
    print(s.y)
    s.func()
    print(s.x)
    print(s.__dict__)

```
以上代码执行时输出结果为：
```text
子类的属性
父类的方法
父类的属性
{'x': '父类的属性', 'y': '子类的属性'}
```
我们可以看到，输出的结果中正确的将父类的属性打印了出来，在__dict__中显示确实有父类的属性这个成员。
## 总结
通过以上两个例子我们可以看出在子类中调用父类的__init__方法可以确保实例化后对象可以访问父类的属性，因此在编码时最好写上super().\_\_init__()。