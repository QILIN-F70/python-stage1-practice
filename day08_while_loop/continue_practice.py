# continue 的作用是：
# 跳过本轮循环中剩余的代码，然后返回循环开头，继续判断下一轮。它与 break 不同：
# break：结束整个循环。
# continue：只跳过当前这一轮。

count = 0
while count < 5:
    count = count + 1

    if count == 3:
        continue

    print(count)

print("循环结束")
