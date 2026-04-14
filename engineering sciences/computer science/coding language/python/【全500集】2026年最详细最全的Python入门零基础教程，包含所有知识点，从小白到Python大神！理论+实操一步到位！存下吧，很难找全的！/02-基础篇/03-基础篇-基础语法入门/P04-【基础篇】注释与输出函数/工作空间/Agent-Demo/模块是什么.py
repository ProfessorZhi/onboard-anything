# ============================================================
# 模块是什么？模块是数据类型吗？
# ============================================================
import os
import types

print("=== 1. 模块是真实存在的数据类型 ===")
print(f"type(os) = {type(os)}")
print(f"type(os).__name__ = {type(os).__name__}")
print("结论：模块的数据类型叫 'module'，是一个内置类型")
print()

print("=== 2. module 不是特殊的类，就是普通的内置类型 ===")
print(f"module 的父类: {type(os).__bases__}")
print("module 继承自 object，和 int、str 一样是内置类型")
print()

print("=== 3. 模块对象 vs 类对象 ===")
print(f"isinstance(os, object)  = {isinstance(os, object)}   ← os 是对象")
print(f"isinstance(str, object)  = {isinstance(str, object)}   ← str 也是对象")
print(f"isinstance(os, type)     = {isinstance(os, type)}     ← os 不是类")
print(f"isinstance(str, type)    = {isinstance(str, type)}     ← str 是类（类型本身）")
print()
print("区分：")
print("  os   → 模块对象（module 类型的实例）")
print("  str  → 类对象（type 类型的实例）")
print()

print("=== 4. 手动创建一个模块对象（不用 import）===")
my_module = types.ModuleType("my_custom_module")
my_module.x = 100
my_module.greet = lambda: "hello"
print(f"my_module.__name__ = {my_module.__name__}")
print(f"my_module.x = {my_module.x}")
print(f"my_module.greet() = {my_module.greet()}")
print(f"type(my_module) = {type(my_module)}")
print()
print("结论：模块本质上就是一个'命名空间容器'")
print("      装着各种变量、函数、其他模块的引用")
print()

print("=== 5. 模块的本质（等价代码）===")
print("""
# Python 内部，模块大概是这样实现的：
class ModuleType:
    def __init__(self, name):
        self.__name__ = name    # 模块名
        self.__dict__ = {}       # 存放所有内容的字典
        self.__file__ = None    # 文件路径
        self.__package__ = None # 包名

# import os 的过程：
# 1. Python 找到 os.py / os 包
# 2. 创建一个 ModuleType 实例
# 3. 执行模块里的代码，填充 __dict__
# 4. 把这个模块对象绑定到当前作用域的 os 变量
""")

print("=== 6. 万物皆对象 ===")
print(f"type(1)           = {type(1)}             ← int 是对象")
print(f"type('hello')     = {type('hello')}         ← str 是对象")
print(f"type(print)       = {type(print)}           ← 函数也是对象")
print(f"type(int)         = {type(int)}             ← int 类本身是 type 的实例")
import types
module_type = types.ModuleType
print(f"type(ModuleType)  = {type(module_type)}          ← module 类是 type 的实例")
print()
print("在 Python 里，所有东西都是对象：")
print("  - 数据（数字、字符串、列表）→ 对象的实例")
print("  - 函数 → function 类的实例")
print("  - 类 → type 类的实例")
print("  - 模块 → module 类的实例")
print("  - type → type 类的实例（type 是自己的实例）")
