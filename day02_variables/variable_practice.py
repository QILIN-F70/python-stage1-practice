# name = "Qi"
# 变量名 赋值符号 保存的值
# 把字符串"Qi"保存到变量name中

# 变量与普通文字区别
# print(name) # 读取变量中的内容
# print("name") # 直接输出字符串"name"

# 赋值不是数字等号
# age = 23    # =：把右边23保存到左边的age变量中
# 区分： = 赋值 // == 判断是否相等

# 变量命名写法（英文，数字，下划线）
# 见名知意；多个英文单词可用_下划线链接；
# 不能以数字开头，不能包含空格 减号 -；

# 四种基础数据类型
# 字符串 str (字符串要使用引号)
# name1 = "ql"
# 整数 int (整数，不加引号)
# age1 = 23
# year = 2026
# 浮点数 float (带小数点的数)
# height = 1.65
# price = 23.3
# 布尔值 bool (表示“是或否、真或假”)
# is_student = True
# 布尔值只有 True / False （首字母必须大写，并且不加引号）
print("-" * 30)


# 变量练习
name = "Qi"
age = 22
major = "计科"
height = 1.65
is_student = True
has_development_internship = False

print(name)
print(age)
print(major)
print(height)
print(is_student)
print(has_development_internship)

print("-" * 30)

# type()查看类型
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print("-" * 30)

# 变量可以被重新赋值
current_stage = "Day1"
print(current_stage)
current_stage = "Day2"
print(current_stage)
# 第二次赋值会把变量中的旧值替换成新值
