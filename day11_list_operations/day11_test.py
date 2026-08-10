print("=" * 30)
print("交互式学习任务维护器")
print("=" * 30)

tasks = ["学习Python","整理笔记","完成练习"]

print(f"初始完整列表：{tasks}")
print(f"初始任务数量：{len(tasks)}")
print("-" * 30)

tasks.insert(1,"复习列表操作")

new_task = input("请输入一个新任务：")
if new_task not in tasks:
    tasks.append(new_task)
    print("任务添加成功")
else:
    print("任务已经存在")
print("-" * 30)

delete_task = input("请输入需要删除的任务：")
if delete_task in tasks:
    tasks.remove(delete_task)
    print("任务删除成功")
else:
    print("任务不存在，无法删除")
print("-" * 30)

first_task = tasks.pop(0)

print(f"被取出的第一个任务：{first_task}")
print(f"最终完整列表：{tasks}")
print(f"最终任务数量：{len(tasks)}")
print(f"最后一个任务：{tasks[-1]}")

print("=" * 30)

