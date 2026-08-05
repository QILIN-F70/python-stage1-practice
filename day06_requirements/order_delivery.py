print("=" * 30)
print("订单配送判断器")
print("=" * 30)

product_name = input("请输入商品名称：")
unit_price = float(input("请输入商品单价："))
quantity = int(input("请输入商品数量："))
membership_status = input("是否为会员：")

total_amount = unit_price * quantity
print("-" * 30)

print(f"商品名称：{product_name}")
print(f"商品单价：{unit_price}")
print(f"购买数量：{quantity}")
print(f"是否为会员：{membership_status}")
print(f"商品总金额：{total_amount:.2f}")
print("-" * 30)

if total_amount >= 500 and membership_status == "是":
    print("会员优先配送")
elif total_amount >= 200:
    print("订单免配送费")
else:
    print("需支付配送费12元")

print("-" * 30)

if quantity >= 5 or total_amount >= 500:
    print("这是大额或批量订单")
    print("-" * 30)

print("订单配送判断结束")
print("=" * 30)