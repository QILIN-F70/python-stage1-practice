# 从JSON文件恢复Python数据

import json

with open("day16_json/tasks.json","r",encoding="utf-8")as file:
    tasks = json.load(file)
    # json.load(file)：从已经打开的JSON文件读取数据，并转换成对应的 Python数据
    # load 和昨天的 read 不同：
    # file.read() 得到一个字符串；
    # json.load(file) 会根据JSON结构恢复列表、字典、布尔值等数据

print(f"读取结果类型：{type(tasks)}")
print(f"任务数量：{len(tasks)}")

for task in tasks:
    print("-" * 30)
    print(f"任务名称：{task['name']}")
    print(f"任务优先级：{task['priority']}")
    print(f"是否完成：{task['completed']}")

print("-" * 30)
print("JSON数据读取结束")

# Python列表/字典
# → json.dump()
# → JSON文件
# → json.load()
# → Python列表/字典