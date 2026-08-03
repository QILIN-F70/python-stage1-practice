print("=" * 30)
print("优惠资格判断")
print("-" * 30)
order_amount = float(input("请输入订单金额："))
membership = input("是否是会员：")
print("-" * 30)
if order_amount >= 200 and membership == "是":
    print("获得会员大额优惠")
elif order_amount >= 99:
    print("获得普通满减优惠")
else:
    print("暂时没有优惠")
print("-" * 30)
print("优惠检查结束")
print("=" * 30)