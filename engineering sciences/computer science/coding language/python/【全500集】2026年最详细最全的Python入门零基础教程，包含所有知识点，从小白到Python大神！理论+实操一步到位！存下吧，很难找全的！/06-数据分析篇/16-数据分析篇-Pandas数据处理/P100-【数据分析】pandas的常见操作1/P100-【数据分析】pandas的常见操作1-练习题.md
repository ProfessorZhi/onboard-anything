---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 100-【数据分析】pandas的常见操作1
page_index: 100
page_title: 【数据分析】pandas的常见操作1
type: 练习题
tags:
  - 网课
  - 练习题
---

# P100 练习题 - 【数据分析】pandas的常见操作1
## 一、结构识别

**题目 1.1**：请根据以下需求匹配对应的pandas操作方法：

| 需求 | 匹配操作 |
|------|----------|
| 将DataFrame的行索引全部替换为0~99的连续整数 | ① |
| 将某几列的列名从"语文"改为"语文成绩" | ② |
| 在现有DataFrame右侧新增一列"总分" | ③ |
| 将df2的记录合并到df1的下方 | ④ |

可选操作：`df.rename()`、`df.append()`、`df.columns = [...]`、`df[新列名] = 数据`、`df.index = np.arange()`

---

## 二、机制理解

**题目 2.1**：以下代码能否正确修改索引？为什么？

```python
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.index[0] = 100
print(df)
```

**题目 2.2**：执行以下代码后，变量df1、df2、df3的值分别是什么？请说明原因。

```python
import pandas as pd
df1 = pd.DataFrame({'语文': [90, 85], '数学': [88, 92]})
df2 = df1.append({'语文': 78, '数学': 81}, ignore_index=True)
df3 = df1.copy()
df3['英语'] = [85, 88, 92]  # 这里故意多写了一个值
```

**题目 2.3**："df.append()方法会修改原DataFrame"——这句话正确吗？请结合pandas的设计原则解释。

---

## 三、最小实践

**题目 3.1**：已知DataFrame `students` 包含3列：姓名、语文、数学。请完成以下操作：

1. 将列名从 ["姓名", "语文", "数学"] 改为 ["name", "chinese", "math"]
2. 添加一列"总分"，值为三门课成绩之和
3. 使用 `np.arange()` 将行索引改为 [10, 11, 12]

```python
import pandas as pd
import numpy as np

students = pd.DataFrame({
    '姓名': ['小明', '小红', '小李'],
    '语文': [88, 92, 85],
    '数学': [90, 87, 93]
})
# 请在此处补充代码
```

**题目 3.2**：将两个结构相同但数据不同的DataFrame垂直拼接，并确保新DataFrame的索引从0开始连续编号。

```python
import pandas as pd

df_a = pd.DataFrame({'水果': ['苹果', '香蕉'], '数量': [5, 3]})
df_b = pd.DataFrame({'水果': ['橙子', '葡萄'], '数量': [8, 6]})
# 请补充代码，得到索引为0,1,2,3的合并结果
```

---

## 四、扩展思考

**题目 4.1**：在pandas较新版本中，`df.append()`已被标记为过时方法（deprecated）。请查阅资料，查找它的替代方案是什么？新方法相比旧方法有什么优势？

**题目 4.2**：对比以下两种修改列名的写法，分析它们的适用场景：

```python
# 写法A
df.columns = ['新名1', '新名2', '新名3']

# 写法B
df.rename(columns={'旧名1': '新名1', '旧名2': '新名2', '旧名3': '新名3'})
```

---

## 五、最小替代练习

**题目 5.1（本P外部资源替代）**：本P使用 `np.random.randint()` 生成随机数列来演示添加列。若不使用numpy库，你有什么替代方案生成类似的测试数据？请写出代码。

**题目 5.2（数据源替代）**：本P依赖 `data1.csv` 作为输入数据。如果手边没有CSV文件，如何用pandas快速创建一个用于练习的DataFrame？请写出两种方法。
