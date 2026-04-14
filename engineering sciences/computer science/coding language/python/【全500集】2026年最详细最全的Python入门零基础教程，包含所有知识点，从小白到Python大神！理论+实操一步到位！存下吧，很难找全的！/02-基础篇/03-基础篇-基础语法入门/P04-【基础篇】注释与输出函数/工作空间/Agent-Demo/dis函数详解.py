# ============================================================
# dis 模块完整演示
# dis = disassembler（反汇编器），Python 标准库自带
# 把字节码翻译成人类可读的指令
# ============================================================

import dis

# -----------------------------------------------------------
# dis 是什么？
# -----------------------------------------------------------
# Python 代码执行流程：
#   源代码(.py) → 解析器(parser) → 字节码(.pyc) → Python虚拟机(VM)执行
#                              ↑
#                     dis.dis() 把字节码翻译成人话
#
# 字节码指令（常见）：
#   LOAD_CONST  — 把常量加载到栈顶
#   STORE_FAST  — 把栈顶值存到局部变量
#   LOAD_FAST   — 把局部变量加载到栈顶
#   BINARY_OP   — 栈顶两个值做运算（+ - * / 等）
#   RETURN_VALUE — 返回值
#   POP_TOP     — 弹出栈顶（丢弃）
#   JUMP_FORWARD — 跳转（for/if 逻辑）
# -----------------------------------------------------------

# -----------------------------------------------------------
# 1. dis.dis(函数) —  disassemble 一个函数
# -----------------------------------------------------------
print("=== 1. dis.dis(函数) ===")

def add(a, b):
    return a + b

dis.dis(add)
# 格式说明：
# 第1列：源代码行号
# 第2列：字节码指令偏移量（offset）
# 第3列：指令名称（opcode）
# 第4列：指令参数

print()
print("解释：")
print("  LOAD_FAST  0 (a)  → 把局部变量 a 加载到栈顶")
print("  LOAD_FAST  1 (b)  → 把局部变量 b 加载到栈顶")
print("  BINARY_OP  +       → 栈顶两个值相加")
print("  RETURN_VALUE       → 返回栈顶的值")

print()
print("=" * 50)

# -----------------------------------------------------------
# 2. dis.dis(代码对象) — 反汇编任意代码
# -----------------------------------------------------------
print("=== 2. dis.dis(代码对象) ===")
# 直接反汇编函数的字节码对象
code_obj = add.__code__
print(f"   {add.__name__} 的字节码对象: {code_obj}")
print()
dis.dis(code_obj)

print()
print("=" * 50)

# -----------------------------------------------------------
# 3. dis.dis(code_string) — 反汇编字符串代码（exec）
# -----------------------------------------------------------
print("=== 3. dis.dis('代码字符串') — exec 方式 ===")
dis.dis("x = 10 + 20")
print()
print("解释：")
print("  LOAD_CONST  1 (10)  → 把常数 10 入栈")
print("  LOAD_CONST  2 (20)  → 把常数 20 入栈")
print("  BINARY_OP  +        → 栈顶两数相加，30 入栈")
print("  STORE_FAST 0 (x)   → 栈顶值存到变量 x")

print()
print("=" * 50)

# -----------------------------------------------------------
# 4. dis.code_info(函数) — 比 dis.dis 更详细
# -----------------------------------------------------------
print("=== 4. dis.code_info(函数) — 完整代码信息 ===")
print(dis.code_info(add))

print()
print("=" * 50)

# -----------------------------------------------------------
# 5. dis.show_code(函数) — 显示代码的详细信息
# -----------------------------------------------------------
print("=== 5. dis.show_code(函数) ===")
dis.show_code(add)

print()
print("=" * 50)

# -----------------------------------------------------------
# 6. 查看常量池、局部变量名、属性名
# -----------------------------------------------------------
print("=== 6. 字节码底层数据结构 ===")
print(f"   co_consts  (常量池): {add.__code__.co_consts}")
print(f"   co_varnames(局部变量): {add.__code__.co_varnames}")
print(f"   co_names   (属性名): {add.__code__.co_names}")
print(f"   co_stacksize (栈大小): {add.__code__.co_stacksize}")
print(f"   co_nlocals  (局部变量数): {add.__code__.co_nlocals}")
print(f"   co_freevars / co_cellvars: {add.__code__.co_freevars} / {add.__code__.co_cellvars}")

print()
print("=" * 50)

# -----------------------------------------------------------
# 7. dis.findlinestarts — 找每条指令对应的源代码行
# -----------------------------------------------------------
print("=== 7. dis.findlinestarts ===")
for offset, line in dis.findlinestarts(add.__code__):
    print(f"   偏移 {offset:2d} → 第 {line} 行")

print()
print("=" * 50)

# -----------------------------------------------------------
# 8. 一个更复杂的例子：带分支的函数
# -----------------------------------------------------------
print("=== 8. 复杂函数反汇编 ===")

def classify(score):
    if score >= 90:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "C"

dis.dis(classify)
print()
print("解释：")
print("  LOAD_FAST   → 把 score 入栈")
print("  LOAD_CONST  → 把 90 入栈")
print("  COMPARE_OP   → 比较两个值（>=）")
print("  POP_JUMP_IF_FALSE → 如果是 False，跳转到某行（elif）")
print("  LOAD_CONST   → 把 'A' 入栈")
print("  RETURN_VALUE → 返回")
print("  JUMP_FORWARD → 跳过 elif 分支")
print("  ...")

print()
print("=" * 50)

# -----------------------------------------------------------
# 9. 装饰器对字节码的影响
# -----------------------------------------------------------
print("=== 9. 装饰器对字节码的影响 ===")
import functools

def my_decorator(func):
    @functools.wraps(func)          # 保留原函数元信息（关键！）
    def wrapper(*args):
        return func(*args) + " (装饰后)"
    return wrapper

def original_greeting(name):
    """打招呼函数"""
    return f"Hello, {name}"

greeting = my_decorator(original_greeting)

print("原函数字节码（__wrapped__ 可用）：")
dis.dis(greeting.__wrapped__)
print()
print("装饰后 wrapper 字节码：")
dis.dis(greeting)
print()
print("关键区别：")
print("  @functools.wraps(func) 让 wrapper.__wrapped__ 指向原函数")
print("  wrapper 多了一次 CALL_FUNCTION + BINARY_CONCAT")
print(f"  greeting.__name__ = {greeting.__name__}  （functools.wraps 保留了函数名）")

print()
print("=" * 50)

# -----------------------------------------------------------
# 10. Python 版本差异（了解即可）
# -----------------------------------------------------------
print("=== 10. 不同版本字节码差异 ===")
import sys
print(f"   当前 Python 版本: {sys.version}")
print()
print("   Python 3.11+ 的变化：")
print("   - RESUME / RETURN_CONST 新指令")
print("   - LOAD_GLOBAL 变成了 LOAD_GLOBAL_MODULE")
print("   - 指令更少，虚拟机更快")
print()
print("   Python 3.12+ 的变化：")
print("   - BINARY_OP 指令统一了 + - * / 等操作")
print("   - 更激进的内联缓存优化")
