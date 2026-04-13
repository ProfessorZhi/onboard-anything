---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 90-【数据分析】numpy的简介和数组的创建
page_index: 90
page_title: 【数据分析】numpy的简介和数组的创建
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P90 知识框架 - 【数据分析】numpy的简介和数组的创建
## 本P位置

数据分析章节·入门第一课。前置章节：Python解释器安装、PyCharm环境配置。本P承上启下：上承环境准备，下启NumPy数组属性、运算、索引切片等核心内容。

## 核心问题

- NumPy为何比Python列表快10倍？
- 一维数组有哪几种创建路径？
- 二维数组的本质是什么？

## 知识骨架

### 1. NumPy定位

Numerical Python。Python数值计算基石。核心对象：ndarray（N维数组）。核心能力：基于元素的快速计算、线性代数、矩阵运算。

### 2. ndarray 性能优势

性能对比结论：NumPy数组求和 vs Python列表求和，NumPy快约10倍。原因：底层C实现，向量化操作，无需Python解释器逐个元素遍历。

### 3. 一维数组创建方法

| 方法 | 函数/语法 | 特点 |
|------|----------|------|
| 传入range | np.array(range(n)) | 转换生成 |
| 传入列表 | np.array([0,1,2,3,4]) | 直接构造 |
| 传入元组 | np.array((0,1,2,3,4)) | 直接构造 |
| np.arange | np.arange(start,stop,step) | 左开右闭，固定步长，类似range |
| np.linspace | np.linspace(start,stop,num) | 均匀分布生成样本，默认50个 |

### 4. 二维数组创建

本质：列表嵌套列表。语法：np.array([[...], [...]])。要求：内层列表长度必须一致。

## 关系与依赖

```
PyCharm (开发环境)
    ↓ 创建项目，运行代码
NumPy (第三方库，版本1.19.2)
    ↓ 核心对象
ndarray
    ↓ 一维创建
arr + np.arange / np.linspace
    ↓ 二维创建
嵌套列表 → np.array([[], []])
    ↓ 性能验证
time.time() (标准库) → 计时
```

## 输入 / 输出 / 前置 / 支撑

| 角色 | 说明 |
|------|------|
| 输入 | Python range对象、列表、元组、数值参数 |
| 输出 | numpy.ndarray 类型对象 |
| 前置依赖 | Python基础语法、PyCharm环境、pip包管理 |
| 支撑工具 | time模块（计时）、pip（安装NumPy） |

## 易错点

1. 版本差异导致方法行为不一致 → 建议统一使用numpy==1.19.2
2. 执行顺序不影响性能测试结果 → time.time()独立计时，排除顺序干扰
3. linspace（均匀分布）≠ arange（固定步长）→ 使用场景不同
4. 二维数组必须是两层嵌套 → 一层是列表不是二维，三层是三维
5. 内层列表长度不一致 → NumPy报错

## 外部资源与对象

| 资源 | 类型 | 作用 | 关联 |
|------|------|------|------|
| PyCharm | 开发工具 | 项目管理、代码编写运行 | 环境基础 |
| NumPy 1.19.2 | 第三方库 | 本课核心，数值计算 | pip install numpy==1.19.2 |
| time.time() | 标准库函数 | 性能计时 | 性能对比验证 |
| pip | 包管理工具 | 查看/安装包 | pip list / pip install |
| numpy.ndarray | 数据结构 | NumPy核心对象 | 本课所有输出的类型 |
