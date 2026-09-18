# 为什么不推荐使用空的 except:。
# 空的 except: 会捕获几乎所有异常。表面上程序不崩溃，但它可能把代码本身的错误伪装成用户输入错误

try:
    age = int(input("请输入年龄："))
    print(f"明年的年龄：{age + 1}")
except ValueError:
    print("输入格式错误，请输入整数")

print("程序结束")