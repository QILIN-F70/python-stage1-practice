# 类型转换input()
age_text = input("请输入年龄：")
print(type(age_text))

# int()
age = int(age_text)
print(type(age))

# 验证转换后可以参与数字运算
next_age = age + 1
print(f"明年的年龄：{next_age}")
#"23"（str）→ int() → 23（int）→ 可以计算得到24

# float()
height_text = input("请输入身高（米）：")
print(type(height_text))

height = float(height_text)
print(type(height))
print(f"你的身高是：{height}米")

# 错误练习
# wrong_age = input("请输入年（错误练习）：")
# wrong_next_age = int(wrong_age) + 1
# 原因：
# wrong_age是 input()返回的 str
# 1是 int
# str + int类型不兼容
# print(wrong_next_age)

