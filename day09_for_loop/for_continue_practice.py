# continue 用在 for 循环中
# continue 的作用仍然是：跳过本轮剩余代码，直接进入下一轮。
# 不过这里有一个重要区别：for 会自动取得下一个数据，所以不需要像 while 那样担心把计数更新写在 continue 后面而形成死循环。

for number in range(1, 6):
    if number == 3:
        continue

    print(number)

print("循环结束")