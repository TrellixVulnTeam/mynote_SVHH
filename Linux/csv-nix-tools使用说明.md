# csv-nix-tools使用说明
## csv-add-concat
Read CSV stream from standard input and print it back to standard output with a new column produced by concatenation of columns and fixed strings.

-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
 head 用户常驻小区（日3夜3）.csv |csv-add-concat -s -- newname = %serv_number - %city_code -460

serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   newname
18739862113   202103   398         70192002   1             2               18739862113-398-460
18739862113   202103   398         64979212   2             2               18739862113-398-460
18739862113   202103   398         64979213   2             3               18739862113-398-460
18739862113   202103   398         64979213   1             3               18739862113-398-460
18739862113   202103   398         70192062   1             1               18739862113-398-460
18739862113   202103   398         70192062   2             1               18739862113-398-460
18739817913   202103   398         31942414   2             1               18739817913-398-460
18739817913   202103   398         31942414   1             2               18739817913-398-460
18739817913   202103   398         64954637   2             3               18739817913-398-460
```
## csv-add-exec
Read CSV stream from standard input and print it back to standard output with a new column produced by reading standard output of an external command whose standard input is fed with input column.

-c, --column=NAME
use column NAME as an input
-n, --new-name=NAME
create column NAME as an output
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
head 用户常驻小区（日3夜3）.csv |csv-add-exec -s  -c sdate -n new -- sed  's/2021/aaa/'
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   new
18739862113   202103   398         70192002   1             2               aaa03
18739862113   202103   398         64979212   2             2               aaa03
18739862113   202103   398         64979213   2             3               aaa03
18739862113   202103   398         64979213   1             3               aaa03
18739862113   202103   398         70192062   1             1               aaa03
18739862113   202103   398         70192062   2             1               aaa03
18739817913   202103   398         31942414   2             1               aaa03
18739817913   202103   398         31942414   1             2               aaa03
18739817913   202103   398         64954637   2             3               aaa03
```
## csv-add-replace
Read CSV stream from standard input and print it back to standard output with a new column produced by performing string substitution either using fixed strings or regular expression.

-c NAME
use column NAME as an input data
-e REGEX
use REGEX as a basic regular expression
-E EREGEX
use EREGEX as an extended regular expression
-F PATTERN
use PATTERN as a fixed string pattern
-i, --ignore-case
perform matching ignoring case distinction
-n NEW-NAME
create column NEW-NAME as an output
-r REPLACEMENT
use REPLACEMENT as an replacement for pattern; for fixed string pattern it is not interpreted, but for regular expression %1 to %9 are replaced by corresponding matching sub-expression, and %0 is the whole matching expression
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
head 用户常驻小区（日3夜3）.csv |csv-add-replace -c serv_number -F '187' -r '188' -n new -s
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   new
18739862113   202103   398         70192002   1             2               18839862113
18739862113   202103   398         64979212   2             2               18839862113
18739862113   202103   398         64979213   2             3               18839862113
18739862113   202103   398         64979213   1             3               18839862113
18739862113   202103   398         70192062   1             1               18839862113
18739862113   202103   398         70192062   2             1               18839862113
18739817913   202103   398         31942414   2             1               18839817913
18739817913   202103   398         31942414   1             2               18839817913
18739817913   202103   398         64954637   2             3               18839817913
```
## csv-add-rev
Read CSV stream from standard input and print it back to standard output with a new column produced by reversing another column characterwise.

-c NAME
use column NAME as an input
-n NEW-NAME
create column NEW-NAME as an output
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply the filter to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
head 用户常驻小区（日3夜3）.csv |csv-add-rev -c serv_number -n new -s
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   new
18739862113   202103   398         70192002   1             2               31126893781
18739862113   202103   398         64979212   2             2               31126893781
18739862113   202103   398         64979213   2             3               31126893781
18739862113   202103   398         64979213   1             3               31126893781
18739862113   202103   398         70192062   1             1               31126893781
18739862113   202103   398         70192062   2             1               31126893781
18739817913   202103   398         31942414   2             1               31971893781
18739817913   202103   398         31942414   1             2               31971893781
18739817913   202103   398         64954637   2             3               31971893781
```
## csv-add-rpn
Read CSV stream from standard input and print it back to standard output with a new column produced by evaluation of RPN (reverse Polish notation) expression.

