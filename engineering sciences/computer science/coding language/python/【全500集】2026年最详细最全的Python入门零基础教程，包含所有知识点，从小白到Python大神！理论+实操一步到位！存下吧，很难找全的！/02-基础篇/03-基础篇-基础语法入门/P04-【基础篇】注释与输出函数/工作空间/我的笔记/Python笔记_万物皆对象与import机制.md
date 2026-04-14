# Python 万物皆对象与 import 机制

## 一、万物皆对象

Python 中**所有东西都是对象**——数字、字符串、函数、类、模块、甚至是 `True`、`None`：

```python
# 这些都是对象
type(1)          # <class 'int'>
type("hello")    # <class 'str'>
type(print)      <class 'builtin_function_or_method'>
type(os)         <class 'module'>
type(123)        <class 'int'>
```

---

## 二、对象的属性可以是任意对象

对象的属性可以是：子模块、函数、变量、类、常量——**任意 Python 对象**。

```python
import os

os.path       # 属性是子模块 (module)
os.getcwd     # 属性是函数 (function)
os.name       # 属性是字符串 (str)  → 'nt'
os.sep        # 属性是字符串 (str)  → '\\'
os.linesep    # 属性是字符串 (str)  → '\r\n'
```

**本质**：模块就是一个字典（名字 → 对象），任何类型的值都可以往里放。

```python
# 类比：模块类似这样的结构
class Module:
    path = SomeModule()
    getcwd = some_function
    name = "nt"
    sep = "\\"
```

---

## 三、模块的特殊性

模块本质上**就是一个容器**，特殊性仅此而已：

| 特性 | 说明 |
|------|------|
| 通过 `import` 加载 | 创建后全局唯一（单例） |
| 有 `__name__` 属性 | 标识模块身份 |
| `__file__` 属性 | 指向源码文件路径 |
| 顶层代码会执行 | import 时整文件跑一遍 |

---

## 四、import 机制：顶层代码执行

### 什么是"顶层代码"

模块文件**最外层、不在任何函数/类内部的代码**，就是顶层代码。import 时这些代码会立刻执行。

```python
# demo.py
print("开始加载 demo")      # ← 顶层，会执行

x = 123                    # ← 顶层，会执行（定义变量）

def foo():                 # ← 顶层，只注册函数名，不执行函数体
    print("foo 被调用")

print("demo 加载完成")      # ← 顶层，会执行
```

```python
import demo
# 输出：
# 开始加载 demo
# demo 加载完成
```

**函数体内部的代码不会在 import 时执行**，只有在调用函数时才执行。

### import 做了哪 4 步

`import demo` 本质上等于：

1. **找到** `demo.py` 文件
2. **创建**一个模块对象
3. **执行** `demo.py` 里的所有顶层代码（产生变量、函数、类都挂到模块上）
4. **建立名字绑定**：`demo` 这个名字指向该模块对象

```python
# import demo 约等于：
module_obj = types.ModuleType("demo")
exec(open("demo.py").read(), module_obj.__dict__)
demo = module_obj
```

### 常见坑

```python
# bad.py
print("连接数据库")   # import 时就会执行！
data = load_big_file()  # import 时就会执行！
```

### 正确写法：`if __name__ == "__main__"`

```python
# demo.py
def main():
    print("执行主逻辑")

if __name__ == "__main__":
    main()
```

- **直接运行** `python demo.py` → `__name__ == "__main__"`，执行 `main()`
- **被 import** → `__name__ == "demo"`，不执行 `main()`

---

## 五、一句话总结

> **模块 = 一边运行文件，一边把产生的名字装进容器的命名空间。**
> 属性可以是任意对象，import 就是执行 + 收集。

---

## 六、示例：os 模块结构

```
os.py      →  主模块文件（frozen，编译进解释器）
             包含：getcwd(), mkdir(), remove() 等系统函数
             以及：name = 'nt', sep = '\\' 等常量

os.path    →  os 的一个属性，指向 ntpath.py（Windows 路径处理模块）
             在 Linux 上指向 posixpath.py
```

```python
import os
os.name        # 'nt'（变量）
os.sep         # '\\'（变量）
os.getcwd      # <built-in function>（函数）
os.path        # <module 'ntpath'>（子模块）
```
