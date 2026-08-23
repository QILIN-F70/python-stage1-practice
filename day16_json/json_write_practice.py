# 把 Python数据写入 JSON文件
# JSON是一种用于保存和交换结构化数据的文本格式
# 适合保存我们已经学过的“列表中包含多个字典”
# JSON文件可以保留这种结构；
# 以后读取时，可以重新得到列表和字典，而不只是普通文本。

import json # import json：导入Python自带的JSON工具模块。

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
    }    
]

with open("day16_json/tasks.json","w",encoding="utf-8")as file:
    json.dump(tasks,file,ensure_ascii=False,indent=4)
    # json.dump(...)：把 Python数据写入已经打开的 JSON文件
    # tasks：需要写入的数据。
    # file：已经打开的文件对象。
    # ensure_ascii=False：让中文以正常文字保存，而不是转换成字符编码形式。
    # indent=4：使用4个空格缩进，让JSON文件更容易阅读。
    # "w"：文件不存在时创建，存在时先清空旧内容再写入。
print("任务数据已经写入JSON文件")