print("-" * 30)
print("BMI计算")
print("=" * 30)
name = input("请输入称呼：")
height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（千克）："))

bmi = weight / (height ** 2)

print(f"{name}的BMI为{bmi:.2f}")
print("=" * 30)