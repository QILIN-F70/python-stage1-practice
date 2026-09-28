# 模块名必须和文件名一致；你的文件叫 task_utils.py，如果导入时少写一个 s，Python 就找不到对应模块

print("导入前")
# import task_util 少写s的情况下错误观察
# 准确异常名称是 ModuleNotFoundError：Python 找不到名为 task_util 的模块

import task_utils
print("导入后")

# 错误2
# 模块找到了，但你写的函数名不在模块里。task_utils.py 定义的是 create_task，没有定义 make_task。这种情况会产生 AttributeError。

# AttributeError
# task = task_utils.make_task("完成练习","高")


task = task_utils.create_task("完成练习","高")
print(task)