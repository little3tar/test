def multiply_and_print_result():
    while True:
        user_input = input("请输入一个数字（输入000结束程序）: ")

        if user_input == "000":
            print("程序结束。")
            break

        try:
            num = float(user_input)
            result = 120 * num

            # 保留小数点后三位
            result = round(result, 3)

            print(f"T乘以{user_input}的结果是：{result}")
        except ValueError:
            print("无效输入，请输入一个数字。")


if __name__ == "__main__":
    multiply_and_print_result()
