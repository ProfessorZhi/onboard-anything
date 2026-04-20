# P06 str 实例对象与 str 类型对象

## 先把三层分清

```python
"abc"
str
type
```

- `"abc"`：`str` 的实例对象
- `str`：类型对象
- `type`：类型的类型，也是类型对象

验证：

```python
type("abc")   # <class 'str'>
type(str)     # <class 'type'>
type(type)    # <class 'type'>
```

## 这页真正想解决什么

很多人一开始会把下面几件事混在一起：

- `"abc".split`
- `str.split`
- `"abc".__doc__`
- `str.__doc__`
- “为什么字符串实例上方法特别多，但普通数据属性很少”

这页就是把这些点一次分清。

## 最关键的本质

`"abc".split()` 能成立，不是因为 `"abc"` 自己天生单独带了一份 `split`，而是因为：

- `"abc"` 是 `str` 的实例
- `split` 这套能力定义在 `str` 这个类型对象上
- 实例对象可以通过自己的类型去使用这些方法

一句话：

**实例对象负责“当前这个对象是什么”，类型对象负责“这一类对象有哪些能力”。**

## 再补一个特别容易混的点：实例方法隐含了 `self`

当你写：

```python
"a b".split(" ")
```

表面上你只传了一个参数 `" "`，但更接近底层的写法是：

```python
str.split("a b", " ")
```

所以要把两层分开：

- `str.split(self, /, sep=None, maxsplit=-1)`：类型对象上的方法定义视角
- `"a b".split(" ")`：实例对象上的绑定方法视角

一句话记忆：

**实例方法不是没有 `self`，而是 `self` 已经默认绑定到当前对象了。**

## 术语规范

- `attribute`：属性，总称
- `method`：方法，可调用属性
- `data attribute`：数据属性，不可调用属性
- `instance attribute`：实例属性
- `type attribute` / `class attribute`：类型对象属性

“属性方法”“属性变量”这种说法能懂，但不算最规范。更规范的是：

- 方法
- 数据属性

## 一个容易带偏你的坑：不要只按 `callable(...)` 粗分

如果你只是简单按：

- 可调用 -> 方法
- 不可调用 -> 数据属性

去分，结果也会有点失真。

原因是 Python 内置类型里还会出现很多特殊成员，比如：

- `wrapper_descriptor`
- `method_descriptor`
- `builtin_function_or_method`
- 各种双下划线成员

所以这页的目标不是做“绝对严苛的底层对象分类”，而是做对学习最有帮助的区分：

1. 当前实例最常用的能力是什么
2. 类型对象本身带了哪些元信息
3. 为什么实例上看起来“数据属性少、方法多”

## 一、str 实例对象

先准备一个实例：

```python
s = "abc def"
```

### 1. 实例方法

| 名称 | 更接近底层的定义视角 | 作用 | 返回值 | 是否修改原对象 |
|------|----------------------|------|--------|----------------|
| `split` | `str.split(self, /, sep=None, maxsplit=-1)` | 拆分字符串 | `list[str]` | 否 |
| `upper` | `str.upper(self, /)` | 转大写 | `str` | 否 |
| `lower` | `str.lower(self, /)` | 转小写 | `str` | 否 |
| `replace` | `str.replace(self, old, new, count=-1, /)` | 替换子串 | `str` | 否 |
| `strip` | `str.strip(self, chars=None, /)` | 去掉两端字符 | `str` | 否 |
| `find` | `str.find(self, sub, start=0, end=len(self), /)` | 查找位置，找不到返回 `-1` | `int` | 否 |
| `startswith` | `str.startswith(self, prefix, start=0, end=len(self), /)` | 判断前缀 | `bool` | 否 |
| `endswith` | `str.endswith(self, suffix, start=0, end=len(self), /)` | 判断后缀 | `bool` | 否 |

说明：

- 平时常写成 `s.split()`、`s.upper()`。
- 你在实例上看到的签名经常不显示 `self`，因为 `self` 已经默认绑定到 `s` 了。
- `str` 是不可变对象，所以这些常见方法几乎都是“返回新字符串”，不是原地修改。

### 2. 实例数据属性

