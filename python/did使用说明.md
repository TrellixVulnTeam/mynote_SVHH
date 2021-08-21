# python命令行工具快速生成csv文件入库脚本

日常工作中经常会遇到大量数据分析，当数据量超过excel所能容纳的行数时，分析数据变得困难，此时就需要将数据导入到数据库中分析，此处推荐使用PostgreSQL数据库，windows版本安装包不是太大，部署起来也方便。

当数据量大到excel打不开时，怎么快速编写入库脚本文件比较棘手。推荐大家使用python编写的命令行工具来实现入库脚本的自动生成。
## <table><tr><td bgcolor=green> <font color=white>   功能介绍    </font></td></tr></table>

实现csv文件入库PostgreSQL数据库时自动生成入库语句。

## <table><tr><td bgcolor=green> <font color=white>   特色功能    </font></td></tr></table>

注：PostgreSQL对文件编码有要求，如果文件编码格式和入库脚本指明的编码格式不一致会导致乱码。

使用过程中不需要关心待入库文件的编码格式，程序会自动识别编码格式，并生成对应编码格式的入库语句。


## <table><tr><td bgcolor=green> <font color=white>   注意事项 </font></td></tr></table>

生成的SQL入库语句每列的数据类型均采用文本方式，不对类型进行猜测。如需对字段类型进行转换，可在入库后使用sql语句转换成自己需要的类型。
待入库的csv文件的路径不能有中文，否则PostgreSQL无法识别。

## <table><tr><td bgcolor=green> <font color=white>   使用方法    </font></td></tr></table>

查看帮助信息

命令行界面输入did -h查看工具帮助信息

```
usage: postgresql入库工具 [-h] -t TABLENAME -f FILENAME [-v]

postgresql入库工具

optional arguments:
  -h, --help            show this help message and exit
  -t TABLENAME, --tablename TABLENAME
                        需要建的表名
  -f FILENAME, --filename FILENAME
                        待入库的文件名
  -v, --version         版本信息
```

## <table><tr><td bgcolor=green> <font color=white>   参数说明  </font></td></tr></table>

-t 表示需要创建的表名， -f 表示需要入库的csv文件名
两个参数的位置可以<font color=red>**随意调换位置**</font>,如下两种写法效果一样。
```linux
did -f example.csv -t example
did -t example -f example.csv
```


## <table><tr><td bgcolor=green> <font color=white>   使用举例   </font></td></tr></table>

-t参数后面输入的待入库文件的路径可以写<font color=red>**绝对路径**</font>也可以写<font color=red>**相对路径**</font>，生成脚本时程序会自动转换为绝对路径。

以下三种文件路径写法生成的脚本内容一样。

```sql
❯ did -f .\example.csv -t example
------------------------------------------------------------------------------------------
CREATE TABLE example
(
City text,
State text,
Population text,
Latitude text,
Longitude text
);
COPY example FROM 'F:\file\tmp\example.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
------------------------------------------------------------------------------------------
```

```sql
❯ did -f example.csv -t example
------------------------------------------------------------------------------------------
CREATE TABLE example
(
City text,
State text,
Population text,
Latitude text,
Longitude text
);
COPY example FROM 'F:\file\tmp\example.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
------------------------------------------------------------------------------------------
```

```sql
❯ did -f F:\file\tmp\example.csv -t example
------------------------------------------------------------------------------------------
CREATE TABLE example
(
City text,
State text,
Population text,
Latitude text,
Longitude text
);
COPY example FROM 'F:\file\tmp\example.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
------------------------------------------------------------------------------------------
```
## <table><tr><td bgcolor=green> <font color=white>   命令安装   </font></td></tr></table>
```
pip install python-tool-qinxuan
```