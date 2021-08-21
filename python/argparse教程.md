# argparse教程
## metavar参数
```python
def arg(self):
        parser = argparse.ArgumentParser(description="Process some integers.")
        #metavar的作用是提供参数示例：usage: arg.py [-h] [--sum] 1,2,3,4 [1,2,3,4 ...]
        parser.add_argument('integers', metavar='N', type=int, nargs='+',
                            help='an integer for the accumulator')
        
        parser.add_argument('--sum', dest='accumulate', action='store_const',
                            const=sum, default=max,
                            help='sum the integers (default: find the max)')
        args = parser.parse_args()

        return args
❯ python3 arg.py
usage: arg.py [-h] [--sum] N [N ...]
arg.py: error: the following arguments are required: N
```
## nargs
```python
def arg_nargs(self):
        parser = argparse.ArgumentParser()
        # 加-- foo是个可选参数，只能是2个参数
        parser.add_argument('--foo', nargs=2)
        #不加-- bar这个位置参数是必须的且只能是一个，输入的bar参数为到一个列表里面，列表长度为1
        parser.add_argument('bar', nargs=1)
        p = parser.parse_args()
        return p
❯ python3 arg.py dd --foo a b
Namespace(bar=['dd'], foo=['a', 'b'])
```
```python
def arg_nargs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--foo', nargs='?', const='c', default='d')
        parser.add_argument('bar', nargs='?', default='d')
        p = parser.parse_args()
        return p
#有const 参数nargs必须用？，上面结果生成的参数列表是字符串，不使用--foo的时候使用默认值d 带了--foo单没有指定参数时候使用c
❯ python3 arg.py f
Namespace(bar='f', foo='d')
❯ python3 arg.py f --foo
Namespace(bar='f', foo='c')
❯ python3 arg.py f --foo e
Namespace(bar='f', foo='e')
❯ python3 arg.py
Namespace(bar='d', foo='d')
```
允许可选的输入或输出文件:
```python
def arg_nargs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('infile', nargs='?', type=argparse.FileType('r',encoding='gbk'),default=sys.stdin)
        parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),default=sys.stdout)
        p = parser.parse_args()
        return p
❯ python3 arg.py input.txt output.txt
Namespace(infile=<_io.TextIOWrapper name='input.txt' mode='r' encoding='gbk'>, outfile=<_io.TextIOWrapper name='output.txt' mode='w' encoding='UTF-8'>)
❯ python3 arg.py
Namespace(infile=<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>, outfile=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)
```
\* 所有当前命令行参数被聚集到一个列表中。注意通过 nargs='*' 来实现多个位置参数通常没有意义，但是多个选项是可能的
```python
def arg_nargs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--foo', nargs='*')
        parser.add_argument('--bar', nargs='*')
        parser.add_argument('baz', nargs='*')
        p = parser.parse_args()
        return p
❯ python3 arg.py
Namespace(bar=None, baz=[], foo=None)
❯ python3 arg.py aa
Namespace(bar=None, baz=['aa'], foo=None)
❯ python3 arg.py aa --bar dss
Namespace(bar=['dss'], baz=['aa'], foo=None)
❯ python3 arg.py aa --bar dss --foo adf
Namespace(bar=['dss'], baz=['aa'], foo=['adf'])
❯ python3 arg.py aa --bar ds s --foo adf
Namespace(bar=['ds', 's'], baz=['aa'], foo=['adf'])
❯ python3 arg.py aa --bar ds s --foo ad f
Namespace(bar=['ds', 's'], baz=['aa'], foo=['ad', 'f'])
```
+和\*类似，只不过用+的话如果不提供位置参数会报错，用\*号 不提供位置参数不报错 默认为空列表
```python
def arg_nargs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('foo', nargs='+')
        p = parser.parse_args()
        return p
❯ python3 arg.py
usage: arg.py [-h] foo [foo ...]
arg.py: error: the following arguments are required: foo
❯ python3 arg.py dd
Namespace(foo=['dd'])
❯ python3 arg.py dd
Namespace(foo=['dd'])
❯ python3 arg.py
Namespace(foo=[])
```
对于比较长的命令行选项可以把内容写到文件里面
```python
def arg_nargs(self):
        with open('args.txt', 'w') as fp:
            fp.write('-f\nbar')
        parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
        parser.add_argument('-f')
        p = parser.parse_args()
        return p
❯ cat args.txt
-f
bar%
❯ ls
arg.py  args.txt  input.txt  output.txt
❯ python3 arg.py -f 10  @args.txt
Namespace(f='bar')
❯ python3 arg.py -f 10000  @args.txt
Namespace(f='bar')
❯ python3 arg.py -f 1000
Namespace(f='1000')
```
## action
action='store_const', const=42 要一起出现 好比是参数  --list作用
```python
def arg_nargs(self):
        parser = argparse.ArgumentParser(prog='PROG',allow_abbrev=True)
        parser.add_argument('--foo', action='store_const', const=42)
        p = parser.parse_args()
        return p
❯ python3 arg.py --foo 10
usage: PROG [-h] [--foo]
PROG: error: unrecognized arguments: 10
❯ python3 arg.py --foo
Namespace(foo=42)
```