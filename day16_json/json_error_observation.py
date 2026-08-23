# JSON格式错误。
# JSON对格式要求比较严格，常见问题包括：
# 键和值之间缺少冒号；
# 两个键值对之间缺少逗号；
# 括号没有配对；
# 手动写入了不符合JSON规则的内容。

import json

with open("day16_json/invalid_tasks.json","r",encoding="utf-8")as file:
    tasks = json.load(file)
    # json.load() 还要分析文件内容是否符合JSON格式；
    # 观察错误时，文件中的两个键值对之间故意缺少逗号，
    # 因此 json.load() 无法解析，并出现 JSONDecodeError。
    # 补回逗号后，文件已恢复为有效JSON。

print(tasks)