---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 98-【数据分析】pandas入门2df常见操作
page_index: 98
page_title: 【数据分析】pandas入门2df常见操作
type: 练习题
tags:
  - 网课
  - 练习题
---

# P98 练习题 - 【数据分析】pandas入门2df常见操作
---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 98-【数据分析】pandas入门2df常见操作
page_index: 98
page_title: 【数据分析】pandas入门2df常见操作
type: 练习题
tags:
  - 网课
  - 练习题
---

# P98 练习题 - 【数据分析】pandas入门2df常见操作

---

## 一、结构识别

**Q1** 下列六种创建方式中，哪两种在实际项目里最常用？请从"数据来源灵活性"角度说明原因。

> 六种：空DataFrame / NumPy数组 / 指定index / 字典 / zip打包 / 字典组成的列表

**Q2** 阅读以下代码片段，指出每个属性调用会返回什么类型（写出 Python 类型名）：

```
import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

df.shape    # 返回类型：___
df.dtypes   # 返回类型：___
df.values   # 返回类型：___
df.index    # 返回类型：___
df.ndim     # 返回类型：___
```

---

## 二、机制理解

**Q3** 下面两行代码的切片结果是否相同？说明理由。

```
df.loc[1:4]
df.iloc[1:4]
```

> 提示：关注"左闭右开"规则在 loc 与 iloc 上的差异，以及"标签索引"与"位置索引"的本质区别。

**Q4** 为什么 dtypes 返回的列类型是 `object` 而不是 `string`？`object` 与 `string` 有什么关系？如何将其转为真正的 string 类型？

**Q5** 以下代码能否正常执行？如果能，结果是什么；如果不能，报什么错？请分别判断。

```
# 情况 A
pd.DataFrame({'x': [1, 2, 3], 'y': [10, 20]})

# 情况 B
pd.DataFrame({'x': [1, 2, 3], 'y': [10, 20, 30]})

# 情况 C
names = ['Alice', 'Bob', 'Carol']
scores = [90, 85, 92]
pd.DataFrame(zip(names, scores))
```

---

## 三、最小实践

**Q6** 用两种不同方式（字典创建 + zip创建）构建同一个 DataFrame，要求：

- 列名为 `name`、`age`、`city`
- 至少包含 3 行数据
- 创建后分别打印 `shape`、`dtypes`、`values`

验收标准：两种方式输出结果完全一致。

**Q7** 基于 Q6 创建的 DataFrame，完成以下切片操作并写出预期输出：

1. 用 `loc` 取第 1、2 行（标签为 1、2）
2. 用 `iloc` 取最后一行
3. 用 `loc` 只取 `name` 和 `city` 两列
4. 用 `head(2)` 取前两行

---

## 四、扩展思考

**Q8** `df.values` 返回的是二维 NumPy 数组，这意味着 DataFrame 的底层存储依赖 NumPy。试思考：如果一个 DataFrame 的列同时包含 int 和 str 类型，`values` 返回的数组类型会是什么？为什么 pandas 不会报错而 NumPy 原生数组可能需要指定 dtype？

---

## 五、最小替代练习（外部工具）

> 本P提到 **pandas 120题 / 300题** 作为配套题库。

**Q9** 在 GitHub 上搜索关键词 `pandas exercises` 或 `pandas 120`，找到任意一份题库，完成其中与以下知识点对应的题目各 1 道：

- DataFrame 创建
- 属性查询（shape / dtypes / values 任选一）
- loc 或 iloc 切片

完成后，在笔记中记录：题目编号、你的解法、与本P知识点的对应关系。

---

## 答题提示索引

| 题号 | 对应知识骨架节点 | 易错提示 |
|---|---|---|
| Q1 | 创建层（六种） | 不看来源只看语法是表层思维 |
| Q2 | 属性层（五个） | 注意 dtypes 返回的是 Series，不是 dict |
| Q3 | 切片层 loc vs iloc | loc 右端闭合，iloc 右端开放 |
| Q4 | dtypes / object 类型 | object 是 pandas 默认字符串类型，非严格 string |
| Q5 | 创建层易错点 | 情况A会填充NaN，不是报错 |
| Q6 | 创建层全流程 | zip() 返回迭代器，需外套 list |
| Q7 | 切片层综合 | loc 可接列名，iloc 只接整数位置 |
| Q8 | values + NumPy关系 | 混合类型会向上转为 object |
| Q9 | 全P综合 | 建立题库与知识点的双向链接 |
