"""
P05 Agent-Demo: GC 垃圾回收机制
================================
演示 Python 的分代垃圾回收器如何处理循环引用

运行方式：python Agent-Demo/P05_GC垃圾回收机制.py
"""

import gc
import sys


def separator(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)


def show_gc_stats():
    """显示当前GC各代对象数量"""
    count = gc.get_count()    # (0代, 1代, 2代) 对象数量
    threshold = gc.get_threshold()
    print(f"  GC统计: 第0代={count[0]}, 第1代={count[1]}, 第2代={count[2]}")
    print(f"  触发阈值: 第0代={threshold[0]}, 第1代={threshold[1]}, 第2代={threshold[2]}")


# ============================================================
# Demo 1: 引用计数立即回收（非循环引用）
# ============================================================
separator("Demo 1: 引用计数立即回收（非循环引用）")

print("\n  普通对象没有循环引用，引用计数归零就立即回收")
print("  GC不参与！")

x = [1, 2, 3]                 # 创建列表对象
print(f"  x = [1, 2, 3]")
print(f"  此时 [1,2,3] 的 refcnt = 1")

x = None                      # 删除引用
print(f"  x = None")
print(f"  [1,2,3] 的 refcnt = 0 → 立即被 Python 回收（不经过GC）")

print("\n  【结论】非循环引用的对象，引用计数归零就立即释放，不需要GC")


# ============================================================
# Demo 2: 什么是循环引用
# ============================================================
separator("Demo 2: 什么是循环引用？")

print("\n  循环引用：两个对象互相引用，外部已经没有标签指向它们")
print("  但它们的引用计数都 ≠ 0，无法被引用计数回收")

a = []                        # 创建列表A
b = []                        # 创建列表B
print(f"  a = []; b = []")

a.append(b)                   # A引用B
b.append(a)                   # B引用A
print(f"  a.append(b); b.append(a)")

print(f"""
  此时内存结构：

    外部标签
       ↓
    a ──→ [ 列表A ] ──→ [ 列表B ]
                ↑              │
                └──────────────┘
              互相引用，refcnt都=1
""")

print(f"  删除外部标签：del a; del b")
del a
del b

print(f"\n  【问题】a 和 b 都没了，但 A 和 B 互相指着对方")
print(f"         引用计数都是1，无法被引用计数回收")
print(f"         必须靠 GC 分代回收来处理！")


# ============================================================
# Demo 3: 分代回收机制
# ============================================================
separator("Demo 3: 分代回收机制")

print("""
  Python 把所有对象分成3代：

  ┌─────────────────────────────────────────────────────┐
  │ 第0代（年轻代）│ 新创建的对象                        │
  │ 第1代（中年代）│ 第0代回收后还存活的对象              │
  │ 第2代（老年代）│ 第1代回收后还存活的对象              │
  └─────────────────────────────────────────────────────┘

  触发规则：
  - 第0代对象数 ≥ 700 → 触发第0代GC（最频繁）
  - 第1代对象数 ≥ 600 → 触发第1代GC（较少）
  - 第2代对象数 ≥ 600 → 触发第2代GC（最少）
""")

print("  查看当前GC状态：")
show_gc_stats()


# ============================================================
# Demo 4: 手动触发GC观察回收
# ============================================================
separator("Demo 4: 手动触发 GC 观察循环引用回收")

# 先禁用自动GC，看得更清楚
gc.disable()
print("\n  gc.disable() — 禁用自动GC")

# 批量创建循环引用
print("\n  创建100个循环引用对象...")
cycle_refs = []
for i in range(100):
    a = []          # 创建列表A
    b = []          # 创建列表B
    a.append(b)     # A引用B
    b.append(a)     # B引用A
    cycle_refs.append((a, b))

print(f"  100个循环引用创建完毕！")
show_gc_stats()

# 删除外部引用
cycle_refs.clear()
print(f"\n  cycle_refs.clear() — 删除所有外部引用")
print(f"  这100个循环引用对象现在完全不可达（但还在内存里）")

collected = gc.collect()
print(f"\n  手动 gc.collect() → 回收了 {collected} 个对象！")
show_gc_stats()

# 重新启用GC
gc.enable()
print("\n  gc.enable() — 恢复自动GC")


# ============================================================
# Demo 5: 观察分代晋升
# ============================================================
separator("Demo 5: 观察对象在分代间的晋升")

