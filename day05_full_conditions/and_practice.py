# and表示“并且”
# 连接的两个条件必须同时为 True，整体结果才是 True。
# True  and True  → True
# True  and False → False
# False and True  → False
# False and False → False

score = int(input("请输入成绩："))
attendance = int(input("请输入出勤率："))

if score >= 60 and attendance >= 80:
    print("满足综合资格")
else:
    print("不满足综合资格")

print("资格检查结束")