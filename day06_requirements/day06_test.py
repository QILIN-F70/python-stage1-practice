print("=" * 30)
print("每周学习状态评估器")
print("=" * 30)

name = input("请输入称呼：")
day_hours = float(input("请输入每天学习小时数："))
week_days = int(input("请输入每周学习天数："))
week_review_status = input("请输入是否完成本周复盘：")

total_week_hours = day_hours * week_days

print("-" * 30)
print(f"称呼：{name}，每周学习总小时数：{total_week_hours:.2f}")
print(f"每天学习小时数：{day_hours}")
print(f"每周学习天数：{week_days}")
print(f"是否完成本周复盘：{week_review_status}")
print("-" * 30)

if total_week_hours >= 15 and week_review_status == "是":
    print("学习状态：优秀")
elif total_week_hours >= 8:
    print("学习状态：达标")
else:
    print("学习状态：需要调整")

print("-" * 30)

if day_hours >= 3 or week_days == 7:
    print("本周有一项高投入表现")
    print("-" * 30)

print("每周学习状态评估结束")
print("=" * 30)