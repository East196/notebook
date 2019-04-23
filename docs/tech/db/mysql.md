# Mysql
port 3306

## ui
heidisql

## 重置密码
```
mysql> UPDATE user SET Password=PASSWORD('newpassword') where USER='root';
mysql> FLUSH PRIVILEGES;
```

## 可以用wampserver安装傻瓜版
windows + apache + mysql/mariadb + php

## 元数据获取
```sql
select column_name as  `name`,column_comment as `label`,data_type as `type`,column_type as `col_type`,
			ORDINAL_POSITION as `order`,IS_NULLABLE as `required`,COLUMN_KEY as `key`
from information_schema.columns where TABLE_SCHEMA='aiot' and table_name='sys_user';

select table_name as `name`,TABLE_COMMENT as `label`,engine,TABLE_COLLATION as `encode` from information_schema.tables where TABLE_SCHEMA='aiot';

select * from information_schema.columns where TABLE_SCHEMA='aiot' and table_name='sys_user';
select * from information_schema.tables where TABLE_SCHEMA='aiot';
```
