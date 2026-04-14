"""
P05 Agent-Demo: 变量是标签，对象在等号右边
=============================================
演示变量与对象的绑定关系，以及垃圾回收机制

⚠️ 注意：本Demo中关于CPython底层结构的描述已过时。
正确的信息请参考笔记 P05-变量是标签-对象在等号右边.md 中的"Python对象的C层实现"章节。

运行方式：在终端执行 python Agent-Demo/P05_变量是标签_对象在右边.py
"""

import sys
import ctypes


def get_ref_count(obj):
    """获取对象的引用计数"""
    try:
        return sys.getrefcount(obj)
    except TypeError:
        return "无法获取（对象不可哈希）"


def show_binding(label_name, obj, annotation=""):
    """显示变量和对象的绑定关系"""
    obj_type = type(obj)
    obj_id = id(obj)
    print(f"  {label_name:8} ──────→ [ {obj_type.__name__:8} ] id={obj_id}  值={repr(obj)}  {annotation}")


def separator(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)


# ============================================================
# Demo 1: 最简单的绑定 — x 只是标签，真正的对象在右边
# ============================================================
separator("Demo 1: x = 10 — x是标签，对象在等号右边")

x = 10
show_binding("x", x, "← x贴在此对象上")

print(f"\n  验证：x是指向对象的标签，而不是对象本身")
print(f"  id(x)        = {id(x)}          ← 对象的内存地址")
print(f"  type(x)      = {type(x)}       ← 对象的类型")
print(f"  x            = {x}             ← 对象存储的值")
print(f"  x is 10      = {x is 10}       ← x和10是同一个对象")


# ============================================================
# Demo 2: 重新绑定 — x撕下来贴到新对象
# ============================================================
separator("Demo 2: x = 3.14 — x撕下来贴到新对象")

print("\n  执行 x = 3.14 之前：")
print(f"  对象10的引用计数: {get_ref_count(10)}")

print("\n  执行 x = 3.14 之后：")
x = 3.14
show_binding("x", x)

print(f"\n  对象10的引用计数(现在): {get_ref_count(10)}  ← 因为x不再指向它")
print(f"  对象3.14的引用计数: {get_ref_count(3.14)}")


# ============================================================
# Demo 3: 多个标签指向同一个对象
# ============================================================
separator("Demo 3: a和b同时指向同一个对象")

a = 10
b = a  # b也贴在对象10上

print("\n  a = 10 之后：")
show_binding("a", a)

print("\n  b = a 之后（b也指向同一个对象）：")
show_binding("a", a)
show_binding("b", b, "← 与a绑定同一对象")

print(f"\n  id(a) = {id(a)}")
print(f"  id(b) = {id(b)}  ← 相同！")
print(f"  a is b = {a is b}  ← 确认是同一个对象")


# ============================================================
# Demo 4: 一个对象可以有无限多个标签
# ============================================================
separator("Demo 4: 一个对象可以有多个标签")

original = [1, 2, 3]
alias_1 = original
alias_2 = original
alias_3 = original
alias_4 = original

print(f"\n  original = [1, 2, 3]")
print(f"  alias_1 = alias_2 = alias_3 = alias_4 = original")
print(f"\n  所有标签都指向同一个对象：")
show_binding("original", original)
show_binding("alias_1", alias_1)
show_binding("alias_2", alias_2)
show_binding("alias_3", alias_3)
show_binding("alias_4", alias_4)

print(f"\n  original is alias_3 = {original is alias_3}")


# ============================================================
# Demo 5: 重新绑定导致标签分离
# ============================================================
separator("Demo 5: a重新绑定后，a和b分离")

a = 10
b = a  # 最初a和b指向同一个对象

print(f"\n  a = 10; b = a 之后：")
show_binding("a", a)
show_binding("b", b, "← 同一对象")

a = 20  # a重新绑定到新对象，b不变

print(f"\n  a = 20 之后：")
show_binding("a", a, "← 新对象")
show_binding("b", b, "← 仍绑定原对象")

print(f"\n  a = {a}, b = {b}  ← 值不同了！")


