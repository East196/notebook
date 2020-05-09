[TOC]

https://blog.csdn.net/forezp/article/details/81041012

## springcloud-gateway网关服务器搭建

### 1.springcloud-gateway网关服务器搭建
1.1 新建springboot项目  
1.2 pom.xml导入依赖
```
<!--导入springcloud依赖-->
<properties>
    <java.version>1.8</java.version>
    <spring-cloud.version>Greenwich.SR3</spring-cloud.version>
</properties>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>${spring-cloud.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <!-- spring cloud gateway 网关服务器-->
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-gateway</artifactId>
    </dependency>
    <!-- eureka注册中心客户端-->
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
    </dependency>
    <!-- hystrix 断路器 用了openFeign可以不导入这个包-->
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
    </dependency>
    <!-- 从springcloud-config配置中心 获取配置文件-->
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-config</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-kafka</artifactId>
    </dependency>
    <!-- 从springcloud-config配置中心 实时刷新需要调用/actuator/bus-refresh -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-devtools</artifactId>
        <scope>runtime</scope>
        <optional>true</optional>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```
1.3 bootstrap.yml配置文件  
因为要把最原始配置文件放在配置中心的仓库中，所以应用中要新建bootstrap.yml配置文件
```
server:
  port: 8000

spring:
  #给应用起个名字
  application:
    name: springcloud-gateway

  #集成kafka
  kafka:
    bootstrap-servers: localhost:9092


  #从配置中心获取配置
  cloud:
    #配置消息总线
    bus:
      enabled: true
      refresh:
        enabled: true
    config:
      discovery:
        enabled: true
        service-id: SPRINGCLOUD-CONFIG
      label: master
      name: springcloud-gateway
      profile: prod
    #配置网关可以从配置中心发现服务
    gateway:
      discovery:
        locator:
          enabled: true
          #默认service-id是大写，转换成小写，不建议使用
          #lower-case-service-id: true
      # 配置允许所有 https 访问 （后续待测试）
      httpclient:
        ssl:
          useInsecureTrustManager: true

management:
  endpoints:
    web:
      exposure:
        include: '*'
      #include: metrics,httptrace,health,info,beans,env
  endpoint:
    health:
      show-details: always


eureka:
  client:
    #是否将这个服务注册到注册中心
    register-with-eureka: true
    #是否从注册中心获取注册信息
    fetch-registry: true
    #客户端与服务端进行交互的地址
    #查询服务和注册服务都需要依赖这个地址，多个地址可用逗号（英文的）分割。
    serviceUrl:
      defaultZone: http://localhost:8001/eureka/
  instance:
    #主机映射名称修改
    instance-id: ${spring.application.name}:${spring.cloud.client.ip-address}:${server.port}
    #访问路径可以显示IP地址
    prefer-ip-address: true

```
1.4 配置中心仓库的springcloud-gateway-prod.yml    
原先的访问地址： http://localhost:9900/owAdmin/testSpringCloud   
通过路由访问地址： http://localhost:8000/OFFICIALWEBSITE-V1/owAdmin/testSpringCloud  
localhost:8000 ：为路由服务器地址   
OFFICIALWEBSITE-V1 ：相当于localhost:9900   
<font color="red">默认情况下不需要配置下面内容，网关会直接用eureka中识别默认的serviceid</font>
```
# 默认情况下不需要配置下面内容，网关会直接用eureka中识别默认的serviceid
spring:
  cloud:
    gateway:
      routes:
        ---------------------基础服务配置-------------------------
        - id:  OFFICIALWEBSITE-V1
          # 重点！uri是目标路径（分lb(注册中心名称)和ws(webservice路径)）
          uri: lb://OFFICIALWEBSITE-V1
          predicates:
            # 重点！转发该路径！
            - Path=/OFFICIALWEBSITE-V1/**
          # 加上StripPrefix=1，否则转发到后端服务时url会带上OFFICIALWEBSITE-V1前缀
          filters:
            - StripPrefix=1

```
### 2.springcloud-gateway 与 zuul比较
#### 2.1 开源组织
    Spring Cloud Gateway 是 Spring Cloud 微服务平台的一个子项目，属于 Spring 开源社区，依赖名叫：spring-cloud-starter-gateway。
    Zuul 是 Netflix 公司的开源项目，Spring Cloud 在 Netflix 项目中也已经集成了 Zuul，依赖名叫：spring-cloud-starter-netflix-zuul。
#### 2.2 底层实现
    据 Spring Cloud Gateway 原作者的解释：
    Zuul构建于 Servlet 2.5，兼容 3.x，使用的是阻塞式的 API，不支持长连接，比如 websockets。
    Spring Cloud Gateway构建于 Spring 5+，基于 Spring Boot 2.x 响应式的、非阻塞式的 API。同时，它支持 websockets，和 Spring 框架紧密集成，开发体验相对来说十分不错
#### 2.3 性能表现
    这个没什么好比的，要比就和 Zuul 2.x 比，Zuul 2.x 在底层上有了很大的改变，使用了异步无阻塞式的 API，性能改善明显，不过现在 Spring Cloud 也没集成 Zuul 2.x，所以就没什么好比的。
#### 2.4 如何选择
    推荐 Spring Cloud Gateway 