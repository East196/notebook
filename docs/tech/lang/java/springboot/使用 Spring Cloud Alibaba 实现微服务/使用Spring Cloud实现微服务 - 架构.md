## 简介
`Spring Cloud Alibaba`为分布式应用程序开发提供了一站式解决方案。它包含开发分布式应用程序所需的所有组件，使您可以轻松地使用`Spring Cloud`开发应用程序。

使用`Spring Cloud Alibaba`，您只需要添加一些注释和少量配置即可将`Spring Cloud`应用程序连接到Alibaba的分布式解决方案，并使用Alibaba中间件构建分布式应用程序系统。

## 特征
- **流量控制和服务降级：** 使用`Sentinel`进行流量控制，断路和系统自适应保护。
> `Sentinel` 哨兵，僧特诺

- **服务注册和发现：** 实例可以在`Nacos`中注册，客户可以使用`Spring`管理的bean发现实例。支持通过`Spring Cloud Netflix`的客户端负载均衡器`Ribbon`。

- **分布式配置：** 使用`Nacos`作为数据存储
> `Nacos` 内考斯

- **事件驱动：** 构建与`Spring Cloud Stream RocketMQ Binder`连接的高度可扩展的事件驱动微服务

- **消息总线：** 使用`Spring Cloud Bus RocketMQ`链接分布式系统的节点
> `RocketMQ` 火箭MQ，如啊可A特MQ
- **分布式事务：** 支持高性能且易于使用的`Seata`分布式事务解决方案
> `Seata` 斯以塔
- **Dubbo RPC：** 通过`Dubbo RPC`扩展`Spring Cloud`服务到服务调用的通信协议
> `Dubbo` 丢包

- **阿里云对象存储：** `OSS`的`Spring`资源抽象。阿里云对象存储服务（OSS）是一种加密，安全，经济高效且易于使用的对象存储服务，可让您在云中存储，备份和存档大量数据