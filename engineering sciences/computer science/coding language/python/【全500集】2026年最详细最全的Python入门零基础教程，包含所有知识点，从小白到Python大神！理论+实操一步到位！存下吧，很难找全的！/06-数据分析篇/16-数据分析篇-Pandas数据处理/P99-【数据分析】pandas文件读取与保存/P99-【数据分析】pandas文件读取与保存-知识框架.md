---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 99-【数据分析】pandas文件读取与保存
page_index: 99
page_title: 【数据分析】pandas文件读取与保存
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P99 知识框架 - 【数据分析】pandas文件读取与保存
## 本P位置
pandas数据分析章节 → 数据准备阶段 → 与数据清洗、可视化、统计分析形成数据处理流水线

## 核心问题
如何高效完成外部文件与DataFrame之间的双向转换，以及如何在大文件场景下避免内存溢出

## 知识骨架

```
外部文件 ←→ DataFrame
     ↑
  read_csv / read_excel  ←→  to_csv / to_excel
     ↑
  核心参数体系（6个）
     ↑
  逐块读取 ←→ 大文件分批处理
```

**read_csv参数优先级**

| 层级 | 参数 | 说明 |
|------|------|------|
| 必须 | filepath | 文件路径 |
| 高频 | header | 列名行位置（None=无列名） |
| 高频 | names | 自定义列名列表 |
| 高频 | index_col | 指定索引列 |
| 辅助 | skiprows / nrows | 跳过行 / 只读前N行 |
| 辅助 | sep | 分隔符（正则） |

**逐块读取机制**

- 参数：chunksize=N → 返回可迭代对象，每次yield N行DataFrame
- 典型用法：配合for循环 + break精确控制读取范围
- 应用场景：文件>内存容量时必须使用

**to_csv对称参数**

- filepath → path_or_buf
- 编码：encoding（UTF-8 / GBK）
- 索引：index（是否写出自动生成的整型索引）

## 关系与依赖

```
前置知识：pandas数据结构（Series/DataFrame）→ 本P：数据加载存储
          ↓
后续知识：本P → 数据清洗 → 可视化 → 统计分析
```

**模块间关系**

- read_* 系列（read_csv、read_excel） → 返回DataFrame
- to_* 系列（to_csv、to_excel） → 接收DataFrame
- chunksize迭代器 → 每次产出DataFrame子集
- display选项 → 仅影响Jupyter显示，不影响数据本身

## 输入 / 输出 / 前置 / 支撑

| 类型 | 内容 |
|------|------|
| 输入 | CSV文件路径、Excel文件路径、字节流 |
| 输出 | DataFrame对象（read_*）、文件（to_*） |
| 前置 | pandas库导入、文件存在性检查 |
| 支撑 | Jupyter Notebook环境、display选项控制 |

## 易错点

1. **header默认第0行** → 不想用第一行当列名时必须显式设header=None
2. **中文编码** → Windows默认GBK，跨平台需指定encoding='utf-8'
3. **逐块迭代器只能遍历一次** → 遍历后需重新read_csv才能再次使用
4. **to_csv默认写出索引列** → 中国人写文件通常index=False
5. **chunksize + break组合** → 防止读取超出预期范围

## 外部资源与对象

| 名称 | 类型 | 作用 |
|------|------|------|
| CSV | 文件格式 | 最通用的表格数据交换格式 |
| Excel | 文件格式 | 商业场景标配，含多sheet支持 |
| JSON | 文件格式 | 前后端数据传输格式，本P次要掌握 |
| Jupyter Notebook | 开发环境 | 本P演示载体 |
| 数据一.csv | 示例数据 | 小型数据集（16行），演示基础参数 |
| 某招聘网站数据.csv | 示例数据 | 大型数据集（105行52列），演示逐块读取 |
