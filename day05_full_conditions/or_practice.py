# or表示“或者”
# 两个条件中只要至少一个为 True，整体结果就是 True。
# True  or True  → True
# True  or False → True
# False or True  → True
# False or False → False

day = input("请输入星期：")

if day == "周六" or day == "周日":
    print("今天是休息日")
else:
    print("今天是学习日")

print("星期判断结束")