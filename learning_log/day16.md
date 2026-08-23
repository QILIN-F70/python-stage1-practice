# Day 16 学习日志

## 今天学习了什么

json的学习以及使用

json.dump()

 `ensure_ascii=False` 和 `indent=4`

`json.load()`

## JSON是什么，为什么需要它

JSON是一种保存和交换结构化数据的文本格式。它可以保留列表、字典、布尔值等数据之间的结构关系，读取后也容易恢复为对应的 Python数据。

## json.dump和json.load分别有什么作用

.dump是把python数据存入json文件

.load是从json文件将内容读取出来

## ensure_ascii和indent有什么作用

`ensure_ascii`：中文以正常文字保存，而不是转换成字符编码形式。不写 ensure_ascii=False 时，中文可能显示为 Unicode 转义形式，但中文数据不会丢失，读取后仍能恢复。

`indent=4`： 表示使用4个空格对JSON进行格式化缩进，让文件结构更容易阅读。它只改变文件的排版显示，不会改变任务数量、键和值等实际数据。

## Python列表和JSON数组有什么关系

JSON中不使用“列表”这个正式名称，而称为“数组”。两者结构相近，`json.dump()` 和 `json.load()` 会自动转换。

## 为什么修改JSON任务时不能直接使用a模式

a只会在文件的末尾追加，那么就不在同一个列表结构里面了，会多一个结构

## JSON任务的正确修改流程

正确流程是，先读取该文件保存到新变量，然后将新任务追加到新变量后面，最后再用w重新将新变量写入json文件

## 今天完成了什么程序

JSON学习任务保存与读取器

## 今天主动观察了什么错误

JSONDecodeError：json格式错误

## JSONDecodeError为什么出现

JSONDecodeError：是json文件格式错误JSON对格式要求比较严格，常见问题包括：
键和值之间缺少冒号；
两个键值对之间缺少逗号；
括号没有配对；
手动写入了不符合JSON规则的内容。

## 空文件和空JSON列表有什么区别

如果要表示空列表，JSON文件必须包含：[]

空文件是没有任何json值，不能被json.load正常读取

## 我仍然不熟悉什么

空文件和空json列表的区别给忘记了

## 明天需要复习什么

json的学习以及使用

空文件和空JSON列表有什么区别

JSON任务的正确修改流程