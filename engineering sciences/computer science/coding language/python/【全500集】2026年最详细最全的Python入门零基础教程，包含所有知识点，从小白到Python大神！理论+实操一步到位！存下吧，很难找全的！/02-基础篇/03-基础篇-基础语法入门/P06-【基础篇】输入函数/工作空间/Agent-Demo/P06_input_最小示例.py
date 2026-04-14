name = input("请输入你的名字：")
print("你好，", name)

age_text = input("请输入你的年龄：")
print("你刚才输入的是：", age_text)
print("它现在的类型是：", type(age_text))

age = int(age_text)
print("明年你就是", age + 1, "岁了")
