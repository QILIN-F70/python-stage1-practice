# 修改“列表中的字典”

tasks = [
    {
        "name":"学习Python",
        "priority":"高",
        "completed":False
    },
    {
        "name":"整理笔记",
        "priority":"中",
        "completed":False
    }
]

print(f"修改前：{tasks[0]}")

tasks[0]["completed"] = True
tasks[0]["priority"] = "中"

print(f"修改后：{tasks[0]}")
print(f"任务总数：{len(tasks)}")
print(f"第二个任务名称：{tasks[1]['name']}")