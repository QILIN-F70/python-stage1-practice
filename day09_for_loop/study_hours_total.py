# 使用 for 固定次数接收输入并累加。

total_hours = 0

for day in range(1, 4):
    hours = float(input(f"请输入第{day}天学习小时数："))
    total_hours = total_hours + hours

print(f"三天学习总小时数：{total_hours:.2f}")