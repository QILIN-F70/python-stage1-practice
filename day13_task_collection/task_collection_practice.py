# 列表中保存字典
# tasks[0]["name"]：先找到第一个任务，再读取它的名称
tasks = [
    {
        "name":"学习Python",
        "priority":"高",
        "completed":False
     },
     {
         "name":"整理笔记",
         "priority":"中",
         "completed":True
     }
]

print(tasks)
print(type(tasks))
print(len(tasks))
print(tasks[0])
print(type(tasks[0]))

print(tasks[0]["name"])
# 执行顺序是：
# tasks[0]：从列表中取出第一个任务字典。
# ["name"]：从这个字典中取出任务名称。
