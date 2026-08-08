# 使用 append() 在列表末尾添加元素。
# append 可以理解为“追加”。
# 当程序运行过程中产生一个新任务时，可以把它添加到现有列表末尾

tasks = ["学习Python","整理笔记"]

print(f"添加前：{tasks}")
print(f"添加前数量：{len(tasks)}")

tasks.append("完成练习")

print(f"添加后：{tasks}")
print(f"添加后数量：{len(tasks)}")
print(f"最后一个任务：{tasks[-1]}")