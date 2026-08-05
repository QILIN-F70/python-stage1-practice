# 订单配送判断器需求分析

## 程序目标

接收商品名称、商品单价、购买数量、是否为会员的信息

计算商品总金额

判断一种主要配送结果

## 用户输入

商品名称：变量名product_name，类型str，

商品单价：变量名unit_price，类型float，

购买数量：变量名quantity，类型int，

是否为会员：变量名membership_status，类型str，

## 需要进行的计算

商品总金额 = 商品单价 * 购买数量

total_amount = unit_price * quantity

## 主要配送规则

三种主要结果使用同一条 `if / elif / else` 条件链，最终只输出一种。

规则一：
如果总金额大于等于500，并且是会员，输出“会员优先配送”。

total_amount `>=` 500 and membership_status `==` "是"

规则二：
否则，如果总金额大于等于200，输出“订单免配送费”。

total_amount `>=` 200

规则三：
否则，输出“需支付配送费12元”。

## 额外提醒规则

这条规则使用新的独立 `if`，无论前面的主要配送结果是什么，都需要单独判断。

如果购买数量大于等于5，或者总金额大于等于500，

输出“这是大额或批量订单”。

quantity `>=` 5 or total_amount `>=` 500

## 程序输出

程序标题
商品名称
商品单价
购买数量
商品总金额（使用 `.2f` 显示两位小数）
一种主要配送结果
可能出现的大额或批量订单提醒
程序结束提示

## 变量名和数据类型

商品名称：变量名product_name，类型str，

商品单价：变量名unit_price，类型float，

购买数量：变量名quantity，类型int，

是否为会员：变量名membership_status，类型str，

商品总金额：变量名total_amount，类型float,

商品总金额，是计算产生的，