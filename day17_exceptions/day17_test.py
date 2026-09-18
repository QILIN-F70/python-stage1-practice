import json

print("=" * 30)
print("异常处理版学习任务读取器")
print("=" * 30)

try:
    quantity = int(input("请输入本周完成练习数量："))
    print(f"转换成功，练习数量：{quantity}")
except ValueError:
    print("转换失败，练习数量必须是整数")

try:
    with open("day17_exceptions/day17_tasks.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)
        print(f"数据类型：{type(tasks)}")
        print(f"任务总数：{len(tasks)}")
        print("-" * 30)
        for task in tasks:
            print(f"每个任务的名称：{task['name']}")
            print("-" * 30)

except FileNotFoundError:
    print("任务文件不存在")
    print("-" * 30)
except json.JSONDecodeError:
    print("任务文件格式错误")
    print("-" * 30)


print("程序结束")
print("=" * 30)