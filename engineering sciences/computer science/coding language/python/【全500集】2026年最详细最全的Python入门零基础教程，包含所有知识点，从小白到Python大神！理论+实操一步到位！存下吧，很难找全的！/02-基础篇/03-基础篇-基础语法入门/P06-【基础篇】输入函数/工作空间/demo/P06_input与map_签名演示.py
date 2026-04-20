import inspect


def show(title):
    print(f"\n===== {title} =====")


def show_item(name, obj):
    print(f"\n{name}")
    print("  value      =", obj)
    print("  type       =", type(obj))
    try:
        print("  signature  =", inspect.signature(obj))
    except Exception as e:
        print("  signature  = <取不到签名>", e)


show("1. input 本身")
show_item("input", input)

show("2. map 本身")
show_item("map", map)

show("3. input 的典型使用")
print('示例代码: age = int(input("请输入年龄："))')
print("说明: input() 先拿到 str, int(...) 再把它转成 int")

show("4. map 的典型使用")
m = map(int, ["1", "2", "3"])
show_item("m = map(int, ['1', '2', '3'])", m)
print("print(m) 的典型结果类似 = <map object at 0x...>")
print("type(m) =", type(m))
print("list(m) =", list(m))

show("5. input 和 map 组合使用的典型写法")
print("典型写法: a, b = map(int, input().split())")
print("拆开理解:")
print("  1. input()      -> 先得到一整行 str")
print("  2. split()      -> 拆成多个 str")
print("  3. map(int, ..) -> 创建一个 map 对象, 逐个把 str 转成 int")
print("  4. 展开赋值      -> 得到多个 int")

show("6. 最短结论")
print("input -> builtin_function_or_method")
print("map   -> type")
print("input() 默认返回 str")
print("map(...) 返回 map 对象")
print("print(map(...)) 看到的是 <map object at 0x...>")
print("list(map(...)) 才能把结果真正展开出来")
