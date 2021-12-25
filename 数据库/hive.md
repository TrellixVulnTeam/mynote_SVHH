# hive
删除表分区
```sql
ALTER TABLE table_name DROP IF EXISTS PARTITION(year = 2015, month = 10, day = 1);
```