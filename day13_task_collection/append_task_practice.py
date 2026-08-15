# 把一个新任务字典添加到任务列表中

tasks =[
    {
        "name":"学习Python",
        "priority":"高",
        "completed":False
    }
]

new_task = {
    "name":"整理笔记",
    "priority":"中",
    "completed":False
}

print(f"添加前任务数量：{len(tasks)}")

tasks.append(new_task)
# 是把整个 new_task 字典作为一个新元素，追加到 tasks 列表末尾。字典内部虽然有三个键值对，但它在外层列表中只算一个元素

print(f"添加后任务数量：{len(tasks)}")
print(f"最后一个任务：{tasks[-1]}")
print(f"最后一个任务名称：{tasks[-1]['name']}")