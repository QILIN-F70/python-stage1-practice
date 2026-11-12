# 作为主程序，导入并使用统计函数
# 让同一个模块既能被主程序导入，又能单独运行自测
import task_statistics
my_tasks = [
    {
        "name":"学习Python",
        "priority":"中",
        "completed":False
    },
    {
        "name":"整理笔记",
        "priority":"中",
        "completed":True
    },
    {
        "name":"完成练习",
        "priority":"高",
        "completed":True
    },
]
print("-" * 30)
print("主程序开始")
print("-" * 30)
task_statistics.show_summary(my_tasks)
print("主程序结束")
print("-" * 30)