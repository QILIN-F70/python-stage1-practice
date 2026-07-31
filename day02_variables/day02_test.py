name = "宠物鱼油"
price = 14.99
quantity = 2
is_store = True

total = price * quantity

print("=" * 30)
print("商品订单金额卡片")
print("=" * 30)
print(f"商品：{name}")
print(f"单价：{price}")
print(f"数量：{quantity}")
print(f"是否有库存：{is_store}")
print(f"总价：{total}")
print("=" * 30)