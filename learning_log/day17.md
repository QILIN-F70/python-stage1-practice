# Day 17 学习日志

## 今天学习了什么

异常处理基础（`try` 和 `except`）

观察错误

捕获指定异常

处理用户输入产生的 `ValueError`

处理文件读取产生的 `FileNotFoundError`

处理JSON格式错误

为什么不应随意使用空泛的 `except`

## try和except分别有什么作用

try：放置并执行可能产生异常的代码

except：发生异常，寻找匹配的except

## try和except的执行过程

Python 先执行 try 中的代码

没有异常就跳过except

出现匹配的异常，就停止执行try中剩余代码，转去执行except

except 执行完后，程序可以继续向下运行

## ValueError在什么情况下出现

数据类型可以被当前操作接收，但具体的值无法处理。例如 `int()` 可以接收字符串，但 `"三"` 不能转换成整数。

## FileNotFoundError在什么情况下出现

文件不存在的情况下

## json.JSONDecodeError在什么情况下出现

文件存在但文件格式错误的情况下，完全为空的 JSON 文件也会产生该异常

## 为什么要捕获明确的异常类型

让不同异常得到对应处理，并防止不相关的代码错误被隐藏

## 为什么不推荐使用空的except

空的except会捕获几乎所有异常，表面上程序不崩溃，但他可能把代码本身的错误伪装成用户的输入错误

## 今天完成了什么程序

异常处理版学习任务读取器

空的 except

文件不存在异常：FileNotFoundError

文件存在，但 JSON 格式错误：json.JSONDecodeError

## 今天主动观察了什么错误

用户输入错误

json文件不存在

json文件格式错误

空的except

## NameError为什么出现

变量名没有被定义

## 我仍然不熟悉什么

NameError

TypeError

ValueError

## 明天需要复习什么

简单区分：
- ValueError：数据类型可以接收，但具体内容不合法。
- TypeError：传入的数据类型不适合该操作。
- NameError：没有定义的变量

try 代码块的作用：放置并执行可能产生异常的代码。发生异常后，Python 才去寻找匹配的 except。
