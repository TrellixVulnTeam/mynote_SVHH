# python OrderedDict用法


Python中的字典对象可以以“键：值”的方式存取数据。OrderedDict是它的一个子类，实现了对字典对象中元素的排序。比如下面比较了两种方式的不同：
```python
import collections
 
print 'Regular dictionary:'
d={}
d['a']='A'
d['b']='B'
d['c']='C'
for k,v in d.items():
    print (k,v)
 
print ('\nOrderedDict:')
d=collections.OrderedDict()
d['a']='A'
d['b']='B'
d['c']='C'
for k,v in d.items():
    print (k,v)
```
输出结果
```python
Regular dictionary:
a A
c C
b B
 
OrderedDict:
a A
b B
c C
```
可以看到，同样是保存了ABC三个元素，但是使用OrderedDict会根据放入元素的先后顺序进行排序。由于进行了排序，所以OrderedDict对象的字典对象，如果其顺序不同那么Python也会把他们当做是两个不同的对象，比如下面的代码：
```python
import collections
 
print ('Regular dictionary:')
d1={}
d1['a']='A'
d1['b']='B'
d1['c']='C'
 
d2={}
d2['c']='C'
d2['a']='A'
d2['b']='B'
 
print (d1==d2)
 
print ('\nOrderedDict:')
d1=collections.OrderedDict()
d1['a']='A'
d1['b']='B'
d1['c']='C'
 
d2=collections.OrderedDict()
d2['c']='C'
d2['a']='A'
d2['b']='B'
 
print  (d1==d2)
```
输出结果如下：
```python
Regular dictionary:
True
 
OrderedDict:
False
```