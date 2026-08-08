# 在 for 循环中使用 break。
# 区别需要记牢：
# continue：只跳过当前这一轮，然后继续下一轮。
# break：直接终止整个循环，后面的数据不再处理。


for number in range(1, 7):
    if number == 4:
        break

    print(number)

print("循环结束")