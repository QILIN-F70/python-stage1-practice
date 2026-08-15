# 在任务列表中查找指定任务
# 用户输入任务名称，程序逐个检查列表中的字典，找到目标任务后显示其信息

# 程序需要一个“是否找到”的状态标记：
# found = False
# 开始查找前，我们默认还没有找到任务，所以是 False。如果循环中找到名称相同的任务，就把它修改为 True，并用 break 结束查找

tasks = [
    {
        "name":"学习Python",
        "priority":"高",
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
        "completed":False
    }
]

target_name = input("请输入要查找的任务名称：")
found = False

for task in tasks:
    if task["name"] == target_name:
        print(f"找到任务：{task['name']}")
        print(f"任务优先级：{task['priority']}")
        print(f"是否完成：{task['completed']}")
        # 观察一个“逻辑错误”
        # 临时在前面添加 #
        found = True
        break

if not found:
    print("没有找到该任务")

print("任务查找结束")