print("main.py 开始")
import helper
# import helper 会执行 helper.py 中函数外面的代码，其中包括文件末尾的 show_message()
helper.show_message()
print("main.py 结束")