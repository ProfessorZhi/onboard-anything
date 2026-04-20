print("===== 1. 多次 input：一次问一个 =====")
name = input("请输入名字：")
age = int(input("请输入年龄："))
city = input("请输入城市：")
print("姓名：", name, "，年龄：", age, "，城市：", city, sep="")

print("\n===== 2. 一次 input：一行输入多个文本 =====")
first_name, last_name = input("请输入姓和名，用空格分隔：").split()
print("姓：", first_name, "，名：", last_name, sep="")

print("\n===== 3. 一次 input：一行输入多个整数 =====")
a_text, b_text = input("请输入两个整数，用空格分隔：").split()
a = int(a_text)
b = int(b_text)
print("和为：", a + b, sep="")

print("\n===== 4. 更紧凑的写法 =====")
x, y = map(int, input("再输入两个整数，用空格分隔：").split())
print("乘积为：", x * y, sep="")
