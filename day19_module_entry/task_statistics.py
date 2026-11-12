# 放统计函数和模块自测
# 让同一个模块既能被主程序导入，又能单独运行自测

def count_completed(tasks):
    count = 0
    for task in tasks:
        if task["completed"]:
            count += 1
    return count

def show_summary(tasks):
    completed_count = count_completed(tasks)
    print(tasks)
    print(f"任务总数：{len(tasks)}")
    print(f"已完成数量：{completed_count}")
    print(f"未完成数量：{len(tasks) - completed_count}")

if __name__ == "__main__":
    tasks = [
        {
            "name":"学习Python",
            "priority":"高",
            "completed": False
        },
        {
            "name":"整理笔记",
            "priority":"中",
            "completed": True
        }
    ]
    print("=" * 30)
    print("模块独立测试")
    print("=" * 30)
    show_summary(tasks)