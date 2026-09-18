# try:
#     可能出现异常的代码
# except 异常类型:
#     出现这种异常后执行的代码

# 执行规律：
# 1. Python 先执行 try 中的代码。
# 2. 没有异常，就跳过 except。
# 3. 出现匹配的异常，就停止执行 try 中剩余代码，转去执行 except。
# 4. except 执行完后，程序可以继续向下运行。

try:
    age = int(input("请输入年龄："))
    print(f"明年的年龄：{age + 1}")
except ValueError:
    print("输入格式错误，请输入整数")

print("年龄处理程序结束")