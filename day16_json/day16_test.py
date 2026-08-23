import json

print("=" * 30)
print("JSON学习任务保存与读取器")
print("=" * 30)

tasks = []

for number in range(1,3):
    name = input("请输入任务名称：")
    priority = input("请输入优先级：")
    completed_text = input("是否完成：")

    completed = completed_text == "是"

    task = {
        "name":name,
        "priority":priority,
        "completed":completed
    }
    print("-" * 30)
    tasks.append(task)

with open("day16_json/day16_test_tasks.json","w",encoding="utf-8")as file:
    json.dump(tasks,file,ensure_ascii=False,indent=4)
    print("已写入JSON文件")
    print("-" * 30)

with open("day16_json/day16_test_tasks.json","r",encoding="utf-8")as file:
    new_tasks = json.load(file)

print(f"数据类型：{type(new_tasks)}")
print(f"任务总数：{len(new_tasks)}")
print("-" * 30)

for task in new_tasks:
    print(f"任务名称：{task['name']}")
    print(f"优先级：{task['priority']}")
    print(f"是否完成：{task['completed']}")
    print("-" * 30)

print("程序已结束")
print("=" * 30)