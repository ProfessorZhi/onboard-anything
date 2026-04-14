# type() 与 Python 对象模型（完整版）

## Python vs Java/C++：本质差别

### Java/C++ 的分层

```
基本类型（int等） ≠ 对象
类 ≠ 对象
类 = 蓝图，对象 = 根据蓝图 new 出来的
```

类不是对象，基本类型是原始值。

### Python 的统一模型

**一切皆对象，没有例外。**

```
值是对象
类是对象
创建类的机制本身也是对象（type）
```

## 三层概念（必须彻底分开）

```python
int     # 类对象
1       # 由 int 创建出来的实例对象
x       # 指向 1 的名字（不是对象本身）
```

- `1` 是 `int` 的实例
- `x` 不是实例，`x` 是名字，绑定到实例

## type 和 type() 不是一回事

```python
type      # 造类的机器（元类），本身是一个类对象
type()    # 调用 type，返回某个对象的类型
type(x)   # 查看 x 属于哪个类
```

## type(x) 到底看的是什么

> `type(x)` 看的是：x 是哪个类的实例

```python
type(1) is int        # True  → 1 是 int 的实例
type(int) is type      # True  → int 是 type 的实例
type(type) is type     # True  → type 是自己的实例
```

## 三条完全不同的关系（核心，不能混）

### 实例关系（谁造的，用 type() 查看）

```python
1       → int      ← 1 是 int 的实例
[]      → list     ← [] 是 list 的实例
int     → type     ← int 是 type 的实例
type    → type     ← type 是自己的实例
object  → type     ← object 是 type 的实例
```

### 继承关系（谁继承谁，用 issubclass() 查看）

```python
int   → object   ← int 继承 object
type  → object   ← type 继承 object
```

### 名字绑定（名字指向谁）

```python
x = 1
# x → 1
```

## 最容易搞错的三个结论

### 结论 1：不是所有对象都是 type 的实例

```python
isinstance(int, type)      # True  ← 类对象是 type 的实例
isinstance(1, type)        # False ← 普通值不是 type 的实例
isinstance([], type)        # False
```

### 结论 2：不是所有对象都是 object 的子类

```python
issubclass(1, object)      # TypeError  ← 对象不能谈子类
isinstance(1, object)       # True     ← 1 是 object 的实例
issubclass(int, object)    # True     ← int 是 object 的子类
```

### 结论 3：实例关系不能传递

```python
1 → int → type   ← 不能推出 1 → type
isinstance(1, type)        # False
```

## 分层结构（记住这张图）

```
┌─────────────────────────────────────┐
│ 普通对象层                           │
│  1       是 int  的实例             │
│  []      是 list 的实例             │
│  "abc"   是 str  的实例             │
└─────────────────────────────────────┘
          ↑
          │ type()
          │
┌─────────────────────────────────────┐
│ 类对象层                            │
│  int     是 type 的实例             │
│  list    是 type 的实例             │
│  object  是 type 的实例             │
│  type    是 type 的实例（自己）      │
└─────────────────────────────────────┘
          ↑
          │ issubclass()
          │
┌─────────────────────────────────────┐
│ 继承层                              │
│  int    继承 object                 │
│  type   继承 object                 │
└─────────────────────────────────────┘
```

## object 和 type 各解决什么问题

### object 解决"大家继承谁"的问题

> object 是继承体系的根

```python
issubclass(int, object)   # True
issubclass(type, object)  # True
```

### type 解决"类是谁的实例"的问题

> type 是造类体系的根

```python
type(int) is type    # True
type(object) is type # True
```

## 自举闭环（五句一起看就通了）

```python
type(1) is int              # 1 是 int 的实例
type(int) is type            # int 是 type 的实例
type(object) is type         # object 是 type 的实例
type(type) is type           # type 是自己的实例
issubclass(type, object)    # type 继承 object
```

### 为什么 type 既像造物主，又像普通对象

Python 需要同时满足两件事：

1. **所有对象都要有类型** → 落到 type
2. **所有普通类都要有共同祖先** → 落到 object

于是：
- `type` 继承 `object` → `type` 是普通对象
- `type` 是自己的实例 → 造类机器能自己造自己
- `object` 的类型是 `type` → `object` 也是"类"的实例

## 三个必须记住的事实

```
object.__bases__ = ()              ← 万物起源，没有父类
type.__bases__ = (object,)         ← type 继承 object
isinstance(任何类, type) = True   ← 所有类都是 type 的实例
```

## 最准确的判断表

### 实例关系（type() 查看）

| 说法 | 对错 | 说明 |
|------|------|------|
| `1` 是 `int` 的实例 | ✓ | |
| `1` 是 `type` 的实例 | ✗ | 普通值不是 type 的实例 |
| `int` 是 `type` 的实例 | ✓ | 类是 type 的实例 |
| `object` 是 `type` 的实例 | ✓ | |
| `type` 是 `type` 的实例 | ✓ | 自己造自己 |

### 继承关系（issubclass() 查看）

| 说法 | 对错 | 说明 |
|------|------|------|
| `int` 是 `object` 的子类 | ✓ | |
| `type` 是 `object` 的子类 | ✓ | |
| `1` 是 `object` 的子类 | ✗ | 对象不能是子类 |
| `int` 是 `type` 的子类 | ✗ | int 不继承 type |

## 名字绑定 vs 原地修改（核心区别）

### 重新绑定：x = [1]

```python
x = []          # x 绑定到 []
y = x           # y 也绑定到同一个 []
x = [1]         # x 改绑到新对象 [1]

# 结果：
x → [1]
y → []          ← y 没变，因为绑的是原来的对象
```

### 原地修改：x.append(1)

```python
x = []          # x 绑定到 []
y = x           # y 也绑定到同一个 []
x.append(1)   # 修改 x 当前指向的对象本身

# 结果：
x → [1] ← y 也指向同一个对象，所以也看到 [1]
y → [1]
```

## += vs + 的坑

```python
a = [1, 2]
b = a
b += [3]        # 原地修改（extend），b 仍指向同一个对象

a = [1, 2]
b = a
b = b + [3]    # 创建新列表（concat），b 换绑，a 不变
```

## 一句话

**Python 一切皆对象；类是 type 的实例，对象是类的实例，名字只是指向对象的标签；object 解决继承谁的问题，type 解决类是谁的实例的问题；赋值改绑定，方法调用改对象本身。**

---

## 类对象的属性（类对象自己的属性）

> 类本身也是对象，所以类对象自己也有属性

### 哪些是类对象的属性

```python
# 类对象的属性（不是实例的属性）
int.__name__      # 'int'          ← 类自己的名字
int.__bases__     # (<class 'object'>,)  ← 类的父类
int.__doc__       # '...'          ← 类的文档

# 普通对象的属性（由类定义的）
(1).__class__     # <class 'int'>  ← 对象指向它属于的类
(1).real          # 1              ← 类给实例定义的属性
```

### `type(os).__name__` 拆解

```python
import os

type(os)           # → <class 'module'>   ← os 是 module 这个类对象的实例
type(os).__name__  # → 'module'            ← 类对象的属性：类的名字
```

### 所有类对象都有这些属性

```python
int.__name__       # 'int'
str.__name__       # 'str'
list.__name__      # 'list'
type.__name__      # 'type'
object.__name__    # 'object'
```

### 普通对象也有属性（但通常是类定义的）

```python
(1).real          # 1
(1).imag          # 0
(1).__class__     # <class 'int'>
"abc".upper       # <built-in method upper>
```

**结论：一切对象都有属性。类对象的属性是 `__name__`、`__bases__` 等元信息；普通对象的属性是类赋予的。**
