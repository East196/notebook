
# python redis

### windows下redis 开机自启动
 

1，在redis的目录下执行（执行后就作为windows服务了）

redis-server --service-install redis.windows.conf
2，安装好后需要手动启动redis

redis-server --service-start
3，停止服务

redis-server --service-start
4，卸载redis服务

redis-server --service-uninstall