-e RPN-EXPR
use expression RPN-EXPR to create new column; RPN expressions use space as a separator, so this needs to be quoted
-n NEW-NAME
create column NEW-NAME as an output
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit

RPN SYNTAX
Variables:

syntax	description	example
%.*	value of column	%name
Constants:

syntax	description	example
[-][1-9][0-9]*	decimal integer	1, 1294, -89
[-][0-9]+.[0-9]*	floating point number	1.0, 12.94, -0.89
[-]0x[0-9a-fA-F]+	hexadecimal integer	0x1, 0x1A34, -0x8A
[-]0[0-9]+	octal integer	01, 01234, -067
[-]0b[01]+	binary integer	0b1, 0b1101, -0b10
'[^']*'	string	'text'
"[^"]*"	string	"text"
Operators:

name	description	example
+	addition	%num 5 +
-	subtraction	%num 5 -
*	multiplication	%num 5 *
/	division	%num 5 /
%	modulo	%num 5 %
|	bitwise or	%num 5 |
&	bitwise and	%num 5 &
~	bitwise negation	%num ~
^	bitwise xor	%num 5 ^
<<	bitwise left shift	%num 5 <<
>>	bitwise right shift	%num 5 >>
lt, <	less	%num 5 lt, %num 5 <
le, <=	less or equal	%num 5 le, %num 5 <=
gt, >	greater	%num 5 gt, %num 5 >
ge, >=	greater or equal	%num 5 ge, %num 5 >=
eq, ==	equal	%num 5 eq, %num 5 ==
ne, !=	not equal	%num 5 ne, %num 5 !=
and	logical and	%bool1 %bool2 and
or	logical or	%bool1 %bool2 or
xor	logical exclusive or	%bool1 %bool2 xor
not	logical negation	%bool1 not
Functions:

name	description	example
if	if then else	%bool %val1 %val2 if
substr	substring	%str 1 3 substr
strlen,length	string length	%str strlen, %str length
concat	concatenation	%str1 %str2 concat
like	match pattern	%str 'patt%' like
tostring	convert to string	%num %base tostring
toint	convert to integer	%str %base toint
replace	replace string	%str 'pat' 'repl' 1 replace
replace_bre	replace string using basic RE	%str 'pat' 'bre' 1 replace_bre
replace_ere	replace string using ext. RE	%str 'pat' 'ere' 1 replace_ere
matches_bre	string matches basic RE	%str 'pat' 1 matches_bre
matches_ere	string matches extended RE	%str 'pat' 1 matches_ere
next	next integer from sequence	'sequence name' next

