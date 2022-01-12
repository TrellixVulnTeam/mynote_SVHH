# PostgreSQL生成uuid
1、启用扩展
```sql
CREATE EXTENSION pgcrypto;
CREATE EXTENSION "uuid-ossp";
```
2、生成uuid
```sql
SELECT gen_random_uuid();
SELECT uuid_generate_v4();
SELECT uuid_generate_v1mc();
```