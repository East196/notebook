
## install
参考：
http://blog.csdn.net/u010099080/article/details/53418159

cuda8.0 直接执行
cudnnv7 bin+path
注意要让环境变量生效
pip install tensorflow-gpu

# pip 中科大的源
~/pip/pip.ini
[global]
index-url = https://mirrors.ustc.edu.cn/pypi/web/simple/

pip install tensorflow-gpu

## tf.contrib
一些高层方法，新版keras也在其中

## keras
[keras中文文档](http://keras-cn.readthedocs.io/en/latest/)
从 TensorFlow 1.2 版本开始，Keras API 可作为 TensorFlow 的一部分直接使用，这是 TensorFlow 在向数百万新用户开源的道路上迈出的一大步。

Keras 较好被理解为一个 API 技术规范，而不是一个特殊的代码库。事实上，继续发展将会出现 Keras 技术规范的两个不同实现：（a）TensorFlow 的内部实现（如 tf.keras），纯由 TensorFlow 写成，与 TensorFlow 的所有功能深度兼容；（b）外部的多后台实现，同时支持 Theano 和 TensorFlow（并可能在未来有更多的后台）。

类似的，Skymind 正在用 Scala 实现 Keras 份额部分规范，如 ScalNet。为了在浏览器中运行，Keras.js 正在用 JavaScript 运行 Keras 的部分 API。正因如此，Keras API 注定成为深度学习从业者的通用语言，在不同的工作流程中共享并独立于底层平台。像 Keras 这样的统一 API 规范将促进代码共享，提高研究的再生产率，并允许更大支持社区的存在。
