print("=" * 30)
print("有限次数学习口令验证器")
print("=" * 30)

verify_count = 1
password = input("请输入学习口令：")
correct_password = "python"

while verify_count <= 3:
    if password == correct_password:
        print("口令正确")
        print("-" * 30)
        break

    print("口令错误")

    print("-" * 30)
    
    password = input("请输入学习口令：")
    verify_count = verify_count + 1
    print("-" * 30)
    if password != correct_password and verify_count == 3:
        print("口令错误")
        print("尝试次数已用完")
        print("-" * 30)
        break

    
    
print("口令验证结束")
print("=" * 30)
