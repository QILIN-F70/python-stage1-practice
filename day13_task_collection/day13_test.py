print("=" * 30)
print("交互式任务集合统计与查找器")
print("=" * 30)

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
    }
]

name = input("请输入新任务的名称：")
priority = input("请输入新任务的优先级：")
completed_text = input("是否完成：")
print("-" * 30)

completed = completed_text == "是"

new_task = {
    "name":name,
    "priority":priority,
    "completed":completed
}
# 把新任务字典添加到任务列表
tasks.append(new_task)

completed_count = 0

# 使用 for 循环显示全部任务的信息
for task in tasks:
    print(task)
    print("-" * 30)
    if task["completed"] == True:
        completed_count = completed_count + 1
print("-" * 30)
pending_count = len(tasks) - completed_count

# 统计任务总数、已完成数量和未完成数量。
print(f"任务总数：{len(tasks)}")
print(f"已完成数量：{completed_count}")
print(f"未完成数量：{pending_count}")
print("-" * 30)

found = False
target_name = input("请输入要查找的任务：")
for task in tasks:
    if task["name"] == target_name:
        print(f"找到任务：{task['name']}")
        print(f"优先级：{task['priority']}")
        print(f"完成状态：{task['completed']}")
        found = True
        print("-" * 30)
        break

if not found:
    print("没有找到该任务")
    print("-" * 30)

print("程序结束")
print("=" * 30)




