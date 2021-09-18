# PostGIS
空间图形数据入库脚本
```sql
CREATE TABLE County_Boundary
(
wkt_geom geometry,
Name TEXT,
City TEXT,
District TEXT,
Province TEXT
);

MultiPolygon(((经度 纬度,经度 纬度)),((经度 纬度,经度 纬度)))
```