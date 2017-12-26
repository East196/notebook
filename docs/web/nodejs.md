# 换源

npm install express --registry=https://registry.npm.taobao.org
Mark一下 原文国内优秀npm镜像推荐及使用

npm
全称Node Package Manager
，是node.js的模块依赖管理工具。由于npm
的源在国外，所以国内用户使用起来各种不方便。下面整理出了一部分国内优秀的npm
镜像资源，国内用户可以选择使用。

国内优秀npm镜像

淘宝npm镜像

搜索地址：http://npm.taobao.org/
registry地址：http://registry.npm.taobao.org/
cnpmjs镜像

搜索地址：http://cnpmjs.org/
registry地址：http://r.cnpmjs.org/
如何使用

有很多方法来配置npm
的registry地址，下面根据不同情境列出几种比较常用的方法。以淘宝npm

镜像举例：
1.临时使用
npm --registry https://registry.npm.taobao.org install express

2.持久使用

npm config set registry https://registry.npm.taobao.org
// 配置后可通过下面方式来验证是否成功
npm config get registry
// 或npm info express
3.通过cnpm
使用
npm install -g cnpm --registry=https://registry.npm.taobao.org
// 使用cnpm install expresstall express

作者：圣手小青龙
链接：http://www.jianshu.com/p/0deb70e6f395
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。