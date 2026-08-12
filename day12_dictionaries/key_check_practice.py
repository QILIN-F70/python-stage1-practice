# 判断字典中是否存在某个键
# 在字典中使用 in 时，默认判断的是“键”，不是值
# 为什么需要先判断键：如果直接读取一个不存在的键，程序会产生 KeyError。先用 in 判断，可以避免程序因为键不存在而停止

task = {
    "name":"学习Python",
    "priority":"高",
    "completed":False
}

print(f"name键是否存在：{'name' in task}")
print(f"deadline键是否存在：{'deadline' in task}")
print(f"学习Python是否作为键存在：{'学习python' in task}")

if "priority" in task:
    print(f"任务优先级:{task['priority']}")
else:
    print("没有优先级信息")

if "deadline" in task:
    print(f"截止日期：{task['deadline']}")
else:
    print(f"没有截至日期信息")