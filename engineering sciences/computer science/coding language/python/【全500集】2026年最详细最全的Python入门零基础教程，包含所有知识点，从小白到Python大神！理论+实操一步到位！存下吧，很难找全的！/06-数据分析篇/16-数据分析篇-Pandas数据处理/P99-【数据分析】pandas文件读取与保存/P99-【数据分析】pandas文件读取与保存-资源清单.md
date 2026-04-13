---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 99-【数据分析】pandas文件读取与保存
page_index: 99
page_title: 【数据分析】pandas文件读取与保存
type: 资源清单
tags:
  - 网课
  - 资源清单
---

# P99 资源清单 - 【数据分析】pandas文件读取与保存
---

## 一、核心依赖

| 名称 | 类型 | 在本 P 中的作用 | 来源 | 后续可练习方向 |
|------|------|----------------|------|----------------|
| pandas | Python 库 | 数据分析核心库，提供 read_csv / read_excel / to_csv / to_excel 等文件 I/O 方法 | 字幕直接提到 | 结合 NumPy、Matplotlib 完成数据读取→处理→可视化完整流程；探索 merge、groupby 等高级操作 |

---

## 二、开发环境

| 名称 | 类型 | 在本 P 中的作用 | 来源 | 后续可练习方向 |
|------|------|----------------|------|----------------|
| Jupyter Notebook | 开发环境 | 老师演示代码的载体；支持交互式执行与数据预览 | 字幕直接提到 | 学习使用 Jupyter 魔法命令（%timeit 等）；配置 nbextensions 插件提升效率；探索 JupyterLab 作为替代方案 |

---

## 三、数据格式

| 名称 | 类型 | 在本 P 中的作用 | 来源 | 后续可练习方向 |
|------|------|----------------|------|----------------|
| CSV | 文件格式 | 最通用的表格数据交换格式，read_csv / to_csv 的默认处理对象 | 字幕直接提到 | 处理 TSV、SSV 等变种分隔符格式；处理超大型 CSV（GB 级别）的内存优化 |
| Excel | 文件格式 | 商业场景标配，支持多 Sheet；read_excel / to_excel 处理 | 字幕直接提到 | 处理带公式、合并单元格、特殊格式的 Excel 文件；使用 openpyxl 引擎处理 .xlsx 高级特性 |
| JSON | 文件格式 | 前后端数据传输格式；老师顺带提及，本 P 未深入 | 字幕直接提到 | 练习 read_json / to_json 处理嵌套 JSON；处理 API 接口返回的 JSON 数据 |

---

## 四、示例数据文件

| 名称 | 类型 | 在本 P 中的作用 | 来源 | 后续可练习方向 |
|------|------|----------------|------|----------------|
| 数据一.csv | 示例数据文件 | 小型数据集（16 行），用于演示 read_csv 基础读取、header / names / index_col / skiprows / nrows 等参数 | 字幕直接提到 | 用自己的小型 CSV 文件替换练习；练习处理带中文、空格、特殊字符的文件名 |
| 某招聘网站数据.csv | 示例数据文件 | 大型数据集（105 行 52 列），用于演示 chunksize 逐块读取、分块保存逻辑 | 字幕直接提到 | 下载 Kaggle / 天池等公开数据集，用真实招聘或销售数据进行大文件分块处理练习 |

---

## 五、核心函数与方法

| 名称 | 类型 | 在本 P 中的作用 | 来源 | 后续可练习方向 |
|------|------|----------------|------|----------------|
| pd.read_csv | 函数 | 读取 CSV 文件的核心入口；支持 filepath / sep / header / index_col / names / skiprows / nrows / chunksize 等参数 | 字幕直接提到 | 练习使用正则表达式作为 sep 参数；探索 usecols 参数指定只读取部分列；处理不规则分隔符（如多个空格） |
| pd.read_excel | 函数 | 读取 Excel 文件；支持 sheet_name / header / usecols 等参数 | 基于上下文推断 | 练习读取多 Sheet（sheet_name=0 / 'Sheet2' / None）；处理带格式的 Excel 表头合并单元格 |
| DataFrame.to_csv | 方法 | 将 DataFrame 保存为 CSV 文件；核心参数 path_or_buf / encoding / index | 字幕直接提到 | 练习 append 模式追加写入；配合 sep 参数保存为 TSV 格式；处理大文件分块保存逻辑 |
| DataFrame.to_excel | 方法 | 将 DataFrame 保存为 Excel 文件 | 基于上下文推断 | 练习写入多 Sheet；使用 openpyxl 引擎设置单元格格式 |
| pd.set_option | 函数 | 控制 Jupyter 显示行为；本 P 涉及 display.max_rows / display.max_columns | 字幕直接提到 | 探索 set_option 的其他选项如 display.width / display.precision；使用 reset_option 恢复默认 |
| DataFrame.head | 方法 | 获取 DataFrame 前 N 行；默认 5 行 | 字幕直接提到 | 配合 chunksize 使用验证每次读取的块内容；用于大数据集的快速预览 |
| DataFrame.tail | 方法 | 获取 DataFrame 后 N 行；默认 5 行 | 字幕直接提到 | 验证分块保存时最后一块的完整性；检查时间序列数据的最新记录 |

