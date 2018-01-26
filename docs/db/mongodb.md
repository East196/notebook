# mongodb

## ui
官方有compass

## install

### office

<https://docs.mongodb.com/master/tutorial/install-mongodb-on-red-hat/>

vim /etc/yum.repos.d/mongodb-org-3.4 `[mongodb-org-3.4] name=MongoDB Repository baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/ gpgcheck=1 enabled=1 gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc`

### docker install
```
docker search mongo
docker pull mongo
docker run mongo
```
### windows server

下载安装，配置环境变量`e:\appdata\mongodb\conf\mongodb.config`

```
dbpath=e:\appdata\mongodb\data #数据库路径
logpath=e:\appdata\mongodb\logs\mongodb.log #日志输出文件路径
logappend=true #错误日志采用追加模式，配置这个选项后mongodb的日志会追加到现有的日志文件，而不是从新创建一个新文件
journal=true #启用日志文件，默认启用
quiet=true #这个选项可以过滤掉一些无用的日志信息，若需要调试使用请设置为false
port=27017 #端口号 默认为27017
```

管理员身份运行
`mongod.exe --config e:\appdata\mongodb\conf\mongodb.config --install --serviceName "MongoDB"`
`net start MongoDB`
