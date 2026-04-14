# ============================================================
# type 是什么？内置类型有哪些？一切皆对象？
# ============================================================

print("=" * 60)
print("一、type 是什么")
print("=" * 60)
print()

# type 是什么？
print(f"type 是什么: {type(type)}")
print(f"type 是类吗: {isinstance(type, type)}")
print(f"type 的父类: {type.__bases__}")
print()
print("type 有两层身份:")
print("  1. 内置函数: type(x) 用来查 x 的类型")
print("  2. 内置类: type 本身是 type 的实例(type 是什么的实例?)")
print("     type 是自己的实例(type 是 type 的实例)")
print()

# type 的特殊身份
print("type 的特殊身份:")
print(f"  type(int)  = {type(int)}     ← int 是 type 的实例")
print(f"  type(str)  = {type(str)}     ← str 是 type 的实例")
print(f"  type(type) = {type(type)}    ← type 是 type 的实例（自己）")
print()
print("  type 叫'元类'（metaclass），即'类的类'")
print("  type 的实例是类，类的实例是普通对象")
print()

print("=" * 60)
print("二、Python 所有内置类型（数据类型）")
print("=" * 60)
print()

# 基本数据类型
basic_types = [
    (1,         "int",      "整数"),
    (1.5,       "float",    "浮点数（小数）"),
    (True,      "bool",     "布尔值"),
    ("hi",      "str",      "字符串"),
    (b"hi",     "bytes",    "字节串"),
    (None,      "NoneType", "空值"),
]

# 容器类型
container_types = [
    ([1,2,3],           "list",     "列表"),
    ((1,2,3),           "tuple",    "元组"),
    ({"a":1},           "dict",     "字典"),
    ({1,2,3},           "set",      "集合"),
    (frozenset({1,2}),  "frozenset","不可变集合"),
]

# 其他
other_types = [
    (lambda:1,      "function",     "函数"),
    (type,          "type",        "类型/元类"),
    (object,        "object",      "所有类的基类"),
]

print("【基本类型】")
for val, tname, desc in basic_types:
    print(f"  {tname:<10} {desc:<12} 示例: {repr(val)[:30]}")
    print(f"             type({val!r}) = {type(val)}")

print()
print("【容器类型】")
for val, tname, desc in container_types:
    print(f"  {tname:<10} {desc:<12} 示例: {repr(val)[:40]}")
    print(f"             type({tname}()) = {type(val)}")

print()
print("【其他类型】")
for val, tname, desc in other_types:
    print(f"  {tname:<10} {desc:<12} 示例: {repr(val)[:40]}")

print()
print("=" * 60)
print("三、Python 所有内置函数")
print("=" * 60)
print()

# 内置函数一览
builtin_funcs = [
    ("print()",    "打印输出"),
    ("len()",      "返回长度/元素个数"),
    ("input()",    "读取用户输入"),
    ("type()",     "返回对象类型"),
    ("isinstance()","判断对象是否是某类型实例"),
    ("issubclass()","判断类是否是另一类的子类"),
    ("dir()",      "返回对象所有属性/方法名"),
    ("help()",     "显示帮助信息"),
    ("callable()", "判断对象是否可调用"),
    ("id()",       "返回对象内存地址"),
    ("hash()",     "返回哈希值"),
    ("repr()",     "返回对象的字符串表示"),
    ("open()",     "打开文件"),
    ("range()",    "生成整数序列"),
    ("map()",      "映射函数"),
    ("filter()",   "过滤序列"),
    ("sorted()",   "排序"),
    ("enumerate()","枚举索引"),
    ("zip()",      "合并多个序列"),
    ("sum()",     "求和"),
    ("min()",     "最小值"),
    ("max()",     "最大值"),
    ("abs()",     "绝对值"),
    ("round()",   "四舍五入"),
    ("pow()",     "幂运算"),
    ("divmod()",  "返回商和余数"),
    ("all()",     "判断所有元素为真"),
    ("any()",     "判断任一元素为真"),
    ("format()",  "格式化值"),
    ("chr()",     "整数转字符"),
    ("ord()",     "字符转整数"),
    ("hex()",     "转十六进制字符串"),
    ("oct()",     "转八进制字符串"),
    ("bin()",     "转二进制字符串"),
    ("int()",     "转整数"),
    ("float()",   "转浮点数"),
    ("str()",     "转字符串"),
    ("bool()",    "转布尔值"),
    ("list()",    "转列表"),
    ("dict()",    "转字典"),
    ("set()",     "转集合"),
    ("tuple()",   "转元组"),
    ("bytes()",   "转字节串"),
    ("frozenset()","转不可变集合"),
    ("complex()", "转复数"),
]

for fname, fdesc in builtin_funcs:
    print(f"  {fname:<15} — {fdesc}")

print()
print("=" * 60)
print("四、Python 所有内置异常（错误类型）")
print("=" * 60)
print()

builtin_exceptions = [
    "BaseException",     "Exception",        "SystemExit",
    "KeyboardInterrupt","GeneratorExit",     "AssertionError",
    "AttributeError",   "BufferError",       "EOFError",
    "ImportError",      "ModuleNotFoundError","IndexError",
    "KeyError",         "KeyboardInterrupt", "MemoryError",
    "NameError",        "NotImplementedError","OSError",
    "OverflowError",     "RecursionError",   "ReferenceError",
    "RuntimeError",     "StopIteration",     "SyntaxError",
    "SystemError",      "TypeError",         "ValueError",
    "ZeroDivisionError",
]

# 分行显示，每行5个
for i in range(0, len(builtin_exceptions), 5):
    row = builtin_exceptions[i:i+5]
    print("  " + "  ".join(f"{e:<20}" for e in row))

print()
print("=" * 60)
print("五、一切皆对象？")
print("=" * 60)
print()

# 验证：所有东西都是 object 的实例
print("验证：所有东西都是 object 的实例")
print(f"  isinstance(1, object)         = {isinstance(1, object)}")
print(f"  isinstance('hi', object)      = {isinstance('hi', object)}")
print(f"  isinstance([], object)         = {isinstance([], object)}")
print(f"  isinstance(lambda:1, object) = {isinstance(lambda:1, object)}")
print(f"  isinstance(type, object)      = {isinstance(type, object)}")
print(f"  isinstance(object, object)    = {isinstance(object, object)}")
print(f"  isinstance(int, object)       = {isinstance(int, object)}")
print()

print("万物继承关系图:")
print()
print("""
  object（万物起源）
    │
    ├── int str float bool list dict tuple set bytes  ← 内置类型/容器
    │       ↑
    │       └── type  ← type 是 object 的子类
    │
    ├── 函数(function)
    ├── 模块(module)
    ├── 异常类(BaseException 的子类)
    └── ...所有数据类型...
""")

print("结论:")
print("  在 Python 里: 一切皆对象")
print("  不是一切皆类: 类是 type 的实例，普通对象是类的实例")
print("  区分:")
print("    1 是 int 的实例，int 是 type 的实例，type 是 type 的实例")
print("    'hello' 是 str 的实例，str 是 type 的实例")
print("    type 本身是 type 的实例（自己）")
