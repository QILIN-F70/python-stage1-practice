# 学习追加写入模式 "a"

new_note = input("请输入新的学习记录：")

with open("day15_file_io/study_note.txt","a",encoding="utf-8")as file:
    file.write(new_note + "\n")

# "a"来自 append，表示追加。
# 文件存在时，新内容写在原内容末尾，不会删除旧内容。
# 文件不存在时，通常也会创建新文件。
# new_note + "\n"是在用户输入内容后增加换行。


print("新的学习记录已经追加")