print("=" * 30)
print("订单条件检查器")
print("-" * 30)

name = input("请输入商品名称：")
price = float(input("商品的单价："))
quantity = int(input("购买数量："))

total = price * quantity
print(f"{name}的数量有：{quantity}，总金额为：{total:.2f}")

print("-" * 30)

if total >= 99:
    print("满足包邮条件")
    print("-" * 30)
if quantity >= 3:
    print("满足批量购买条件")
    print("-" * 30)
print("订单检查结束")
print("=" * 30)