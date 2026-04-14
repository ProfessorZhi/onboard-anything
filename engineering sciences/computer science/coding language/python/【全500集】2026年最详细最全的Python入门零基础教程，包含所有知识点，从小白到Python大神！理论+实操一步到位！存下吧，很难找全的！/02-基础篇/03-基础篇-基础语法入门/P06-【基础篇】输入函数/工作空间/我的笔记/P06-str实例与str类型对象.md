# P06 str 实例与 str 类型对象

## 先把三层分清

```python
"abc"
str
type
```

- `"abc"` 是一个 `str` 实例对象
- `str` 是一个类型对象
- `type` 也是一个类型对象

验证：

```python
type("abc")   # <class 'str'>
type(str)     # <class 'type'>
type(type)    # <class 'type'>
```

## 这个点真正解决什么问题

帮你区分：

1. 某个具体字符串对象现在能做什么
2. 字符串这个类型本身定义了什么能力

所以：

```python
"abc".split()
```

不是“`abc` 自己天生带了一份 `split`”，而是：

- `"abc"` 是 `str` 的实例
- `split` 这套能力定义在 `str` 这个类型上
- `"abc"` 作为实例可以调用它

## 先纠正一个常见误区

“字符串属性只有函数吗？没有 `name` 吗？”

答案是：

- 对于 `str` 实例对象，常见可见成员几乎都是方法，比如 `split`、`upper`
- 像 `__class__` 这种属性也有，但入门阶段最常用的确实主要是方法
- `__name__` 这种“名字属性”不是字符串实例常用属性，而是 `str` 这种类型对象上的属性

也就是说：

```python
"abc".__class__    # 可以
str.__name__       # 可以
"abc".__name__     # 不成立
```

## 一、`str` 实例对象的常见成员

先准备一个对象：

```python
s = "abc def"
```

### 1. `split`

#### 作用

把一个字符串拆成多个子字符串。

#### 调用形式

```python
s.split(sep=None, maxsplit=-1)
```

更接近真实签名：

```python
split(self, /, sep=None, maxsplit=-1)
```

#### 参数

- `sep`
  - 分隔符
  - 默认是 `None`，表示按任意空白字符拆分
- `maxsplit`
  - 最多拆几次
  - 默认 `-1`，表示不限制

#### 返回值

返回一个新的 `list[str]`

#### 是否修改原对象

不修改原字符串对象。

字符串是不可变对象，`split()` 会返回新对象。

#### 示例

```python
"a b c".split()          # ['a', 'b', 'c']
"a,b,c".split(",")       # ['a', 'b', 'c']
"a b c".split(maxsplit=1) # ['a', 'b c']
```

### 2. `upper`

#### 作用

返回一个转成大写的新字符串。

#### 调用形式

```python
s.upper()
```

#### 参数

无

#### 返回值

返回新的 `str`

#### 是否修改原对象

不修改原对象

#### 示例

```python
"abc".upper()   # 'ABC'
```

### 3. `lower`

#### 作用

返回一个转成小写的新字符串。

#### 调用形式

```python
s.lower()
```

#### 参数

无

#### 返回值

返回新的 `str`

#### 是否修改原对象

不修改原对象

#### 示例

```python
"ABC".lower()   # 'abc'
```

### 4. `replace`

#### 作用

把字符串中的一部分替换成新内容。

#### 调用形式

```python
s.replace(old, new, count=-1)
```

更接近真实签名：

```python
replace(self, old, new, count=-1, /)
```

#### 参数

- `old`
  - 要被替换的旧子串
- `new`
  - 替换成的新子串
- `count`
  - 最多替换几次
  - 默认 `-1`，表示全替换

#### 返回值

返回新的 `str`

#### 是否修改原对象

不修改原对象

#### 示例

```python
"abcabc".replace("a", "x")      # 'xbcxbc'
"abcabc".replace("a", "x", 1)   # 'xbcabc'
```

### 5. `strip`

#### 作用

去掉字符串两端指定字符，默认去掉空白字符。

#### 调用形式

```python
s.strip(chars=None)
```

更接近真实签名：

```python
strip(self, chars=None, /)
```

#### 参数

- `chars`
  - 要去掉的字符集合
  - 默认 `None`，表示去空格、换行、制表符等空白字符

#### 返回值

返回新的 `str`

#### 是否修改原对象

不修改原对象

#### 示例

```python
"  abc  ".strip()      # 'abc'
"--abc--".strip("-")   # 'abc'
```