| 名称 | 含义 | 例子 | 值类型 |
|------|------|------|--------|
| `__class__` | 当前对象的类型 | `s.__class__` -> `<class 'str'>` | `type` |
| `__doc__` | 帮助文档字符串 | `s.__doc__` | `str` |
| `__hash__` | 哈希相关属性 | `s.__hash__` | 可调用对象或相关可访问结果 |

说明：

- `str` 实例能访问 `__doc__`。
- 但入门阶段最常用的仍然是方法，不是这些数据模型属性。
- `str` 实例这边，真正“显眼的普通数据属性”同样不多。

### 3. 为什么 `str` 实例的数据属性看起来也不多

因为 `str` 是内置不可变对象：

- 核心状态主要是“字符内容”
- 这些内容存在更底层的内部结构里
- Python 没有把它们全部暴露成很多普通字段

所以你看到的现象是：

- 方法很多
- 普通数据属性少

## 二、str 类型对象

### 1. 类型对象方法

| 名称 | 签名/形式 | 作用 |
|------|-----------|------|
| `split` | `str.split(self, /, sep=None, maxsplit=-1)` | 定义拆分规则 |
| `upper` | `str.upper(self, /)` | 定义转大写规则 |
| `lower` | `str.lower(self, /)` | 定义转小写规则 |
| `replace` | `str.replace(self, old, new, count=-1, /)` | 定义替换规则 |
| `strip` | `str.strip(self, chars=None, /)` | 定义去两端规则 |
| `maketrans` | `str.maketrans(...)` | 构造翻译表 |
| `mro` | `str.mro()` | 查看继承链 |

说明：

- 这里看到的是类型对象上的方法定义，所以通常会把 `self` 写出来。
- `str.split` 和 `"abc".split` 不是两回事：
  - 前者偏“定义视角”
  - 后者偏“绑定后调用视角”

### 2. 类型对象数据属性

| 名称 | 含义 | 例子 | 值类型 |
|------|------|------|--------|
| `__name__` | 类型名字 | `str.__name__` -> `'str'` | `str` |
| `__qualname__` | 限定名 | `str.__qualname__` | `str` |
| `__module__` | 所属模块 | `str.__module__` -> `'builtins'` | `str` |
| `__bases__` | 父类元组 | `str.__bases__` | `tuple` |
| `__mro__` | 方法解析顺序 | `str.__mro__` | `tuple` |
| `__dict__` | 类型对象自己的命名空间映射 | `str.__dict__` | `mappingproxy` |
| `__doc__` | 类型文档 | `str.__doc__` | `str` |

说明：

- `str` 类型对象这一层，数据属性明显比实例对象多。
- 这些属性大多属于“元信息”，也就是描述这个类型自己是什么、从哪里来、怎么继承。

## 三、实例对象和类型对象的成员个数一定一样吗

不一定。

你在 `str`、`list` 这类内置类型上，可能会看到实例和类型对象的成员数量很接近，甚至某些清单里一样。

但本质上：

- 实例对象看的是“当前这个对象能访问到什么”
- 类型对象看的是“这个类型自己身上定义了什么”

实例对象很多成员，其实是沿着自己的类型去找到的，不等于实例自己单独存了一份。

## 四、最短对照

### 1. 实例对象 vs 类型对象

```python
"abc"        # 实例对象
str          # 类型对象
```

### 2. 绑定方法 vs 类型上的方法

```python
"a b".split      # 绑定到具体实例上的方法
str.split        # 定义在类型对象上的方法
```

### 3. 隐含的 `self`

```python
str.split("a b", " ")
"a b".split(" ")
```

这两句本质上在做同一件事。

## 五、这一页真正要记住什么

1. `"abc"` 是实例对象，`str` 是类型对象。
2. 实例对象的方法能力来自类型对象。
3. 实例方法看起来不写 `self`，其实只是 `self` 已经默认绑定。
4. `str` 实例的数据属性看起来少，不是因为它“没东西”，而是因为内置不可变对象不靠一堆普通字段暴露内部状态。
5. `str` 类型对象这一层，元信息数据属性明显更多，比如 `__name__`、`__module__`、`__bases__`、`__mro__`、`__dict__`。
