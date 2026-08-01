name = input("请输入称呼：")
daily_hours = float(input("请输入每天学习小时数："))
# 执行顺序是：
# 先执行input()
# → 接收输入的字符串
# → float()将字符串转换为浮点数
# → 保存到daily_hours

study_days = int(input("请输入每周学习天数："))

print(type(name))
print(type(daily_hours))
print(type(study_days))

weekly_hours = daily_hours * study_days
print("-" * 30)
print(f"{name}每周计划学习{weekly_hours:.2f}小时")
# {weekly_hours:.2f}
# 表示将结果显示为两位小数.
# 它只改变输出格式，不会永久修改变量 weekly_hours本身。
print("-" * 30)