# Day 5 学习日志

## 今天学习了什么

if...else;if...elif...else;not;and;or

## if、elif、else分别有什么作用

if是要设立条件的情况下使用；

多种情况下使用到elif；

else表示前面所有条件都不成立的剩余情况；

## 为什么条件链最多执行一个分支

 if / elif / else属于同一条条件链。

 Python从上到下判断。

 找到第一个 True分支后立即执行它。

 同一条条件链中的后续分支全部跳过。

## and、or、not分别有什么作用

and表示并且：连接到的两个条件必须同时为True，整体结果才是True。

or表示或：连接到的两个条件有其中一个为True，整体结果为True；两个条件都为False时，整体结果为False；

not表示取反：not True：False；not False：True；

## 为什么严格条件通常要写在前面

 if / elif / else属于同一条条件链。

 Python从上到下判断。

 找到第一个 True分支后立即执行它。

 同一条条件链中的后续分支全部跳过。

比如 `score >= 90` 应放在 `score >= 60` 前面，因为要是`score >= 60` 的在前面，那么输入的成绩为90，立马就判定为True，然后就执行`score >= 60` 这一条分支，剩余分支就不执行了

## 今天完成了哪些程序

and/or/not的练习；

成绩等级；

优惠资格判断；

if...else的练习；

## 今天主动观察了什么错误

错误名称是 `SyntaxError`

错误原因是给 `else` 添加了条件

正确形式是 `else:`

## else后面为什么不能写条件

else表示前面所有条件都不成立的剩余情况，因此不能再写条件

## 我能否独立完成完整条件判断

能

## 我仍然不会什么

目前没有发现明显不理解的内容

## 下一次需要复习什么

if...else;if...elif...else;not;and;or