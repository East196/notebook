1.安装vue-cli全局脚手架
```
npm install --global vue-cli
```
2.创建vue项目
```
vue init webpack mockjs<br>cd mockjs<br>npm install axios --save
```
3.安装mockjs
```
npm install mockjs --save-dev
```
4.定义mock.js文件
```javascript
// 引入mockjs
const Mock = require('mockjs');
// 获取 mock.Random 对象
const Random = Mock.Random;
// mock一组数据
var deviceSummary = Mock.mock({
  cmd: 1002,
  success: true,
  "object|5" : {
    total: "@integer(10, 3000)",
    online: "@integer(10, 3000)",
    offline: "@integer(10, 300)",
    error: "@integer(10, 30)",
    alarm: "@integer(10, 30)"
  }
})
var alarmTrend = Mock.mock(
{
  cmd: 1006,
  success: true,
  "data|3": [{
    time: "@date(yyyy-MM-dd)",
    value: "@integer(10, 30)"
  }]
})

// Mock.mock( url, post/get , 返回的数据)；
Mock.mock('/api/rest/v1/deviceSummary', 'get', deviceSummary);
// Mock.mock('/api/v1/mapData', 'post', mapData);
// Mock.mock('/api/v1/alarmDeviceScale', 'post', alarmDeviceScale);
// Mock.mock('/api/v1/alarmTrend', 'post', alarmTrend);

```


5.在main.js中引入mock.js文件
```javascript
Vue.config.productionTip = false
require('./mock/mock.js')
```

注意在某些时候axios和vue-resoures可能会使用默认前缀，vue.config.js里可能也会有mock路由，mockjs引入的时候覆盖即可
