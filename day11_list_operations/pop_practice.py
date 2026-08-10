# pop() 根据索引删除元素，同时把被删除的元素交还给程序：
# 被删除的元素 = 列表名.pop(索引)
# removed_task = tasks.pop(1)
# 执行过程：
# 找到索引 1 对应的元素；
# 从列表中删除它；
# 把被删除的元素保存到 removed_task。
# pop(1)：根据索引删除，而且可以获得被删除的元素。


tasks = ["学习Python","整理笔记","完成练习"]

print(f"取出前：{tasks}")

removed_task = tasks.pop(1)

print(f"被取出的任务：{removed_task}")
print(f"取出后：{tasks}")
print(f"剩余任务数量：{len(tasks)}")