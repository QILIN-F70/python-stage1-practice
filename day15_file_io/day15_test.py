print("=" * 30)
print("两条学习计划文件管理器")
print("=" * 30)

first_plan = input("请输入第一条学习计划：")
second_plan = input("请输入第二条学习计划：")
print("-" * 30)

with open("day15_file_io/day15_plans.txt","w",encoding="utf-8")as file:
    file.write(first_plan + "\n")

with open("day15_file_io/day15_plans.txt","a",encoding="utf-8")as file:
    file.write(second_plan + "\n")

with open("day15_file_io/day15_plans.txt","r",encoding="utf-8")as file:
    plan_line = file.readlines()

print(f"读取结果的数据类型：{type(plan_line)}")
print(f"计划总数：{len(plan_line)}")
print("-" * 30)

for plan in plan_line:
    clean_plan = plan.strip()
    print(f"学习计划：{clean_plan}")
    print("-" * 30)

print("程序结束")
print("=" * 30)