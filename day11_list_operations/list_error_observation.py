# 主动错误观察：删除不存在的元素。
# ValueError: list.remove(x): x not in list
# Python 无法找到要删除的内容，因此程序会出现 ValueError。这也说明，来自用户的删除要求不能直接交给 remove()，后面需要先用 in 判断。

tasks = ["学习Python","整理笔记","完成练习"]

print(f"删除前：{tasks}")

delete_task = "写学习日志"

if delete_task in tasks:
    tasks.remove(delete_task)
    print("任务删除成功")
else:
    print("任务不存在，无法删除")

print(f"删除后：{tasks}")
