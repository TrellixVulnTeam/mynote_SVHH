oracle安装后部署命令

### 查看当前数据库的表空间名字、大小、路径
```sql
select tablespace_name,file_id,bytes/1024/1024,file_name 
from dba_data_files order by file_id;
```
### 创建用户
```sql
create user fast identified by 123;
```
 
### 查询所有用户所在的表空间
```sql
select username,default_tablespace from dba_users;
```
 
### 为用户创建表空间
```sql
create tablespace FASTSPACE datafile '/u01/app/oracle/oradata/xe/fastpace.dbf' size 500M;
```
 
### 修改用户表空间
```sql
alter user fast default tablespace FASTSPACE;
```
 
### 授予用户权限 
```sql
grant create session,create table,create view,create sequence,unlimited tablespace to fast;
```
### 授予用户dba权限，用于导入dmp文件 
```sql
grant dba to fast;
```
