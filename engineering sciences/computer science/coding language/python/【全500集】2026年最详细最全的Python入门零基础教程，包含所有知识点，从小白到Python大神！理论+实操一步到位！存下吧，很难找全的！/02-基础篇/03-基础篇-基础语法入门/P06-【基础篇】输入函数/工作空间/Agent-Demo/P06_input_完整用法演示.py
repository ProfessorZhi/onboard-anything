print("===== input() 完整用法演示 =====")

# 1. 不传参数：程序会等待输入，但不给提示
raw_text = input()
print("1. 不传参数时拿到的内容：", raw_text, sep="")
print("   类型：", type(raw_text), sep="")

# 2. 传入提示信息：这是最常见、最推荐的写法
name = input("2. 请输入你的名字：")
print("   你好，", name, sep="")

# 3. 输入数字后仍然先得到字符串
age_text = input("3. 请输入你的年龄：")
print("   原始输入：", age_text, sep="")
print("   原始类型：", type(age_text), sep="")

# 4. 需要整数计算时，手动转成 int
age = int(age_text)
print("   明年年龄：", age + 1, sep="")

# 5. 需要小数计算时，手动转成 float
price = float(input("4. 请输入商品价格："))
print("   打九折后价格：", price * 0.9, sep="")

# 6. 多次 input 组合成一个完整交互
city = input("5. 请输入你所在城市：")
hobby = input("6. 请输入你的爱好：")
print("   你住在", city, "，爱好是", hobby, sep="")

print("\n===== 结论 =====")
print("input() 只有一个可选参数 prompt。")
print("它返回的永远是 str。")
print("要做数值运算时，再用 int() 或 float() 转换。")
