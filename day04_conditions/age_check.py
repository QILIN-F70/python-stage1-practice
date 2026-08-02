age = int(input("请输入年龄："))
# 这里必须使用：
# int(input(...))
# 因为 input()默认返回 str，而 18是 int。转换后才能进行数字大小比较。

if age >= 18:
    print("你已满足成年条件")

print("年龄检查结束")