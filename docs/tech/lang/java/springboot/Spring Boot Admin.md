

[TOC]
# springbootadmin集成


1.springboot actuator的集成
1.1在pom文件中导入依赖

<dependency>

    <groupId>org.springframework.boot</groupId>

    <artifactId>spring-boot-starter-actuator</artifactId>

</dependency>

1.2在yml文件中配置信息

management:

  endpoints:

    web:

      exposure:

        #暴露所有的监控信息（或选择性暴露你所需要的信息）

        include: '*'

        #include: metrics,httptrace,health,info,beans,env

  endpoint:

     #设置成always,可以额外监控redis，db等状态

    health:

      show-details: always


#设置应用的信息

info:

  app:

    name: xxx

    version: 1.0


1.3通过项目地址+/actuator 即可查看详细监控信息的具体链接
 变化：/actuator/metrics/{具体的详细信息}  可以查看监控的详细信息

2.升级 与springbootadmin的集成
2.1新建springbootadmin的服务端
pom依赖

<!--spring boot admin服务端引入依赖-->

<dependency>

    <groupId>de.codecentric</groupId>

    <artifactId>spring-boot-admin-starter-server</artifactId>

    <version>2.1.6</version>

</dependency>

<dependency>

    <groupId>org.springframework.boot</groupId>

    <artifactId>spring-boot-starter-web</artifactId>

</dependency>

yml文件

server:

  port: 9999

  servlet:

    context-path: /actuator

主应用配置

@EnableAdminServer

@SpringBootApplication

public class ActuatorApplication {


    public static void main(String[] args) {

        SpringApplication.run(ActuatorApplication.class, args);

    }


}

2.2springbootadmin的客户端
pom依赖

<dependency>

   <groupId>de.codecentric</groupId>

   <artifactId>spring-boot-admin-starter-client</artifactId>

   <version>2.1.6</version>

</dependency>

<dependency>

    <groupId>org.springframework.boot</groupId>

    <artifactId>spring-boot-starter-web</artifactId>

</dependency>

yml文件

spring:

  #配置应用名字

  application:

    name: xxx

  #与springbootadmin集成

  boot:

    admin:

      client:

         #配置springbootadmin服务端的地址，参看服务端的地址

        url: "http://localhost:9999/actuator"

        instance:

          prefer-ip: true

2.3开始监控项目
注意：项目配置了权限的，一定要把路径权限放开
启动springboot服务端
启动springboot客户端
打开地址即可：http://localhost:9999/actuator
2.3 扩展与springboot security的整合
可以设置访问的用户密码
pom

<dependency>

   <groupId>org.springframework.boot</groupId>

   <artifactId>spring-boot-starter-security</artifactId>

</dependency>

需要注入一个bean，不然远程调用可能会出现问题

@Configuration

public  class SecurityPermitAllConfig extends WebSecurityConfigurerAdapter {

    @Override

    protected void configure(HttpSecurity http) throws Exception {

        http.authorizeRequests().anyRequest().permitAll()

                .and().csrf().disable();

    }

}



2.4踩坑指南
关于springbootadmin服务 访问https请求，报ssl异常的错误
1.重写de.codecentric.boot.admin.server.web.client包下的 InstanceWebClient类
覆盖里面的 createDefaultWebClient 方法

public class InstanceWebClient {

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

关于windows系统下 redis可能连接不上的错误
换个系统试一试，或者用在docker环境下运行redis
