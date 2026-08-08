total = 0
# total = 0 是在初始化累加变量，而且必须放在循环外面，只执行一次。这样每轮得到的结果才能保留并继续累加。
# 如果把它放进循环里面：
# for number in range(1, 6):
#     total = 0
#     total = total + number
# 每一轮都会先把 total 重置为 0，前面累计的结果就丢失了，最终得到的会是 5，而不是 15。
for number in range(1, 6):
    total = total + number
    print(f"本轮数字：{number}，当前总和：{total}")

print(f"最终总和：{total}")