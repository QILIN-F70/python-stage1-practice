# 使用 for 循环接收连续5天的学习小时数，统计学习情况
print("=" * 30)
print("统计学习情况")
print("=" * 30)
name = input("请输入称呼：")
total_hours = 0
high_effort_days = 0
print("-" * 30)

for day in range(1, 6):
    hours = float(input(f"请输入第{day}天学习小时数:"))
    total_hours = total_hours + hours
    
    if hours >= 3:
        high_effort_days = high_effort_days + 1
        print(f"第{day}天算高投入学习")

    print("-" * 30)

print(f"{name}的五天学习总小时数：{total_hours:.2f}，高投入的天数为：{high_effort_days}")

if total_hours >= 15:
    print("学习状态：优秀")
elif total_hours >= 8:
    print("学习状态：达标")
else:
    print("学习状态：需要调整")

print("-" * 30)

if high_effort_days >=3:
    print("本周至少有3天进行了高投入学习")
    print("-" * 30)

print("统计学习情况结束")
print("=" * 30)