### 6. `find`

#### 作用

查找子串第一次出现的位置。

#### 调用形式

```python
s.find(sub[, start[, end]])
```

#### 参数

- `sub`
  - 要查找的子串
- `start`
  - 起始查找位置，可选
- `end`
  - 结束查找位置，可选

#### 返回值

返回 `int`

- 找到返回下标
- 找不到返回 `-1`

#### 是否修改原对象

不修改原对象

#### 示例

```python
"abc def".find("d")   # 4
"abc".find("x")       # -1
```

### 7. `startswith`

#### 作用

判断字符串是否以某个前缀开头。

#### 调用形式

```python
s.startswith(prefix[, start[, end]])
```

#### 参数

- `prefix`
  - 前缀内容
- `start`
  - 起始位置，可选
- `end`
  - 结束位置，可选

#### 返回值

返回 `bool`

#### 是否修改原对象

不修改原对象

#### 示例

```python
"python".startswith("py")   # True
```

### 8. `endswith`

#### 作用

判断字符串是否以某个后缀结尾。

#### 调用形式

```python
s.endswith(suffix[, start[, end]])
```

#### 参数

- `suffix`
  - 后缀内容
- `start`
  - 起始位置，可选
- `end`
  - 结束位置，可选

#### 返回值

返回 `bool`

#### 是否修改原对象

不修改原对象

#### 示例

```python
"note.md".endswith(".md")   # True
```

### 9. `__class__`

#### 作用

查看这个实例对象的类型。

#### 示例

```python
"abc".__class__   # <class 'str'>
```

#### 说明

这更接近“实例属性”，不是日常业务字符串处理方法，但它能帮助你理解对象模型。

## 二、`str` 类型对象本身的常见属性 / 方法

这里讨论的不是 `"abc"`，而是 `str` 本身。

### 1. `__name__`

#### 作用

类型名字。

#### 返回值

返回 `str`

#### 示例

```python
str.__name__   # 'str'
```

### 2. `__mro__`

#### 作用

方法解析顺序。

#### 返回值

返回一个 `tuple`

#### 示例

```python
str.__mro__
# (<class 'str'>, <class 'object'>)
```

#### 说明

它告诉你：`str` 最终继承自 `object`。

### 3. `__bases__`

#### 作用

直接父类。

#### 返回值

返回一个 `tuple`

#### 示例

```python
str.__bases__
# (<class 'object'>,)
```

### 4. `__doc__`

#### 作用

类型帮助文档。

#### 返回值

返回 `str`

#### 示例

```python
str.__doc__
```

### 5. `split`

#### 作用

这是定义在 `str` 类型上的方法定义，不是某个具体字符串实例的绑定方法。

#### 示例

```python
str.split
# <method 'split' of 'str' objects>
```

#### 说明

它和下面这个不是一回事：

```python
"abc".split
```

后者是“绑定到实例上的方法”。

### 6. `upper`

和 `split` 一样，也是定义在 `str` 上的方法定义。

```python
str.upper
```

### 7. `mro()`

#### 作用

以列表形式查看方法解析顺序。

#### 返回值

返回一个 `list[type]`

#### 示例

```python
str.mro()
# [<class 'str'>, <class 'object'>]
```

## 三、实例方法和类型属性到底怎么区分

看这组对比最清楚：

```python
s = "abc"

s.split        # 绑定到实例 s 的方法
str.split      # 定义在类型 str 上的方法

s.__class__    # s 的类型
str.__name__   # 类型对象自己的名字
```

一句话：

- `s.xxx` 更偏向“这个具体对象现在怎么用”
- `str.xxx` 更偏向“字符串这个类型本身定义了什么”

## 四、回到 `input().split()`

```python
input().split()
```

之所以能成立，是因为：

1. `input()` 返回一个 `str` 实例对象
2. 任何 `str` 实例对象都可以调用 `split()`
3. `split()` 不修改原字符串，而是返回一个新的 `list[str]`

所以它本质上等价于：

```python
text = input()
parts = text.split()
```

## 五、现在最值得记住的结论

1. `"abc"` 是实例对象，`str` 和 `type` 是类型对象。
2. `"abc"` 常见成员以方法为主，比如 `split`、`upper`。
3. `str` 自己也有属性，比如 `__name__`、`__mro__`、`__doc__`。
4. `split()` 返回新对象，不会原地修改原字符串。
5. `input().split()` 能成立，是因为 `input()` 返回的是 `str` 实例对象。