gc.collect()  # 先清空
print("\n  先 gc.collect() 清空当前各代")
show_gc_stats()

# 创建一个对象，观察它在第0代的生命周期
print("\n  创建对象，观察其分代变化：")

class Tracked:
    """追踪对象在各代的晋升"""
    instances = []
    def __init__(self, name):
        self.name = name
        Tracked.instances.append(self)
    def __repr__(self):
        return f"Tracked({self.name})"

# 创建一些对象，有些会被回收，有些会晋升
objs = []
for i in range(10):
    objs.append(Tracked(f"obj_{i}"))

# 触发0代GC多次
for i in range(3):
    collected = gc.collect()
    print(f"  第{i+1}次GC: 回收了 {collected} 个对象")
    show_gc_stats()

# 清理
objs.clear()
Tracked.instances.clear()
gc.collect()


# ============================================================
# Demo 6: gc.get_referrers() 查看谁在引用某个对象
# ============================================================
separator("Demo 6: gc.get_referrers() 查看引用关系")

x = [1, 2, 3]
y = x                    # y也指向同一个对象
z = [x]                  # z包含x

print(f"  x = [1, 2, 3]")
print(f"  y = x")
print(f"  z = [x]")

print(f"\n  查看是什么在引用 x（对象[1,2,3]）：")
referrers = gc.get_referrers(x)
print(f"  gc.get_referrers(x) 返回 {len(referrers)} 个引用者：")
for i, ref in enumerate(referrers):
    print(f"    [{i}] {type(ref)}: {repr(ref)[:50]}...")

print(f"""
  解释：
  - y = x → y 引用了 x
  - z = [x] → z[0] 引用了 x
  - 还有 gc.get_referrers 本身也会产生一个临时引用
""")


# ============================================================
# Demo 7: 循环引用无法被引用计数回收的证据
# ============================================================
separator("Demo 7: 循环引用对象的内存地址不变（证明没被回收）")

gc.collect()  # 先清空

a = []
b = []
a.append(b)
b.append(a)
a_id = id(a)
b_id = id(b)

print(f"  创建循环引用：a = []; b = []; a.append(b); b.append(a)")
print(f"  a 的 id: {a_id}")
print(f"  b 的 id: {b_id}")

del a
del b
print(f"\n  del a; del b — 外部标签删除")

print(f"  但 a 的 id 仍然是: {a_id}")
print(f"  但 b 的 id 仍然是: {b_id}")

collected = gc.collect()
print(f"\n  gc.collect() → 回收了 {collected} 个对象")


# ============================================================
# Demo 8: 启用/禁用 GC
# ============================================================
separator("Demo 8: gc.enable() / gc.disable()")

print("""
  gc.enable()  — 启用自动垃圾回收（默认启用）
  gc.disable() — 禁用自动垃圾回收

  禁用后：
  - 引用计数归零 → 立即回收（这个不受影响）
  - 循环引用 → 永远不会自动回收（直到你手动 gc.collect()）
""")

gc.disable()
print("  gc.disable() 已执行")

# 创建循环引用
a = []
b = []
a.append(b)
b.append(a)
del a
del b

print("  创建并删除循环引用")
print("  由于 GC 被禁用，循环引用不会自动回收")
print(f"  当前第0代对象数: {gc.get_count()[0]}")

gc.collect()  # 手动回收
print(f"  手动 gc.collect() 后，第0代对象数: {gc.get_count()[0]}")

gc.enable()
print("  gc.enable() — 恢复自动GC")


# ============================================================
# 总结
# ============================================================
separator("总结")

print("""
  Python 的内存管理分两层：

  ┌─────────────────────────────────────────────────────┐
  │  第1层：引用计数（自动回收非循环引用）               │
  │         - refcnt 归零 → 立即释放，不经过GC          │
  │         - 优点：零开销、无延迟                       │
  │         - 缺点：无法处理循环引用                    │
  ├─────────────────────────────────────────────────────┤
  │  第2层：分代GC（回收循环引用）                       │
  │         - 第0代对象 ≥ 700 → 触发第0代GC            │
  │         - 循环引用靠"标记-清除"算法                 │
  │         - 优点：自动处理循环引用                     │
  │         - 缺点：有延迟、有性能开销                  │
  └─────────────────────────────────────────────────────┘

  为什么要分代？
  → 大部分对象是"朝生夕死"的，分代可以少扫描老对象，效率更高
""")
