# Day 14 学习日志

## 今天学习了什么

定义和调用函数

重复调用函数

单个和多个参数

`return`返回计算结果

返回字典

把列表传入函数

主动观察并修复缺少参数导致的 `TypeError`

## 函数是什么，为什么需要函数

函数就是用来做功能性的，若是需要重复的一段代码处理不同的数据，那么使用函数就更方便

## 如何定义和调用函数

def 函数名():

其中：

def表示“定义函数”。

函数名是我们给这段代码起的名称。

()表示这是一个函数。

:表示函数头结束。

函数名()是调用函数

## 参数有什么作用

希望同一个函数每次处理不同的数据，就需要参数

## 多个参数如何对应传入的数据

多个参数之间使用英文逗号隔开，调用时通常按照从左到右的顺序对应

## return有什么作用

return把结果交回函数调用位置；如果调用时使用变量接收，返回结果才会保存到该变量中，并可供后续代码使用。

## print和return有什么区别

print是负责输出到终端给终端显示

return只是把结果交回函数调用位置，并不在终端显示

## 函数如何返回一个字典

def create_task(task_name,priority,completed):

  task = {

​    "name":task_name,

​    "priority":priority,

​    "completed":completed

  }

  return task

first_task = create_task("学习Python","高",False)

second_task = create_task("整理笔记","中",True)

tasks = []

tasks.append(first_task)

tasks.append(second_task)

## 如何把列表传给函数

调用 `count_completed(tasks)` 时，列表 `tasks`作为实参传给参数 `task_list`。函数内部可以使用 `for task in task_list:`遍历列表，并通过 `return`返回统计结果。

result = count_completed(tasks)

## 今天观察了什么TypeError

函数参数错误

函数要求的参数数量与实际传入数量不匹配，因此会出现 TypeError

## status使用双等号为什么出现NameError

`status == "优秀"`只是比较，不会给变量赋值。Python需要先读取尚未定义的 `status`进行比较，因此出现NameError。应该使用赋值操作让status先获得值。

## 函数为什么应该使用自己的参数

函数应该使用自己接收的参数完成处理，避免错误依赖函数外部变量。这样传入不同数据时，函数才能根据实际参数得到正确结果。

## 今天完成了什么程序

函数版学习准备状态评估版

## 我仍然不会什么

目前没有不会的，但在考试过程中独立发现并修复了两个重要问题：
把赋值 =误写成比较 ==，导致 status没有被定义。
函数虽然接收 score参数，却错误使用外部 points变量。

## 明天需要复习什么

定义和调用函数

重复调用函数

单个和多个参数

`return`返回计算结果

返回字典

把列表传入函数