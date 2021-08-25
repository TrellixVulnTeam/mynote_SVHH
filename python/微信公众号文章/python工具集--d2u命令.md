# python工具集--d2u命令功能更新
日常工作中当对csv文件进行入库(PostgreSQL数据库)操作时，有时会遇到下方错误提示：
```sql
qx=# COPY nr_test FROM 'F:\file\tmp\nr1.csv' DELIMITER ',' CSV HEADER ENCODING 'GB18030';
错误:  在数据中找到了未用引号引起来的新行
提示:  使用用引号因起来的CSV字段来表示新行.
背景:  COPY nr_test, 行 2
```
产生以上错误的原因是待入库的文件--nr.csv的换行符为\r\n

windows、unix、mac系统的换行符是不同的，Unix下一般只有一个 0x0A 表示换行（"\n"），Windows 下一般都是 0x0D 和 0x0A 两个字符，即 0D0A（"\r\n"），苹果机（MAC OS系统）则采用回车符 CR 表示下一行（"\r"）。

Unix 系统中：每行结尾只有 "<换行>"，即 "\n"；

Windows 系统中：每行结尾是 "<回车><换行>"，即 "\r\n"；

Mac 系统中：每行结尾是 "<回车>"，即 "\r"。

而PostgreSQL数据库在对文件进行入库时，它只识别unix的换行符（“\n”）而对于大部分使用windows系统生成的文件，入库时候就会报上面的错误。

怎么解决这个问题呢，可以使用python工具集中的d2u命令，该命令可以将文档中的windows换行符（“\r\n”）替换为unix系统的换行符（“\n”）。替换后在入库就不会报错了。

## d2u命令使用说明
d2u命令是用python写的一个命令行工具，直接输入d2u回车会显示命令行的使用简介
```powershell
usage: 换行符转换 [-h] [-v] file [file ...]
换行符转换: error: the following arguments are required: file
```
输入d2u -h可以显示帮助信息
```powershell
usage: 换行符转换 [-h] [-v] file [file ...]

换行符转换

positional arguments:
  file           源文件

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  版本信息
```

输入d2u -v 可显示版本信息
```powershell
PS F:\file\tmp> d2u -v
换行符转换 0.0.2
```
### 使用举例
```powershell
PS F:\file\tmp> d2u .\nr1.csv .\nr2.csv .\nr3.csv .\nr4.csv
```
命令后面跟1个文件或多个文件均可以，多个文件的话程序会依次处理，处理完毕后，原始文件会增加.bk的后缀。
经过上面的处理，nr1.csv、nr2.csv、nr3.csv、nr4.csv文件就可以直接入库了，不会在报换行符的错误了。

