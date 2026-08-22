# 综合练习：把列表中的多个任务逐行保存到文件，再读取回来


# 遍历内存中的 tasks列表，把每个任务写成一行。
# 从文件重新读取任务，得到新的 saved_tasks列表。
tasks = [
    "学习Python",
    "整理笔记",
    "完成练习"
]

with open("day15_file_io/tasks.txt","w",encoding="utf-8")as file:
    for task in tasks:
        file.write(task + "\n")

print("任务列表已经保存")

with open("day15_file_io/tasks.txt","r",encoding="utf-8")as file:
    saved_tasks = file.readlines()

print(f"读取结果类型：{type(saved_tasks)}")
print(f"已保存任务数量：{len(saved_tasks)}")

for task in saved_tasks:
    print(f"任务：{task.strip()}")