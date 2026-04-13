---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 100-【数据分析】pandas的常见操作1
page_index: 100
page_title: 【数据分析】pandas的常见操作1
type: 资源清单
tags:
  - 网课
  - 资源清单
---

# P100 资源清单 - 【数据分析】pandas的常见操作1
---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 100-【数据分析】pandas的常见操作1
page_index: 100
page_title: 【数据分析】pandas的常见操作1
type: 资源清单
tags:
  - 网课
  - 资源清单
---

# P100 资源清单 - 【数据分析】pandas的常见操作1

> 本P涉及资源共 5 项，均为 Python 数据分析生态中的标准工具或文件对象。无需额外安装配置，前置环境满足 Python + pandas + numpy 即可复现全部演示。

---

## 1. pandas

| 字段 | 内容 |
|------|------|
| **类型** | Python 第三方库 |
| **在本P中的作用** | 本P所有操作的主体库；提供 DataFrame 数据结构及其修改、扩充、拼接的全部方法，包括 `.index`、`.columns`、`.rename()`、`.append()`、`.loc[]`、`.head()` 等 |
| **来源** | 字幕直接提到 |
| **涉及的具体 API** | `df.index`、`df.columns`、`df.rename(index/columns, inplace)`、`df.append(other, ignore_index)`、`df.loc[]`、`df.head()` |

**建议方向**

- 系统阅读 pandas 官方文档中 [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html) 一节，对比本P演示的索引修改方式与 `.set_index()`、`.reset_index()` 的适用场景
- 注意 `df.append()` 已在 pandas 2.0 中被移除，建议同步学习 `pd.concat([df1, df2], ignore_index=True)` 作为替代，避免版本迁移时踩坑
- 练习 `inplace=True` 与重新赋值两种写法在不同方法上的差异，形成对"是否修改原对象"的判断习惯

---

## 2. numpy

| 字段 | 内容 |
|------|------|
| **类型** | Python 第三方库 |
| **在本P中的作用** | 作为 DataFrame 操作的数据生成工具；`np.arange()` 用于生成连续整数索引序列，`np.random.randint()` 用于生成随机整数列作为新列数据 |
| **来源** | 字幕直接提到 |
| **涉及的具体 API** | `np.arange(start, stop)`、`np.random.randint(low, high, size)` |

**建议方向**

- 练习 `np.arange()` 的三参数形式（start、stop、step），掌握生成步长不为 1 的索引序列的方法
- 对比 `np.random.randint()` 与 `np.random.uniform()`，理解整数随机数与浮点随机数的生成差异，为后续模拟不同类型数据做准备
- 练习用 `np.random.seed()` 固定随机种子，使每次运行结果可复现，养成数据实验可重复的习惯

---

## 3. data1.csv

| 字段 | 内容 |
|------|------|
| **类型** | CSV 数据文件 |
| **在本P中的作用** | 本P所有演示操作的基础输入数据；由上一节课保存，包含日期、姓名、学历、薪资范围、年龄、城市等列，共 16 行，用于演示索引修改、列名修改、添加列/行、DataFrame 拼接等全部操作 |
| **来源** | 字幕直接提到（"上节课保存的数据文件 data1"） |
| **备注** | 文件结构为课程自制数据，非公开数据集；学习者可用任意结构相似的 CSV 文件替代 |

**建议方向**

- 用自己熟悉的真实数据集（如公开的薪资调查数据、招聘网站导出数据）替换 data1.csv，在真实数据上复现本P的所有操作，检验代码的泛化能力
- 练习在读取 CSV 时通过 `pd.read_csv(index_col=...)` 直接指定索引列，对比与读取后再修改索引的区别

---

## 4. `df.rename()` 方法

| 字段 | 内容 |
|------|------|
| **类型** | pandas DataFrame 方法（重点单列方法，单独列出） |
| **在本P中的作用** | 同时承担行索引选择性修改（`rename(index={旧值: 新值})`）和列名选择性修改（`rename(columns={旧名: 新名})`）两种职责；与直接赋值方式形成对比，适用于不需要全量替换的场景 |
| **来源** | 字幕直接提到 |
| **关键参数** | `index`（字典，指定行索引映射）、`columns`（字典，指定列名映射）、`inplace`（布尔值，是否原地修改） |

**建议方向**

- 练习 `rename()` 接受函数而非字典的用法（如 `df.rename(columns=str.upper)`），掌握批量规则化列名的技巧
- 对比 `rename(inplace=True)` 与 `df = df.rename(...)` 两种写法在链式调用场景下的优劣

---

## 5. `pd.concat()` / `df.append()`（版本对比）

| 字段 | 内容 |
|------|------|
| **类型** | pandas 函数 / DataFrame 方法 |
| **在本P中的作用** | 本P演示使用 `df.append()` 完成添加单行（传入字典）和垂直拼接两个 DataFrame 的操作；`ignore_index=True` 参数用于自动重建连续整数索引 |
| **来源** | 字幕直接提到（`df.append()`）；`pd.concat()` 基于上下文推断（pandas 2.0 移除 `append` 后的替代方案） |
| **版本说明** | `df.append()` 在 pandas 1.4 起被标记为 deprecated，在 pandas 2.0 中已正式移除；现行推荐写法为 `pd.concat([df1, df2], ignore_index=True)` |

**建议方向**

- 对照本P演示，用 `pd.concat()` 改写全部 `df.append()` 示例，确认两者输出一致
- 练习 `pd.concat()` 的 `axis` 参数，理解垂直拼接（`axis=0`）与水平拼接（`axis=1`）的适用场景，为下一节数据合并内容做铺垫
- 练习在循环中批量构建行数据后，用 `pd.concat()` 一次性合并，对比逐行 `append` 的性能差异，理解"先收集、后合并"的最佳实践

---

## 资源总览

| # | 名称 | 类型 | 本P核心作用 | 来源依据 |
|---|------|------|-------------|----------|
| 1 | pandas | Python 第三方库 | DataFrame 结构与所有操作方法的提供者 | 字幕直接提到 |
| 2 | numpy | Python 第三方库 | 生成索引序列与随机数列 | 字幕直接提到 |
| 3 | data1.csv | CSV 数据文件 | 本P全部演示的输入数据源 | 字幕直接提到 |
| 4 | `df.rename()` | pandas DataFrame 方法 | 选择性修改行索引与列名 | 字幕直接提到 |
| 5 | `pd.concat()` / `df.append()` | pandas 函数 / 方法 | 添加行与垂直拼接 DataFrame | 字幕提到 append；concat 为上下文推断 |
