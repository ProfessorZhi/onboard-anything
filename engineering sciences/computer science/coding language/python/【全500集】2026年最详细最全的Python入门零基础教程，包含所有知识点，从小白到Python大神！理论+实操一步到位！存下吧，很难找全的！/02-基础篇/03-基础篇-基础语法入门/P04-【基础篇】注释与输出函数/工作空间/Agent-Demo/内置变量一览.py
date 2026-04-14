# ============================================================
# Python 所有内置变量（模块级特殊变量）完整展示
# ============================================================
"""
这是本文件的文档字符串
会被自动存到 __doc__ 里
"""

# -----------------------------------------------------------
# 【重要】两类"内置变量"的区别
# -----------------------------------------------------------
#
# 很多初学者会把所有"直接能用的名字"都叫"内置变量"
# 其实分两类，来源完全不同：
#
# 1. 解释器内置（builtins）
#    - Python 解释器启动时就加载好的
#    - 任何 .py 文件里直接写就能用
#    - 例如：print, len, str, True, None, Exception
#
# 2. 模块内置变量（每个.py文件运行时自动注入）
#    - 解释器在运行 .py 文件时，自动注入到当前模块的 globals
#    - 只有当前模块能用，被 import 的模块各有各的值
#    - 例如：__name__, __file__, __doc__, __package__
#
# 【验证】__name__ 不在 builtins 里，而是在当前模块的 globals 里
# -----------------------------------------------------------

import os
import sys
import types

print("=" * 60)
print("一、先区分两类内置：解释器 vs 模块")
print("=" * 60)
print()

# 演示：两类名字的来源差异
print("【验证：print 来自哪里？】")
import builtins
print("  print 在 builtins 里：", 'print' in dir(builtins))
print()

print("【验证：__name__ 来自哪里？】")
# 注意：'__name__' 是字符串，__name__ 是变量（值是 '__main__'）
print("  字符串 '__name__' 在 builtins 里：", '__name__' in dir(builtins))
print("  变量 __name__ 的值：", __name__)
print("  变量 '__name__' 在当前模块 globals 里：", '__name__' in globals())
print()

print("【结论】")
print("  print  ->  来自 builtins（解释器启动就加载好了）")
print("  __name__  ->  来自当前模块的 globals（运行时注入的）")
print()

print("=" * 60)
print("二、解释器内置变量（builtins）一览")
print("=" * 60)
print()

# 列出所有 builtins
builtin_items = [(name, getattr(builtins, name)) for name in dir(builtins)]
print("  builtins 一共", len(builtin_items), "个名字")
print()

# 按类别分组展示
categories = {
    "内置函数": ["print", "len", "type", "isinstance", "open", "input", "range",
                "map", "filter", "sorted", "enumerate", "zip", "any", "all",
                "min", "max", "sum", "abs", "round", "pow", "hex", "oct", "bin",
                "chr", "ord", "repr", "format", "id", "hash", "callable",
                "dir", "help", "vars", "globals", "locals", "exec", "eval", "compile"],
    "内置类型": ["int", "str", "float", "bool", "list", "dict", "set", "tuple",
                "bytes", "bytearray", "frozenset", "complex", "type"],
    "内置异常": ["Exception", "BaseException", "SystemExit", "KeyboardInterrupt",
                "ValueError", "TypeError", "KeyError", "IndexError",
                "AttributeError", "RuntimeError", "StopIteration", "AssertionError",
                "ImportError", "ModuleNotFoundError", "FileNotFoundError",
                "ZeroDivisionError", "PermissionError"],
    "内置常量": ["True", "False", "None", "NotImplemented", "Ellipsis"],
}

for cat_name, names in categories.items():
    print("  【" + cat_name + "】")
    existing = [n for n in names if hasattr(builtins, n)]
    print("    " + ", ".join(existing))
    print()

print("=" * 60)
print("三、模块内置变量一览（每个.py文件运行时自动注入）")
print("=" * 60)
print()

