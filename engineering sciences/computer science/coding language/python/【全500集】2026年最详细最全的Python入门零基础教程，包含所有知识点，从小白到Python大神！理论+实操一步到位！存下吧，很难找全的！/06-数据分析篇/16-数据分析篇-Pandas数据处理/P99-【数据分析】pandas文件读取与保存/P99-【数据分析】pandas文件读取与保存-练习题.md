---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 99-【数据分析】pandas文件读取与保存
page_index: 99
page_title: 【数据分析】pandas文件读取与保存
type: 练习题
tags:
  - 网课
  - 练习题
---

# P99 练习题 - 【数据分析】pandas文件读取与保存
## 结构识别

**题目 1.1** 给定以下 `read_csv` 核心参数，请判断哪些参数的默认值可能导致“第一行数据被当作列名”：

```
filepath、header、names、index_col、sep、skiprows、nrows、encoding
```

请在参数后面标注：**默认值安全** 或 **需显式设置**。

---

**题目 1.2** `to_csv` 与 `read_csv` 在以下功能上形成对称关系，请完成表格：

| 功能 | read_csv 参数 | to_csv 参数 |
|------|--------------|-------------|
| 指定文件路径 | filepath | ？ |
| 指定列名 | names | — |
| 指定索引列 | index_col | ？ |
| 处理中文内容 | encoding | ？ |
| 是否输出索引 | — | ？ |

---

## 机制理解

**题目 2.1** 代码：

```python
import pandas as pd
reader = pd.read_csv('big_data.csv', chunksize=10)
for chunk in reader:
    print(type(chunk))
```

以上代码的输出类型是什么？`chunksize` 返回的 `reader` 对象本质上是什么数据结构？

---

**题目 2.2** 阅读以下代码，说出存在的问题：

```python
df1 = pd.read_csv('data.csv', chunksize=5)
df2 = pd.concat([chunk for chunk in df1])  # 第2行

df3 = pd.read_csv('data.csv', chunksize=5)
for chunk in df3:
    if len(chunk) < 5:
        break
print(len(chunk))
```

第 2 行和第 6 行分别存在什么问题？请解释原因。

---

**题目 2.3** 在 Windows 系统下，用户 A 导出 CSV 文件（`to_csv`），用户 B 在 macOS 系统下读取（`read_csv`），出现中文乱码。请分析根本原因，并给出双方各自的解决方案。

---

## 最小实践

**题目 3.1** 已知 `score.csv` 内容如下（无列名）：

```
语文,85
数学,92
英语,78
```

请用一行代码读取为 DataFrame，并自定义列名为 `['科目', '分数']`。

---

**题目 3.2** 将以下 DataFrame 保存为 `result.csv`，要求：

- 不保存 pandas 自动生成的整型索引
- 文件编码为 UTF-8
- 用中文逗号 `，` 作为分隔符

```python
df = pd.DataFrame({'姓名': ['张三', '李四'], '年龄': [25, 30]})
```

---

**题目 3.3** 假设 `sales.csv` 有 10000 行数据，只需要读取前 100 行用于快速预览。请写出两种不同的实现方式（不需要实际文件）。

---

**题目 3.4** 使用 `chunksize` 分批读取 `large_file.csv`，将所有批次合并为一个完整 DataFrame，并统计总行数。

```python
# 补全代码
chunks = pd.read_csv('large_file.csv', chunksize=500)
# 你的代码
```

---

## 扩展思考

**题目 4.1** `read_excel` 除了 `sheet_name` 参数外，还有一个常用参数可以指定读取第几个工作表。请思考：

- `sheet_name=0` 和 `sheet_name='Sheet1'` 在什么情况下效果不同？
- 如果要读取 Excel 文件中的所有工作表，`sheet_name` 应该设置为什么值？

---

**题目 4.2** 当 DataFrame 列中包含列表或字典等复杂结构时，直接保存为 CSV 再读取会导致结构被破坏（变成字符串）。

请思考：除了保存为 Excel，还有哪种格式可以完整保留这类嵌套结构？它的读取函数是什么？

---

**题目 4.3** 假设你负责处理一个 10GB 的日志 CSV 文件，你的服务器内存只有 4GB。请设计一个数据处理流水线思路，要求：

- 不一次性加载整个文件
- 逐块处理后计算全局统计量（如每列均值）
- 伪代码即可

---

## 最小替代练习

**题目 5.1** 如果暂时没有安装 pandas，能否只用 Python 标准库完成 CSV 文件的读写？请使用 `csv` 模块：

1. 用 `csv.reader` 读取 `data.csv`，打印前 3 行
2. 用 `csv.writer` 将以下数据写入 `output.csv`

```python
data = [['城市', '温度'], ['北京', 28], ['上海', 31]]
```

完成后对比：pandas 的 `read_csv` 与标准库 `csv.reader` 在使用体验上有哪些主要差异？

---

**参考答案概览**

| 题号 | 考察点 |
|------|--------|
| 1.1 | header 默认值为 0，需注意 |
| 1.2 | path_or_buf、index、encoding |
| 2.1 | 迭代器，每次 yield DataFrame |
| 2.2 | 迭代器不可复用、break 后保留最后 chunk |
| 2.3 | Windows GBK vs UTF-8 |
| 3.1 | header=None + names 参数组合 |
| 3.2 | index=False, encoding='utf-8', sep='，' |
| 3.3 | nrows=100 或 skiprows + header |
| 3.4 | concat 合并 chunks |
| 4.1 | sheet_name 支持整数和字符串 |
| 4.2 | JSON 格式，read_json |
| 4.3 | chunksize + 累加器模式 |
| 5.1 | csv 模块基础操作对比 |
