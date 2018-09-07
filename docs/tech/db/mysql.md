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
