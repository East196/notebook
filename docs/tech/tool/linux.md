

## 文件
mkdir iamdir
rm -rf iamdir

touch iamfile.txt
cat iamfile.txt
more iamfile.txt
tailf iamfile.txt

## 杀进程
https://www.cnblogs.com/zjdxr-up/p/8408885.html
ps -ef | grep python
kill -9 xxx

lsof -i :8080

## ping
ping baidu.com
telnet 120.79.179.223 7000
## 

find命令查找文件
find . -name "filename"


## iptables
```bash
vim /etc/sysconfig/iptables
systemctl restart iptables.service
iptables -L -n
```

## frp
```bash
wget https://github.com/fatedier/frp/releases/download/v0.26.0/frp_0.26.0_linux_amd64.tar.gz
tar xzvf frp_0.26.0_linux_amd64.tar.gz
mv frp_0.26.0_linux_amd64 frp
cd frp
nohup ./frps -c ./frps.ini &
```

```shell
cd frp
./frpc -c ./frpc.ini
```
注意内网防火墙
注意查看是否真的成功，有的时候可以打通但是显示错误
