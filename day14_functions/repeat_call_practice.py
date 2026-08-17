# 同一个函数可以调用多次，而函数内部的代码只需要写一次

def show_task_menu():
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 退出程序")

print("第一次显示菜单")
show_task_menu()

print("-" * 30)

print("第二次显示菜单")
show_task_menu()