


## BUG
1. eclipse 执行main方法 错误: 找不到或无法加载主类
在properties->Java Build Path->Libraries下有jar包没有红×的情况下
直接把workspace里面的.metadata和RemoteSystemsTempFiles文件夹删了，重新导入这个workspace,重新导入项目就好了。eclipse有点抽风！