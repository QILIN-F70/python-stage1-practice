# 把函数和 Day 13的任务字典连接起来

def create_task(task_name,priority,completed):
    task = {
        "name":task_name,
        "priority":priority,
        "completed":completed
    }
    return task

first_task = create_task("学习Python","高",False)
second_task = create_task("整理笔记","中",True)

tasks = []
tasks.append(first_task)
tasks.append(second_task)

print(f"第一个任务：{first_task}")
print(f"第二个任务：{second_task}")
print(f"任务总数：{len(tasks)}")
print(f"第一个任务名称：{tasks[0]['name']}")