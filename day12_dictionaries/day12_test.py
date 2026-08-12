print("=" * 30)
print("交互式学习任务信息维护器")
print("=" * 30)

name = input("请输入任务名称：")
priority = input("请输入任务优先级：")
completed_text = input("是否完成：")

completed = completed_text == "是"

task = {
    "name": name,
    "priority": priority,
    "completed": completed
}
print("-" * 30)

print(f"初始完整字典：{task}")
print(f"字典数据类型：{type(task)}")
print(f"初始键值对数量：{len(task)}")
print("-" * 30)
print(f"任务名称：{task['name']}")
print(f"任务优先级：{task['priority']}")
print(f"是否完成：{task['completed']}")
print("-" * 30)

task["deadline"] = input("请输入截止日期：")
task["priority"] = input("请输入修改后的优先级")
print("-" * 30)

print(f"修改后的完整字典：{task}")
print(f"修改后的键值对数量：{len(task)}")
print(f"截止日期：{task['deadline']}")
print(f"修改后的优先级：{task['priority']}")
print("-" * 30)

if "note" in task:
    print(task["note"])
else:
    print("没有备注信息")
print("-" * 30)

print("程序结束")
print("=" * 30)
