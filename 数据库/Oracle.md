Oracle

### 查看表空间的名称及大小

```sql
SELECT t.tablespace_name, round(SUM(bytes / (1024 * 1024)), 0) ts_size 
FROM dba_tablespaces t, dba_data_files d 
WHERE t.tablespace_name = d.tablespace_name 
GROUP BY t.tablespace_name; 
```

### 查看表空间物理文件的名称及大小

```sql
SELECT tablespace_name, 
file_id, 
file_name, 
round(bytes / (1024 * 1024), 0) total_space 
FROM dba_data_files 
ORDER BY tablespace_name; 
```

### 查看回滚段名称及大小

```sql
SELECT segment_name, 
tablespace_name, 
r.status, 
(initial_extent / 1024) initialextent, 
(next_extent / 1024) nextextent, 
max_extents, 
v.curext curextent 
FROM dba_rollback_segs r, v$rollstat v 
WHERE r.segment_id = v.usn(+) 
ORDER BY segment_name; 
```

### 查看控制文件

```sql
SELECT NAME FROM v$controlfile; 
```

### 查看日志文件

```sql
SELECT MEMBER FROM v$logfile; 
```

### 查看表空间的使用情况

```sql
SELECT SUM(bytes) / (1024 * 1024) AS free_space, tablespace_name 
FROM dba_free_space 
GROUP BY tablespace_name; 
SELECT a.tablespace_name, 
a.bytes total, 
b.bytes used, 
c.bytes free, 
(b.bytes * 100) / a.bytes "% USED ", 
(c.bytes * 100) / a.bytes "% FREE " 
FROM sys.sm$ts_avail a, sys.sm$ts_used b, sys.sm$ts_free c 
WHERE a.tablespace_name = b.tablespace_name 
AND a.tablespace_name = c.tablespace_name; 
```

### 查看数据库库对象

```sql
SELECT owner, object_type, status, COUNT(*) count# 
FROM all_objects 
GROUP BY owner, object_type, status; 
```

### 查看数据库的版本

```sql
SELECT version 
FROM product_component_version 
WHERE substr(product, 1, 6) = 'Oracle';
```

### 查看数据库的创建日期和归档方式

```sql
SELECT created, log_mode, log_mode FROM v$database; 
```

### 查看表空间有哪些表

```sql
select table_name,tablespace_name from user_tables;
```