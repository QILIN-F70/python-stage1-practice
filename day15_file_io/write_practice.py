# 把数据写入文件

with open("day15_file_io/study_note.txt","w",encoding="utf-8") as file:
    file.write("今天学习Python文件写入\n")
    file.write("目标是让程序保存数据\n")

print("学习记录已经写入文件")

# open()：打开文件。
# "day15_file_io/study_note.txt"：文件保存位置。
# "w"：写入模式。文件不存在时会创建；文件已存在时会覆盖原内容。
# encoding="utf-8"：指定文本编码，使中文能够正常保存和读取。
# as file
# 把打开的文件交给变量 file操作。
# file.write(...)
# 把字符串写入文件。
# \n
# 表示换行。write()不会像 print()一样自动换行，所以需要主动写入 \n。
# with代码块结束后，Python会自动关闭文件。