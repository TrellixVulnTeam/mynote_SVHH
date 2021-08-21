Postgresql创建dblink

### 1、创建dblink扩展
``` sql
create extension dblink;
```
### 2、创建dblink连接
```sql
select dblink_connect(‘test’,‘dbname=qx host=192.168.137.111 port=5432 user=postgres password=aa’);
```
### 3、查询数据
```sql
select * from dblink(‘test’,‘select enb from omc') as t1 (enb text);
```
### 注意事项：
#### 1、修改pg_hba.conf文件，使所用用户可以访问自己数据库
```
host    all             all             0.0.0.0/0            md5
```
#### 2、防火墙设置，关闭防火墙或者添加5432端口的入站规则