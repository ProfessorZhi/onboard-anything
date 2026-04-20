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


def top_func(x, y=10):
    return x + y


class Demo:
    class_value = "class-data"

    def instance_method(self, x, y=10):
        return x + y

    @staticmethod
    def static_method(x, y=10):
        return x + y

    @classmethod
    def class_method(cls, x, y=10):
        return x + y


show("1. 普通 def 函数")
show_item("top_func", top_func)

show("2. 类对象上的成员")
show_item("Demo.instance_method", Demo.instance_method)
show_item("Demo.static_method", Demo.static_method)
show_item("Demo.class_method", Demo.class_method)

show("3. 实例对象上的成员")
obj = Demo()
show_item("obj.instance_method", obj.instance_method)
show_item("obj.static_method", obj.static_method)
show_item("obj.class_method", obj.class_method)

show("4. 最短结论")
print("top_func               -> 普通 function 对象")
print("Demo.instance_method   -> 类对象上的函数定义，签名里常看到 self")
print("obj.instance_method    -> 绑定到实例后的 method，self 已隐含绑定")
print("Demo.static_method     -> staticmethod 解包后，调用时不自动传 self/cls")
print("Demo.class_method      -> 绑定到类后的 method，cls 已隐含绑定")
