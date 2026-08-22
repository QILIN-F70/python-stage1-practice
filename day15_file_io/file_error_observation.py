# FileNotFoundError。它通常发生在：使用只读模式打开一个不存在的文件

with open("day15_file_io/study_note.txt","r",encoding="utf-8")as file:
    content = file.read()


print(content)