[TOC]
## Spring Cloud

Spring Cloud为开发人员提供了工具，以快速构建分布式系统中的某些常见模式（例如，配置管理，服务发现，断路器，智能路由，微代理，控制总线，一次性令牌，全局锁，领导选举，分布式会话，群集状态）。分布式系统的协调导致样板式样，并且使用Spring Cloud开发人员可以快速站起来实现这些样板的服务和应用程序。它们可以在任何分布式环境中正常工作，包括开发人员自己的笔记本电脑，裸机数据中心以及Cloud Foundry等托管平台。

## 特征
Spring Cloud致力于为典型的用例和扩展机制提供良好的开箱即用体验，以涵盖其他用例。

- 分布式/版本化配置

- 服务注册和发现

- 路由

- 服务到服务的呼叫

- 负载均衡

- 断路器

- 全局锁

- 领导选举和集群状态

- 分布式消息传递

Spring Cloud采用了一种非常声明性的方法，通常只需更改类路径和/或注释即可获得许多功能。作为发现客户端的示例应用程序：
```java
@SpringBootApplication
@EnableDiscoveryClient
public class Application {
	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
```
## 什么是微服务
“微服务架构的系统是一个分布式的系统，按业务进行划分为独立的服务单元，解决单体系统的不足，同时也满足越来越复杂的业务需求。每个微服务仅关注于完成一件任务并很好地完成该任务。在所有情况下，每个任务代表着一个小的业务能力。”


## 目前集成的功能
#### 1.注册中心（eureka： 美 [juˈriːkə]   读音：优瑞卡）（Netflix :['netfliːks]  奈特福莱克斯）  
    作用：统一管理我们的服务，方便服务间调用，方便实现负载均衡  
#### 2.配置中心（springcloud-config）  
    作用：统一管理我们的配置文件  
#### 3.配置中心仓库（springcloud-configrepository)  
    作用：和配置中心分离，存放所有的配置文件  
<font color="red">注意：配置仓库和配置中心放在一起，会造成git回滚问题，不建议放在一起  </font>  
#### 4.监控中心（springbootadmin)  
    作用：用来监控我们的应用状态  
    注意：用微服务集成，springbootadmin直接从配置中心获取应用状态  
#### 5.客户端弹性机制  （hystrix ：美 [hɪst'rɪks]  读音：海斯锤科思）
    5.1 客户端负载均衡（client load balance)模式
    开多个应用
    5.2 断路器（circuit breaker)模式
    快速响应失败，不占用资源
    5.3 后备（fallback)模式
    响应失败，可以补救，自定义响应失败返回内容
    5.4 舱壁 （bulkhead)模式
    独立线程池，防止一个问题，拖垮所有应用
#### 6.服务网关（springcloud-gateway)
    作用：服务路由，过滤器 
