---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 100-【数据分析】pandas的常见操作1
page_index: 100
page_title: 【数据分析】pandas的常见操作1
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P100 知识框架 - 【数据分析】pandas的常见操作1
## 本P位置

- 课程模块：数据分析 → pandas进阶
- 系列定位：pandas常见操作系列·第一讲
- 前置知识：pandas基本属性、读取保存（data1.csv）
- 后续衔接：数据合并三种方式（下一P内容）

## 核心问题

1. 如何修改DataFrame的行索引和列名
2. 如何向DataFrame添加新列/新行
3. 如何垂直拼接两个DataFrame

## 知识骨架

```
pandas DataFrame 操作层
├── 修改层
│   ├── 行索引修改
│   │   ├── df.index = np.arange()        # 全量替换
│   │   └── df.rename(index={}, inplace)  # 选择性修改
│   └── 列名修改
│       ├── df.columns = [列表]           # 批量替换
│       └── df.rename(columns={})         # 选择性修改
├── 扩充层
│   ├── 添加列：df[新列名] = 数据          # 直接赋值
│   └── 添加行：df.append(字典, ignore_index)
└── 拼接层
    └── df1.append(df2)                    # 垂直拼接
```

## 关系与依赖

| 操作 | 依赖项 | 产出 |
|------|--------|------|
| 行索引全量修改 | numpy.arange() | 新索引对象 |
| 添加列 | numpy.random.randint() | 新Series |
| 添加行 | ignore_index参数 | 新DataFrame |
| 拼接 | 两个DataFrame结构兼容 | 合并DataFrame |

关键依赖链：numpy → DataFrame修改 → DataFrame扩充 → DataFrame拼接

## 输入 / 输出 / 前置 / 支撑

- **输入**：data1.csv（原始DataFrame）、numpy数组/随机数
- **输出**：修改后的DataFrame
- **前置**：df基本属性、df读取保存
- **支撑**：numpy库（生成索引序列、随机数列）

## 易错点

- df.index[下标] = 值 → 无效，需整体赋值
- df.columns = [列表] → 列表长度必须==列数
- 添加列数据长度必须==df行数
- df.append() → 不修改原对象，必须接收返回值
- df.append(df2) → 索引保持原值，不自动连续

## 外部资源与对象

| 资源 | 角色 | 关系 |
|------|------|------|
| data1.csv | 基础数据源 | 本P所有操作的输入对象 |
| numpy | 工具库 | 提供np.arange()、np.random.randint() |
| pandas | 核心库 | 本P所有操作的主语 |
