# input()用于暂停程序，等待用户在终端输入内容。输入完成并按回车后，内容会被保存在变量中
name = input("请输入称呼：")
major = input("请输入专业：")
# age = input("请输入年龄：")# age现在属于字符串类型
school = input("请输入学校：")

print(f"你好，{name}")
print(f"专业：{major}")
print(f"学校：{school}")
# print(f"年龄：{age}")
# 只要由 input()直接接收，结果默认就是字符串
# print(type(age))

