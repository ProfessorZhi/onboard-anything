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


show("1. builtin function_or_method：常见内置函数")
show_item("print", print)
show_item("len", len)
show_item("input", input)

show("2. method_descriptor：定义在类型对象上的方法")
show_item("list.append", list.append)
show_item("str.split", str.split)
show_item("dict.get", dict.get)

show("3. builtin_function_or_method：绑定到实例后的方法")
nums = [1, 2, 3]
s = "a b"
d = {"x": 1}
show_item("nums.append", nums.append)
show_item("s.split", s.split)
show_item("d.get", d.get)

show("4. type：内置类型对象本身")
show_item("int", int)
show_item("float", float)
show_item("list", list)
show_item("str", str)

show("5. 最短对照")
print("print           -> 常见内置函数，type 常是 builtin_function_or_method")
print("list.append     -> 类型对象上的方法定义，type 常是 method_descriptor")
print("nums.append     -> 绑定到实例后的方法对象，type 常是 builtin_function_or_method")
print("int / list / str -> 它们本身是类型对象，type 是 type")
