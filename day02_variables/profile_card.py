name = "Qi"
age = 23
major = "计科"
graduation_year = 2028
current_year = 2026

years_until_graduation = graduation_year - current_year

print("-" * 30)
print("个人信息卡")
print("=" * 30)
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"专业：{major}")
print(f"预计毕业年份：{graduation_year}")
print(f"距离毕业：约{years_until_graduation}年")
print("=" * 30)

# 三个错误
# 使用不存在的变量
# print(user_name)
# 字符串和整数之间用加号
# print("年龄：" + age)
# 字符串没有引号
# name1 = Qi