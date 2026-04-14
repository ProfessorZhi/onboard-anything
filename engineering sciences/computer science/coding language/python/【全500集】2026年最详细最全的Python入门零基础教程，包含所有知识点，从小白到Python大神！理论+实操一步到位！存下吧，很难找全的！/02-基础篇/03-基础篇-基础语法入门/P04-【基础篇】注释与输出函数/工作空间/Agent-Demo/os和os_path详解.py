# ============================================================
# os 模块 和 os.path 完整演示
# ============================================================
"""
os 是标准库，import os 就能用
os.path 是 os 模块里的一个"子模块"
两个点 = 属性访问（.运算符）
"""
import os

print("=" * 60)
print("一、先搞清楚 os.path 到底是什么")
print("=" * 60)
print()

# os.path 到底是什么？
print(f"os.path 是什么？ → {type(os.path)}")
print(f"os.path 的值: {os.path}")
print()
print("解释：os 模块在加载时，会把自己的 path 属性指向一个专门处理路径的子模块")
print(f"在 Windows 上，os.path 实际上指向的是: {os.path.__name__}")
print()
print("os 模块和 os.path 的关系：")
print("  os        → os.py       (处理操作系统相关功能)")
print("  os.path   → ntpath.py   (处理路径字符串，仅 Windows)")
print("  两个点 .  → 访问 os 这个对象的 path 属性")
print()

print("=" * 60)
print("二、os 模块主要功能")
print("=" * 60)
print()

# -----------------------------------------------------------
# 1. os.getcwd() — 获取当前工作目录
# -----------------------------------------------------------
print("【1. os.getcwd() — 获取当前工作目录】")
cwd = os.getcwd()
print(f"  当前目录: {cwd}")
print()

# -----------------------------------------------------------
# 2. os.listdir() — 列出目录内容
# -----------------------------------------------------------
print("【2. os.listdir(目录) — 列出目录内容】")
items = os.listdir(cwd)
print(f"  当前目录内容: {items[:5]}{'...' if len(items)>5 else ''}")
print()

# -----------------------------------------------------------
# 3. os.mkdir() / os.makedirs() — 创建目录
# -----------------------------------------------------------
print("【3. os.mkdir() / os.makedirs() — 创建目录】")
print("  os.mkdir('abc')       → 创建单个目录，父目录不存在会报错")
print("  os.makedirs('a/b/c')  → 递归创建目录（父目录不存在一起创建）")
print()

# -----------------------------------------------------------
# 4. os.remove() / os.rmdir() — 删除文件/目录
# -----------------------------------------------------------
print("【4. os.remove() / os.rmdir() — 删除文件/目录】")
print("  os.remove('file.txt')  → 删除文件")
print("  os.rmdir('dir')       → 删除空目录")
print()

# -----------------------------------------------------------
# 5. os.rename() / os.replace() — 重命名或移动
# -----------------------------------------------------------
print("【5. os.rename() / os.replace() — 重命名或移动】")
print("  os.rename('旧名', '新名')  → 重命名或移动文件")
print()

# -----------------------------------------------------------
# 6. os.path.exists() — 判断路径是否存在
# -----------------------------------------------------------
print("【6. os.path.exists(路径) — 判断路径是否存在】")
print(f"  os.path.exists('{cwd}'): {os.path.exists(cwd)}")
print(f"  os.path.exists('不存在'): {os.path.exists('不存在路径')}")
print()

# -----------------------------------------------------------
# 7. os.path.isfile() / os.path.isdir() — 判断是文件还是目录
# -----------------------------------------------------------
print("【7. os.path.isfile() / os.path.isdir() — 判断类型】")
print(f"  os.path.isfile('{cwd}'): {os.path.isfile(cwd)}")
print(f"  os.path.isdir('{cwd}'): {os.path.isdir(cwd)}")
print()

# -----------------------------------------------------------
# 8. os.path.join() — 拼接路径（跨平台正确拼接）
# -----------------------------------------------------------
print("【8. os.path.join() — 拼接路径】")
p1 = os.path.join('home', 'user', 'desktop', 'file.txt')
p2 = os.path.join('C:\\Users', 'Admin', 'file.txt')
print(f"  os.path.join('home', 'user', 'desktop', 'file.txt'):")
print(f"  Linux/Mac 结果: {p1}")
print(f"  Windows 结果: {'/'.join(['home', 'user', 'desktop', 'file.txt'])}")
print(f"  注意: 在 Windows 上会自动用 \\ 分隔，不用手动写死")
print()

