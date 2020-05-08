[toc]
## springcloud-config 配置中心与 configrepository配置中心仓库
    作用：统一管理我们的配置文件  
### 1.springcloud-config 配置中心服务器搭建 + 同步刷新功能
1.1 新建一个springboot项目
1.2 pom.xml文件导入依赖
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
    <!-- 配置中心服务器导入的依赖 -->
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-config-server</artifactId>
    </dependency>
    <!-- eureka 客户端导入的依赖 -->
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
    </dependency>
    
    <!-- 以下是为了配置同步刷新用到的 集成 springcloud-bus 以及使用kafka -->
    <!-- 配置文件同步刷新要用到 -->
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-kafka</artifactId>
    </dependency>
    <!-- 配置文件同步刷新要用到 为了暴露刷新端口-->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-actuator</artifactId>
    </dependency>


    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```
1.3 yml配置文件
```
server:
  port: 8002

spring:
  application:
    #给自己起个名称
    name: springcloud-config
  #集成kafka 配置文件同步刷新要用到
  kafka:
    #kafka 地址
    bootstrap-servers: localhost:9092


#  #本地测试版 本地管理配置文件（不要用git配置本地，会回滚本地配置）
  profiles:
    #告诉服务,我现在要启用本地配置(优先考虑采用工程目录resources下配置)
    active: native
  cloud:
    # springcloud bus 配置实时刷新需要用到
    # 开启使用 springcloud bus
    bus:
      enabled: true
      # 开启使用 springcloud bus 进行实时刷新
      refresh:
        enabled: true
    config:
      server:
        native:
          # windows系统：{file:///}
          search-locations: file:///D:\software\project\yjupi\springcloud-configrepository\config-repo



  #服务器版 配置Git管理配置文件
#  cloud:
#    bus:
#      enabled: true
#      refresh:
#        enabled: true
#    config:
#      server:
#        label: master
#        git:
#          uri: https://code.aliyun.com/xxx.git
#          search-paths: config-repo
#          #用户名和密码不是阿里云code的用户名与密码 是里面git账号的
#          #不清楚的这个地址设置密码 https://code.aliyun.com/profile/password/edit
#          username: xxxxxx
#          password: xxxxxx
#          # 防止git拉取配置缓存，导致配置不是最新的问题
#          force-pull: true


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
    instance-id: springcloud-config
    #访问路径可以显示IP地址
    prefer-ip-address: true

info:
  app:
    name: springcloud-config
    version: 1.0


```
1.4 应用添加注解 @EnableConfigServer和@EnableDiscoveryClient
```
@SpringBootApplication
@EnableConfigServer
@EnableDiscoveryClient
public class SpringcloudConfigApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringcloudConfigApplication.class, args);
    }


}
```
### 2.搭建configrepository配置中心仓库
    配置仓库不需要是springboot项目，仅仅是一个文件夹存放配置文件即可
![image](http://yjupi-bucket001.oss-cn-shenzhen.aliyuncs.com/officialwebsite/markdowm-images/springcloud/config-repository.jpg)
### 3.测试配置中心服务端是不是搭建完成
3.1 启动配置中心服务器端项目
3.2 属于配置文件地址，查看配置文件内容
格式：http://localhost:8002/配置文件名称/配置文件类型  
示例：http://localhost:8002/officialwebsite-v1/prod
![image](http://yjupi-bucket001.oss-cn-shenzhen.aliyuncs.com/officialwebsite/markdowm-images/springcloud/config-test.jpg)
### 4.客户端集成配置中心，将配置文件放置在配置中心 + 实时刷新
4.1 pom文件导入依赖  

```
    <!-- 从springcloud-config配置中心 获取配置文件-->
	<dependency>
		<groupId>org.springframework.cloud</groupId>
		<artifactId>spring-cloud-starter-config</artifactId>
	</dependency>
	<!-- 为了和配置中心同步实时刷新 + kafka -->
	<dependency>
		<groupId>org.springframework.cloud</groupId>
		<artifactId>spring-cloud-starter-bus-kafka</artifactId>
	</dependency>
	<!-- 从springcloud-config配置中心 实时刷新需要调用/actuator/bus-refresh -->
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-actuator</artifactId>
	</dependency>
	
	<!-- 连接配置中心重试的依赖 可以不导入 -->
	<dependency>
		<groupId>org.springframework.retry</groupId>
		<artifactId>spring-retry</artifactId>
	</dependency>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-aop</artifactId>
	</dependency>
```
4.2 建立bootstrap.yml文件 将原来配置文件迁移至配置中心仓库  
<font color="red">强烈建议：将端口号提前抽取出来放在这里配置，原来配置文件中的端口号注掉（便于linux下一个应用多端口启用）</font>  
```
# bootstrap.yml文件内容如下，将eureka配置提前抽取出来放在这里
server:
  port: 9900

info:
  app:
    name: officialwebsite-v1
    version: 1.0

spring:
  #给应用起个名字
  application:
    name: officialwebsite-v1

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
      #快速失败
      fail-fast: true
      #快速失败重连机制
      retry:
        initial-interval: 1100        #首次重试间隔时间，默认1000毫秒
        multiplier: 1.1D              #下一次重试间隔时间的乘数，比如开始1000，下一次就是1000*1.1=1100
        max-interval: 2000            #最大重试时间，默认2000
        max-attempts: 3               #最大重试次数，默认6次
      #从配置中心获取配置文件
      discovery:
        enabled: true
        service-id: SPRINGCLOUD-CONFIG
      label: master
      # 文件名 + 文件类型
      name: officialwebsite-v1
      profile: prod

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
4.3 配置快速失败以及快速失败重连机制的作用  
    快速失败：启动时，会直接去配置中心找文件，如果没有直接失败  
    快速失败重连：失败后进行重连操作
### 5.实时同步刷新正确用法
<font color="red">误区：以为上述配置好实时同步刷新，当你更改配置中心仓库文件的时候，其他应用都自动刷新   
同步刷新的原理是，你刷新一个应用，同步springcloud bus传递消息会同步到所有应用   
重点：需要用Post请求调用同步刷新接口http://localhost:8002/actuator/bus-refresh</font>  
![image](http://yjupi-bucket001.oss-cn-shenzhen.aliyuncs.com/officialwebsite/markdowm-images/springcloud/config-refresh.jpg)

如果你在本地测试，修改完配置文件，然后用postman用POST请求调用上述接口 

如果在服务器端，用git提交配置文件，触发webhook，直接调用上述接口，或调用自己写的方法，再调用上述接口

### 6.客户端应该怎么配置才能接受到同步刷新的内容呢 
<font color="red"> 需要在引用配置文件的数据的地方加注解@RefreshScope  
自动刷新只能刷新 @RefreshScope 注解下的配置，一些特殊配置，如数据库等，需要同样先设置数据库链接ConfigServer类，然后通过加 @RefreshScope 注解方式</font>  

```
@RestController
@RefreshScope
public class TestRefreshController {

    @Value("${name}")
    private String name;
    
    }
```
对于fegin的配置并不起作用  
重点：如果有大的配置文件改动，建议重启应用，不需要重启springcloud-config





