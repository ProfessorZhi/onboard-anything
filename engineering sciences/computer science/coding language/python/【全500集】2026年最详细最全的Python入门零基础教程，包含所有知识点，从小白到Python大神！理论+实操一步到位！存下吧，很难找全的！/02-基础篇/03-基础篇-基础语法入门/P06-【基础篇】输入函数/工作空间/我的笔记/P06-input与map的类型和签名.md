# P06 input 与 map 的类型、签名和结果

## 这份笔记真正解决什么问题

很多人会把 `input` 和 `map` 都笼统地叫成“函数”，但它们其实不是同一类对象。

这份笔记只解决 4 件事：

1. `input` 到底是什么类型的对象
2. `input` 的完整签名是什么
3. `map` 到底是什么类型的对象
4. `map(...)` 创建出来的到底是什么，以及打印结果长什么样

## 一、先给结论

### 1. `input`

```python
type(input)
```

结果：

```python
<class 'builtin_function_or_method'>
```

`input` 的完整签名：

```python
input(prompt='', /)
```

这说明：

- `input` 是内置函数
- 它有一个参数 `prompt`
- `prompt` 有默认值 `''`
- `prompt` 是仅位置参数，因为它在 `/` 前面

### 2. `map`

```python
type(map)
```

结果：

```python
<class 'type'>
```

这说明：

- `map` 本身不是普通内置函数对象
- `map` 本身是一个类型对象
- 你写 `map(...)` 时，本质上是在调用这个类型对象，创建一个 `map` 对象

一句话：

- `input`：内置函数
- `map`：内置类型对象

## 二、`input` 的完整签名怎么读

```python
input(prompt='', /)
```

可以拆成：

- `prompt`：提示信息
- `=''`：默认值是空字符串
- `/`：前面的参数只能按位置传

所以正确写法：

```python
input("请输入年龄：")
input()
```

在你现在这条学习线上，最重要的是记住：

**`input()` 默认返回 `str`。**

例如：

```python
age = input("请输入年龄：")
```

如果用户输入 `18`，那么：

- `age` 的值是 `"18"`
- `age` 的类型是 `str`

## 三、`input` 的常见用法

### 1. 接收普通文本

```python
name = input("请输入名字：")
print(name)
```

### 2. 接收整数，再转类型

```python
age = int(input("请输入年龄："))
print(age + 1)
```

### 3. 一次输入一行，再自己拆分

```python
a, b = input("请输入两个整数，用空格分隔：").split()
```

注意：

- `split()` 后的 `a`、`b` 仍然是字符串
- 要计算还要继续转类型

## 四、`map` 到底是什么

`map` 本身是一个类型对象。

你可以先这样理解：

```python
map(int, ["1", "2", "3"])
```

意思不是“`map` 这个函数神奇地替你做事”，而是：

- 你调用了 `map` 这个类型对象
- 它创建了一个 `map` 对象
- 这个 `map` 对象会把 `int` 依次作用到后面的可迭代对象上

### 这算不算构造函数式调用

可以先这样帮助自己理解：

- `map(...)` 很像“构造出一个 map 对象”

但更规范地说：

- `map` 是内置类型对象
- `map(...)` 是在调用这个类型对象创建实例

不建议把它直接等同于 `__init__`，因为 Python 里“创建对象”和“初始化对象”底层还会区分 `__new__` 和 `__init__`。

一句话：

**`map(...)` 可以先理解成“构造出一个 map 对象”，但更规范地说，是“调用 map 这个类型对象创建实例”。**

## 五、`map(...)` 打印出来到底是什么

例如：

```python
m = map(int, ["1", "2", "3"])
print(m)
print(type(m))
print(list(m))
```

更完整地理解：

### 1. `print(m)`

输出类似：

```python
<map object at 0x00000123456789AB>
```

说明：

- 这是一个 `map` 对象
- 后面的十六进制地址每次运行都可能不同
- 所以你不该死记地址，只要知道“它打印出来像 `<map object at 0x...>`”

### 2. `print(type(m))`

输出：

```python
<class 'map'>
```

说明：

- `map(...)` 创建出来的结果，类型是 `map`

### 3. `print(list(m))`

输出：

```python
[1, 2, 3]
```

说明：

- `map` 对象里保存的是“把函数依次作用后的结果流”
- 用 `list(...)` 把它真正展开，就能看到具体结果

## 六、`map` 的常见用法

### 1. 和 `list()` 一起看结果

```python
nums = map(int, ["1", "2", "3"])
print(nums)         # <map object at 0x...>
print(type(nums))   # <class 'map'>
print(list(nums))   # [1, 2, 3]
```

### 2. 和 `input().split()` 搭配

```python
a, b = map(int, input().split())
print(a + b)
```

### 3. 批量转小数

```python
x, y = map(float, input().split())
print(x + y)
```

## 七、为什么 `map` 常和 `input()` 放在一起

因为这是一种很常见的“输入后批量转类型”写法：

```python
a, b = map(int, input().split())
```

这句可以拆成 4 步：

1. `input()` 读取一整行文本
2. `split()` 把一整行拆成多个字符串
3. `map(int, ...)` 把每个字符串转成整数
4. 最后把结果分别赋值给 `a`、`b`

例如用户输入：

```python
3 5
```

那么流程是：

```python
input()            -> "3 5"
split()            -> ["3", "5"]
map(int, ...)      -> 创建一个 map 对象
展开后            -> 依次得到 3 和 5
a, b = ...         -> a = 3, b = 5
```

## 八、最容易混的点

### 1. `input` 和 `map` 不都是 `builtin_function_or_method`

不是。

更准确地说：

- `input` 是 `builtin_function_or_method`
- `map` 是 `type`

### 2. `map` 不直接返回列表

例如：

```python
m = map(int, ["1", "2"])
```

这里 `m` 不是列表，而是一个 `map` 对象。

通常要这样看得更清楚：

```python
list(m)
```

### 3. `a, b = map(int, input().split())` 不是 `input` 自己会返回两个整数

真正发生的是：

- `input()` 还是先返回一个字符串
- 多个整数是后面的 `split()` 和 `map(int, ...)` 帮你处理出来的

## 九、最短对照表

| 名字 | `type(...)` | 完整签名 | 它本质上是什么 | 典型结果 |
|---|---|---|---|---|
| `input` | `builtin_function_or_method` | `input(prompt='', /)` | 内置函数 | `input()` 返回 `str` |
| `map` | `type` | 对 `map` 类型本身常常直接取不到签名 | 内置类型对象 | `map(...)` 返回 `map` 对象 |

## 十、你现在最该记住什么

1. `input` 是内置函数，完整签名是 `input(prompt='', /)`。
2. `input()` 默认返回 `str`。
3. `map` 本身不是普通函数对象，而是一个类型对象。
4. `map(...)` 可以先理解成“构造出一个 map 对象”，更规范地说是“调用 map 这个类型对象创建实例”。
5. `print(m)` 会打印出类似 `<map object at 0x...>` 的结果，`list(m)` 才会把结果真正展开出来。
