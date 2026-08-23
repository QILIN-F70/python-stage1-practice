# 向JSON任务集合中增加一个任务并永久保存
# 这里有一个关键点：
# 不能简单地使用 "a" 把一个字典追加到JSON文件末尾。
# 因为整个 tasks.json 是一个完整的列表结构。
# 直接在文件末尾追加内容，可能会变成两个结构拼在一起，导致JSON格式无效。

# 正确流程：
# 读取整个JSON
# → 得到Python列表
# → 向列表append新字典
# → 使用w重新写入完整列表

import json

with open("day16_json/tasks.json","r",encoding="utf-8")as file:
    tasks = json.load(file)

name = input("请输入新任务名称：")
priority = input("请输入新任务优先级：")
completed_text = input("是否完成：")

completed = completed_text == "是"

new_task = {
    "name":name,
    "priority":priority,
    "completed":completed
}

tasks.append(new_task)

with open("day16_json/tasks.json","w",encoding="utf-8")as file:
    json.dump(tasks,file,ensure_ascii=False,indent=4)

print("新任务已经添加并保存")
print(f"当前任务数量：{len(tasks)}")
print(f"最后一个任务：{tasks[-1]}")