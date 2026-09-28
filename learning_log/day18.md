# Day 18 学习日志

## 今天学习了什么

模块（导入）

自建模块、两种导入方式

`ModuleNotFoundError` 和 `AttributeError`

## 模块是什么，为什么要使用模块

模块通常是一个.py文件，里面可以放函数，也可以放变量等代码；

把任务函数单独放进 task_tools.py，其他文件就能导入复用

## import 模块名与 from 模块名 import 函数名有什么区别

import 模块名：调用函数时使用模块名.函数名

`from 模块名 import 函数名` 后，调用时直接写**函数名**

## 调用函数与把返回值加入列表有什么区别

调用函数与把返回值加入列表：调用 `create_task()` 会返回一个任务字典；用变量接住后，还要执行 `tasks.append(...)`，字典才进入列表。调用函数本身不会自动加入列表。

## 为什么任务列表要在循环外初始化

放在循环内就每一次循环都会初始化，我们只需在外第一次初始化

## 今天完成了什么程序

`task_tools.py`：放任务处理函数。

`day18_test.py`：放用户输入和程序运行流程。

## 今天主动观察了什么错误

模块名与文件名不一致时：ModuleNotFoundError

模块找到了，但你写的函数名不在模块里：AttributeError

## ModuleNotFoundError 为什么出现

模块名必须和文件名一致，比如你的文件叫 task_utils.py，如果导入时少写一个 s，Python 就找不到对应模块

## AttributeError 为什么出现

模块找到了，但你写的函数名不在模块里

比如task_utils.py 定义的是 create_task，没有定义 make_task。这种情况会产生 AttributeError

## __pycache__ 是什么，为什么要用 .gitignore 忽略它

`__pycache__` 是 Python 自动生成的字节码缓存。.gitignore 的作用是让 Git 忽略它，避免把缓存提交到仓库；缓存仍会留在电脑上。

## 我仍然不熟悉什么

忘记了初始化要在循环外，判断completed = completed_text == "是"只在一个.py文件内判断

## 明天需要复习什么

循环外初始化列表、把用户输入的“是/否”转换为布尔值应由哪个文件负责，以及两种导入写法。
