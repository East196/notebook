## 新建文件模板
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

## README.md
简述系统内容，可以使用markdown语法自定义格式

## 重设系统编码
```python
import sys

try:
reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    # The only supported default encodings in Python are:

    #  Python 2.x: ASCII
    #  Python 3.x: UTF-8
    # So no need to sys.setdefaultencoding('utf-8')
    pass # py3
```

## log设置与使用
0. logging.conf 配置命令行和文件的日志读写
```python
[loggers]
keys=root,kol

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_kol]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=kol
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]  
class=logging.handlers.RotatingFileHandler  
level=DEBUG  
formatter=simpleFormatter  
args=('kol.log','a',20000,5,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
```
1. \__init__.py 初始化logger
```python
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(\__name__)
logger.debug("started logging %s." % \__name__)
```
2. .gitignore 在项目中排除log文件
```python
# project
*.log
```

## config使用
```python
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("d:/influence.conf")
username = config.get("weibo", "username")
password = config.get("weibo", "password")
```

## 缓存的使用
python3自带，python2下使用lru_cache_function
```python
import lru

cookies = [000, 111, 222, 333, 444]


@lru.lru_cache_function(max_size=1024, expiration=15 * 60)
def f(account):
    print "Calling f(" + str(account) + ")"
    return cookies[account]

    print f(3)
    print f(0)
    print f(3)  # 15分钟内有效
```

## 异常的使用
```python
import traceback

try:
    raise IOError("io error!!!")  # 抛出第一个异常，被except捕获了    
except IOError, io_error:
    traceback.print_exc()   # 打印异常栈，第一个异常的栈
    print sys.exc_info()    # 打印异常信息
    print io_error          # 打印异常消息
    pass  # 异常处理完毕，系统正常继续
finally:
    print "1 print always..."

try:
    raise IOError("io error!!!")  # 抛出第一个异常，被except捕获了
except IOError, io_error:
    raise IOError("raise io error!!!")  # 抛出第二个异常，会被系统捕获，系统退出
finally:
    print "2 print always..."  # 但是还是会运行这里
```
注意：异常中不要使用裸露的except，except后跟具体的exceptions

## 异常和日志的组合
python编译时能检查的问题相对较少
except 一定要打印 & 出WARN/ERROR的log


## 语法杂项
1.使用random choice随机选取seq一个值
```python
import random

print random.choice((1, 2, 3))
print random.choice(['3', '4', 12L])
```
2.使用sum代替连加的reduce

新建文件test_sum.py,使用py.test测试验证结果
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_sum():
assert sum([1, 2, 3], 0) == 6
assert reduce(lambda a, b: a + b, [1, 2, 3], 0) == 6
F:\gitlab\mola\house\learnpy>py.test
============================= test session starts =============================
platform win32 -- Python 2.7.11, pytest-2.8.5, py-1.4.31, pluggy-0.3.1
rootdir: F:\gitlab\mola\house\learnpy, inifile:
collected 1 items

test_sum.py .

========================== 1 passed in 0.01 seconds ===========================
```
3.使用with处理文件连接（类似java7的自动关闭try）
4.json编码存文件（注意两段的区别）：
```python
person = {"name": "哈哈哈"}
with open(file_name, "a") as f:
    f.write(json.dumps(person, ensure_ascii=False) + "\n")

person = {"name": u"哈哈哈"}
with codecs.open(file_name, "a", "utf-8") as f:
    f.write(json.dumps(person, ensure_ascii=False) + "\n")
