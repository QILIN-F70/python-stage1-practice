# 实习准备状态评估器需求分析

## 1. 程序目标

接收用户输入的称呼、本周学习小时数、本周完成的练习文件数量、是否完成本周复盘

计算准备积分

判断主要状态

## 2. 用户输入

称呼：变量名name

本周学习小时数：变量名week_study_hours

本周完成的练习文件数量：变量名week_practice_quantity

是否完成本周复盘：变量名week_review_status

## 3. 需要进行的计算

准备积分 = 本周学习小时数 + 本周完成的练习文件数量 × 2

prepare_points = week_study_hours + week_practice_quantity * 2

## 4. 主要状态规则

三种主要结果使用同一条 `if / elif / else` 条件链，最终只输出一种。

准备积分大于等于20，并且完成本周复盘：输出“准备状态：优秀”

prepare_points `>=` 20 and week_review_status `==` "是"

否则，准备积分大于等于12：输出“准备状态：达标”

prepare_points `>=` 12

其他情况：输出“准备状态：需要调整”

## 5. 额外提醒规则

这条规则使用新的独立 `if`，无论前面的主要学习状态是什么，都需要单独判断。

本周学习小时数大于等于15，或者完成的练习文件数量大于等于5，输出“本周有一项高投入表现”

week_study_hours `>=` 15 or week_practice_quantity `>=` 5

## 6. 程序输出

程序标题

用户输入的信息

准备积分，按两位小数显示(.2f)

一种主要准备状态

符合条件时的额外提醒

程序结束提示

分隔线

## 7. 变量名和数据类型

称呼：变量名name，类型字符串str

本周学习小时数：变量名week_study_hours，类型浮点数float

本周完成的练习文件数量：变量名week_practice_quantity，类型整数int

是否完成本周复盘：变量名week_review_status，类型字符串str

准备积分：变量名prepare_points，类型浮点数float，是计算产生