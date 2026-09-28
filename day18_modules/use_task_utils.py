import task_utils

first_task = task_utils.create_task("学习Python","高")

print(first_task)
print(f"任务名称：{first_task['name']}")