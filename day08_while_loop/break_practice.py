# break 的作用是立即结束它所在的循环。即使 while 条件仍然是 True，执行到 break 后也会直接离开循环。它适合“达到某个条件就提前停止”的场景。

count = 1
while count <= 10:
    if count ==4:
        break

    print(count)
    count = count + 1

print("循环结束")