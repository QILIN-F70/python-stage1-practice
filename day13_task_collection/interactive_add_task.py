# 把 Day 12 和今天的知识连接起来：接收用户输入，建立任务字典，再添加到任务列表

tasks = []

name = input("请输入任务名称：")
priority = input("请输入任务优先级：")
completed_text = input("是否完成：")

completed = completed_text == "是"

new_task = {
    "name":name,
    "priority":priority,
    "completed":completed
}

tasks.append(new_task)

print("-" * 30)
print(f"新增任务：{new_task}")
print(f"当前任务数量：{len(tasks)}")
print(f"第一个任务名称：{tasks[0]['name']}")
print(f"第一个任务完成状态：{tasks[0]['completed']}")