# -----------------------------------------------------------
# 9. os.path.split() — 拆分路径
# -----------------------------------------------------------
print("【9. os.path.split() — 拆分路径为目录 + 文件名】")
full = "C:\\Users\\Admin\\Documents\\file.txt"
parts = os.path.split(full)
print(f"  os.path.split('{full}'):")
print(f"  结果: {parts}")
print(f"  目录: {parts[0]}")
print(f"  文件名: {parts[1]}")
print()

# -----------------------------------------------------------
# 10. os.path.splitext() — 拆分路径 + 扩展名
# -----------------------------------------------------------
print("【10. os.path.splitext() — 拆分路径 + 扩展名】")
name, ext = os.path.splitext("report_final_v2.pdf")
print(f"  os.path.splitext('report_final_v2.pdf'):")
print(f"  文件名: {name}")
print(f"  扩展名: {ext}")
print()

# -----------------------------------------------------------
# 11. os.path.abspath() — 转绝对路径
# -----------------------------------------------------------
print("【11. os.path.abspath() — 相对路径转绝对路径】")
rel = "..\\..\\file.txt"
abs_ = os.path.abspath(rel)
print(f"  os.path.abspath('..\\\\..\\\\file.txt'):")
print(f"  结果: {abs_}")
print()

# -----------------------------------------------------------
# 12. os.path.dirname() / os.path.basename() — 目录/文件名
# -----------------------------------------------------------
print("【12. os.path.dirname() / basename()】")
path = "C:\\Users\\Admin\\Documents\\file.txt"
print(f"  os.path.dirname('{path}'): {os.path.dirname(path)}")
print(f"  os.path.basename('{path}'): {os.path.basename(path)}")
print()

# -----------------------------------------------------------
# 13. os.path.getsize() — 文件大小
# -----------------------------------------------------------
print("【13. os.path.getsize() — 文件大小（字节）】")
demo_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "os和os_path详解.py")
size = os.path.getsize(demo_py)
print(f"  本文件大小: {size} 字节 ({size/1024:.1f} KB)")
print()

# -----------------------------------------------------------
# 14. os.walk() — 递归遍历目录树
# -----------------------------------------------------------
print("【14. os.walk() — 递归遍历目录（生成器）】")
print("  for root, dirs, files in os.walk('目录'):")
print("    root  = 当前目录路径")
print("    dirs  = 该目录下的子目录列表")
print("    files = 该目录下的文件列表")
print()

# -----------------------------------------------------------
# 15. os.getenv() / os.environ — 读取环境变量
# -----------------------------------------------------------
print("【15. os.getenv() / os.environ — 环境变量】")
print(f"  os.getenv('PATH') 前100字符: {os.getenv('PATH', '')[:100]}...")
print()

# -----------------------------------------------------------
# 16. os.system() — 执行系统命令
# -----------------------------------------------------------
print("【16. os.system() — 执行系统命令】")
print("  os.system('cls')      → Windows 清屏")
print("  os.system('clear')    → Linux/Mac 清屏")
print("  os.system('notepad')  → 打开记事本")
print()

# -----------------------------------------------------------
# 17. os 模块的路径相关属性的真相
# -----------------------------------------------------------
print("=" * 60)
print("三、os.path 到底是什么（深入）")
print("=" * 60)
print()

print(f"  os.path 是: {os.path}")
print(f"  os.path.__name__ = {os.path.__name__}")
print(f"  os.path.__file__ = {os.path.__file__}")
print()
print("  os.py 文件里有一行：")
print("    from ntpath import path as path  (Windows)")
print("    from posixpath import path as path  (Linux/Mac)")
print("  所以 os.path 就是 ntpath / posixpath 这个子模块")
print()
print("  两个点 . 的含义：")
print("    点(.) = 访问对象的属性/方法")
print("    os.path = 访问 os 这个对象的 path 属性")
print("    os.path.join = 访问 os.path 这个子模块的 join 函数")
print()

# -----------------------------------------------------------
# 18. os 的其他子模块
# -----------------------------------------------------------
print("=" * 60)
print("四、os 模块的其他子模块（不只是 path）")
print("=" * 60)
print()

print("  os 有哪些子模块/子包？")
print(f"  os.path:    {os.path.__name__}  ← 最常用，处理路径字符串")
print()

# 尝试访问 os 的其他属性，看有没有子模块
attrs = [a for a in dir(os) if not a.startswith('_')]
submodules = []
for a in attrs:
    obj = getattr(os, a)
    if isinstance(obj, type(os)):  # 是否是 module 类型
        submodules.append((a, obj))
print(f"  其他子模块: {submodules if submodules else '（只有 os.path）'}")
