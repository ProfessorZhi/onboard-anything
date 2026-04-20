# P06 list inventory 清单

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
- 为什么 `list` 实例看起来“方法很多，普通数据属性很少”

## 一、list 实例对象

示例实例：

```python
nums = [1, 2, 3]
```

### 1. 最值得先看的实例方法

| 名称 | 更接近底层的定义视角 | 作用 | 返回值 | 是否修改原对象 |
|---|---|---|---|---|
| `append` | `list.append(self, object, /)` | 末尾追加一个元素 | `None` | 是 |
| `extend` | `list.extend(self, iterable, /)` | 批量追加元素 | `None` | 是 |
| `insert` | `list.insert(self, index, object, /)` | 指定位置插入 | `None` | 是 |
| `remove` | `list.remove(self, value, /)` | 删除第一个匹配值 | `None` | 是 |
| `pop` | `list.pop(self, index=-1, /)` | 删除并返回元素 | 被删元素 | 是 |
| `clear` | `list.clear(self, /)` | 清空列表 | `None` | 是 |
| `index` | `list.index(self, value, start=0, stop=..., /)` | 查找位置 | `int` | 否 |
| `count` | `list.count(self, value, /)` | 统计次数 | `int` | 否 |
| `sort` | `list.sort(self, /, *, key=None, reverse=False)` | 原地排序 | `None` | 是 |
| `reverse` | `list.reverse(self, /)` | 原地反转 | `None` | 是 |

### 2. 实例对象的数据属性 / 元信息属性

| 名称 | 含义 | 例子 | 值类型 |
|---|---|---|---|
| `__class__` | 当前对象的类型 | `nums.__class__` -> `<class 'list'>` | `type` |
| `__doc__` | 帮助文档字符串 | `nums.__doc__` | `str` |
| `__hash__` | 哈希相关属性；对 `list` 来说通常是 `None` | `nums.__hash__` | `NoneType` 或相关可访问结果 |

说明：

- `list` 实例这边，普通数据属性确实不多。
- 这不等于 `list` “内部只有这么几个东西”，而是因为它不是靠一堆普通字段暴露内部状态。
- `list` 实例通常没有普通的 `__dict__`。

### 3. 实例对象的全部方法清单

| 名称 | 说明 |
|---|---|
| `append` | 末尾追加元素 |
| `clear` | 清空列表 |
| `copy` | 浅拷贝 |
| `count` | 统计元素出现次数 |
| `extend` | 追加多个元素 |
| `index` | 查找元素位置 |
| `insert` | 指定位置插入 |
| `pop` | 删除并返回元素 |
| `remove` | 删除第一个匹配值 |
| `reverse` | 原地反转 |
| `sort` | 原地排序 |
| `__add__` | 列表相加 |
| `__contains__` | 成员测试 |
| `__delitem__` | 删除下标项 |
| `__eq__` | 相等比较 |
| `__ge__` | 大于等于比较 |
| `__getitem__` | 取下标项 |
| `__gt__` | 大于比较 |
| `__iadd__` | 原地加法 |
| `__imul__` | 原地乘法 |
| `__iter__` | 返回迭代器 |
| `__le__` | 小于等于比较 |
| `__len__` | 返回长度 |
| `__lt__` | 小于比较 |
| `__mul__` | 重复列表 |
| `__ne__` | 不等比较 |
| `__reduce__` | 序列化支持 |
| `__reduce_ex__` | 序列化支持 |
| `__repr__` | 官方字符串表示 |
| `__reversed__` | 反向迭代 |
| `__rmul__` | 右乘 |
| `__setitem__` | 设置下标项 |
| `__sizeof__` | 占用内存大小 |
| `__str__` | 普通字符串表示 |
| `__class_getitem__` | 泛型下标支持 |
| `__delattr__` | 删除属性 |
| `__dir__` | 列出成员 |
| `__format__` | 格式化 |
| `__getattribute__` | 获取属性 |
| `__getstate__` | 状态提取 |
| `__init__` | 初始化 |
| `__init_subclass__` | 子类初始化钩子 |
| `__new__` | 创建对象 |
| `__setattr__` | 设置属性 |
| `__subclasshook__` | 子类判断钩子 |

