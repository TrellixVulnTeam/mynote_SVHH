csvtk使用方法

### csvtk使用前注意

- csvtk处理时默认会**自动保留表头**。认为csv文件的第一行为header信息，如果没有header，需指定参数`-H`
- 默认是处理以`,`作为分割的csv文件，**处理`\t tab`分割的tsv文件**，指定参数`-t`
- csv文件默认每行(rows)都有相同的列数(columns)，`-I/--ignore-illegal-row`跳过这些错误行
- csv文件每列(columns)的名字不重复。
- 默认会忽略`#`，指定header的符号`-C`
- 若每列中存在双引号`""`，指定参数`-1`

------

### 文件基本信息（Information）

##### 1. `headers` 只显示表头

##### 2. `dim` 显示csv文件的每行每列数目

##### 3. `summary` 可根据分组信息(group_by)对每列(columns)进行数学统计

**类似于R中dplyr包中的summary函数**，其中**对数字进行的数学统计**包括countn（统计数字有多少）, min, max, sum, mean, stdev, variance, median, q1, q2, q3, entropy, prod,**对字符文本**的包括：count（计数）, first, last, rand（随机取值）, uniq（去重）, collapse（转为以;的一行信息）, countunique(uniq之后计数有多少)。基本用法：`csvtk summary -f 2:sum`

- `-f 2/column_name2:sum/mean...` 指定第几列进行统计，可进行多列统计。
- `-i` 忽略列中的非数字缺失值NA
- `-g` 类似于dplyr中的group_by，根据某列进行分组统计。
- `-n 2` 保留几位小数
- `-S 11` 设置随机种子
- `-s ;` 设置collapse的为一列时的分割符号



```ruby
## 第四列 总和
cat digitals2.csv  | csvtk summary -f f4:sum

## 多列进行计算，忽略NA
cat digitals2.csv | csvtk summary -f f4:sum,f5:sum -i
cat digitals2.csv | csvtk summary -f 4:sum,5:sum -i

## 分组统计
cat digitals2.csv | csvtk summary -i -f f4:sum,f5:sum -g f1,f2 | csvtk pretty
## 去第一行header
cat digitals2.csv|csvtk summary -f 4:sum -f 5:sum -i -g 1,2|sed 1d

## 分组统计多个信息：
cat digitals2.csv | csvtk summary -i -g f1 -f f4:countn,f4:mean,f4:stdev,f4:q1,f4:q2,f4:mean,f4:q3,f4:min,f4:max
cat digitals2.csv | csvtk summary -i -g f1 -f f4:collapse,f4:max|csvtk pretty
```

------

### 格式转变

##### 1. `pretty` 方便阅读的展示方式。

- `-r` 靠右对齐
- `-s` 指定分割符号 " | "

##### 2. `transpose` 对数据进行转置，行列转换

##### 3. `space2tab` 以空格分割的转为tab分割的。

##### 4. `csv2md` csv/tsv转变为markdown格式。

##### 5. `csv2json` csv转变为json格式

##### 6. `xlsx2csv` 对EXCEL的xlsx文件转换为csv文件

- `-a` 显示所有的附表sheets
- `-i 2` 对第几个附表进行操作。 `csvtk xlsx2csv accounts.xlsx -i 3`
- `-n` 根据附表的名字进行提取。

------

### 集合操作 set operation

##### 1. `head` 显示前n行，包括表头header

##### 2. `concat` concatenate。对多个tsv/csv表根据表头columns对行rows合并。

只保留第一个表的header，类似于dplyr中的`left_join()`。

- `-i` 每个表的表头column_name忽略大小写。
- `-u NA` 未匹配到的空的数据以任意"NA"表示
- `-k` 保留未匹配到合并的数据，以`-u`字符表示



```objectivec
## 合并col_names相同的表
csvtk concat names.csv names.reorder.csv |csvtk pretty

## 忽略大小写，保留空的行，以"NA"表示
csvtk concat names.csv names.with-unmatched-colname.csv -i -u NA | csvtk pretty
```

##### 3. `sample` 随机取一定比例的行数

- `-p 0.1` 取的比例
- `-s 10` 设置随机种子，默认11。`seq 100 | csvtk sample -H -p 0.1 -s 1`
- `-n` 显示随机的行rownames名，

##### 4. `cut` 取指定列columns，

类似于dplyr中的`select`，或者linux中进阶的`cut`。

