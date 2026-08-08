# 列表索引
# 索引可以理解为列表中每个元素的位置编号
# Python 从 0 开始编号，不是从 1 开始

# 正向索引
tasks = ["学习Python","整理笔记","完成练习"]

print(tasks[0])
print(tasks[1])
print(tasks[2])

# 负数索引。
# Python 除了从左向右使用 0、1、2 编号，也可以从右向左使用负数编号：
# 需要特别记住：
# tasks[-1]
# 表示最后一个元素。

print("-" * 30)
print(tasks[-1])
print(tasks[-2])
print(tasks[-3])