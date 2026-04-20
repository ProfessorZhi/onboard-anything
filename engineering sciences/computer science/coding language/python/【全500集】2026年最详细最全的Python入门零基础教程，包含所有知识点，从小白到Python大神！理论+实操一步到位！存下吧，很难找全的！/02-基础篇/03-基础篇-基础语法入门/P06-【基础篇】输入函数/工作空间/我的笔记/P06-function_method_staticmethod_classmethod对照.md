# P06 function、method、staticmethod、classmethod 对照

## 这份笔记真正解决什么问题

你现在已经看到过：

- `print`
- `list.append`
- `nums.append`

下一步最容易混的是自定义类里的：

- 普通函数 `function`
- 实例方法
- `staticmethod`
- `classmethod`

这份笔记就是把这四种东西分清。

## 一、普通函数 `function`

例如：

```python
def top_func(x, y=10):
    return x + y
```

这时：

```python
type(top_func)
```

常见结果是：

```python
<class 'function'>
```

它的特点是：

- 就是普通函数对象
- 没有自动绑定 `self`
- 没有自动绑定 `cls`

## 二、实例方法

例如：

```python
class Demo:
    def instance_method(self, x, y=10):
        return x + y
```

### 1. 在类对象上看

```python
Demo.instance_method
```

这里看到的是类里定义的函数成员，签名常写成：

```python
(self, x, y=10)
```

也就是说：

- 这时还没绑定具体实例
- 所以 `self` 还要显式出现

### 2. 在实例对象上看

```python
obj = Demo()
obj.instance_method
```

这时 `self` 已经自动绑定到 `obj` 了，所以签名常会变成：

```python
(x, y=10)
```

一句话：

**实例方法不是没有 `self`，而是 `self` 已经隐含绑定到当前实例。**

## 三、`staticmethod`

例如：

```python
class Demo:
    @staticmethod
    def static_method(x, y=10):
        return x + y
```

它的特点是：

- 不自动传 `self`
- 也不自动传 `cls`
- 更像“只是碰巧写在类里面的普通函数”

所以：

```python
Demo.static_method
obj.static_method
```

调用时都不需要 `self` / `cls`。

一句话：

**`staticmethod` = 放在类命名空间里的普通函数。**

## 四、`classmethod`

例如：

```python
class Demo:
    @classmethod
    def class_method(cls, x, y=10):
        return x + y
```

它的特点是：

- 自动绑定的不是实例 `self`
- 而是类对象 `cls`

所以：

```python
Demo.class_method
obj.class_method
```

背后更接近：

```python
Demo.class_method(Demo, x, y)
```

一句话：

**`classmethod` = 自动把类对象绑定给 `cls` 的方法。**

## 五、最短对照表

| 形式 | 自动绑定什么 | 常见签名变化 | 本质 |
|---|---|---|---|
| `function` | 不自动绑定 | `(x, y=10)` | 普通函数 |
| 实例方法 | 自动绑定 `self` | 类上看 `(self, x)`，实例上看 `(x)` | 绑定到实例的方法 |
| `staticmethod` | 不自动绑定 | `(x, y=10)` | 放在类里的普通函数 |
| `classmethod` | 自动绑定 `cls` | 类上/实例上都偏向省掉显式 `cls` | 绑定到类的方法 |

## 六、最该记住什么

1. 普通 `def` 得到的通常是 `function` 对象。
2. 实例方法的 `self` 不是消失了，而是绑定后被隐含传入。
3. `staticmethod` 不自动传 `self` / `cls`。
4. `classmethod` 自动传的是类对象 `cls`。
5. 同一个名字，放在“类对象视角”和“实例对象视角”下看，类型和签名都可能变化。
