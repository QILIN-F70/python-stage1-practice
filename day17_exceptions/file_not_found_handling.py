# 接着处理另一种常见异常：FileNotFoundError。
# # 当我们用 "r" 读取一个不存在的文件时

# 进入 try
# → open() 产生 FileNotFoundError
# → try 剩余代码停止
# → 进入 except FileNotFoundError
# → 继续执行结构外代码

try:
    with open(
        "day17_exceptions/missing_tasks.txt",
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("任务文件不存在，请先创建文件")

print("文件读取程序结束")