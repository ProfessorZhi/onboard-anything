def show(title):
    print(f"\n===== {title} =====")


show("1. map 本身是什么")
print("map =", map)
print("type(map) =", type(map))

show("2. 创建一个 map 对象")
m = map(int, ["1", "2", "3"])
print("m =", m)
print("type(m) =", type(m))

show("3. 为什么 print(m) 不是最终结果")
print("print(m) 看到的是 map 对象本身, 不是展开后的列表")
print(m)

show("4. list(m) 会把结果展开出来")
m = map(int, ["1", "2", "3"])
print("list(m) =", list(m))

show("5. map 常常会被消费掉")
m = map(int, ["1", "2", "3"])
print("第一次 list(m) =", list(m))
print("第二次 list(m) =", list(m))

show("6. map 可以换别的函数")
m = map(str.upper, ["a", "b", "c"])
print("list(map(str.upper, ['a', 'b', 'c'])) =", list(m))

show("7. map 也可以处理多个可迭代对象")
m = map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30])
print("list(map(lambda x, y: x + y, [1,2,3], [10,20,30])) =", list(m))

show("8. 和 P06 主线最相关的写法")
print("典型写法: a, b = map(int, input().split())")
print("意思: 输入一行 -> split 拆开 -> map(int, ...) 批量转成整数")
