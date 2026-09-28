import task_tools

# 在循环外定义
tasks = []

for number in range(1,3):
    name = input("请输入任务名称:")
    priority = input("请输入任务优先级:")
    completed_text = input("任务是否完成:")

    new_task = task_tools.create_task(name,priority,completed_text)

    print("-" * 30)
    print(new_task)

    tasks.append(new_task)

print("-" * 30)
print(tasks)
print("-" * 30)

completed_count = task_tools.count_completed(tasks)
print(f"任务总数:{len(tasks)}")
print(f"已完成数量:{completed_count}")
print(f"未完成数量:{len(tasks) - completed_count}")

for task in tasks:
    print(f"任务名称：{task['name']}")