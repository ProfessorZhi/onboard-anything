---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 98-【数据分析】pandas入门2df常见操作
page_index: 98
page_title: 【数据分析】pandas入门2df常见操作
type: 资源清单
tags:
  - 网课
  - 资源清单
---

# P98 资源清单 - 【数据分析】pandas入门2df常见操作
## 资源列表

**pandas**
- 类型：Python库
- 在本P中的作用：DataFrame操作的核心库，承担所有数据创建、属性查询、索引切片的演示任务
- 来源：字幕直接提到
- 建议方向：熟练掌握DataFrame对象的创建方式（六种）和常用属性方法，理解其与NumPy数组的底层关联

**NumPy（np）**
- 类型：Python库
- 在本P中的作用：提供np.arange()创建测试数组，作为DataFrame的数据来源之一；同时DataFrame的shape、ndim、values等概念直接沿用NumPy的维度思想
- 来源：字幕直接提到
- 建议方向：结合NumPy二维数组的概念理解DataFrame的行列结构，为后续数据处理打基础

**zip()函数**
- 类型：Python内置函数
- 在本P中的作用：将多个列表（names、ages、genders）打包成元组列表，作为DataFrame的高效数据构造方式
- 来源：字幕直接提到
- 建议方向：练习zip与list的转换组合，掌握多列表快速合并构建DataFrame的用法

**Excel文件**
- 类型：数据文件格式
- 在本P中的作用：老师预告后续会用pandas读取Excel文件作为数据来源，替代手动构造数据的方式
- 来源：基于上下文推断（老师明确提到后续会用Excel文件）
- 建议方向：了解pd.read_excel()的基本用法，为真实数据分析场景做准备

**pandas 120题 / pandas 300题**
- 类型：练习题库
- 在本P中的作用：老师预告后续会提供的练习资源，覆盖DataFrame创建、属性查询、切片等知识点
- 来源：字幕直接提到
- 建议方向：在掌握本集内容后，通过做题检验六种创建方法和loc/iloc切片的使用熟练度

**pyecharts**
- 类型：Python可视化库
- 在本P中的作用：老师预告后续会结合pandas进行数据可视化，DataFrame作为数据输入源
- 来源：字幕直接提到
- 建议方向：了解pyecharts的基本图表类型，理解DataFrame与可视化工具的数据对接流程

## 资源关联图

```
NumPy ──────► pandas ──────► pyecharts
 (底层依赖)     (本集主角)      (可视化收口)
    ▲
    │
zip() ────► Excel文件
(数据打包)    (后续数据源)
    │
    └──► pandas 120题/300题
              (练习验证)
```

## 资源获取优先级

| 优先级 | 资源 | 说明 |
|---|---|---|
| 必须 | pandas、NumPy | pip install pandas numpy |
| 内置 | zip() | Python标准库，无需安装 |
| 后续 | Excel文件 | 真实数据集，可自行准备CSV替代 |
| 后续 | pandas 120题/300题 | 搜索GitHub或老师提供的资源 |
| 后续 | pyecharts | pip install pyecharts |
