# ============================================================
# print 函数所有参数完整演示
# ============================================================

# -----------------------------------------------------------
# 1. sep — 多个参数之间的分隔符，默认是一个空格
# -----------------------------------------------------------
print("苹果", "香蕉", "樱桃")           # 默认 sep=空格
print("苹果", "香蕉", "樱桃", sep=",")  # 用逗号分隔
print("苹果", "香蕉", "樱桃", sep=" | ")# 自定义分隔符
print("hello", "world", sep="")         # 空字符串 = 连在一起

print()

# -----------------------------------------------------------
# 2. end — 结尾字符，默认是换行 \n
# -----------------------------------------------------------
print("第一行", end=" ")                # 空格结尾，不换行
print("接着打印")                       # 接着上一行末尾继续

print("进度", end="")
print("加载中", end="...")
print("完成")

print()

# -----------------------------------------------------------
# 3. file — 输出到哪里，默认是 sys.stdout（屏幕）
# -----------------------------------------------------------
# -----------------------------------------------------------
# 3. file — 输出到哪里，默认是 sys.stdout（屏幕）
# -----------------------------------------------------------
# 屏幕输出
print("打印到屏幕")

# -----------------------------------------------------------
# 用绝对路径创建文件，确保文件建在脚本所在目录，不受 cwd 影响
# -----------------------------------------------------------
# __file__ 是 Python 内置变量，每个 .py 文件都有
# __file__ 的值 = 这个 .py 文件自己的路径（相对路径或绝对路径）
#   例如：__file__ = "print参数详解.py"  或  __file__ = "E:/.../Agent-Demo/print参数详解.py"
#
# os.path.abspath(__file__) 把相对路径转成绝对路径
#   __file__ = "print参数详解.py"  （相对路径）
#   os.path.abspath(__file__) = "E:/.../Agent-Demo/print参数详解.py"  （绝对路径）
#
# os.path.dirname(绝对路径) 提取文件所在的目录
#   os.path.dirname("E:/.../Agent-Demo/print参数详解.py")
#   = "E:/.../Agent-Demo"
#
# os.path.join(目录, "文件名") 拼接成完整路径
#   os.path.join("E:/.../Agent-Demo", "output.txt")
#   = "E:/.../Agent-Demo/output.txt"
#
# 完整流程：
#   __file__ = "print参数详解.py"
#             ↓ os.path.abspath()
#   "E:/.../Agent-Demo/print参数详解.py"
#             ↓ os.path.dirname()
#   "E:/.../Agent-Demo"
#             ↓ os.path.join("output.txt")
#   "E:/.../Agent-Demo/output.txt"

import os
script_dir = os.path.dirname(os.path.abspath(__file__))   # 脚本所在目录的绝对路径
output_path = os.path.join(script_dir, "output.txt")      # 拼接出文件完整路径

# 输出到文件（会覆盖文件内容）
with open(output_path, "w", encoding="utf-8") as f:
    print("写入文件第一行", file=f)
    print("写入文件第二行", file=f)

# 追加模式写入
with open(output_path, "a", encoding="utf-8") as f:
    print("追加第三行", file=f)

print(f"文件已写入: {output_path}")

# -----------------------------------------------------------
# 4. flush — 是否立刻刷新输出，默认 False
# -----------------------------------------------------------
import time

print("不刷新（带缓冲）:", end=" ")
time.sleep(0.5)
print("等待中...", end=" ")
time.sleep(0.5)
print("结束")

print("强制刷新（无缓冲）:", end=" ")
time.sleep(0.5)
print("立刻显示", end=" ", flush=True)
time.sleep(0.5)
print("完成")

# -----------------------------------------------------------
# 5. 组合使用：sep + end + file + flush
# -----------------------------------------------------------
print("数据", 123, True, sep=" -> ", end=" | ")
print("下一条", sep=" | ", flush=True)

print()

# -----------------------------------------------------------
# 6. f-string / format / % 三种格式化全部展示
# -----------------------------------------------------------
name = "小明"
age = 25
height = 1.75

# f-string（最推荐，Python 3.6+）
print(f"姓名：{name}，年龄：{age}，身高：{height}")

# format 方法
print("姓名：{}，年龄：{}，身高：{:.2f}".format(name, age, height))
print("姓名：{0}，年龄：{1}，身高：{2:.2f}".format(name, age, height))
print("姓名：{n}，年龄：{a}，身高：{h:.2f}".format(n=name, a=age, h=height))

# % 格式化（旧式）
print("姓名：%s，年龄：%d，身高：%.2f" % (name, age, height))

print()

# -----------------------------------------------------------
# 7. 转义字符完整演示
# -----------------------------------------------------------
print("=== 转义字符 ===")
print("\\n 换行：\n这是换行后的第二行")
print("\\t 制表符：\t对齐的列1\t对齐的列2\t对齐的列3")
print("\\r 回车：\r覆盖前面的内容")      # 会覆盖该行前面的内容
print("\\b 退格：hello\b\bworld")       # 退格删除两个字符
print("\\\\ 反斜杠：路径是 C:\\\\Users\\\\Name")
print("\\\" 双引号：他说\"你好\"")
print("\\' 单引号：她说'再见'")
print("\\a 响铃：\a（如果终端支持会响）")

# 原始字符串（r 前缀，转义字符不生效）
print(r"原始字符串 \\n \\t 不生效：C:\Users\Name\temp")

# 垂直制表符和换页
print("垂直制表符：\v第一行\v第二行")
print("换页符：\f第一页\f第二页")

print()

# -----------------------------------------------------------
# 8. 一个特别特别复杂的 print
# -----------------------------------------------------------
title = "Python"
version = 3.12
author = "Guido"
features = ["简单", "优雅", "强大"]
year = 2024

print("=" * 60)
print("  《{:<15}》 v{:.1f}  作者：{:^10}".format(title, version, author))
print("=" * 60)
print(f"  特点：{' | '.join(features)}")
print(f"  发布年份：{year}")
print(f"  Python > C++? {True if version > 3 else False}")
print("-" * 60)
print("  格式化数字演示：")
print(f"    整数填充：{42:>5}（右对齐，占5位）")
print(f"    整数填充: {42:<5}（左对齐，占5位）")
print(f"    整数填充: {42:^5}（居中对齐，占5位）")
print(f"    带符号:   {+42:>+5}（显示正号）")
print(f"    带符号:   {-42:>+5}（显示负号）")
print(f"    十六进制: {255:>#6x}（0xff）")
print(f"    二进制:   {42:>#10b}（0b101010）")
print(f"    科学计数法: {1234567.89:.2e}")
print(f"    千位分隔: {1234567:,}")
print(f"    百分比:   {0.856:.1%}")
print(f"    多重填充: {42:0>10.2f}（数字转字符串再填充）")
print("-" * 60)
print(f"  嵌套格式化：{[x**2 for x in range(1,6)]}")
print(f"  字典访问：{features[0]}, {features[-1]}")
print("=" * 60)
