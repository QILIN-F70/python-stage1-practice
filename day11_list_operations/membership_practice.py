# in 用来判断某个元素是否存在于列表中，结果是布尔值：
# 元素 in 列表
# 存在时得到：
# True
# 不存在时得到：
# False

# 假如用户要求删除 "写学习日志"，我们最好先判断这个任务是否存在。否则直接使用 remove() 删除不存在的内容，程序会报错。

tasks = ["学习Python","整理笔记","完成练习"]

search_task = input("请输入要查找的任务：")

print(f"是否存在：{search_task in tasks}")

if search_task in tasks:
    print("任务已在列表中")
else:
    print("列表中没有这个任务")