# 收集模块的所有特殊变量（以下划线开头或结尾的）
special_vars = {k: v for k, v in globals().items() if k.startswith('__')}
regular_vars = {k: v for k, v in globals().items() if not k.startswith('__')}

print("【以下划线开头的特殊变量】")
print("  （这些是解释器注入到当前模块 globals 的，不是 builtins）")
print()
for name in sorted(special_vars):
    value = special_vars[name]
    value_type = type(value).__name__
    value_repr = repr(value)
    if len(value_repr) > 60:
        value_repr = value_repr[:60] + "..."
    print("  " + name.ljust(20) + " 类型: " + value_type.ljust(15) + " 值: " + value_repr)

print()
print("【普通变量（你自己定义的）】")
for name in sorted(regular_vars.keys()):
    if name not in ('os', 'sys', 'types'):
        print("  " + name)

print()
print("=" * 60)
print("四、逐个详解每个模块内置变量")
print("=" * 60)
print()

# -----------------------------------------------------------
# 1. __name__ — 模块名称
# -----------------------------------------------------------
print("【1. __name__】")
print("  值: " + str(__name__))
print("  含义: 当你 import 这个模块时，Python 用这个名字来引用它")
print("  特殊情况: 直接运行 python xxx.py 时，__name__ == '__main__'")
print()

# -----------------------------------------------------------
# 2. __file__ — 模块文件路径
# -----------------------------------------------------------
print("【2. __file__】")
print("  值: " + str(__file__))
print("  含义: 这个 .py 文件的路径（相对路径或绝对路径）")
print("  绝对路径: " + os.path.abspath(__file__))
print()

# -----------------------------------------------------------
# 3. __doc__ — 文档字符串
# -----------------------------------------------------------
print("【3. __doc__】")
print("  值: " + repr(__doc__))
print("  含义: 文件开头的三引号文档字符串")
print()

# -----------------------------------------------------------
# 4. __package__ — 包名
# -----------------------------------------------------------
print("【4. __package__】")
print("  值: " + str(__package__))
print("  含义: 当前模块所属的包名，没有包就是 None")
print("  例子: import os 时，os.__package__ == ''（空字符串）")
print()

# -----------------------------------------------------------
# 5. __loader__ — 模块加载器
# -----------------------------------------------------------
print("【5. __loader__】")
print("  值: " + str(__loader__))
print("  含义: 负责把这个模块加载进 Python 的对象（很少直接用）")
loader_name = __loader__.name if __loader__ else None
print("  加载器名称: " + str(loader_name))
print()

# -----------------------------------------------------------
# 6. __spec__ — 模块规格信息
# -----------------------------------------------------------
print("【6. __spec__】")
print("  值: " + str(__spec__))
if __spec__:
    print("  模块名: " + str(__spec__.name))
    print("  文件路径: " + str(__spec__.origin))
    print("  加载器: " + str(__spec__.loader))
print()

# -----------------------------------------------------------
# 7. __annotations__ — 类型注解
# -----------------------------------------------------------
name_str: str = "小明"
age_int: int = 25
print("【7. __annotations__】")
print("  值: " + str(__annotations__))
print("  含义: 记录 :type 注解的变量，格式 {变量名: 类型}")
print("  注意: 只有写了 : 类型 的变量才会被记录")
print()

# -----------------------------------------------------------
# 8. __dict__ — 模块的全局命名空间
# -----------------------------------------------------------
print("【8. __dict__（用 vars() 访问）】")
module_dict = vars()
print("  键数量: " + str(len(module_dict)) + " 个")
keys_list = list(module_dict.keys())[:5]
print("  前5个键: " + str(keys_list))
print("  含义: 这个模块里所有全局变量的字典容器")
print("  注意: __dict__ 本身不是全局变量，用 vars() 访问")
print()

