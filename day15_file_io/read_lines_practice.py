# 按行读取，并把多行结果保存为列表

with open("day15_file_io/study_note.txt","r",encoding="utf-8")as file:
    lines = file.readlines()

print(f"读取结果类型：{type(lines)}")
print(f"文件行数：{len(lines)}")

for line in lines:
    clean_line = line.strip()
    print(f"学习记录：{clean_line}")

# read()：把全部内容读取成一个字符串。
# readlines()：把每一行作为一个字符串，组成一个列表。
# 每一行末尾通常带有 \n。
# line.strip()会去掉字符串开头和末尾的空白内容，包括末尾换行。