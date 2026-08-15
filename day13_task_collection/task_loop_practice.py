# 使用 for 循环遍历多个任务字典

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

for task in tasks:
    print(f"任务名称：{task['name']}")
    print(f"任务优先级：{task['priority']}")
    print(f"是否完成：{task['completed']}")
    print("-" * 30)

print("任务遍历结束")