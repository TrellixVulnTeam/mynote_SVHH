# PostgreSQL安装Python扩展
1、打开F:\Program Files\PostgreSQL\14\doc\installation-notes.html文件查看当前数据库支持的Python版本。
2、将F:\Programs\Python\Python39\下的python3.dll文件  复制到F:\Program Files\PostgreSQL\14\lib\ 下修改为python39.dll
在报错的话将:\Programs\Python\Python39\下的python39.dll复制到C:\Windows\System32\目录下
3、Python安装postgresql扩展包：
python -m pip install postgresql-extension-installer
4、在数据库中执行：
```sql
CREATE EXTENSION plpython3u
```
启用python扩展
创建一个python函数测试下是否能用
```sql
CREATE FUNCTION pymax (a integer, b integer)
  RETURNS integer
AS $$
  if a > b:
    return a
  return b
$$ LANGUAGE plpython3u;
```