# 一个函数也可以接收多个参数。多个参数之间使用英文逗号分隔，调用时通常按从左到右的顺序对应

def show_task(task_name,priority,completed):
    print("-" * 30)
    print(f"任务名称：{task_name}")
    print(f"优先级：{priority}")
    print(f"是否完成：{completed}")

show_task("学习Python","高",False)
show_task("整理笔记","中",True)