---

## 六、关键参数速查

### 6.1 read_* 系列参数

| 参数 | 类型 | 在本 P 中的作用 | 来源 | 后续可练习方向 |
|------|------|----------------|------|----------------|
| filepath / path | 参数 | 文件路径，必填项 | 字幕直接提到 | 练习使用相对路径和绝对路径；处理 URL 远程文件路径 |
| sep | 参数 | 分隔符，默认逗号；支持正则表达式 | 字幕直接提到 | 处理制表符分隔（`\t`）、分号分隔、多空格分隔；使用正则处理混合分隔符 |
| header | 参数 | 指定哪一行作为列名，默认第 0 行；header=None 表示无列名 | 字幕直接提到 | 处理列名在第 N 行的情况（header=N）；处理多行标题 |
| index_col | 参数 | 指定某列作为行索引 | 字幕直接提到 | 处理多级索引（index_col=[0,1]）；处理日期列作为索引 |
| names | 参数 | 自定义列名列表，类型为 list | 字幕直接提到 | 与 header=None 配合使用；处理列名需要清洗的场景 |
| skiprows | 参数 | 跳过文件开头的行数 | 字幕直接提到 | 跳过注释行；使用 callable 函数选择性跳过行 |
| nrows | 参数 | 只读取前 N 行，用于快速预览 | 字幕直接提到 | 结合 chunksize 做小样本测试；处理大文件时的快速检查 |
| chunksize | 参数 | 逐块读取参数，每次返回 N 行，返回可迭代对象 | 字幕直接提到 | 配合 break 精确控制读取范围；配合 enumerate 获取块编号 |

### 6.2 to_* 系列参数

| 参数 | 类型 | 在本 P 中的作用 | 来源 | 后续可练习方向 |
|------|------|----------------|------|----------------|
| path_or_buf | 参数 | 保存路径，必填项；与 read 的 filepath 对应 | 字幕直接提到 | 练习使用文件对象而非路径；输出到内存 BytesIO |
| encoding | 参数 | 文件编码格式；常用 UTF-8 和 GBK | 字幕直接提到 | 处理 GB2312、GB18030 等中文编码；统一使用 UTF-8-sig 处理带 BOM 的文件 |
| index | 参数 | 是否写出 DataFrame 的整型索引列；默认 True | 字幕直接提到 | 中国人写文件通常 index=False；保留索引以便后续读取恢复 |

---

## 七、工具配置参考

| 名称 | 类型 | 在本 P 中的作用 | 来源 | 后续可练习方向 |
|------|------|----------------|------|----------------|
| display.max_rows | 配置项 | 设置 DataFrame 显示的最大行数；None 表示不限制 | 字幕直接提到 | 设置合理的行数上限避免输出过长；用于日志记录时控制输出 |
| display.max_columns | 配置项 | 设置 DataFrame 显示的最大列数；None 表示不限制 | 字幕直接提到 | 处理超宽表格时的列数控制；结合 head/tail 配合使用 |

---

## 八、本 P 资源全景图

```
外部文件 ←─ CSV / Excel / JSON
                ↓
        pandas 库（核心依赖）
                ↓
    ┌───────────┼───────────┐
    ↓           ↓           ↓
read_*    to_*    set_option
    ↓           ↓           ↓
DataFrame  文件   Jupyter 显示控制
    ↑
    │
chunksize 迭代器（处理大文件）
    ↑
    │
Jupyter Notebook（运行环境）
```

---

## 九、补充说明

1. **编码问题是中文数据的痛点**：Windows 默认 GBK，跨平台推荐统一使用 UTF-8；遇到乱码优先排查 encoding 参数
2. **逐块迭代器是一次性的**：遍历后需要重新调用 read_csv 才能再次使用
3. **display 选项不影响数据本身**：只影响 Jupyter 中的可视化展示，便于调试但不会改变 DataFrame 实际内容
4. **读取和保存参数高度对称**：掌握 read_* 的关键参数后，to_* 的使用逻辑基本一致，只是方向相反
