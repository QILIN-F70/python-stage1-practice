print("=" * 30)
print("课程综合资格判断器")
print("=" * 30)
name = input("请输入称呼：")
score = int(input("请输入考试成绩："))
attendance = int(input("请输入出勤率："))
project_status = input("是否完成项目：")
print("-" * 30)
print(f"{name}的成绩是：{score},出勤率为：{attendance},是否完成项目：{project_status}")
print("-" * 30)
if score >= 90 and attendance >= 90 and project_status == "是":
    print("综合等级：优秀")
elif score >= 60 and attendance >= 80:
    print("综合等级：合格")
else:
    print("综合等级：需要继续努力")
print("-" * 30)
if score == 100 or attendance == 100:
    print("有一项获得满分")
    print("-" * 30)
print("综合资格检查结束")
print("=" * 30)