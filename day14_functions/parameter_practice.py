# “函数参数”。
# 刚才的菜单函数每次输出完全相同的内容。如果希望同一个函数每次处理不同的数据，就需要参数

# def show_task(task_name):
# 这里的 task_name叫“参数”，可以理解为函数内部暂时使用的变量
# show_task("学习Python")
# 这里的 "学习Python"是调用函数时传入的实际数据，也常叫“实参”。调用时，这个值会暂时交给 task_name使用

def show_task(task_name):
    print("-" * 30)
    print(f"任务名称：{task_name}")

show_task("学习Python")
show_task("整理笔记")
show_task("完成练习")