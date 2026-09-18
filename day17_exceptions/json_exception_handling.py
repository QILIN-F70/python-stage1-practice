# - 文件不存在：FileNotFoundError
# - 文件存在，但 JSON 格式错误：json.JSONDecodeError
# 不同问题应该给出不同提示，所以可以连续写多个 except。发生异常后，Python会寻找与异常类型匹配的分支，只执行其中一个。

import json

try:
    with open(
        "day17_exceptions/tasks_data.json",
        "r",
        encoding="utf-8"
    ) as file:
        tasks = json.load(file)

    print(f"读取成功，任务数量：{len(tasks)}")
except FileNotFoundError:
    print("JSON文件不存在")
except json.JSONDecodeError:
    print("JSON文件格式错误")

print("JSON读取程序结束")