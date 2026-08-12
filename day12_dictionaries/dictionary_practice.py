# 创建字典并读取数据
# 字典使用一对花括号
# 字典中的每项数据由“键”和“值”组成："键": 值
# 键，用来表示这项数据的含义
# 键和值之间使用英文冒号 :
# 不同键值对之间使用英文逗号 ,

task = {
    "name": "学习Python",
    "priority": "高",
    "completed": False
}

print(task)
print(type(task))
# task 的数据类型是字典，dict
print(len(task))
# len(task) 计算的是字典中键值对的数量，也可以理解为键的数量

print(f"任务名称：{task['name']}")
print(f"任务优先级：{task['priority']}")
print(f"是否完成：{task['completed']}")
