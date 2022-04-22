# Python字典一个键对应多个值
怎样实现一个键对应多个值的字典（也叫 multidict）？
一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中，比如列表或者集合里面。比如，你可以像下面这样构造这样的字典：
```python
d = {
'a' : [1, 2, 3],
'b' : [4, 5]
}
e = {
'a' : {1, 2, 3},
'b' : {4, 5}
}
```
选择使用列表还是集合取决于你的实际需求。如果你想保持元素的插入顺序就应该使用列表，如果想去掉重复元素就使用集合（并且不关心元素的顺序问题）。
你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。比如：
```python
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
```

## 实际应用
前几天遇到一个需求：将LTE网络的邻区关系进行行转列转换。源文件将近300万行，excel手动处理显然不现实。简单的问题模型如下：
原始表：
| 站号-源小区    |  CI-源小区   | 站号-目标小区    |  CI-目标小区   |
| --- | --- | --- | --- |
|  100   |   1  |  200   |    1 |
|   100  |   1  |  200   |   2  |
|  100   |  1  |    200 |   3  |

目标表：
| 源小区 |        邻小区        |
| ------ | ------------------- |
| 100_1  | 200_1\|200_2\|200_3 |

在这个实际应用中就关键点就是要生成一个多值字典，键为源小区，值为邻小区用“|”连接起来的字符串。python的collections 模块 中的defaultdict就可以满足这个需求。代码实现过程如下：
```python
import csv
import time
from collections import defaultdict


def handle_csv(csv_file):
    d = defaultdict(list)
    with open(csv_file, "r") as f_csv:
        rows = csv.reader(f_csv)
        for row in rows:
            d[row[0] + "_" + row[1]].append(row[2] + "_" + row[3])
    return d


def write_csv(multidict):
    with open("result.csv", "w", newline='') as f_csv:
        writer = csv.writer(f_csv)
        for k, v in multidict.items():
            lst = [k, ("|".join(v))]
            writer.writerow(lst)


if __name__ == "__main__":
    start = time.time()
    dic = handle_csv("cx.txt")
    write_csv(dic)
    end = time.time()
    print('Time taken: {:.3} seconds'.format(end - start))

```
Output:
```text
Time taken: 3.21 seconds
```
针对300万行的邻区数据3秒中就处理完毕，defaultdict的性能还是可以的。