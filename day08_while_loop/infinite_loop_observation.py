# “死循环”。
# 死循环是指循环条件一直为 True，程序不断重复执行，无法自然结束。计数器没有更新，是初学阶段最常见的原因之一。

count = 1
while count <= 5:
    print(count)
    count = count + 1
    