# javafaker 数据生成利器

## maven
```
<dependency>
  <groupId>com.github.javafaker</groupId>
  <artifactId>javafaker</artifactId>
  <version>0.14</version>
</dependency>
```

## code
```
//设置 语言 ，地区
Locale local = new Locale("zh","CN");
//创建对象
Faker faker = new Faker(local) ;
Hello hello = new Hello() ; hello.setName(faker.name().name()); hello.setAddress(faker.address().fullAddress()); hello.setJob(faker.job().seniority()); System.out.println(hello.toString());
```
## advance
直接读对象，获取对象的名称和注解，生成数据
```
class Person{
  String name;
  String gender;
  @Fake("int:0-150")
  String age;
  String company;
  String address;
  String email;
}


```

上传github，gitee，maven库
