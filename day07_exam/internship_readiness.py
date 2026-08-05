print("=" * 30)
print("实习准备状态评估器")
print("=" * 30)

name = input("请输入称呼：")
week_study_hours = float(input("请输入本周学习小时数："))
week_practice_quantity = int(input("请输入本周完成的练习文件数量："))
week_review_status = input("请输入是否完成本周复盘：")

prepare_points = week_study_hours + week_practice_quantity * 2
print("-" * 30)

print(f"称呼：{name}，准备积分：{prepare_points:.2f}")
print(f"本周学习小时数：{week_study_hours}")
print(f"本周完成的练习文件数量：{week_practice_quantity}")
print(f"是否完成本周复盘：{week_review_status}")
print("-" * 30)

if prepare_points >= 20 and week_review_status == "是":
    print("准备状态：优秀")
elif prepare_points >= 12:
    print("准备状态：达标")
else:
    print("准备状态：需要调整")

print("-" * 30)
if week_study_hours >= 15 or week_practice_quantity >= 5:
    print("本周有一项高投入表现")
    print("-" * 30)

print("实习准备评估结束")
print("=" * 30)