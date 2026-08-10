# append() 只能把新元素追加到列表末尾。
# 如果我们想把任务插入列表中间，就需要：
# 列表名.insert(索引, 新元素)
# 例如：
# tasks.insert(1, "整理笔记")

# insert()：在指定位置插入元素
tasks = ["学习Python","完成练习"]

print(f"插入前：{tasks}")

tasks.insert(1,"整理笔记")

print(f"插入后：{tasks}")
print(f"任务数量：{len(tasks)}")