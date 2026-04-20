# P06 builtin function、method、type 的类型、签名、输入输出

## 这份笔记真正解决什么问题

你现在已经会看到这些名字：

```python
print
input
list.append
nums.append
str.split
s.split
int
```

但如果只知道“它们的完整签名”，还不够。

真正要搞清的是 4 件事：

1. 它是什么类型的对象
2. 它的完整签名是什么
3. 它通常吃什么类型的输入
4. 它通常返回什么类型的结果

## 一、先看最短分类

| 例子 | 它本质上是什么 | 常见 `type(...)` |
|---|---|---|
| `print` / `input` / `len` | 内置函数 | `builtin_function_or_method` |
| `list.append` / `str.split` | 类型对象上的方法定义 | `method_descriptor` |
| `nums.append` / `s.split` | 绑定到实例后的方法对象 | `builtin_function_or_method` |
| `int` / `list` / `str` | 类型对象 | `type` |

## 二、builtin function：内置函数

这里先看两个和本 P 最相关的：`input`、`print`。

### 1. `input`

| 项目 | 内容 |
|---|---|
| 对象名 | `input` |
| `type(...)` | `builtin_function_or_method` |
| 完整签名 | `input(prompt='', /)` |
| 输入什么 | 一个可选的提示文本，通常是 `str` |
| 输出什么 | 用户输入的一整行文本，类型总是 `str` |
| 最小例子 | `age = input("请输入年龄：")` |

说明：

- `input()` 的返回值默认永远是 `str`
- 即使用户输入的是 `18`，拿到的也是 `"18"`

例子：

```python
age = input("请输入年龄：")
print(age)        # 假设输入 18，这里打印 18
print(type(age))  # <class 'str'>
```

### 2. `print`

| 项目 | 内容 |
|---|---|
| 对象名 | `print` |
| `type(...)` | `builtin_function_or_method` |
| 完整签名 | `print(*args, sep=' ', end='\\n', file=None, flush=False)` |
| 输入什么 | 任意多个对象 |
| 输出什么 | 返回值是 `None`；副作用是把内容打印到终端 |
| 最小例子 | `print("hello", 123)` |

说明：

- `print` 真正“返回”的不是打印出来的文字
- 它的返回值是 `None`
- 真正有意义的是它的打印副作用

例子：

```python
result = print("hello")
print(result)   # None
```

### 3. `len`

| 项目 | 内容 |
|---|---|
| 对象名 | `len` |
| `type(...)` | `builtin_function_or_method` |
| 完整签名 | `len(obj, /)` |
| 输入什么 | 支持长度概念的对象，如 `str`、`list`、`tuple` |
| 输出什么 | `int` |
| 最小例子 | `len("abc")` |

例子：

```python
n = len("abc")
print(n)        # 3
print(type(n))  # <class 'int'>
```

## 三、method_descriptor：类型对象上的方法定义

这类东西常见于：

```python
list.append
str.split
dict.get
```

它们本质上是：

- 定义在类型对象上的方法成员
- 还没有绑定到具体实例

### 1. `list.append`

| 项目 | 内容 |
|---|---|
| 对象名 | `list.append` |
| `type(...)` | `method_descriptor` |
| 完整签名 | `(self, object, /)` |
| 输入什么 | 第一个参数 `self` 要是某个 `list` 实例；第二个参数可以是任意对象 |
| 输出什么 | `None` |
| 最小例子 | `list.append(nums, 4)` |

例子：

```python
nums = [1, 2, 3]
result = list.append(nums, 4)
print(nums)         # [1, 2, 3, 4]
print(result)       # None
print(type(result)) # <class 'NoneType'>
```

### 2. `str.split`

| 项目 | 内容 |
|---|---|
| 对象名 | `str.split` |
| `type(...)` | `method_descriptor` |
| 完整签名 | `(self, /, sep=None, maxsplit=-1)` |
| 输入什么 | `self` 要是某个 `str` 实例；`sep` 通常是 `str` 或 `None`；`maxsplit` 通常是 `int` |
| 输出什么 | `list[str]` |
| 最小例子 | `str.split("a b c")` |

例子：

```python
parts = str.split("a b c")
print(parts)         # ['a', 'b', 'c']
print(type(parts))   # <class 'list'>
```

### 3. `dict.get`

| 项目 | 内容 |
|---|---|
| 对象名 | `dict.get` |
| `type(...)` | `method_descriptor` |
| 完整签名 | `(self, key, default=None, /)` |
| 输入什么 | `self` 要是某个 `dict`；`key` 是键；`default` 可选 |
| 输出什么 | 对应的值，或者默认值 |
| 最小例子 | `dict.get(d, "x", 0)` |

例子：

```python
d = {"x": 1}
value = dict.get(d, "x", 0)
print(value)        # 1
print(type(value))  # <class 'int'>
```

## 四、绑定到实例后的方法对象

这类东西常见于：

```python
nums.append
s.split
d.get
```

它们常见的 `type(...)` 往往又会变成：

```python
builtin_function_or_method
```

原因是：

- 现在方法已经绑定到具体实例
- `self` 已经默认塞进去了

### 1. `nums.append`

| 项目 | 内容 |
|---|---|
| 对象名 | `nums.append` |
| `type(...)` | `builtin_function_or_method` |
| 完整签名 | `(object, /)` |
| 输入什么 | 任意对象 |
| 输出什么 | `None` |
| 最小例子 | `nums.append(4)` |

