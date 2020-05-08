[toc]
## springcloud微服务hystrix集成（客户端弹性机制）
### 1.作用
1.1 配置独立线程池，防止服务雪崩  
1.2 配置服务调用超时时间，超时快速响应失败
### 2.客户端hystrix集成（feign版）
2.1 添加pom依赖  
<font color="red">注意: openfeign已经集成了负载均衡ribbon和断路器hystrix</font>  
```
...默认你的客户端已经集成了eureka，可以参考eureka集成...
<!-- feign -->
<dependency>
	<groupId>org.springframework.cloud</groupId>
	<artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
<!-- hystrix 断路器 用了openFeign可以不导入这个包-->
<dependency>
	<groupId>org.springframework.cloud</groupId>
	<artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
</dependency>
```
2.2 yml文件配置
```
feign:
#开启断路器
  hystrix:
    enabled: true
    
#hystrix断路器配置
hystrix:
  #线程池核心线程数配置
  threadpool:
    default:
      #设置线程池的大小
      coreSize: 100
      # 最大排队长度。默认-1，如果为-1，则不使用队列，hystrix将阻塞请求，直到有一个线程可以处理
      maxQueueSize: -1
      #即使maxQueueSize没有达到，达到queueSizeRejectionThreshold该值后，请求也会被拒绝，默认值5
      queueSizeRejectionThreshold:

    #单个服务独立线程池，独立线程池只能配置到应用级别
    #BHALLEM-V1（线程池名字，为eureka中的服务Id)
    BHALLEM-V1:
      #设置线程池的大小
      coreSize: 5
      # 最大排队长度。默认-1，如果为-1，则不使用队列，hystrix将阻塞请求，直到有一个线程可以处理
      maxQueueSize: -1
      #即使maxQueueSize没有达到，达到queueSizeRejectionThreshold该值后，请求也会被拒绝，默认值5
      queueSizeRejectionThreshold:

  #超时时间配置
  command:
    default:
      #配置默认超时时间
      execution:
        isolation:
          thread:
            timeoutInMilliseconds: 10000
      #配置默认断路机制
      circuitBreaker:
        # 当在配置时间窗口内达到此数量的失败后，进行断路，快速失败
        requestVolumeThreshold: 20
        sleepWindowInMilliseconds: 5000 #短路5秒钟，尝试恢复
        errorThresholdPercentage: 75 #出错百分比阈值


    #单个接口的超时时间配置
    #BhallemClient#testSpringCloud() fegin接口名字+方法
    BhallemClient#testSpringCloud():
      execution:
        isolation:
          thread:
            timeoutInMilliseconds: 5000
```
2.3 应用添加注解 @EnableHystrix
```
@EnableHystrix
@SpringBootApplication
@EnableDiscoveryClient
public class XxxxxApplication {

    public static void main(String[] args) {
        SpringApplication.run(XxxxxApplication.class, args);
    }

}
```
2.4 feign代码示例  
接口代码示例：
```
#name 是 eureka服务注册中心的服务Id,相当于 ip + port
#path 是 访问路径的公共部分
#fallback 是调用失败后，调用的方法类，新建一个类，实现这个接口即可
@FeignClient(name = "BHALLEM-V1",path = "/xxxx",fallback = BhallemClientFallback.class)
public interface BhallemClient {

    @RequestMapping(value = "/testSpringCloud",method = RequestMethod.GET)
    String testSpringCloud();

}

```
回调方法类示例：  
```
@Component
@Slf4j
public class BhallemClientFallback implements BhallemClient{

    #重写方法自定义返回内容
    @Override
    public String testSpringCloud(){
        return "bhallem调用失败";
    }
    
}
```
<font color="red">注意: 记得配置feignConfig</font>  
```
@Configuration
@EnableDiscoveryClient
# basePackages 是feign接口所在的包路径
@EnableFeignClients(basePackages="com.yjupi")
public class FeignConfig {
}

```