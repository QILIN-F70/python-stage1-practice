print("=" * 30)
print("学习任务清单管理器")
print("=" * 30)

tasks = ["复习Python","整理笔记","完成练习"]

print(f"初始完整列表：{tasks}")
print(f"列表数据的类型：{type(tasks)}")
print(f"初始任务数量：{len(tasks)}")

print("-" * 30)

print(f"第一个任务：{tasks[0]}")
print(f"最后一个任务：{tasks[-1]}")

print("-" * 30)

tasks[1] = input("修改后的第二个任务：")
tasks.append(input("输入一个新任务："))
print("-" * 30)

for task in tasks:
    print(task)

print(f"最终任务数量：{len(tasks)}")
print(f"添加后的最后一个任务：{tasks[-1]}")
print("-" * 30)
print("学习任务清单管理结束")
print("=" * 30)