# 主动观察错误

# 1.缺少冒号-----SyntaxError
# 冒号表示 for 循环头部结束，下一行将开始循环体。
# for number in range(1, 4)
#     print(number)


# 2.循环体没有缩进-----IndentationError
# for number in range(1, 4):
# print(number)


# 3.range() 结束值造成的逻辑错误
# 假设需求是输出 1 到 5
for number in range(1, 6):
    print(number)