[toc]
## springcloud-eureka服务端与客户端搭建
### 1.搭建Eureka服务器 
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
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!--spring cloud eureka 服务端导入依赖-->
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
    </dependency>
    
    <!--spring boot admin引入依赖 为了和springbootadmin集成-->
    <dependency>
        <groupId>de.codecentric</groupId>
        <artifactId>spring-boot-admin-starter-client</artifactId>
        <version>2.1.6</version>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>

</dependencies>

```
1.3 yml文件配置
```
server:
  port: 8001

spring:
  application:
    #给自己起个名称
    name: springcloud-eureka

eureka:
  instance:
    hostname: localhost

  server:
    #在服务器接收请求之前等待的初始时间 （本地测试取消注释此行）
    #wait-time-in-ms-when-sync-empty: 5
  client:
    #是否将这个服务注册到注册中心
    register-with-eureka: false
    #是否从注册中心获取信息
    fetch-registry: false
    #客户端与服务端进行交互的地址
    #查询服务和注册服务都需要依赖这个地址，多个地址可用逗号（英文的）分割。
    serviceUrl:
      defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/
```
1.4 应用添加注解 @EnableEurekaServer
```
@SpringBootApplication
@EnableEurekaServer
public class SpringcloudEurekaApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringcloudEurekaApplication.class, args);
    }

}
```
1.5 启动Eureka服务端
http://localhost:8001
![image](http://yjupi-bucket001.oss-cn-shenzhen.aliyuncs.com/officialwebsite/markdowm-images/springcloud/eureka.jpg)

### 2.搭建Eureka客户端
2.1 新建springboot项目  
2.2 pom.xml导入依赖
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
	<!-- eureka注册中心客户端依赖-->
	<dependency>
		<groupId>org.springframework.cloud</groupId>
		<artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
	</dependency>
	
	...此处省略了其他依赖
</dependencies>
```
2.3 yml文件配置
```
server:
  port: 9001

spring:
  application:
    #给自己起个名称
    name: eureka-client

eureka:
  client:
    #是否将这个服务注册到注册中心
    register-with-eureka: true
    #是否从注册中心获取注册信息
    fetch-registry: true
    #客户端与服务端进行交互的地址
    #查询服务和注册服务都需要依赖这个地址，多个地址可用逗号（英文的）分割。
    serviceUrl:
      # eureka服务端的注册地址
      defaultZone: http://localhost:8001/eureka/
  instance:
    #主机映射名称修改 (写这么多是为了同一个应用启多次不被覆盖)
    instance-id: ${spring.application.name}:${spring.cloud.client.ip-address}:${server.port}
    #访问路径可以显示IP地址
    prefer-ip-address: true
```
2.4 应用添加注解 @EnableDiscoveryClient或@EnableEurekaClient  

spring cloud中discoveryservice有许多种实现（eureka、consul、zookeeper等等）
@EnableDiscoveryClient基于spring-cloud-commons, @EnableEurekaClient基于spring-cloud-netflix。
```
#此处添加@EnableAdminServer，是因为此应用是springbootadmin的服务器端
#后续会进行 eureka 与springbootadmin的集成
@EnableAdminServer
@SpringBootApplication
@EnableDiscoveryClient
public class ActuatorApplication {

    public static void main(String[] args) {
        SpringApplication.run(ActuatorApplication.class, args);
    }

}
```