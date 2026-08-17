# 函数有两种常见行为：
# print()：把内容显示在终端中。
# return：把计算结果交回函数调用的位置，供后续代码保存、计算或判断

def calculate_total(unit_price,quantity):
    total = unit_price * quantity
    return total#会把结果交回调用位置

# return回来的结果会保存到 order_total中
order_total = calculate_total(14.99,2)

print(f"订单总金额：{order_total:.2f}")
print(f"返回结果类型：{type(order_total)}")