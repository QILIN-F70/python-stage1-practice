# 统计已完成和未完成的任务数量
tasks = [
    {
        "name":"学习Python",
        "priority":"高",
        "completed":True
    },
    {
        "name":"整理笔记",
        "priority":"中",
        "completed":False
    },
    {
        "name":"完成练习",
        "priority":"高",
        "completed":True
    }
]

completed_count = 0

# 遍历列表中的三个字典
for task in tasks:
    if task["completed"] == True:
        completed_count = completed_count + 1

pending_count = len(tasks) - completed_count
# 通过总数减已完成数，得到未完成数量

print(f"任务总数：{len(tasks)}")
print(f"已完成任务数量：{completed_count}")
print(f"未完成任务数量：{pending_count}")