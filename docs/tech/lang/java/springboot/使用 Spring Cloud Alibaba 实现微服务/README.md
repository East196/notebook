[TOC]

# Spring Cloud Alibaba
[Github](https://github.com/alibaba/spring-cloud-alibaba/blob/master/README-zh.md)

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

## 入门
入门的最简单方法是包括Spring Cloud BOM，然后将其添加spring-cloud-alibaba-dependencies到应用程序的类路径中。如果您不想包括所有Spring Cloud Alibaba功能，则可以为所需的功能添加单个启动器。

spring-cloud-alibaba-dependenciespom中的依赖项：
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-alibaba-dependencies</artifactId>
            <version>2.1.0.RELEASE</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

只要Spring Cloud Alibaba Nacos和Nacos API在类路径上，任何Spring Boot应用程序@EnableDiscoveryClient都将尝试通过以下方式联系Nacos服务器localhost:8848（默认值为spring.cloud.nacos.discovery.server-addr）：
```java
@SpringBootApplication
public class Application {
​
  @RequestMapping("/")
  public String home() {
    return "Hello World";
  }
​
  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }
​
}
```

本地Nacos服务器必须正在运行。请参阅有关如何运行Nacos服务器的[Nacos文档](https://nacos.io/zh-cn/docs/quick-start.html)。
