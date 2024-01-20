def calculate():
    while True:
        number = input("请输入一个数（输入000结束程序）：")

        # 检查用户是否输入了000，如果是则结束程序
        if number == "000":
            break

        # 尝试将输入转换为小数
        try:
            decimal_number = float(number)
        except ValueError:
            print("输入无效，请输入一个整数或小数。")
            continue

        # 执行乘法运算，并输出结果
        result = decimal_number * 120
        print(f"{number} 乘 L = {result:.3f}")


calculate()
