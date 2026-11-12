# “模块入口”：导入一个 .py 文件时，哪些代码会执行，以及怎样让某些代码只在直接运行该文件时执行

# print(f"helper.py的 __name__:{__name__}")
# Python 如何区分“直接运行”和“被导入”。Python 会自动给模块设置 __name__：
# 直接运行一个文件时，它的 __name__ 是 "__main__"。
# 作为模块被导入时，它的 __name__ 是模块名。


# print("helper.py 的普通代码开始执行")

def show_message():
    print("show_message 函数被调用")

if __name__ == "__main__":
    print("helper.py 作为主程序运行")
    show_message()