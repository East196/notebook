


[toc]
## springbootadmin服务端搭建与eureka集成
### 1.原理介绍
1.1 单独使用springbootadmin与项目集成需要每个项目都进行集成  
1.2 使用Eureka集成之后，只需将springbootadmin服务端与eureka集成  
1.3 springbootadmin服务端直接从eureka注册中心获取项目的信息
### 2.springbootadmin服务端搭建
2.1 新建springboot项目
2.2 pom.xml文件导入依赖
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
    <!--spring boot admin服务端引入依赖-->
    <dependency>
        <groupId>de.codecentric</groupId>
        <artifactId>spring-boot-admin-starter-server</artifactId>
        <version>2.1.6</version>
    </dependency>
    <!-- eureka注册中心客户端引入依赖-->
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```
2.3 yml文件配置
```
server:
  port: 9999
  servlet:
    #注意：此时已经不是默认路径了，后面需要配置路径，才可以监控到
    context-path: /actuator
    
#这是是添加此应用的监控信息
info:
  app:
    name: springbootadmin
    version: 1.0


#暴露端口供监控信息访问
management:
  endpoints:
    web:
      exposure:
        include: '*'
      #include: metrics,httptrace,health,info,beans,env
  endpoint:
    health:
      show-details: always

spring:
  application:
    #给自己起个名称
    name: springbootadmin


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
    instance-id: ${spring.application.name}:${http.port}
    #访问路径可以显示IP地址
    prefer-ip-address: true
    #配置路径，使springbootadmin可以监控到信息
    metadata-map:
      management:
        #配置端口
        port: 9999
        #配置路径，默认是/actuator，当你自己配置了server.servlet.context-path，
        #此时需要在这里配置 /${server.servlet.context-path}/actuator
        context-path: /actuator/actuator
```
2.4 应用添加注解 @EnableAdminServer和@EnableDiscoveryClient
此时此项目是springbootadmin服务端,也是eureka客户端
```
@EnableAdminServer
@SpringBootApplication
@EnableDiscoveryClient
public class ActuatorApplication {

    public static void main(String[] args) {
        SpringApplication.run(ActuatorApplication.class, args);
    }

}
```
2.5 springbootadmin界面展示  
启动应用访问地址：http://localhost:9999/actuator  
效果展示：
![image](http://yjupi-bucket001.oss-cn-shenzhen.aliyuncs.com/officialwebsite/markdowm-images/springcloud/springbootadmin.jpg)
### 3.与eureka服务端集成
只用在eureka服务端pom文件中导入spring boot admin客户端依赖
```
<!--spring boot admin引入依赖 为了和springbootadmin集成-->
<dependency>
    <groupId>de.codecentric</groupId>
    <artifactId>spring-boot-admin-starter-client</artifactId>
    <version>2.1.6</version>
</dependency>
```
### 4.扩展解决https不能监控的问题
4.1 关于springbootadmin服务 访问https请求，报ssl异常的错误  
重写de.codecentric.boot.admin.server.web.client包下的 InstanceWebClient类  
覆盖里面的 createDefaultWebClient 方法
```
public class InstanceWebClient {
    
    /.....省略前面的....../
    //重写下面这个方法
    private static org.springframework.web.reactive.function.client.WebClient.Builder createDefaultWebClient(Duration connectTimeout, Duration readTimeout) {
    //配置ssl信任
    SslContext sslContext=null;
    try {
        sslContext = SslContextBuilder
                .forClient()
                .trustManager(InsecureTrustManagerFactory.INSTANCE)
                .build();
    } catch (
            SSLException e) {
        e.printStackTrace();
    }
    final SslContext _sslContext =sslContext;
    HttpClient httpClient = HttpClient.create().compress(true).tcpConfiguration((tcp) -> {
        //建立连接关系的代码，跳过ssl验证
        return tcp.secure(SslProvider.builder().sslContext(_sslContext).build()).bootstrap((bootstrap) -> {
            return (Bootstrap)bootstrap.option(ChannelOption.CONNECT_TIMEOUT_MILLIS, (int)connectTimeout.toMillis());
        }).observe((connection, newState) -> {
            if (State.CONNECTED.equals(newState)) {
                connection.addHandlerLast(new ReadTimeoutHandler(readTimeout.toMillis(), TimeUnit.MILLISECONDS));
            }

        });
    });
    ReactorClientHttpConnector connector = new ReactorClientHttpConnector(httpClient);
    return WebClient.builder().clientConnector(connector);
}
    
}
```
4.2 关于https应用 的eureka客户端配置   
<font color="red">重点：yml文件配置 配置文件中的 xxxx 取决于你是否配置了${server.servlet.context-path}</font>

```
#https端口
server:
  port: 444
#http断口
http:
  port: 9910

#暴露监控端口信息
management:
  endpoints:
    web:
      exposure:
        include: '*'
      #include: metrics,httptrace,health,info,beans,env
  endpoint:
    health:
      show-details: always

spring:
  #给应用起个名字
  application:
    name: https-client
    
eureka:
  instance:
    #主机映射名称修改
    instance-id: ${spring.application.name}:${spring.cloud.client.ip-address}:${http.port}
    #访问路径可以显示IP地址
    prefer-ip-address: true
    hostname: localhost
    #修改端口号为 http 的访问端口号（这个不知道有没有用）
    non-secure-port: ${http.port}
    #重点：配合springbootadmin监控获取不到信息配置的
    metadata-map:
      instanceId: ${spring.application.name}:${spring.cloud.client.ip-address}:${http.port}
      management:
        port: ${http.port}
        context-path: /xxxx/actuator
    #重点： 把 https 请求转换成 http 请求,用 feign调用
    status-page-url: http://${eureka.instance.hostname}:${http.port}/xxxx/actuator/info
    health-check-url: http://${eureka.instance.hostname}:${http.port}/xxxx/actuator/health
    home-page-url: http://${eureka.instance.hostname}:${http.port}/xxxx/actuator
  client:
    #是否将这个服务注册到注册中心
    register-with-eureka: true
    #是否从注册中心获取注册信息
    fetch-registry: true
    #客户端与服务端进行交互的地址
    #查询服务和注册服务都需要依赖这个地址，多个地址可用逗号（英文的）分割。
    serviceUrl:
      defaultZone: http://${eureka.instance.hostname}:8001/eureka/
```  
### 5.springbootadmin单独与项目集成配置参考
文档：springbootadmin集成.note  
链接：http://note.youdao.com/noteshare?id=56c6409c894f40eadf75a6cee9f00171&sub=36D20474937A4FAE95365E045F1B09A5
