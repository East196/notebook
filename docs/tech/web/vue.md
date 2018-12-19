## Vue
https://cn.vuejs.org/v2/guide/

v-model='model' {{model}}
v-bind:prop 	:prop
v-on:event   	@event

data(){ return {}}

props 传递数据
slot 内容分发
events $emit @click 事件

## 全家桶
vue-router
vue-rescource / axios
vuex / vue-events

npm install vue-events --save
npm install vue-rescource --save
npm i axios --save

# ui
iview vs element
目前使用iview-admin，注意启动需要用powershell
mui- material 风格

# form
直接使用iview 的form 完成valid
基于[async-validator](https://github.com/yiminghe/async-validator)

# table
npm install vuetable-2 --save
直接用iview的table也是不错的
https://blog.csdn.net/u013144287/article/details/78879044
对照spring data rest的分页


## vue-devtools 浏览器方便查看
https://github.com/vuejs/vue-devtools

## 动态组件
1. v-if
2. h方法
可以考虑写一个从标签变成h的生成器，或者考虑用jsx？
iview已经内置动态表单

注意：字符串的on方法全面用不了了，只能用
```
on: {
  click: () => {
    this.show(params.index)
  }
}
```
此处作为function的click可以用，作为string的'click'不可以用

##### Manual Installation

Make sure you are using Node 6+ and NPM 3+

    Clone this repo
    npm install (Or yarn install if you are using yarn as the package manager)
    npm run build
    Open Chrome extension page
    Check "developer mode"
    Click "load unpacked extension", and choose shells/chrome.

## webpack
http://webpack.github.io/
##### [一小时包教会Webpack](http://www.w2bc.com/Article/50764)
##### [入门Webpack，看这篇就够了](http://www.jianshu.com/p/42e11515c10f)


## Element UI
http://element.eleme.io/#/zh-CN