- `-f 1,2 || colA,colB` 根据数字 or col_name来选指定列。可反选 `-f -1,-2`
- `-i` 忽略col_name中的大小写
- `-F` 允许部分正则匹配 `*name`



```bash
## 根据表头column名进行挑选
cat names.csv |csvtk cut -f first_name,username

## 选第2~4列
cat names.csv | csvtk cut -f 2-4

## 反选，即除了第一，二列
cat names.csv | csvtk cut -f -1,-2
cat names.csv | csvtk cut -f -username

## 允许部分正则匹配的 * 
cat names.csv | csvtk cut -f "*_name"
```

##### 5. `uniq` 对指定多列自动排序去重复

等同于Linux中的`sort | uniq`

##### 6. `freq`对指定列去重复，顺便计数排序。

等同于Linux中的`sort |uniq -c`。`-f`,`-F`,`-i`同`cut`子命令

- `-n` 根据计数从小到大排序
- `-k` 根据名字key排序
- `-r` 反过来



```bash
### 对第二列排序，并按照frequency的数值从大到小排列
cat names.csv |csvtk freq -f 2 -nr
```

##### 7. `inter` 多个文件之间的交集。

`-f`, `-F`, `-i`等同于`cut`子命令。

##### 8. `grep` 对指定列进行key的正则匹配提取

类似于dplyr中的`filter()`函数对某column的字符串chr进行匹配操作。

- `-f` 指定列的col_name，1-3列
- `-p pattern` 搜索提取的pattern
- `-P` 提取pattern的文件，多个pattern进行提取
- `-i` 忽略大小写
- `-v` 反向匹配。
- `-r` 支持正则匹配
- `-n` 显示提取的行号。



```ruby
cat names.csv | cavtk grep -f 1 -ir -p rob |csvtk pretty 

## 对names.csv的first_name随机取几个名子作为file，再对names.csv文件根据文件进行提取
cat names.csv |csvtk cut -f 3 |sed 1d|csvtk sample -p 0.5 -H| csvtk grep -f 3 -ir -P - names.csv |csvtk pretty
```

##### 9. `filter` 利用数学公式，对指定列进行数值的过滤提取。

类似于dplyr中的`filter()`函数对数值的处理方式。

- `-f 1,2>0` 对指定列进行数值的过滤
- `--any` 多列进行过滤，满足任意一列条件皆保留。
- `-F`, `-n`



```bash
## 第1~3列任意列大于0即保留。
cat  digitals.tsv | csvtk -t -H filter -f "1-3>0" --any
```

##### 10. `filter2`类似于awk的数据过滤方式。

支持awk中的数值/表达式，按指定多列的数值进行过滤。



```dart
## id列大于3
cat names.csv | csvtk filter2 -f '$id > 3'

## id列大于3 或 username列 为 "ken"
cat names.csv | csvtk filter2 -f ' $id > 3 || $username == "ken" '

## other arithmatic expressions
cat digitals.tsv | csvtk filter2 -H -t -f '$1 > 2 && $2 % 2 == 0'

cat digitals.tsv | csvtk filter2 -H -t -f '$2 <= $3 || ( $1 / $2 > 0.5 )'
```

##### 11. `join` 对多个文件按指定列进行合并。

类似concat？或者dplyr中的`left_join()`

- `-f` 按第一个文件指定列进行合并，文件中的col_name名不用完全相同。若指定匹配的列 以`-f "colA_1;colB_2"`表示。
- `-k -fill NA` 保留未匹配的，以NA表示。



```csharp
csvtk join {1,2,3}.csv -f name -k
csvtk join {3,1,2}.csv -f name -k
```

##### 12. `split` 根据指定column的value进行分割文件。

- `-f 1~3 || columnA` 指定列以factor方式分割文件
- `-o` 对分割的文件指定输出文件夹



```bash
### 根据first_name, last_name分割文件
csvtk split names.csv -f first_name,last_name

### 分割输出到result文件夹
seq 100 | csvtk split -H -o result
```

##### 13. `splitxlsx` 类似于split，对xlsx表内按照列column进行分割出多个文件。

------

### 文件的内容编辑相关

##### 1. `add-header` 添加列的名字。`-n a,b,c`

##### 2. `del-header` 删除列的名字

##### 3. `rename` 对column名修改

- `-f 1,2` 指定列进行改名
- `-n a,b` 对指定列进行改名。



