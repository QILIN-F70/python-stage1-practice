# 观察字典常见错误：KeyError

task = {
    "name":"学习Python",
    "priority":"高",
    "completed":False
}

if "deadline" in task:
    print(f"截止日期：{task['deadline']}")
else:
    print("没有截止日期信息")