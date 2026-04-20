# P06 str inventory 清单

## 这份清单怎么读

这份文档按 4 块来列：

1. 实例对象的方法
2. 实例对象的数据属性 / 元信息属性
3. 类型对象的方法
4. 类型对象的数据属性 / 元信息属性

这里的分类口径是学习口径，不是 CPython 最底层的严苛分类。  
目标是让你先看清：

- 当前实例最常用的能力是什么
- 类型对象自己带了哪些元信息
- 为什么 `str` 实例看起来“方法很多，普通数据属性很少”

## 一、str 实例对象

示例实例：

```python
s = "abc"
```

### 1. 最值得先看的实例方法

| 名称 | 更接近底层的定义视角 | 作用 | 返回值 | 是否修改原对象 |
|---|---|---|---|---|
| `split` | `str.split(self, /, sep=None, maxsplit=-1)` | 拆分字符串 | `list[str]` | 否 |
| `upper` | `str.upper(self, /)` | 转大写 | `str` | 否 |
| `lower` | `str.lower(self, /)` | 转小写 | `str` | 否 |
| `replace` | `str.replace(self, old, new, count=-1, /)` | 替换子串 | `str` | 否 |
| `strip` | `str.strip(self, chars=None, /)` | 去掉两端字符 | `str` | 否 |
| `find` | `str.find(self, sub, start=0, end=len(self), /)` | 查找位置，找不到返回 `-1` | `int` | 否 |
| `startswith` | `str.startswith(self, prefix, start=0, end=len(self), /)` | 判断前缀 | `bool` | 否 |
| `endswith` | `str.endswith(self, suffix, start=0, end=len(self), /)` | 判断后缀 | `bool` | 否 |
| `join` | `str.join(self, iterable, /)` | 连接字符串序列 | `str` | 否 |
| `format` | `str.format(self, *args, **kwargs)` | 格式化字符串 | `str` | 否 |

### 2. 实例对象的数据属性 / 元信息属性

| 名称 | 含义 | 例子 | 值类型 |
|---|---|---|---|
| `__class__` | 当前对象的类型 | `s.__class__` -> `<class 'str'>` | `type` |
| `__doc__` | 帮助文档字符串 | `s.__doc__` | `str` |
| `__hash__` | 哈希相关属性 | `s.__hash__` | 可调用对象或相关可访问结果 |

说明：

- `str` 实例这边，普通数据属性也不多。
- 这不等于 `str` “内部只有这么几个东西”，而是因为它不是靠一堆普通字段暴露内部状态。

### 3. 实例对象的全部方法清单