### 4. 实例对象的全部数据属性 / 元信息属性清单

| 名称 | 说明 |
|---|---|
| `__class__` | 当前对象的类型 |
| `__doc__` | 文档字符串 |
| `__hash__` | 哈希相关属性 |

## 二、list 类型对象

类型对象就是：

```python
list
```

### 1. 类型对象的方法

| 名称 | 签名/形式 | 作用 |
|---|---|---|
| `append` | `list.append(self, object, /)` | 定义追加规则 |
| `extend` | `list.extend(self, iterable, /)` | 定义批量追加规则 |
| `insert` | `list.insert(self, index, object, /)` | 定义插入规则 |
| `remove` | `list.remove(self, value, /)` | 定义删除规则 |
| `pop` | `list.pop(self, index=-1, /)` | 定义弹出规则 |
| `sort` | `list.sort(self, /, *, key=None, reverse=False)` | 定义排序规则 |
| `reverse` | `list.reverse(self, /)` | 定义反转规则 |
| `mro` | `list.mro()` | 查看继承链 |

### 2. 类型对象的数据属性 / 元信息属性

| 名称 | 含义 | 例子 | 值类型 |
|---|---|---|---|
| `__name__` | 类型名字 | `list.__name__` -> `'list'` | `str` |
| `__qualname__` | 限定名 | `list.__qualname__` | `str` |
| `__module__` | 所属模块 | `list.__module__` -> `'builtins'` | `str` |
| `__bases__` | 父类元组 | `list.__bases__` | `tuple` |
| `__mro__` | 方法解析顺序 | `list.__mro__` | `tuple` |
| `__dict__` | 类型对象自己的命名空间映射 | `list.__dict__` | `mappingproxy` |
| `__doc__` | 类型文档 | `list.__doc__` | `str` |
| `__hash__` | 哈希相关属性 | `list.__hash__` | 常见为 `None` 或相关对象 |

### 3. 类型对象的全部方法清单

| 名称 | 说明 |
|---|---|
| `append` | 定义追加方法 |
| `clear` | 定义清空方法 |
| `copy` | 定义浅拷贝方法 |
| `count` | 定义统计方法 |
| `extend` | 定义扩展方法 |
| `index` | 定义查找方法 |
| `insert` | 定义插入方法 |
| `pop` | 定义弹出方法 |
| `remove` | 定义删除方法 |
| `reverse` | 定义反转方法 |
| `sort` | 定义排序方法 |
| `mro` | 返回方法解析顺序 |
| `__add__` | 列表加法定义 |
| `__contains__` | 成员测试定义 |
| `__delitem__` | 删除项定义 |
| `__eq__` | 比较定义 |
| `__ge__` | 比较定义 |
| `__getitem__` | 取项定义 |
| `__gt__` | 比较定义 |
| `__iadd__` | 原地加法定义 |
| `__imul__` | 原地乘法定义 |
| `__iter__` | 迭代定义 |
| `__le__` | 比较定义 |
| `__len__` | 长度定义 |
| `__lt__` | 比较定义 |
| `__mul__` | 乘法定义 |
| `__ne__` | 比较定义 |
| `__reduce__` | 序列化支持 |
| `__reduce_ex__` | 序列化支持 |
| `__repr__` | 字符串表示定义 |
| `__reversed__` | 反向迭代定义 |
| `__rmul__` | 右乘定义 |
| `__setitem__` | 设置项定义 |
| `__sizeof__` | 内存大小定义 |
| `__str__` | 字符串表示定义 |
| `__class_getitem__` | 泛型支持 |
| `__delattr__` | 删除属性定义 |
| `__dir__` | 成员列举定义 |
| `__format__` | 格式化定义 |
| `__getattribute__` | 获取属性定义 |
| `__getstate__` | 状态提取定义 |
| `__init__` | 初始化定义 |
| `__init_subclass__` | 子类初始化钩子 |
| `__new__` | 创建对象定义 |
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
| `__hash__` | 哈希相关属性 |

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