```linux
head 用户常驻小区（日3夜3）.csv |csv-add-rpn -n new -e "%serv_number 1 3 substr" -s
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   new
18739862113   202103   398         70192002   1             2               187
18739862113   202103   398         64979212   2             2               187
18739862113   202103   398         64979213   2             3               187
18739862113   202103   398         64979213   1             3               187
18739862113   202103   398         70192062   1             1               187
18739862113   202103   398         70192062   2             1               187
18739817913   202103   398         31942414   2             1               187
18739817913   202103   398         31942414   1             2               187
18739817913   202103   398         64954637   2             3               187


head 用户常驻小区（日3夜3）.csv |csv-add-rpn -n new -e "%serv_number strlen" -s
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   new
18739862113   202103   398         70192002   1             2                11
18739862113   202103   398         64979212   2             2                11
18739862113   202103   398         64979213   2             3                11
18739862113   202103   398         64979213   1             3                11
18739862113   202103   398         70192062   1             1                11
18739862113   202103   398         70192062   2             1                11
18739817913   202103   398         31942414   2             1                11
18739817913   202103   398         31942414   1             2                11
18739817913   202103   398         64954637   2             3                11


head 用户常驻小区（日3夜3）.csv |csv-add-rpn -n new -e "%serv_number length" -s
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   new
18739862113   202103   398         70192002   1             2                11
18739862113   202103   398         64979212   2             2                11
18739862113   202103   398         64979213   2             3                11
18739862113   202103   398         64979213   1             3                11
18739862113   202103   398         70192062   1             1                11
18739862113   202103   398         70192062   2             1                11
18739817913   202103   398         31942414   2             1                11
18739817913   202103   398         31942414   1             2                11
18739817913   202103   398         64954637   2             3                11
```
## csv-add-split
Read CSV stream from standard input and print it back to standard output with a new column produced by splitting another one using a separator.

-c NAME
use column NAME as an input data
-e SEPARATOR
use all characters from SEPARATOR as separators
-n NAME1,NAME2
create columns NAME1 and NAME2 as an output
-r, --reverse
start looking for separator from the end of input string
-p --print-separator=yes/no/auto
include separator in 2nd output column (auto means yes if there’s more than 1 separator and no if there’s only one), defaults to auto
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
head 用户常驻小区（日3夜3）.csv |csv-add-split -c serv_number -e '3' -n new1,new2 -s
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   new1   new2
18739862113   202103   398         70192002   1             2               187    9862113
18739862113   202103   398         64979212   2             2               187    9862113
18739862113   202103   398         64979213   2             3               187    9862113
18739862113   202103   398         64979213   1             3               187    9862113
18739862113   202103   398         70192062   1             1               187    9862113
18739862113   202103   398         70192062   2             1               187    9862113
18739817913   202103   398         31942414   2             1               187    9817913
18739817913   202103   398         31942414   1             2               187    9817913
18739817913   202103   398         64954637   2             3               187    9817913
```
## csv-add-sql
Read CSV stream from standard input and print it back to standard output with a new column produced by evaluation of SQL expression.

-e SQL-EXPR
use expression SQL-EXPR to create new column; SQL expressions use space as a separator, so this needs to be quoted
-n NEW-NAME
create column NEW-NAME as an output
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
head 用户常驻小区（日3夜3）.csv |csv-add-sql -e "substr(serv_number ,1,8) as new" -s
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   new
18739862113   202103   398         70192002   1             2               18739862
18739862113   202103   398         64979212   2             2               18739862
18739862113   202103   398         64979213   2             3               18739862
18739862113   202103   398         64979213   1             3               18739862
18739862113   202103   398         70192062   1             1               18739862
18739862113   202103   398         70192062   2             1               18739862
18739817913   202103   398         31942414   2             1               18739817
18739817913   202103   398         31942414   1             2               18739817
18739817913   202103   398         64954637   2             3               18739817
```
## csv-add-substring
Read CSV stream from standard input and print it back to standard output with a new column produced by extracting substring of another column.