| 名称 | 说明 |
|---|---|
| `capitalize` | 首字母大写 |
| `casefold` | 更强的小写化 |
| `center` | 居中填充 |
| `count` | 统计子串次数 |
| `encode` | 编码成字节 |
| `endswith` | 判断后缀 |
| `expandtabs` | 展开制表符 |
| `find` | 查找子串位置 |
| `format` | 格式化 |
| `format_map` | 映射格式化 |
| `index` | 查找子串位置，找不到报错 |
| `isalnum` | 是否字母数字 |
| `isalpha` | 是否字母 |
| `isascii` | 是否 ASCII |
| `isdecimal` | 是否十进制字符 |
| `isdigit` | 是否数字字符 |
| `isidentifier` | 是否合法标识符 |
| `islower` | 是否全小写 |
| `isnumeric` | 是否数值字符 |
| `isprintable` | 是否可打印 |
| `isspace` | 是否空白字符 |
| `istitle` | 是否标题格式 |
| `isupper` | 是否全大写 |
| `join` | 连接字符串序列 |
| `ljust` | 左对齐填充 |
| `lower` | 转小写 |
| `lstrip` | 去左侧字符 |
| `partition` | 分成三段 |
| `removeprefix` | 去前缀 |
| `removesuffix` | 去后缀 |
| `replace` | 替换子串 |
| `rfind` | 从右查找 |
| `rindex` | 从右查找，找不到报错 |
| `rjust` | 右对齐填充 |
| `rpartition` | 从右分成三段 |
| `rsplit` | 从右拆分 |
| `rstrip` | 去右侧字符 |
| `split` | 拆分字符串 |
| `splitlines` | 按行拆分 |
| `startswith` | 判断前缀 |
| `strip` | 去两端字符 |
| `swapcase` | 大小写互换 |
| `title` | 转标题格式 |
| `translate` | 按映射翻译 |
| `upper` | 转大写 |
| `zfill` | 左侧补零 |
| `__add__` | 字符串相加 |
| `__contains__` | 成员测试 |
| `__eq__` | 相等比较 |
| `__format__` | 格式化 |
| `__getitem__` | 取字符 |
| `__hash__` | 哈希 |
| `__iter__` | 返回迭代器 |
| `__len__` | 返回长度 |
| `__mod__` | `%` 格式化 |
| `__mul__` | 重复字符串 |
| `__repr__` | 官方字符串表示 |
| `__rmod__` | 右侧 `%` |
| `__rmul__` | 右乘 |
| `__sizeof__` | 占用内存大小 |
| `__str__` | 普通字符串表示 |
| `__delattr__` | 删除属性 |
| `__dir__` | 列出成员 |
| `__ge__` | 大于等于比较 |
| `__getattribute__` | 获取属性 |
| `__getnewargs__` | 构造参数支持 |
| `__getstate__` | 状态提取 |
| `__gt__` | 大于比较 |
| `__init__` | 初始化 |
| `__init_subclass__` | 子类初始化钩子 |
| `__le__` | 小于等于比较 |
| `__lt__` | 小于比较 |
| `__ne__` | 不等比较 |
| `__new__` | 创建对象 |
| `__reduce__` | 序列化支持 |
| `__reduce_ex__` | 序列化支持 |
| `__setattr__` | 设置属性 |
| `__subclasshook__` | 子类判断钩子 |

### 4. 实例对象的全部数据属性 / 元信息属性清单

| 名称 | 说明 |
|---|---|
| `__class__` | 当前对象的类型 |
| `__doc__` | 文档字符串 |

## 二、str 类型对象

类型对象就是：

```python
str
```

### 1. 类型对象的方法

| 名称 | 签名/形式 | 作用 |
|---|---|---|
| `split` | `str.split(self, /, sep=None, maxsplit=-1)` | 定义拆分规则 |
| `upper` | `str.upper(self, /)` | 定义转大写规则 |
| `lower` | `str.lower(self, /)` | 定义转小写规则 |
| `replace` | `str.replace(self, old, new, count=-1, /)` | 定义替换规则 |
| `strip` | `str.strip(self, chars=None, /)` | 定义去两端规则 |
| `join` | `str.join(self, iterable, /)` | 定义连接规则 |
| `format` | `str.format(self, *args, **kwargs)` | 定义格式化规则 |
| `maketrans` | `str.maketrans(...)` | 构造翻译表 |
| `mro` | `str.mro()` | 查看继承链 |

### 2. 类型对象的数据属性 / 元信息属性

| 名称 | 含义 | 例子 | 值类型 |
|---|---|---|---|
| `__name__` | 类型名字 | `str.__name__` -> `'str'` | `str` |
| `__qualname__` | 限定名 | `str.__qualname__` | `str` |
| `__module__` | 所属模块 | `str.__module__` -> `'builtins'` | `str` |
| `__bases__` | 父类元组 | `str.__bases__` | `tuple` |
| `__mro__` | 方法解析顺序 | `str.__mro__` | `tuple` |
| `__dict__` | 类型对象自己的命名空间映射 | `str.__dict__` | `mappingproxy` |
| `__doc__` | 类型文档 | `str.__doc__` | `str` |
| `__hash__` | 哈希相关属性 | `str.__hash__` | 相关对象 |

### 3. 类型对象的全部方法清单

