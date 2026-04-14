# P06 list 实例与 list 类型对象

## 先把三层分清

```python
[1, 2, 3]
list
type
```

- `[1, 2, 3]` 是一个 `list` 实例对象
- `list` 是一个类型对象
- `type` 也是一个类型对象

验证：

```python
type([1, 2, 3])   # <class 'list'>
type(list)        # <class 'type'>
type(type)        # <class 'type'>
```

## 这个点真正解决什么问题

帮你区分：

1. 某个具体列表对象现在能做什么
2. 列表这个类型本身定义了什么能力

所以：

```python
[1, 2, 3].append(4)
```

不是“这个列表自己凭空有 `append`”，而是：

- `[1, 2, 3]` 是 `list` 的实例
- `append` 这套能力定义在 `list` 这个类型上
- 这个实例对象可以调用它

## 一、`list` 实例对象的常见成员

先准备一个对象：

```python
nums = [1, 2, 3]
```

### 1. `append`

#### 作用

在列表末尾追加一个元素。

#### 调用形式

```python
nums.append(object)
```

更接近真实签名：

```python
append(self, object, /)
```

#### 参数

- `object`
  - 要追加进去的对象

#### 返回值

返回 `None`

#### 是否修改原对象

会，原地修改列表对象。

#### 示例

```python
nums = [1, 2, 3]
result = nums.append(4)

print(nums)    # [1, 2, 3, 4]
print(result)  # None
```

### 2. `extend`

#### 作用

把另一组元素逐个追加到当前列表末尾。

#### 调用形式

```python
nums.extend(iterable)
```

更接近真实签名：

```python
extend(self, iterable, /)
```

#### 参数

- `iterable`
  - 一个可迭代对象，比如列表、元组、字符串等

#### 返回值

返回 `None`

#### 是否修改原对象

会，原地修改列表对象。

#### 示例

```python
nums = [1, 2, 3]
nums.extend([4, 5])
print(nums)   # [1, 2, 3, 4, 5]
```

### 3. `insert`

#### 作用

在指定位置插入元素。

#### 调用形式

```python
nums.insert(index, object)
```

更接近真实签名：

```python
insert(self, index, object, /)
```

#### 参数

- `index`
  - 插入位置下标
- `object`
  - 要插入的对象

#### 返回值

返回 `None`

#### 是否修改原对象

会，原地修改列表对象。

#### 示例

```python
nums = [1, 2, 3]
nums.insert(1, 99)
print(nums)   # [1, 99, 2, 3]
```

### 4. `remove`

#### 作用

删除第一个值等于指定内容的元素。

#### 调用形式

```python
nums.remove(value)
```

更接近真实签名：

```python
remove(self, value, /)
```

#### 参数

- `value`
  - 要删除的值

#### 返回值

返回 `None`

#### 是否修改原对象

会，原地修改列表对象。

#### 示例

```python
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)   # [1, 3, 2]
```

### 5. `pop`

#### 作用

删除并返回某个位置的元素。

#### 调用形式

```python
nums.pop(index=-1)
```

更接近真实签名：

```python
pop(self, index=-1, /)
```

#### 参数

- `index`
  - 要弹出的下标
  - 默认 `-1`，表示最后一个元素

#### 返回值

返回被删除的那个元素

#### 是否修改原对象

会，原地修改列表对象。

#### 示例

```python
nums = [10, 20, 30]
x = nums.pop()

print(x)      # 30
print(nums)   # [10, 20]
```

### 6. `clear`

#### 作用

清空整个列表。

#### 调用形式

```python
nums.clear()
```

#### 参数

无

#### 返回值

返回 `None`

#### 是否修改原对象

会，原地修改列表对象。

#### 示例

```python
nums = [1, 2, 3]
nums.clear()
print(nums)   # []
```

### 7. `index`

#### 作用

查找某个元素第一次出现的位置。

#### 调用形式

```python
nums.index(value, start=0, stop=很大值)
```

更接近真实签名：

```python
index(self, value, start=0, stop=9223372036854775807, /)
```

#### 参数

- `value`
  - 要查找的值