# ============================================================
# Demo 6: 序列赋值 — 同时绑定多个标签
# ============================================================
separator("Demo 6: 序列赋值 a, b = 1, 2")

a, b = 1, 2
show_binding("a", a)
show_binding("b", b)

print(f"\n  等价于：")
print(f"    a = 1")
print(f"    b = 2")
print(f"\n  但一行搞定：a, b = b, a 可以交换两个变量的值")

a, b = 1, 2
print(f"\n  交换前：a = {a}, b = {b}")
a, b = b, a  # 右侧先构建元组(b, a) = (2, 1)，然后解包赋值
print(f"  交换后：a = {a}, b = {b}")


# ============================================================
# Demo 7: 标签可以贴在任何对象上 — 动态类型
# ============================================================
separator("Demo 7: x可以先后指向不同类型的对象")

x = 42
print(f"  x = 42    → ", end="")
show_binding("x", x, "")

x = "你好"
print(f"  x = '你好' → ", end="")
show_binding("x", x, "")

x = [1, 2, 3]
print(f"  x = [1,2,3] → ", end="")
show_binding("x", x, "")

x = None
print(f"  x = None   → x不指向任何对象（空标签）")


# ============================================================
# Demo 8: 标签删除 — del只是撕标签，不删除对象
# ============================================================
separator("Demo 8: del x 只是撕掉标签，不一定删除对象")

obj = [4, 5, 6]
print(f"\n  obj = [4, 5, 6] 之后：")
show_binding("obj", obj)

ref_count_before = get_ref_count([4, 5, 6])
print(f"  列表对象 [4,5,6] 的引用计数: {ref_count_before}")

other = obj  # 多一个标签
print(f"\n  other = obj 之后（引用计数+1）:")
print(f"  列表对象 [4,5,6] 的引用计数: {get_ref_count([4,5,6])}")

del obj  # 只是撕掉obj标签
print(f"\n  del obj 之后：")
print(f"  other 仍然指向该对象: {other}  ← 对象还在！")


# ============================================================
# Demo 9: 引用计数降到0，对象被回收
# ============================================================
separator("Demo 9: 引用计数归零时，对象被垃圾回收")

print("\n  当没有任何标签指向某个对象时，引用计数变为0")
print("  Python的垃圾回收器(GC)会回收这个内存")
print("\n  手动演示：")

big_obj = {"key": "value"}  # 创建一个大对象
print(f"  big_obj = {{'key': 'value'}}")
print(f"  对象id: {id(big_obj)}")

big_obj_id = id(big_obj)
del big_obj  # 删除标签

# 尝试访问已删除的对象会报错
try:
    print(big_obj)
except NameError as e:
    print(f"  del big_obj 之后访问big_obj → {e}")

print(f"\n  对象 {{'key': 'value'}} 现在没有任何标签引用它")
print(f"  Python的垃圾回收器会在适当时候回收它的内存")


# ============================================================
# Demo 10: 函数参数也是标签
# ============================================================
separator("Demo 10: 函数参数也是标签")

def change_label(x):
    """传入的x只是内部使用的临时标签"""
    print(f"\n  函数内部，参数x绑定到: {x}, id={id(x)}")
    x = 100  # 重新绑定x到新对象
    print(f"  x = 100 后，x绑定到: {x}, id={id(x)}")
    return x

num = 50
print(f"  调用前：num = {num}, id = {id(num)}")
result = change_label(num)
print(f"  调用后：num = {num}  ← 外部num不变！")
print(f"  返回值 result = {result}")

print("\n  原因：num和函数参数x是两个不同的标签")
print("  x = 100只是把x撕下来贴到100上，不影响外部的num")


# ============================================================
# 总结
# ============================================================
separator("总结：变量赋值的本质")

print("""
  1. 等号右边创建/定位对象
  2. 等号左边是标签，贴在右边的对象上
  3. 赋值操作 = 撕标签 + 贴新对象
  4. 没有标签的对象会被GC回收（但时机不确定）

  所以：
    x = 10
  的真实含义是：
    "找到int对象10，把标签x贴在它上面"
  而不是：
    "把10放进x里面"
""")