```ruby
## 对A,B列进行改名
cat phones.csv | csvtk rename -f A,B -n a,b | csvtk pretty
```

##### 4. `rename2` 正则匹配来对指定多列名进行修改。

类似于dplyr中的rename_all() `iris %>% rename_all(tolower) %>% rename_all(~str_replace_all(., "\\.", "_"))`

- `-f` 指定列进行修改。
- `-p` 正则匹配的字符。
- `-r` 修改过后的字符。'${1}'的使用 '{nr}', '{nk}'
- `-k` 按照指定key-value的文件进行改名。
- `-K` 保留-k中未匹配的到的列名



```bash
### 对所有的列名进行修改，添加prefix_${1}_suffix
cat phones.csv | csvtk rename2 -F -f "*" -p '(.*)' -r 'prefix_${1}_suffix'

### 根据barcodes的key-value对应关系 来 对tables.tsv进行改列名。
csvtk cut -t barcodes.tsv -f 2,1 | csvtk rename2 -t -F -f "*" -k - -p '(.+)' -r '{kv}' -K tables.tsv

### 改列名利用增长的1~n
echo "a,b,c,d" | csvtk rename2 -f 2-4 -p '(\w+)' -r 'seq_{nr}' --start-num 2
```

##### 5. `replace` 根据正则匹配对指定多列进行替换编辑

类似于rename的一些操作。

- `-F -f "*"`指定所有列
- `-p pattern` 正则匹配的pattern
- `-r` 替换的string，支持${1}自动捕获，{nr}，{nk}
- `-k` 可根据key-value的文件进行批量替换
- `-K` -k中保留未匹配的文字。



```csharp
###删除文件中的汉字
csvtk replace -F -f "*_name" -p "\p{Han}+" -r ""

### 根据key-value的文件进行匹配替换，时刻记住处理tsv文件加参数 -t

csvtk replace -t -f 2 -p 'ID(\d+)' -r '{kv}' -K -k alias.txt data.tsv
```

##### 6. `mutate` 根据正则匹配创建新的一列

类似于dplyr中的`mutate()`

- `-f` 指定列,`-i`ignore case
- `-p pattern` 对列的内容 利用正则匹配捕获
- `-n` 添加新列的新的名字



```bash
### 复制新列
csvtk mutate -f id -n newname

### 对username列 的第一个字母进行匹配，以新列展示
cat phones.csv | csvtk mutate -f 1 -p '^(\w)' -n 'first_name' | csvtk pretty
```

##### 7. `mutate2` 类似于awk的方式创建新的列

- `-e` awk类似的表达式， 连接，数值的相加等~
- `-L 2` 数值计算时，默认保留2位小数。
- `-s` 将数值num当字符chr



```dart
### 添加新列
cat digitals.tsv |csvtk mutate2 -t -H -e ' "a" '

### 添加新列，自建变量
var=123
cat digitals.tsv |csvtk mutate2 -t -H -e "$var"

### 两列进行连接
cat names.csv | csvtk mutate2 -n full_name -e ' $first_name + " " + $last_name'

### 数值的相加
cat digitals.tsv | csvtk mutate2 -t -H -L 0 -e ' $1 + $2 '

### 相比较
cat digitals.tsv | csvtk mutate2 -t -H -L 0 -e ' $1 >5 ? "big":"small" '
```

##### 8. `gather` 表格的整理

类似于tidyr中的`gather()`函数，对相同的列数据进行整理。



```csharp
cat names.csv | csvtk gather -f -1 -k name -v value 
```

------

### 排序

##### `sort` 对指定列 排序

- `-i` 忽略大小写
- `-k` 对指定列排序 `-k 1:N/n/u/r`



```ruby
### 对指定列排序
cat names.csv | csvtk sort -k first_name | csvtk pretty

### 对指定列倒序
cat names.csv | csvtk sort -k first_name:r | csvtk pretty

### 对指定列按数值排序,倒序
cat names.csv | csvtk sort -k first_name:nr | csvtk pretty

### 按自然顺序排序N
echo "X,Y,1,10,2,M,11,1_c,Un_g,1_g" | csvtk transpose | csvtk sort -H -k 1:N

### 按多列进行排序
cat names.csv | csvtk sort -k first_name -k id:n
```

##### `plot` 画一些通常的直方图，箱线图，散点图。

- `csvtk plot hist`
- `csvtk plot box`
- `csvtk plot line`

足够强大的工具！推荐学习使用！