# 从文件读取内容

with open("day15_file_io/study_note.txt","r",encoding="utf-8") as file:
    content = file.read()

# "r"表示只读模式。
# file.read()读取文件中的全部文本
# read()：把全部内容读取成一个字符串
# 读取结果会作为一个字符串返回，并保存到 content
# read()负责读取，不会自动显示；仍需使用 print()输出


print("读取到的文件内容：")
print(content)
print(f"读取结果的数据类型：{type(content)}")