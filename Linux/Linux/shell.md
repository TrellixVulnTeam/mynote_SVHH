shell

### shell脚本 打印 *号被转义
用shell脚本开发数据库相关操作脚本时，发现一个问题
``` sh
a='select * from table1'
echo $a
```
运行结果居然是：
select test.log test.sh from table1

这里的test.log 和test.sh 是当前目录下的所有文件。。。。
经过查询发现shell脚本默认把 ‘*’ 转义成当前目录下的文件了。。。
要是想跳过这个操作，只需要在引用时把参数用双引号引起来既可
``` sh
a='select * from table1'
echo "$a"
```