---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 98-【数据分析】pandas入门2df常见操作
page_index: 98
page_title: 【数据分析】pandas入门2df常见操作
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P98 知识框架 - 【数据分析】pandas入门2df常见操作
## 本P位置

Python数据分析→pandas入门→P97末尾创建报错→P98系统纠错与进阶
作用：从"能跑通"到"理解原理"，为后续数据筛选、文件读取、可视化打桩

## 核心问题

DataFrame怎么建、怎么查、怎么切

## 知识骨架

**DataFrame创建→属性查询→数据切片** 三层递进

创建层（六种）：
- 空DataFrame
- NumPy数组直接转
- 指定index参数
- **字典创建**（外套list）
- **zip()打包**多列表
- 字典组成的列表

属性层（五个）：
- shape→维度元组
- dtypes→列类型（object≈string）
- values→二维数组（纯数据）
- index→索引对象
- ndim→维度数

切片层（两种）：
- **loc**→标签索引
- **iloc**→位置索引

## 关系与依赖

NumPy数组 → 概念基底（shape、ndim直接沿用）
zip() → 数据打包工具 → 输入list，输出tuple列表
字典 → 键值对结构 → 外套list变成"字典的列表"
pandas → 封装层 → 底层调NumPy，上层输出Series/DataFrame
head/tail → 依赖shape存在才能看效果

## 输入 / 输出 / 前置 / 支撑

| 节点 | 输入 | 输出 | 前置 | 支撑 |
|---|---|---|---|---|
| DataFrame创建 | list/dict/np.array | DataFrame对象 | Python基础数据结构 | NumPy |
| shape | - | (m,n)元组 | DataFrame存在 | NumPy shape概念 |
| dtypes | - | Series对象 | DataFrame存在 | Python类型系统 |
| values | - | 二维ndarray | DataFrame存在 | NumPy数组 |
| index | - | RangeIndex对象 | DataFrame存在 | - |
| ndim | - | int（固定为2） | DataFrame存在 | NumPy ndim |
| loc | 标签（int/str/slice） | Series/DataFrame | 列名或行索引 | DataFrame.index |
| iloc | 位置（int/slice） | Series/DataFrame | 整数下标 | Python切片规则 |

## 易错点

**创建类**：
- 字典传给DataFrame不加外套list → TypeError
- zip()结果直接用会得到tuple列表 → 需外套list转
- 数据长度不一致 → 填充NaN而非报错（pandas比NumPy宽松）

**属性类**：
- object类型是string的父类 → astype('string')可转换
- index返回的是对象不是列表 → list(df.index)转换

**切片类**：
- **loc切片是左闭右开** → df.loc[1:4]取1,2,3而非1,2,3,4
- loc用标签，iloc用位置，混淆会导致取错行
- head(n)参数超范围不报错，自动返回所有

## 外部资源与对象

**工具层**：
NumPy (np) → DataFrame内部数据存储依赖二维数组概念
pandas → 本集主角，离散点：创建→属性→切片

**数据层**：
zip() → 多列表打包成元组列表，快速构建DataFrame数据源
Excel文件 → 后续真实数据来源（替代手动构造）

**练习层**：
pandas 120题/300题 → 本集知识点对应基础题库
pyecharts → 数据可视化收口（需要DataFrame作为输入）
