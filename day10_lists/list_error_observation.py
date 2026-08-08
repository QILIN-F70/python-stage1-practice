# 主动错误观察：访问不存在的索引
# 索引错误
# IndexError: list index out of range
# tasks = ["学习Python","整理笔记","完成练习"]

# print(tasks[2])
# print(tasks[-1])

# 观察第二个错误：列表方法名拼写错误
# 属性错误
# AttributeError: 'list' object has no attribute 'apend'. Did you mean: 'append'?
tasks = ["学习Python","整理笔记"]

tasks.append("完成练习")
print(tasks)