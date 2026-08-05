# 数字运算
a = 10
b = 3
print(a + b) # 加法
print(a - b) # 减法
print(a * b) # 乘法
print(a / b) # 除法
print(a // b) # 整除 向下取整除法
print(a % b) # 取余
print(a ** b) # 幂运算
print("-" * 30)
#变量参与计算
current_year = 2026
future_year = 2028
years = future_year - current_year
print(years)
print("-" * 30)

daily_study_hours = 4
study_hours = 7
weekly_study_hours = daily_study_hours * study_hours
print(weekly_study_hours)
print("-" * 30)

# 运算顺序
one = 10 + 2 * 3
two = (10 + 2) * 3
print(one)
print(two)
# Python会先计算乘除，再计算加减。
# 括号中的内容优先计算。
# 项目中遇到复杂公式时，主动使用括号会更清楚
print("-" * 30)

# 字符串连接
first = "qiqi"
last = "linlin"
full = first + last
print(full)
# 字符串使用 + 时表示连接。

word = "python"
print(word * 3)

print("-" * 30)

# 字符串不能直接与数字相加
# age1 = 23
# print("年龄：" + age1) # 字符串 与 整数不能使用+连接

# f-string可以把变量值放进字符串中。
name = "Qi"
age = 23
print(f"我的名字{name},今年{age}岁。")
# 官方文档规定，格式化字符串在引号前加 f 或 F，并在 {} 中放入需要显示的表达式。
print("-" * 30)

price = 12.5
quantity = 3
total = price * quantity
print(f"商品单价：{price}")
print(f"商品数量：{quantity}")
print(f"商品总价：{total}")