# -----------------------------------------------------------
# 9. __builtins__ — 内置函数和异常的容器
# -----------------------------------------------------------
print("【9. __builtins__】")
print("  类型: " + type(__builtins__).__name__)
print("  含义: 所有内置函数(print, len, input 等)和内置异常的集合")
non_underscore = [x for x in dir(__builtins__) if not x.startswith('_')]
print("  内置名字数量: " + str(len(non_underscore)))
print("  部分内置名字: " + str(non_underscore[:10]))
print()

# -----------------------------------------------------------
# 10. __all__ — 导出列表（如果定义了的话）
# -----------------------------------------------------------
print("【10. __all__】")
has_all = '__all__' in dir()
print("  值: " + str(__all__ if has_all else '（未定义）'))
print("  含义: from 模块 import * 时，哪些名字会被导出。没定义就用所有公开名字")
print()

# -----------------------------------------------------------
# 11. __cached__ — 编译后的字节码缓存路径
# -----------------------------------------------------------
print("【11. __cached__】")
print("  值: " + str(__cached__))
print("  含义: 这个 .py 文件对应的 .pyc 字节码缓存文件路径")
print()

# -----------------------------------------------------------
# 12. 脚本所在目录
# -----------------------------------------------------------
print("【12. 派生：脚本所在目录】")
script_dir = os.path.dirname(os.path.abspath(__file__))
print("  os.path.dirname(os.path.abspath(__file__)) = " + script_dir)
print()

print("=" * 60)
print("五、验证：删掉模块内置变量会怎样？")
print("=" * 60)
print()

saved_name = __name__
del __name__
try:
    print(__name__)
except NameError as e:
    print("  删掉 __name__ 后访问: " + str(e))
finally:
    __name__ = saved_name
    print("  恢复后: __name__ = " + str(__name__))

print()
print("=" * 60)
print("六、完整内置变量清单（对比表）")
print("=" * 60)
print()

print("【解释器内置 vs 模块内置 对比】")
print()
print("分类".ljust(20) + "变量名".ljust(18) + "含义".ljust(20) + "典型值")
print("-" * 80)
print("解释器内置(builtins)".ljust(20) + "print, len, str".ljust(18) + "解释器启动就加载".ljust(20) + "任何文件可直接用")
print("".ljust(20) + "True, False, None".ljust(18) + "150+个内置函数/类型/异常".ljust(20) + "print() len() str()")
print("模块内置变量".ljust(20) + "__name__".ljust(18) + "模块身份标识".ljust(20) + "__main__ 或 模块名")
print("".ljust(20) + "__file__".ljust(18) + "模块文件路径".ljust(20) + "E:/path/xxx.py")
print("".ljust(20) + "__doc__".ljust(18) + "文档字符串".ljust(20) + "文件开头的三引号")
print("".ljust(20) + "__package__".ljust(18) + "所属包名".ljust(20) + "包名或 None")
print("".ljust(20) + "__loader__".ljust(18) + "模块加载器".ljust(20) + "Loader 对象")
print("".ljust(20) + "__spec__".ljust(18) + "模块规格信息".ljust(20) + "ModuleSpec 对象")
print("".ljust(20) + "__annotations__".ljust(18) + "类型注解字典".ljust(20) + "{x: int, y: str}")
print("".ljust(20) + "__cached__".ljust(18) + "字节码缓存路径".ljust(20) + ".pyc 文件路径")
print()

print("=" * 60)
print("七、核心结论")
print("=" * 60)
print()
print("  1. 解释器内置（builtins）：")
print("     print, len, str, True, None, Exception 等")
print("     -> 解释器启动时就加载好了，任何 .py 文件直接用")
print()
print("  2. 模块内置变量：")
print("     __name__, __file__, __doc__, __package__ 等")
print("     -> 解释器运行 .py 文件时注入到当前模块的 globals，各模块独立")
print()
print("  3. 验证方式：")
print("     '__name__' in dir(builtins)  -> False（不是builtins）")
print("     '__name__' in globals()     -> True（在当前模块globals里）")