例子：

```python
nums = [1, 2, 3]
result = nums.append(4)
print(nums)         # [1, 2, 3, 4]
print(result)       # None
print(type(result)) # <class 'NoneType'>
```

### 2. `s.split`

| 项目 | 内容 |
|---|---|
| 对象名 | `s.split` |
| `type(...)` | `builtin_function_or_method` |
| 完整签名 | `(sep=None, maxsplit=-1)` |
| 输入什么 | `sep` 通常是 `str` 或 `None`；`maxsplit` 通常是 `int` |
| 输出什么 | `list[str]` |
| 最小例子 | `s.split()` |

例子：

```python
s = "a b c"
parts = s.split()
print(parts)         # ['a', 'b', 'c']
print(type(parts))   # <class 'list'>
```

### 3. `d.get`

| 项目 | 内容 |
|---|---|
| 对象名 | `d.get` |
| `type(...)` | `builtin_function_or_method` |
| 完整签名 | `(key, default=None, /)` |
| 输入什么 | `key` 和可选默认值 |
| 输出什么 | 对应的值，或者默认值 |
| 最小例子 | `d.get("x", 0)` |

例子：

```python
d = {"x": 1}
value = d.get("x", 0)
print(value)        # 1
print(type(value))  # <class 'int'>
```

## 五、type：类型对象本身

例如：

```python
int
float
list
str
map
```

它们本身不是“普通函数对象”。

它们本身是：

**类型对象**

所以：

```python
type(int)    # <class 'type'>
type(list)   # <class 'type'>
type(str)    # <class 'type'>
type(map)    # <class 'type'>
```

### 1. `int`

| 项目 | 内容 |
|---|---|
| 对象名 | `int` |
| `type(...)` | `type` |
| 完整签名 | 某些环境里不容易稳定取到 |
| 输入什么 | 常见是字符串、数字 |
| 输出什么 | `int` 对象 |
| 最小例子 | `int("123")` |

例子：

```python
x = int("123")
print(x)            # 123
print(type(x))      # <class 'int'>
```

### 2. `float`

| 项目 | 内容 |
|---|---|
| 对象名 | `float` |
| `type(...)` | `type` |
| 完整签名 | `(x=0, /)` |
| 输入什么 | 常见是数字或像数字的字符串 |
| 输出什么 | `float` 对象 |
| 最小例子 | `float("3.14")` |

例子：

```python
x = float("3.14")
print(x)            # 3.14
print(type(x))      # <class 'float'>
```

### 3. `map`

| 项目 | 内容 |
|---|---|
| 对象名 | `map` |
| `type(...)` | `type` |
| 完整签名 | 对 `map` 类型本身常常直接取不到 |
| 输入什么 | 一个函数 + 一个或多个可迭代对象 |
| 输出什么 | `map` 对象 |
| 最小例子 | `map(int, ["1", "2"])` |

例子：

```python
m = map(int, ["1", "2"])
print(m)            # 一个 map 对象
print(type(m))      # <class 'map'>
print(list(m))      # [1, 2]
```

## 六、最短对照表

| 例子 | 它是什么 | 常见 `type(...)` | 常见输入 | 常见输出 |
|---|---|---|---|---|
| `input` | 内置函数 | `builtin_function_or_method` | 提示文本 `str` | `str` |
| `print` | 内置函数 | `builtin_function_or_method` | 任意对象 | `None` |
| `len` | 内置函数 | `builtin_function_or_method` | 可求长度对象 | `int` |
| `list.append` | 类型对象上的方法定义 | `method_descriptor` | `list` 实例 + 任意对象 | `None` |
| `str.split` | 类型对象上的方法定义 | `method_descriptor` | `str` 实例 + 可选分隔符 | `list[str]` |
| `dict.get` | 类型对象上的方法定义 | `method_descriptor` | `dict` 实例 + key | 任意值 |
| `nums.append` | 绑定到实例后的方法对象 | `builtin_function_or_method` | 任意对象 | `None` |
| `s.split` | 绑定到实例后的方法对象 | `builtin_function_or_method` | 可选分隔符 | `list[str]` |
| `d.get` | 绑定到实例后的方法对象 | `builtin_function_or_method` | key + 可选默认值 | 任意值 |
| `int` | 类型对象 | `type` | 数字或字符串 | `int` |
| `float` | 类型对象 | `type` | 数字或字符串 | `float` |
| `map` | 类型对象 | `type` | 函数 + 可迭代对象 | `map` 对象 |

## 七、最容易错的点

### 1. `builtin_function_or_method` 不只等于 `print`

它也常出现在：

```python
nums.append
s.split
d.get
```

也就是：

**绑定到实例后的内置方法对象。**

### 2. `list.append` 和 `nums.append` 不是同一种对象

- `list.append`：`method_descriptor`
- `nums.append`：`builtin_function_or_method`

### 3. `int`、`list`、`str`、`map` 不是普通函数

它们是：

**类型对象**

只是类型对象也可以被调用，所以看起来有点像函数。

## 八、你现在最该记住什么

1. 只看“完整签名”还不够，还要看它是什么类型的对象。
2. 还要看它通常吃什么输入、返回什么输出。
3. `input()` 默认返回 `str`，这是 P06 主线里最重要的一条。
4. `list.append` 和 `nums.append` 的签名不同，本质是因为一个没绑定实例，一个已经绑定了实例。
