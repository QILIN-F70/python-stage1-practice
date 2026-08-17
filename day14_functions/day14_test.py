print("=" * 30)
print("函数版学习准备状态评估版")
print("=" * 30)

def calculate_score(study_hours,practice_count):

    prepare_points = study_hours + practice_count * 2
    return prepare_points

name = input("请输入称呼：")
study_hours = float(input("本周学习小时数："))
practice_count = int(input("本周完成的练习数量："))
print("-" * 30)
points = calculate_score(study_hours,practice_count)


def evaluate_status(score):
    if score >= 15:
        print("优秀")
        status == "优秀"
    elif score >= 8:
        print("达标")
        status = "达标"
    else:
        print("需要调整")
        status = "需要调整"

    print("-" * 30)

    return status

status = evaluate_status(points)

print(f"称呼：{name}")
print(f"准备积分：{points:.2f}")
print(f"学习状态：{status}")

print("-" * 30)
print("程序已结束")
print("=" * 30)
