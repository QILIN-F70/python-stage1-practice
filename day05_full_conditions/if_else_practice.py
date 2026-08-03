age = int(input("请输入年龄："))

# 与它配对的 else分支会被跳过
# if和 else是互斥分支，只执行其中一个

if age >= 18:
    print("你已成年")
else:
    print("你未成年")
# else表示前面所有条件都不成立的剩余情况，因此不能再写条件
print("年龄判断结束")

# 正确规则：
# if 条件:
# elif 条件:
# else: