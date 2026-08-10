# remove() 根据元素的内容，从列表中删除这个元素：
# 列表名.remove(要删除的元素)
# 这是删除元素，列表长度会减少。

# remove(元素内容)：按照内容删除，成功后直接修改原列表，但不会返回被删除的元素；它的返回值是 None，可以暂时理解为“没有提供可用的返回结果”。
# 如果元素不存在，remove() 不会返回 False，而是直接产生 ValueError。
# pop(索引)：按照索引删除，并返回被删除的元素，所以可以用变量接收。

tasks = ["学习Python","整理笔记","完成练习"]

print(f"删除前：{tasks}")
print(f"删除前数量：{len(tasks)}")

tasks.remove("整理笔记")

print(f"删除后：{tasks}")
print(f"删除后数量：{len(tasks)}")