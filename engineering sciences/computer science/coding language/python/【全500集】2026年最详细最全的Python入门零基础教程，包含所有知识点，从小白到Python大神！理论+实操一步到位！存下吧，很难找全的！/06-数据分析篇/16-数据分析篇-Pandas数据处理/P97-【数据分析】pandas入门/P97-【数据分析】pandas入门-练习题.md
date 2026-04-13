---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 97-【数据分析】pandas入门
page_index: 97
page_title: 【数据分析】pandas入门
type: 练习题
tags:
  - 网课
  - 练习题
---

# P97 练习题 - 【数据分析】pandas入门
## 1. 结构识别

**题目 1.1**  
执行以下代码后，变量 `s` 的 `.index` 和 `.values` 分别返回什么类型？

```python
import pandas as pd
s = pd.Series([10, 20, 30], index=['x', 'y', 'z'])
```

- A. `.index` → `list`，`.values` → `list`
- B. `.index` → `Index` 对象，`.values` → `numpy.ndarray`
- C. `.index` → `RangeIndex`，`.values` → `list`
- D. `.index` → `list`，`.values` → `numpy.ndarray`

---

**题目 1.2**  
下面哪种数据类型**不能**直接作为 `pd.Series()` 的第一个参数 `data` 使用？

- A. Python 列表 `[1, 2, 3]`
- B. Python 字典 `{'a': 1, 'b': 2}`
- C. 字符串 `'hello'`
- D. Python 整数 `42`

---

## 2. 机制理解

**题目 2.1**  
已知 Series：

```python
s = pd.Series([100, 200, 300, 400], index=['甲', '乙', '丙', '丁'])
```

执行 `s[1:3]` 和 `s['乙':'丙']` 的结果分别是：

- A. 两者结果完全相同
- B. `s[1:3]` 返回 `乙/200、丙/300`，`s['乙':'丙']` 返回 `乙/200、丙/300`
- C. `s[1:3]` 返回 `乙/200、丙/300`，`s['乙':'丙']` 返回 `乙/200、丙/300、丁/400`
- D. `s[1:3]` 基于标签，`s['乙':'丙']` 基于整数位置

---

**题目 2.2**  
关于 `.drop()` 方法，以下说法正确的是：

- A. `s.drop('A')` 会永久删除原 Series `s` 中的 `'A'` 元素
- B. `s.drop(['A', 'B'])` 支持切片语法 `s.drop('A':'B')`
- C. `s.drop('A')` 返回一个新 Series，原 Series `s` 保持不变
- D. `s.drop('A', inplace=True)` 和 `s = s.drop('A')` 效果完全相同

---

**题目 2.3**  
阅读以下代码：

```python
s = pd.Series([1, 2, 3])
s_str = s.astype('str')
```

此时执行 `s_str > 2` 会发生什么？

- A. 正常返回布尔 Series `[False, False, True]`
- B. 抛出 `TypeError` 异常，因为字符串不能与数字比较
- C. 返回空 Series
- D. 将所有元素转换为 `False`

---

## 3. 最小实践

**题目 3.1**  
请补全代码：使用字典创建 Series，使得输出结果如下：

```
数学    95
语文    88
英语    92
dtype: int64
```

```python
import pandas as pd
scores = _______
print(scores)
```

---

**题目 3.2**  
现有 Series：

```python
s = pd.Series([5, 12, 7, 20, 15], index=['A', 'B', 'C', 'D', 'E'])
```

请写出实现以下目标的代码：

1. 使用布尔过滤，只保留值大于 10 的元素
2. 将键 `'C'` 的值改为 `100`
3. 删除键 `'E'`，并将结果保存到新变量 `s2`

---

**题目 3.3**  
已知两个 Series：

```python
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5], index=['d', 'e'])
```

请写出用 `append` 方法将 `s2` 接到 `s1` 后面，并生成连续整数索引的代码（结果索引为 0, 1, 2, 3, 4）。

---

## 4. 扩展思考

**题目 4.1**  
`pd.Series()` 底层使用 `numpy` 数组存储数据。请思考：为什么 `Series` 要在 `numpy` 数组的基础上增加"标签/索引"功能？这为数据处理带来了哪些便利？请结合具体场景举例说明。

---

**题目 4.2**  
Series 的 `append` 方法在 pandas 新版本（1.4.0+）中已被标记为废弃。请查阅文档或思考：为什么不推荐使用 `append` 来合并 Series？如果要高效合并多个 Series，有哪些替代方案？

---

## 5. 最小替代练习

**题目 5.1**  
不使用 PyCharm，在浏览器中完成以下操作：

1. 打开 [https://pandas.pydata.org/docs/getting_started/index.html#getting-started](https://pandas.pydata.org/docs/getting_started/index.html#getting-started) 页面
2. 找到 "Getting started → 10 minutes to pandas" 教程
3. 在该页面提供的在线交互式环境中（或使用 [Google Colab](https://colab.research.google.com/)），完成以下练习：
   - 用 `pd.Series` 创建一个包含你家乡名称和人口的 Series
   - 计算人口数据的基本统计量（最大值、最小值、平均值）
   - 将结果截图或复制代码，保存到你的笔记仓库中

> **提示**：Colab 已预装 pandas，可直接运行 `import pandas as pd`。

---

## 参考答案概览

| 题号 | 考察点 | 核心答案提示 |
|------|--------|--------------|
| 1.1 | Series 属性类型 | B |
| 1.2 | data 参数类型 | D（标量需要 index 参数指定长度） |
| 2.1 | 切片 vs 标签切片 | C（标签切片右闭） |
| 2.2 | drop 机制 | C + D（两者等价） |
| 2.3 | 类型转换后果 | B |
| 3.1 | 字典创建 Series | `{'数学': 95, '语文': 88, '英语': 92}` |
| 3.2 | CRUD 操作 | 布尔过滤、条件赋值、drop |
| 3.3 | append + ignore_index | `s1.append(s2, ignore_index=True)` |