| 名称 | 说明 |
|---|---|
| `capitalize` | 定义首字母大写规则 |
| `casefold` | 定义强小写化规则 |
| `center` | 定义居中填充规则 |
| `count` | 定义统计规则 |
| `encode` | 定义编码规则 |
| `endswith` | 定义后缀判断规则 |
| `expandtabs` | 定义制表符展开规则 |
| `find` | 定义查找规则 |
| `format` | 定义格式化规则 |
| `format_map` | 定义映射格式化规则 |
| `index` | 定义查找规则 |
| `isalnum` | 定义判断规则 |
| `isalpha` | 定义判断规则 |
| `isascii` | 定义判断规则 |
| `isdecimal` | 定义判断规则 |
| `isdigit` | 定义判断规则 |
| `isidentifier` | 定义判断规则 |
| `islower` | 定义判断规则 |
| `isnumeric` | 定义判断规则 |
| `isprintable` | 定义判断规则 |
| `isspace` | 定义判断规则 |
| `istitle` | 定义判断规则 |
| `isupper` | 定义判断规则 |
| `join` | 定义连接规则 |
| `ljust` | 定义左对齐规则 |
| `lower` | 定义转小写规则 |
| `lstrip` | 定义去左侧规则 |
| `maketrans` | 构造翻译表 |
| `partition` | 定义三段拆分规则 |
| `removeprefix` | 定义去前缀规则 |
| `removesuffix` | 定义去后缀规则 |
| `replace` | 定义替换规则 |
| `rfind` | 定义从右查找规则 |
| `rindex` | 定义从右查找规则 |
| `rjust` | 定义右对齐规则 |
| `rpartition` | 定义从右三段拆分规则 |
| `rsplit` | 定义从右拆分规则 |
| `rstrip` | 定义去右侧规则 |
| `split` | 定义拆分规则 |
| `splitlines` | 定义按行拆分规则 |
| `startswith` | 定义前缀判断规则 |
| `strip` | 定义去两端规则 |
| `swapcase` | 定义大小写互换规则 |
| `title` | 定义标题格式规则 |
| `translate` | 定义翻译规则 |
| `upper` | 定义转大写规则 |
| `zfill` | 定义补零规则 |
| `mro` | 返回方法解析顺序 |
| `__add__` | 加法定义 |
| `__contains__` | 成员测试定义 |
| `__eq__` | 比较定义 |
| `__format__` | 格式化定义 |
| `__getitem__` | 取字符定义 |
| `__hash__` | 哈希定义 |
| `__iter__` | 迭代定义 |
| `__len__` | 长度定义 |
| `__mod__` | `%` 定义 |
| `__mul__` | 乘法定义 |
| `__repr__` | 字符串表示定义 |
| `__rmod__` | 右侧 `%` 定义 |
| `__rmul__` | 右乘定义 |
| `__sizeof__` | 内存大小定义 |
| `__str__` | 字符串表示定义 |
| `__delattr__` | 删除属性定义 |
| `__dir__` | 成员列举定义 |
| `__ge__` | 比较定义 |
| `__getattribute__` | 获取属性定义 |
| `__getnewargs__` | 构造参数支持 |
| `__getstate__` | 状态提取定义 |
| `__gt__` | 比较定义 |
| `__init__` | 初始化定义 |
| `__init_subclass__` | 子类初始化钩子 |
| `__le__` | 比较定义 |
| `__lt__` | 比较定义 |
| `__ne__` | 比较定义 |
| `__new__` | 创建对象定义 |
| `__reduce__` | 序列化支持 |
| `__reduce_ex__` | 序列化支持 |
| `__setattr__` | 设置属性定义 |
| `__subclasshook__` | 子类判断钩子 |

### 4. 类型对象的全部数据属性 / 元信息属性清单

| 名称 | 说明 |
|---|---|
| `__name__` | 类型名 |
| `__qualname__` | 限定名 |
| `__module__` | 所属模块 |
| `__bases__` | 父类元组 |
| `__mro__` | 方法解析顺序 |
| `__dict__` | 类型命名空间 |
| `__doc__` | 文档字符串 |

## 三、为什么你会觉得“实例对象只有两三个数据属性”

因为对很多内置类型来说：

- 核心状态存在更底层的内部结构里
- Python 不会把这些内部结构全部暴露成一堆普通字段
- 所以你会看到：方法很多，普通数据属性很少

这不等于“这个对象内部只有这么几个东西”，而是说明它不是靠一堆 `obj.name` 这种普通字段来表达自身状态。

## 四、最短记忆版

- 实例对象：更值得先看方法
- 类型对象：更值得先看元信息属性
- `self`：在实例方法里常常被隐含传入
