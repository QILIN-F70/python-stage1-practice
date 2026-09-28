from task_utils import create_task

second_task = create_task("整理笔记","中")

print(second_task)
print(f"是否完成：{second_task['completed']}")