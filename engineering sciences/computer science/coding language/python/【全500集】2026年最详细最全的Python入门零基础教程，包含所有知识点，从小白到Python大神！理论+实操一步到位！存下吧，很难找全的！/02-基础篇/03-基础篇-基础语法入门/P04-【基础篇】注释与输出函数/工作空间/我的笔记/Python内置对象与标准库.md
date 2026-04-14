# Python 内置对象与标准库

## 一、Python 对象的分类

```
Python 运行时
├── 内置对象（builtins 模块）
│   ├── 内置函数（function）
│   ├── 内置类型（type）
│   ├── 内置异常（exception class）
│   └── 内置常量（constant）
│
├── 标准库模块（Standard Library）
│   ├── os, sys, time, datetime, json, re, collections, itertools...
│   └── 需要 import 才能用
│
└── 第三方库 / 用户自定义
```

---

## 二、内置对象（builtins）

**不需要 import**，解释器启动就加载好了，直接用。

### 2.1 内置函数（19个最常用）

| 函数 | 说明 | 例子 |
|------|------|------|
| `print()` | 打印输出 | `print("hello")` |
| `len()` | 返回长度 | `len([1,2,3])` -> 3 |
| `type()` | 返回类型 | `type(1)` -> `<class 'int'>` |
| `isinstance()` | 判断类型 | `isinstance(1, int)` -> True |
| `input()` | 读取输入 | `input("请输入:")` |
| `open()` | 打开文件 | `open("a.txt", "r")` |
| `range()` | 生成序列 | `range(5)` -> 0~4 |
| `int()`, `str()`, `float()`, `list()`, `dict()`, `set()`, `tuple()` | 类型转换/构造 | `int("123")` -> 123 |
| `map()`, `filter()`, `zip()`, `enumerate()` | 迭代工具 | `map(int, ["1","2"])` |
| `sorted()`, `reversed()` | 排序/反转 | `sorted([3,1,2])` -> [1,2,3] |
| `min()`, `max()`, `sum()` | 聚合运算 | `sum([1,2,3])` -> 6 |
| `abs()`, `round()`, `pow()` | 数学运算 | `abs(-1)` -> 1 |
| `hex()`, `oct()`, `bin()` | 进制转换 | `hex(16)` -> '0x10' |
| `chr()`, `ord()` | 字符编码 | `ord('A')` -> 65 |
| `repr()`, `format()` | 字符串格式化 | `repr(1)` -> '1' |
| `dir()`, `vars()`, `globals()`, `locals()` | 查看命名空间 | `dir()` |
| `help()` | 显示帮助 | `help(print)` |
| `id()`, `hash()` | 对象标识/哈希 | `id(1)` |
| `callable()` | 判断是否可调用 | `callable(print)` -> True |
| `exec()`, `eval()`, `compile()` | 执行代码 | `eval("1+1")` -> 2 |

### 2.2 内置类型

| 类型 | 说明 | 例子 |
|------|------|------|
| `int` | 整数 | `type(1)` -> `int` |
| `float` | 浮点数 | `type(1.5)` -> `float` |
| `str` | 字符串 | `type("hi")` -> `str` |
| `bool` | 布尔 | `type(True)` -> `bool` |
| `list` | 列表 | `type([1,2])` -> `list` |
| `dict` | 字典 | `type({})` -> `dict` |
| `set` | 集合 | `type({1})` -> `set` |
| `tuple` | 元组 | `type((1,))` -> `tuple` |
| `bytes`, `bytearray` | 字节序列 | `b"hello"` |
| `complex` | 复数 | `complex(1,2)` |
| `frozenset` | 不可变集合 | `frozenset({1,2})` |
| `type` | 类型本身 | `type` 是所有类型的类型 |

### 2.3 内置异常（部分）

| 异常 | 说明 |
|------|------|
| `Exception` | 所有异常基类 |
| `ValueError` | 值错误 |
| `TypeError` | 类型错误 |
| `KeyError` | 字典键不存在 |
| `IndexError` | 索引超出范围 |
| `AttributeError` | 属性不存在 |
| `FileNotFoundError` | 文件不存在 |
| `ZeroDivisionError` | 除数为零 |
| `ImportError` | 导入失败 |
| `RuntimeError` | 运行时错误 |

### 2.4 内置常量

| 常量 | 说明 |
|------|------|
| `True` | 布尔真 |
| `False` | 布尔假 |
| `None` | 空值/不存在 |
| `NotImplemented` | 未实现（运算符等） |
| `Ellipsis` | 省略号 `...` |

---

## 三、标准库模块（需要 import）

Python 自带的大量模块，无需安装直接 `import` 就能用。

### 3.1 文件/路径操作

| 模块 | 说明 | 例子 |
|------|------|------|
| `os` | 操作系统功能 | `os.getcwd()`, `os.mkdir()` |
| `os.path` | 路径处理 | `os.path.join()`, `os.path.abspath()` |
| `pathlib` | 面向对象的路径 | `Path("a/b") / "c"` |
| `shutil` | 文件/目录操作 | `shutil.copy()`, `shutil.rmtree()` |
| `tempfile` | 临时文件 | `tempfile.mkdtemp()` |

### 3.2 数据类型

| 模块 | 说明 |
|------|------|
| `collections` | 扩展容器（namedtuple, deque, Counter 等） |
| `itertools` | 迭代器工具（count, chain, groupby 等） |
| `functools` | 函数式编程工具（lru_cache, partial 等） |
| `enum` | 枚举类型 |
| `dataclasses` | 数据类装饰器 |

### 3.3 文本/字符串

| 模块 | 说明 |
|------|------|
| `re` | 正则表达式 |
| `string` | 字符串常量和模板 |
| `textwrap` | 文本格式化 |
| `unicodedata` | Unicode 数据库 |

### 3.4 日期/时间

| 模块 | 说明 |
|------|------|
| `datetime` | 日期时间对象 |
| `time` | 时间操作 |
| `calendar` | 日历相关 |

### 3.5 数据格式/序列化

| 模块 | 说明 |
|------|------|
| `json` | JSON 编码/解码 |
| `csv` | CSV 文件读写 |
| `xml.etree.ElementTree` | XML 处理 |
| `pickle` | Python 对象序列化 |

### 3.6 数学/数字

| 模块 | 说明 |
|------|------|
| `math` | 数学函数（sin, cos, sqrt 等） |
| `random` | 随机数生成 |
| `statistics` | 统计函数 |
| `decimal` | 高精度小数 |
| `fractions` | 分数运算 |

### 3.7 网络/并发

| 模块 | 说明 |
|------|------|
| `urllib` | URL 处理和网络请求 |
| `socket` | 底层网络接口 |
| `threading` | 多线程 |
| `multiprocessing` | 多进程 |
| `asyncio` | 异步 IO |
| `concurrent.futures` | 并行计算 |

### 3.8 其他常用

| 模块 | 说明 |
|------|------|
| `sys` | Python 解释器信息（argv, path, version） |
| `argparse` | 命令行参数解析 |
| `logging` | 日志记录 |
| `inspect` | 获取对象信息 |
| `copy` | 对象拷贝（浅拷贝/深拷贝） |
| `weakref` | 弱引用 |
| `gc` | 垃圾回收控制 |

---

## 四、一句话总结

> **内置对象（builtins）**：解释器启动就加载好了，**不用 import**，直接用（`print`, `len`, `True`, `None` 等）
>
> **标准库模块**：解释器自带的模块，**需要 import** 才能用（`os`, `sys`, `json`, `re` 等）
