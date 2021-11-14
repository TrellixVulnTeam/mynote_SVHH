# bisect模块
bisect模块时python自带的模块。
该模块的insort方法可以自动维护一个已排序的序列
```python
import bisect


int_list = []

bisect.insort(int_list, 3)
bisect.insort(int_list, 10)
bisect.insort(int_list, 19)
bisect.insort(int_list, 1)
bisect.insort(int_list, 5)


print(int_list)
```

[1, 3, 5, 10, 19]