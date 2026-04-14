# Python 常见对象分类表

## 总表

| 你看到的东西 | 它是什么 | 它是谁的实例 |
|---|---|---|
| `1` | 整数对象 | `int` |
| `3.14` | 浮点对象 | `float` |
| `True` | 布尔对象 | `bool` |
| `"abc"` | 字符串对象 | `str` |
| `[1,2]` | 列表对象 | `list` |
| `(1,2)` | 元组对象 | `tuple` |
| `{"a":1}` | 字典对象 | `dict` |
| `{1,2}` | 集合对象 | `set` |
| `None` | 特殊单例对象 | `NoneType` |
| `int` | 类对象 | `type` |
| `str` | 类对象 | `type` |
| `list` | 类对象 | `type` |
| `dict` | 类对象 | `type` |
| `str` | 类对象 | `type` |
| `type` | 类对象 | `type` |
| `object` | 类对象 | `type` |
| `os` | 模块对象 | `module` |
| `len` | 内建函数对象 | 内建函数类型 |
| `print` | 内建函数对象 | 内建函数类型 |
| `def f`（你自己写的函数） | 函数对象 | `function` |
| `A`（你自己写的类） | 类对象 | `type` |
| `A()` | 实例对象 | `A` |

## 按类别分

### 1）类对象（最重要，能创建别的对象）

```python
# 两个特殊类对象：
object   ← 继承体系根，所有类的最终父类
type     ← 造类机器，元类，所有类对象的类型

# 普通类对象：
int
str
list
dict
set
tuple
```

* 它们本身是对象
* 它们通常是 `type` 的实例
* 它们可以拿来创建别的对象

```python
type(int) is type
type(list) is type
type(object) is type
```

### 2）基础值对象

```python
1           → int
3.14        → float
True        → bool
"hello"     → str
b"abc"      → bytes
None         → NoneType
```

### 3）容器对象

```python
[1, 2, 3]  → list
(1, 2, 3)  → tuple
{"a": 1}    → dict
{1, 2, 3}  → set
range(10)   → range
```

这些都是具体对象，不是类。

### 4）实例对象

```python
class Dog:
    pass

d = Dog()
# Dog 是类对象
# d 是实例对象
# type(d) is Dog
```

### 5）函数对象

```python
def add(x, y):
    return x + y

f = add
# add 是函数对象
# f 也绑到同一个函数对象
```

### 6）内建函数对象

```python
len
print
open
type
```

### 7）模块对象

```python
import os
import sys
import math
```

* `os` 是模块对象
* `sys` 是模块对象
* `math` 是模块对象

模块是一个打包好的命名空间，里面装着函数、类、常量。

**模块的三层关系：**

```python
os      → module 的实例
module  → 类对象，type 的实例
type    → 类对象，module 的类型

type(os)      → module
type(module)  → type
type(type)    → type

isinstance(os, object)     → True
isinstance(module, type)  → True
```

### 8）方法对象

```python
s = "abc"
s.upper
# upper 是绑定方法对象

lst = []
lst.append
# append 也是绑定方法对象
```

方法对象和普通函数的区别：它已经绑到了某个具体对象上，所以 `lst.append(1)` 不需要再传 `lst`。

### 9）文件对象

```python
f = open("a.txt")
# f 是文件对象
# f.read(), f.write(), f.close()
```

### 10）迭代器 / 生成器对象

```python
it = iter([1, 2, 3])
# it 是迭代器对象

def gen():
    yield 1

g = gen()
# g 是生成器对象
```

## 一眼看上去像"类对象"的

通常是这种名字：

```python
int, str, list, dict, Dog, type, object
```

特点：能拿来 `()` 创建实例，`type(它)` 往往是 `type`。

## 一眼看上去像"实例对象"的

通常是这种：

```python
1, "abc", [1,2], {"a":1}, Dog(), open("a.txt"), os
```

特点：运行时具体东西，`type(它)` 是某个普通类。

## 最常见的"类 → 对象"例子

```
int      → 1, 2, 100
str      → "a", "hello"
list     → [], [1,2]
dict     → {}, {"a":1}
tuple    → (), (1,2)
set      → {1,2}
bool     → True, False
Dog      → Dog()
module   → os, sys, math
function → 你自己 def 出来的函数
```

## 最实用的判断法

看见一个东西，只问两句：

1. `type(x)` 是什么？ → 它属于哪一类
2. 它能拿来创建别的对象吗？ → 它是不是类对象

```
能 new 对象   → 类对象   → type(它) is type
不能 new 对象 → 普通对象 → type(它) is 某个普通类
```

## 套公式

```
type(1)        → int
type(int)       → type
type(os)        → module
type(module)    → type
type(Dog())     → Dog
type(Dog)       → type
type(type)      → type
```

**任何具体东西先问 `type(x)`；如果 `x` 本身又是类，再问 `type(type(x))`。**
