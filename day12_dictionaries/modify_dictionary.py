# 修改和添加键值对
# 字典使用下面的格式修改数据：字典变量[键] = 新值
# 如果键已经存在，就修改原来的值；如果键不存在，就添加新的键值对

task = {
    "name":"学习Python",
    "priority":"高",
    "completed":False
}

print(f"修改前：{task}")
print(f"修改前数量：{len(task)}")

task["priority"] = "中"
task["completed"] = True
task["deadline"] = "2026-08-15"

print(f"修改后：{task}")
print(f"修改后数量：{len(task)}")
print(f"截止日期：{task['deadline']}")