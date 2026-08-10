# 元素 not in 列表
# 表示判断某个元素“不在列表中”。
# 不存在：结果为 True
# 已经存在：结果为 False

# 它很适合防止重复添加任务：
# if new_task not in tasks:
#     tasks.append(new_task)

tasks = ["学习Python","整理笔记","完成练习"]

new_task = input("请输入新任务：")

if new_task not in tasks:
    tasks.append(new_task)
    print("任务添加成功")
else:
    print("任务已经存在，不能重复添加")


print(f"当前任务列表：{tasks}")
print(f"当前任务数量：{len(tasks)}")
