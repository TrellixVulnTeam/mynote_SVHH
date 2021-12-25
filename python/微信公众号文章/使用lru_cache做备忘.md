# 使用lru_cache缓存相同的计算过程
functools.lru_cach 是非常实用的装饰器，它实现了缓存功能。这是一项优化技术，它把耗时的函数结果保存起来，避免传入相同的参数时重复计算。LRU三个字母是“Least Recently Used”的缩写，表明缓存不会无限增长，一段时间不用的缓存条目会被清理掉。
在生成第N个斐波那契数这种慢速递归函数时适合使用lru_cache。
## 不使用lru_cache装饰器
```python
import time
import functools

def fibonacci(n):
    print('函数调用---> fibonacci(%s)' % n)
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    n=6
    print('第%s个斐波那契数为:%s' % (n,fibonacci(n)))
```
输出结果：
```text
函数调用---> fibonacci(6)
函数调用---> fibonacci(4)
函数调用---> fibonacci(2)
函数调用---> fibonacci(0)
函数调用---> fibonacci(1)
函数调用---> fibonacci(3)
函数调用---> fibonacci(1)
函数调用---> fibonacci(2)
函数调用---> fibonacci(0)
函数调用---> fibonacci(1)
函数调用---> fibonacci(5)
函数调用---> fibonacci(3)
函数调用---> fibonacci(1)
函数调用---> fibonacci(2)
函数调用---> fibonacci(0)
函数调用---> fibonacci(1)
函数调用---> fibonacci(4)
函数调用---> fibonacci(2)
函数调用---> fibonacci(0)
函数调用---> fibonacci(1)
函数调用---> fibonacci(3)
函数调用---> fibonacci(1)
函数调用---> fibonacci(2)
函数调用---> fibonacci(0)
函数调用---> fibonacci(1)
第6个斐波那契数为:8
```
fibonacci递归函数的整个调用过程如上所示，统计可知大部分存在重复调用的情况。当计算第N位的斐波那契数N越大时候函数耗时指数级增长。
|           函数            | 调用次数 |
| ------------------------- | -------- |
| 函数调用---> fibonacci(1) | 8        |
| 函数调用---> fibonacci(0) | 5        |
| 函数调用---> fibonacci(2) | 5        |
| 函数调用---> fibonacci(3) | 3        |
| 函数调用---> fibonacci(4) | 2        |
| 函数调用---> fibonacci(5) | 1        |
| 函数调用---> fibonacci(6) | 1        |
## 使用lru_cache装饰器
```python
import time
import functools

@functools.lru_cache()
def fibonacci(n):
    print('函数调用---> fibonacci(%s)' % n)
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    n=6
    print('第%s个斐波那契数为:%s' % (n,fibonacci(n)))

```
输出结果：
```text
函数调用---> fibonacci(6)
函数调用---> fibonacci(4)
函数调用---> fibonacci(2)
函数调用---> fibonacci(0)
函数调用---> fibonacci(1)
函数调用---> fibonacci(3)
函数调用---> fibonacci(5)
第6个斐波那契数为:8
```
当使用了lru_cache()装饰器后，计算相同位置的斐波那契数，函数调用的次数大大减少（不存在同一个值多次调用的情况），这将大大减少整个计算过程的执行时间。

注意，必须像常规函数那样调用 lru_cache。这一行中有一对括号：@functools.lru_cache()。这么做的原因是，lru_cache 可以接受配置参数。lru_cache 可以使用两个可选的参数来配置：
```python
functools.lru_cache(maxsize=128, typed=False)
```
maxsize 参数指定存储多少个调用的结果。缓存满了之后，旧的结果会被扔掉，腾出空间。为了得到最佳性能，maxsize 应该设为 2 的幂。typed 参数如果设为 True，把不同参数类型得到的结果分开保存，即把通常认为相等的浮点数和整数参数（如 1 和 1.0）区分开。顺便说一下，因为 lru_cache 使用字典存储结果，而且键根据调用时传入的定位参数和关键字参数创建，所以被 lru_cache 装饰的函数，它的所有参数都必须是可散列的。
