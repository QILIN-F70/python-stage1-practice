# 函数参数错误
# 但函数要求的参数数量与实际传入数量不匹配，因此会出现 TypeError

def show_task(task_name,priority):
    print(f"任务名称：{task_name}")
    print(f"优先级：{priority}")

# TypeError
# show_task("学习Python")

show_task("学习Python","高")