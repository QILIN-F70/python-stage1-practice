# 把列表传给函数。函数的参数不只能接收字符串和数字，也能接收整个列表

def count_completed(task_list):
    completed_count = 0

    for task in task_list:
        if task["completed"]:
            # 取出来的值本身已经是布尔值，if True:
            #task["completed"] == True:
            completed_count = completed_count + 1

    return completed_count

tasks = [
    {
        "name":"学习Python",
        "completed":True
    },
    {
        "name":"整理笔记",
        "completed":False
    },
    {
        "name":"完成练习",
        "completed":True
    },        
]

result = count_completed(tasks)

print(f"任务总数：{len(tasks)}")
print(f"已完成任务数量：{result}")
print(f"未完成任务数量：{len(tasks) - result}")