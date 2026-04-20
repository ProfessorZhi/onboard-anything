# P06 list 实例与 list 类型对象

## 一、先抓本质

要分清两层：

```python
nums = [1, 2, 3]
```

- `nums`：是一个 `list` 实例对象
- `list`：是 `nums` 所属的类型对象

也就是：

```python
print(type(nums))   # <class 'list'>
print(type(list))   # <class 'type'>
```

一句话：

`nums` 是具体对象，`list` 是“列表这种对象的类型说明书”。

## 二、list 实例对象

### 1. 实例方法

这些方法通常是从 `list` 类型那里获得的：

| 名称 | 常见签名 | 作用 |
| :--- | :--- | :--- |
| `append` | `append(object, /)` | 末尾追加一个元素 |
| `extend` | `extend(iterable, /)` | 批量追加多个元素 |
| `insert` | `insert(index, object, /)` | 在指定位置插入 |
| `remove` | `remove(value, /)` | 删除第一个匹配值 |
| `pop` | `pop(index=-1, /)` | 删除并返回元素 |
| `sort` | `sort(*, key=None, reverse=False)` | 原地排序 |
| `reverse` | `reverse()` | 原地反转 |
| `clear` | `clear()` | 清空列表 |
| `index` | `index(value, start=0, stop=sys.maxsize, /)` | 查找位置 |
| `count` | `count(value, /)` | 统计出现次数 |
| `copy` | `copy()` | 浅拷贝 |

### 2. 实例方法里为什么常看不到 `self`

例如：

```python
nums.append
```

这是绑定到 `nums` 这个实例上的方法对象。

所以这里的 `self` 已经默认绑定成了 `nums`，通常不再显示。

而：

```python
list.append
```

更接近类型对象上的方法定义，所以常能看到 `self`。

### 3. 实例数据属性 / 元信息属性

`list` 实例不像很多自定义对象那样暴露大量普通字段。

更常见的是这些可访问属性：

| 名称 | 含义 | 例子 | 值类型 |
| :--- | :--- | :--- | :--- |
| `__class__` | 当前实例所属类型 | `nums.__class__` | `type` |
| `__doc__` | 类型文档说明 | `nums.__doc__` | `str` |
| `__hash__` | 哈希能力说明 | `nums.__hash__` | `NoneType` |

重点：

- `list` 实例通常没有普通的 `__dict__`
- 这不代表它“没内容”
- 而是它的核心状态主要存在底层内部结构里，不像自定义类那样把大量字段暴露成 `obj.name`

## 三、list 类型对象

### 1. 类型对象方法

| 名称 | 签名 / 形式 | 作用 |
| :--- | :--- | :--- |
| `append` | `list.append(self, object, /)` | 定义追加规则 |
| `extend` | `list.extend(self, iterable, /)` | 定义批量追加规则 |
| `insert` | `list.insert(self, index, object, /)` | 定义插入规则 |
| `remove` | `list.remove(self, value, /)` | 定义删除规则 |
| `pop` | `list.pop(self, index=-1, /)` | 定义弹出规则 |
| `sort` | `list.sort(self, /, *, key=None, reverse=False)` | 定义排序规则 |
| `mro` | `list.mro()` | 查看继承链 |

说明：

- 这里看到的是类型对象上的方法定义
- 所以常常会把 `self` 明确写出来

### 2. 类型对象数据属性 / 元信息属性

| 名称 | 含义 | 例子 | 值类型 |
| :--- | :--- | :--- | :--- |
| `__name__` | 类型名字 | `list.__name__` | `str` |
| `__qualname__` | 限定名 | `list.__qualname__` | `str` |
| `__module__` | 所属模块 | `list.__module__` | `str` |
| `__bases__` | 父类元组 | `list.__bases__` | `tuple` |
| `__mro__` | 方法解析顺序 | `list.__mro__` | `tuple` |
| `__dict__` | 类型对象自己的命名空间映射 | `list.__dict__` | `mappingproxy` |
| `__doc__` | 类型文档 | `list.__doc__` | `str` |

## 四、`append` / `pop` / `sort` / `index` 四个最关键对比

| 方法 | 输入什么 | 返回什么 | 是否修改原列表 |
| :--- | :--- | :--- | :--- |
| `append(x)` | 一个对象 `x` | `None` | 是 |
| `pop(i)` | 下标 `i`，默认最后一个 | 被删除的元素 | 是 |
| `sort(...)` | 排序规则 | `None` | 是 |
| `index(x)` | 要查找的值 | 下标 `int` | 否 |

最容易错的是：

```python
nums = [1, 2, 3]
result = nums.append(4)
```

这时：

```python
nums    # [1, 2, 3, 4]
result  # None
```

原因不是 `append` 没工作，
而是它的设计就是：

- 修改原对象
- 返回 `None`

## 五、为什么 `list.append` 和 `nums.append` 不一样

### `list.append`

```python
print(list.append)
```

看到的是类型对象上的方法定义。

### `nums.append`

```python
print(nums.append)
```

看到的是绑定到实例后的方法对象。

所以：

- `list.append` 更偏“定义层”
- `nums.append` 更偏“绑定后调用层”

## 六、和自定义对象的一个关键差别

自定义对象常常有：

```python
obj.__dict__
```

可以放很多实例字段。

但 `list` 实例通常没有这类普通实例属性字典。

所以不要把 `list` 理解成“一个带很多字段的普通对象”。

更准确地说：

`list` 是一种内置容器对象，它把重点放在“存元素”和“提供操作这些元素的方法”上。

## 七、最该记住的话

一句话收住：

- `[1, 2, 3]` 是 `list` 实例对象
- `list` 是类型对象
- 实例方法常常已经隐含绑定了 `self`
- `append`、`sort` 这类方法很多是原地修改，不返回新列表
