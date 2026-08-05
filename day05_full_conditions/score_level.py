score = int(input("请输入成绩："))

if score >= 90:
    print("成绩优秀")
elif score >= 60:
    print("成绩及格")
else:
    print("成绩不及格")

print("成绩等级判断结束")

# if / elif / else属于同一条条件链。
# Python从上到下判断。
# 找到第一个 True分支后立即执行它。
# 同一条条件链中的后续分支全部跳过。

# elif 用于继续判断其他明确条件，可以有多个。
# else 已经代表“前面所有条件都不成立时的剩余情况”，所以不能再写条件。