```
5. 使用`startswith()` and `endswith()`代替切片进行序列前缀或后缀的检查。比如：
- Yes: `if foo.startswith('bar')`:优于
- No: `if foo[:3] == 'bar'`:
6. 使用isinstance()比较对象的类型。比如
Yes: `if isinstance(obj, int)`: 优于
No: `if type(obj) is type(1)`:
7. 判断序列空或不空，有如下规则
Yes: `if not seq:`
`if seq:`
优于
No: `if len(seq)`
`if not len(seq)`
8. 二进制数据判断使用 `if boolvalue`的方式。

## docstring
模块/类/函数下的第一个字符串，作为文档存在
可使用`help()`或者`__doc__`访问
其间可以夹杂doctest作为简单的测试（较复杂的测试可以使用unittest或者功能强大但更简洁的`py.test`）

## doctest
新建hello_doctest.py,使用doctest验证其作用：
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""


def factorial(n):
"""Return the factorial of n, an exact integer >= 0.

    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000L
    >>> factorial(30L)
    265252859812191058636308480000000L
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000L

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

import math
if not n >= 0:
raise ValueError("n must be >= 0")
if math.floor(n) != n:
raise ValueError("n must be exact integer")
if n + 1 == n:  # catch a value like 1e300
raise OverflowError("n too large")
    result = 1
factor = 2
while factor <= n:
        result *= factor
        factor += 1
return result


if __name__ == "__main__":
import doctest
    doctest.testmod()

```
F:\gitlab\mola\house\learnpy>python hello_doctest.py -v
```python
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    [factorial(n) for n in range(6)]
Expecting:
    [1, 1, 2, 6, 24, 120]
ok
Trying:
    [factorial(long(n)) for n in range(6)]
Expecting:
    [1, 1, 2, 6, 24, 120]
ok
Trying:
    factorial(30)
Expecting:
    265252859812191058636308480000000L
ok
Trying:
    factorial(30L)
Expecting:
    265252859812191058636308480000000L
ok
Trying:
    factorial(-1)
Expecting:
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
ok
Trying:
    factorial(30.1)
Expecting:
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
ok
Trying:
    factorial(30.0)
Expecting:
    265252859812191058636308480000000L
ok
Trying:
    factorial(1e100)
Expecting:
    Traceback (most recent call last):
        ...
    OverflowError: n too large
ok
2 items passed all tests:
   1 tests in __main__
   8 tests in __main__.factorial
9 tests in 2 items.
9 passed and 0 failed.
Test passed.
```
注意：在测试通过的情况下，默认不打印详情。加上-v参数可以查看测试的详情。

## 样式：PEP8
PEP8全文见：https://www.python.org/dev/peps/pep-0008/

自动检测: [autopep8](https://github.com/hhatto/autopep8)

安装：`pip install autopep8`

关键点如下:
1. 模块内容的顺序
模块说明和docstring—import—globals&constants—其他定义。其中import部分，又按标准、三方和自己编写顺序依次排放，之间空一行。

2. 不要在一句import中多个库，比如import os, sys不推荐。

3. 如果采用from XX import XX引用库，可以省略‘module.’，都是可能出现命名冲突，这时就要采用import XX。

4. 模块命名尽量短小，使用全部小写的方式，可以使用下划线。

5. 包命名尽量短小，使用全部小写的方式，不可以使用下划线。

6. 类的命名使用CapWords的方式，模块内部使用的类采用_CapWords的方式。

7. 异常命名使用CapWords+Error后缀的方式。

8. 函数命名使用全部小写的方式，可以使用下划线。

9. 常量命名使用全部大写的方式，可以使用下划线。

10. 类的属性（方法和变量）命名使用全部小写的方式，可以使用下划线。
类的属性有3种作用域public、non-public和subclass API，可以理解成C++中的public、private、protected，non-public属性前，前缀一条下划线。
类的属性若与关键字名字冲突，后缀一下划线，尽量不要使用缩略等其他方式。

11.其他：
- 有语义分隔的加空行
- 标点符号后加空格
- 长行加`\`分行，运算符置于下行头部

## import this：Python 之禅
- Beautiful is better than ugly.
 优美胜于丑陋。

- Explicit is better than implicit.
 显式胜于隐式。

- Simple is better than complex.
  简单胜于复杂。

- Complex is better than complicated.
  复杂胜于难懂。

- Flat is better than nested.
  扁平胜于嵌套。

- Sparse is better than dense.
  分散胜于密集。

- Readability counts.
  可读性应当被重视。

- Special cases aren’t special enough to break the rules. Although practicality beats purity.
  尽管实用性会打败纯粹性，特例也不能凌驾于规则之上。

- Errors should never pass silently. Unless explicitly silenced.
除非明确地使其沉默，错误永远不应该默默地溜走。

- In the face of ambiguity, refuse the temptation to guess.
面对不明确的定义，拒绝猜测的诱惑。

- There should be one– and preferably only one –obvious way to do it.
用一种方法，最好只有一种方法来做一件事。

- Although that way way not be obvious at first unless you’re Dutch.
虽然一开始这种方法并不是显而易见的，但谁叫你不是Python之父呢。

- Now is better than never. Although never is often better than right now.
做比不做好，但立马去做有时还不如不做。

- If the implementation is hard to explain, it’s a bad idea.
如果实现很难说明，那它是个坏想法。

- If the implementation is easy to explain, it may be a good idea.
如果实现容易解释，那它有可能是个好想法。

- Namespaces are one honking great idea – let’s do more of those!
命名空间是个绝妙的想法，让我们多多地使用它们吧！
