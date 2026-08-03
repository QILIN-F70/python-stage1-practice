# not表示“取反”，会把布尔值反过来：
# not True  → False
# not False → True

is_logged_in = True

if not is_logged_in:
    print("请先登录")
else:
    print("欢迎进入系统")

print("登录状态检查结束")