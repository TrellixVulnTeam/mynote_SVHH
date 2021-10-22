# 对私有属性实现getter setter
```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


if __name__ == '__main__':
    p = Person('qinxuan', 30)
    print(p.age)
    p.age = 50
    print(p.age)
```