- `start`
  - 起始位置
- `stop`
  - 结束位置

#### 返回值

返回 `int`

#### 是否修改原对象

不修改原对象。

#### 示例

```python
[10, 20, 30].index(20)   # 1
```

### 8. `count`

#### 作用

统计某个元素出现的次数。

#### 调用形式

```python
nums.count(value)
```

更接近真实签名：

```python
count(self, value, /)
```

#### 参数

- `value`
  - 要统计的值

#### 返回值

返回 `int`

#### 是否修改原对象

不修改原对象。

#### 示例

```python
[1, 1, 2, 1].count(1)   # 3
```

### 9. `sort`

#### 作用

对列表原地排序。

#### 调用形式

```python
nums.sort(key=None, reverse=False)
```

更接近真实签名：

```python
sort(self, /, *, key=None, reverse=False)
```

#### 参数

- `key`
  - 排序依据函数，可选
- `reverse`
  - 是否倒序，默认 `False`

#### 返回值

返回 `None`

#### 是否修改原对象

会，原地修改列表对象。

#### 示例

```python
nums = [3, 1, 2]
nums.sort()
print(nums)   # [1, 2, 3]
```

### 10. `reverse`

#### 作用

把列表顺序原地反转。

#### 调用形式

```python
nums.reverse()
```

#### 参数

无

#### 返回值

返回 `None`

#### 是否修改原对象

会，原地修改列表对象。

#### 示例

```python
nums = [1, 2, 3]
nums.reverse()
print(nums)   # [3, 2, 1]
```

### 11. `__class__`

#### 作用

查看这个实例对象的类型。

#### 示例

```python
[1, 2, 3].__class__   # <class 'list'>
```

## 二、`list` 类型对象本身的常见属性 / 方法

这里讨论的不是某个具体列表，而是 `list` 本身。

### 1. `__name__`

#### 作用

类型名字。

#### 返回值

返回 `str`

#### 示例

```python
list.__name__   # 'list'
```

### 2. `__mro__`

#### 作用

方法解析顺序。

#### 返回值

返回 `tuple`

#### 示例

```python
list.__mro__
# (<class 'list'>, <class 'object'>)
```

### 3. `__bases__`

#### 作用

直接父类。

#### 返回值

返回 `tuple`

#### 示例

```python
list.__bases__
# (<class 'object'>,)
```

### 4. `__doc__`

#### 作用

类型帮助文档。

#### 返回值

返回 `str`

#### 示例

```python
list.__doc__
```

### 5. `append`

#### 作用

这是定义在 `list` 类型上的方法定义，不是某个具体列表实例的绑定方法。

#### 示例

```python
list.append
# <method 'append' of 'list' objects>
```

### 6. `sort`

#### 作用

也是定义在 `list` 类型上的方法定义。

#### 示例

```python
list.sort
```

### 7. `mro()`

#### 作用

以列表形式查看方法解析顺序。

#### 返回值

返回 `list[type]`

#### 示例

```python
list.mro()
# [<class 'list'>, <class 'object'>]
```

## 三、`list` 和 `str` 的关键差异

这点非常重要，因为它直接影响你后面理解“可变对象”和“不可变对象”。

### `str`

像 `split()`、`upper()`、`replace()` 这样的常见方法，通常返回新对象，不改原字符串。

```python
s = "abc"
t = s.upper()

print(s)   # 'abc'
print(t)   # 'ABC'
```

### `list`

像 `append()`、`sort()`、`reverse()` 这样的很多方法，会直接改原列表对象，并且返回 `None`。

```python
nums = [3, 1, 2]
result = nums.sort()

print(nums)    # [1, 2, 3]
print(result)  # None
```

## 四、现在最值得记住的结论

1. `[1, 2, 3]` 是实例对象，`list` 和 `type` 是类型对象。
2. `list.append` 是类型上的方法定义，`nums.append` 是实例上的绑定方法。
3. `list` 实例常见成员里，很多方法会原地修改对象。
4. `str` 和 `list` 的入门差异之一是：`str` 常见方法多返回新对象，`list` 常见方法多原地修改。