-c NAME
use column NAME as an input data
-n NEW-NAME
create column NEW-NAME as an output
-p START-POS
start from position START-POS; first character has position 1; negative value mean starting from the end of string
-l LENGTH
take LENGTH characters from string; must not be negative
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
head 用户常驻小区（日3夜3）.csv |csv-add-substring -c serv_number -n new -p 1 -l 5 -s
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index   new
18739862113   202103   398         70192002   1             2               18739
18739862113   202103   398         64979212   2             2               18739
18739862113   202103   398         64979213   2             3               18739
18739862113   202103   398         64979213   1             3               18739
18739862113   202103   398         70192062   1             1               18739
18739862113   202103   398         70192062   2             1               18739
18739817913   202103   398         31942414   2             1               18739
18739817913   202103   398         31942414   1             2               18739
18739817913   202103   398         64954637   2             3               18739
```
## csv-add-rpn
Read CSV stream from standard input and print it back to standard output with a new column produced by evaluation of RPN (reverse Polish notation) expression.

-e RPN-EXPR
use expression RPN-EXPR to create new column; RPN expressions use space as a separator, so this needs to be quoted
-n NEW-NAME
create column NEW-NAME as an output
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
csv-header -e dst_eci_pro:int<用户常驻小区（日3夜3）.csv |csv-add-rpn -n new -e "%dst_eci_pro 100 +" -s |head
serv_number   sdate    city_code   eci         dst_eci_pro   dst_eci_index   new
18739862113   202103   398         70192002              1   2               101
18739862113   202103   398         64979212              2   2               102
18739862113   202103   398         64979213              2   3               102
18739862113   202103   398         64979213              1   3               101
18739862113   202103   398         70192062              1   1               101
18739862113   202103   398         70192062              2   1               102
18739817913   202103   398         31942414              2   1               102
18739817913   202103   398         31942414              1   2               101
18739817913   202103   398         64954637              2   3               102
```
对列值进行算术运算时，提示类型不匹配的话可以用csv-header功能对特定列修改数据类型后在计算

## csv-count
Read CSV stream from standard input and print back to standard output the number of columns or rows.

-c, --columns
print number of columns
-r, --rows
print number of rows
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
--help
display this help and exit
--version
output version information and exit

```Linux
csv-count -r <用户常驻小区（日3夜3）.csv
rows:int
60326

csv-count -c <用户常驻小区（日3夜3）.csv
columns:int
6
csv-count -c -r -s <用户常驻小区（日3夜3）.csv
columns    rows
      6   60326
```
## csv-cut
Read CSV stream from standard input, remove and/or reorder columns and print resulting file to standard output.

-c, --columns=NAME1[,NAME2…]
select only these columns
-r, --reverse
apply --columns filter in reverse, removing only selected columns
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply the filter to columns only with “NAME.” prefix
--help
display this help and exit
--version
output version information and exit
```linux
csv-cut -s -c serv_number,sdate <用户常驻小区（日3夜3）.csv|head
serv_number   sdate
18739862113   202103
18739862113   202103
18739862113   202103
18739862113   202103
18739862113   202103
18739862113   202103
18739817913   202103
18739817913   202103
18739817913   202103

csv-cut  -r -c serv_number,sdate  -s <用户常驻小区（日3夜3）.csv|head
city_code   eci         dst_eci_pro   dst_eci_index
398         70192002    1             2
398         64979212    2             2
398         64979213    2             3
398         64979213    1             3
398         70192062    1             1
398         70192062    2             1
398         31942414    2             1
398         31942414    1             2
398         64954637    2             3
```

## csv-grep
Searches for PATTERN in column of CSV file read from standard input and print to standard output only rows matching that pattern.

-c NAME
apply the filter to column NAME
-e PATTERN
use PATTERN as a basic regular expression pattern
-E PATTERN
use PATTERN as an extended regular expression pattern
-F STRING
use STRING as a fixed string pattern
-i, --ignore-case
ignore case distinction
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply the filter to rows only with _table column equal NAME
-v, --invert
invert the sense of matching, selecting non-matching rows
-x, --whole
the pattern used by -e, -E or -F options must match exactly (no preceding or succeeding characters before/after pattern)
--help
display this help and exit
--version
output version information and exit
```linux
cat 用户常驻小区（日3夜3）.csv|csv-grep -c serv_number -F '1346134' -s
serv_number   sdate    city_code   eci         dst_eci_pro   dst_eci_index
13461342105   202103   394         67934337    1             2
13461342105   202103   394         67934337    2             3
13461342105   202103   394         142680897   2             2
13461342105   202103   394         142680897   1             1
13461342105   202103   394         69182608    1             3
13461342105   202103   394         69182608    2             1
13461347878   202103   394         193010065   2             2
13461347878   202103   394         248433344   1             1
13461347878   202103   394         246370752   2             3
13461347878   202103   394         246370752   1             2
13461347878   202103   394         193024145   1             3
13461347878   202103   394         193024145   2             1
```
## csv-grep-rpn
Read CSV stream from standard input, compute RPN expression for each row and print back to standard output rows for which expression is non-zero.

