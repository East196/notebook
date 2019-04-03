## 安装
用中文网，英文官网有点慢
http://nodejs.cn/download/

cenos
```bash
# 更新nodejs源
curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -
yum install -y nodejs
npm config set registry https://registry.npm.taobao.org
npm install -g yarn
yarn config set registry http://registry.npm.taobao.org/
```

## 升级
```
npm install -g npm
```

windows下无法装n，直接msi重新安装覆盖就好
```
npm install -g n
n stable
```

## npm
全称Node Package Manager
，是node.js的模块依赖管理工具。由于npm
的源在国外，所以国内用户使用起来各种不方便。下面整理出了一部分国内优秀的npm
镜像资源，国内用户可以选择使用。



## 国内优秀npm镜像
### 换源
`npm install express --registry=https://registry.npm.taobao.org`

### 淘宝npm镜像

搜索地址：http://npm.taobao.org/

registry地址：http://registry.npm.taobao.org/
### cnpmjs镜像

搜索地址：http://cnpmjs.org/

registry地址：http://r.cnpmjs.org/

### 如何使用

有很多方法来配置npm
的registry地址，下面根据不同情境列出几种比较常用的方法。以淘宝npm

## 升级
镜像举例：
1. 临时使用
npm --registry https://registry.npm.taobao.org install express

2. 持久使用
```bash
npm config set registry https://registry.npm.taobao.org
# 配置后可通过下面方式来验证是否成功
npm config get registry

yarn config set registry http://registry.npm.taobao.org/
# 配置后可通过下面方式来验证是否成功
yarn config get registry

```
3. 通过cnpm
使用
npm install -g cnpm --registry=https://registry.npm.taobao.org
// 使用cnpm install expresstall express
