def show(title):
    print(f"\n===== {title} =====")


show("1. 带引号: 这是字符串内容")
nums = [1, 2, 3]
label = "nums.__doc__"
print('label = "nums.__doc__"')
print("label =", label)
print("type(label) =", type(label))
print("说明: 这里只是把一段文本 nums.__doc__ 存进变量, 没有执行它")


show("2. 不带引号: 这是表达式求值")
label2 = nums.__doc__
print("label2 = nums.__doc__")
print("label2 的前 40 个字符 =", label2[:40])
print("type(label2) =", type(label2))
print("说明: 这里真的访问了 nums.__doc__ 属性, 再把结果赋给 label2")


show("3. f-string 插入变量值")
label = "nums.__doc__"
print('原代码: print(f"{label}:")')
print("实际输出:")
print(f"{label}:")
print("说明: 花括号里放的是变量 label, 插入的是变量值 nums.__doc__, 不是去执行 nums.__doc__")


show("4. f-string 里直接放表达式")
print('原代码: print(f"{nums.__doc__[:20]}...")')
print("实际输出:")
print(f"{nums.__doc__[:20]}...")
print("说明: 这里花括号里放的不是字符串变量, 而是真正的表达式 nums.__doc__[:20], 所以会求值")


show("5. 最容易混淆的对比")
print('A: "nums.__doc__"')
print("结果 =", "nums.__doc__")
print("说明: 这是文本")

print("\nB: nums.__doc__ 的前 20 个字符")
print("结果 =", nums.__doc__[:20])
print("说明: 这是表达式的结果")

print("\nC: f\"{label}\"")
print("结果 =", f"{label}")
print("说明: 插入变量 label 的值, 这个值本身仍然只是文本")

print("\nD: f\"{nums.__doc__[:20]}\"")
print("结果 =", f"{nums.__doc__[:20]}")
print("说明: 直接在花括号里写表达式, Python 会先求值再插入")


show("6. 结论")
print("有引号: 优先按字符串文本看")
print("没引号: 优先按表达式求值看")
print("f 前缀: 允许在字符串里用 {} 插入变量或表达式结果")