For full specification of RPN syntax accepted by this tool see csv-add-rpn(1).

-e RPN-EXPR
use expression RPN-EXPR to filter; RPN expressions use space as a separator, so this needs to be quoted
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply the filter to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
cat 用户常驻小区（日3夜3）.csv|csv-grep-rpn -e "%dst_eci_index  '2' >= %serv_number '15838340339' == and" -s
serv_number   sdate    city_code   eci         dst_eci_pro   dst_eci_index
15838340339   202103   371         251150274   1             3
15838340339   202103   371         62013244    1             2
15838340339   202103   371         62013244    2             2
15838340339   202103   371         62013198    2             3
```
## csv-grep-sql
Read CSV stream from standard input, compute SQL expression for each row and print back to standard output rows for which expression is non-zero.

For full specification of SQL syntax accepted by this tool see csv-sql(1).

-e SQL-EXPR
use expression SQL-EXPR to filter; SQL expressions use space as a separator, so this needs to be quoted
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply the filter to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
cat 用户常驻小区（日3夜3）.csv|csv-grep-sql -e "serv_number ='18739862113' and dst_eci_pro = '1'" -s
serv_number   sdate    city_code   eci        dst_eci_pro   dst_eci_index
18739862113   202103   398         70192002   1             2
18739862113   202103   398         64979213   1             3
18739862113   202103   398         70192062   1             1
```
## csv-max or csv-min
Read CSV stream from standard input and print back to standard output maximum values of chosen columns.

-c, --columns=NAME1[,NAME2…]
use these columns
-n NEW-NAME1[,NEW-NAME2]
create columns with these names, instead of default max(NAME)
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
cat 用户常驻小区（日3夜3）.csv|csv-max -c eci
max(eci)
8388289
cat 用户常驻小区（日3夜3）.csv|csv-min -c serv_number
min(serv_number)
13007655311
```
## csv-sort
Read CSV stream from standard input, sort it by chosen column and print resulting file to standard output.

-c, --columns=NAME1[,NAME2…]
sort first by column NAME1, then NAME2, etc.
-r, --reverse
sort in descending order
-s, --show
print output in table format
-S, --show-full
print output in table format with pager
-T, --table=NAME
apply to rows only with _table column equal NAME
--help
display this help and exit
--version
output version information and exit
```linux
cat 用户常驻小区（日3夜3）.csv|csv-sort -c serv_number -s |head
serv_number   sdate    city_code   eci         dst_eci_pro   dst_eci_index
13007655311   202103   397         140605262   1             2
13007655311   202103   397         140605260   1             1
13007655311   202103   397         60760332    2             3
13007655311   202103   397         140576334   2             2
13007655311   202103   397         60760333    2             1
13007655311   202103   397         191278976   1             3
13007655986   202103   397         190713421   1             2
13007655986   202103   397         11543043    1             3
13007655986   202103   397         190744142   2             1
cat 用户常驻小区（日3夜3）.csv|csv-sort -c serv_number -r -s |head
serv_number   sdate    city_code   eci         dst_eci_pro   dst_eci_index
19939112998   202103   397         190747725   1             3
19939112998   202103   397         69045900    2             2
19939112998   202103   397         69045900    1             1
19939112998   202103   397         60808960    2             3
19939112998   202103   397         140592448   2             1
19939112998   202103   397         140592448   1             2
19939007678   202103   397         60792076    1             2
19939007678   202103   397         11545357    2             2
19939007678   202103   397         11545358    1             3
```
多列排序未验证
