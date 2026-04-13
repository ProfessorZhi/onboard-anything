---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 97-【数据分析】pandas入门
page_index: 97
page_title: 【数据分析】pandas入门
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P97 知识框架 - 【数据分析】pandas入门
## 本P位置

Python数据分析模块第1课/pandas入门第一课。承接Python基础语法，引入pandas数据分析包，为后续DataFrame、pandas进阶操作、数据可视化奠定基础。

## 核心问题

pandas如何处理一维带标签数据？Series作为pandas最基本的数据结构，其创建、索引、增删改查的操作规范是什么？

## 知识骨架

```
pandas
└── Series（一维带标签数组）
    ├── 创建：pd.Series(data, index, dtype, name)
    │   ├── data类型：list、dict、标量、numpy数组
    │   └── index：默认0起整数，可自定义，数量须与data匹配
    ├── 属性
    │   ├── .index → RangeIndex或自定义索引对象
    │   ├── .values → numpy一维数组
    │   └── .dtype → 数据类型
    ├── 索引访问
    │   ├── 标签索引：s['A']
    │   ├── 整数下标：s[0]
    │   └── 切片：s[1:4]（左闭右开，基于位置）
    ├── 布尔过滤：s[s > 3] → 返回满足条件的Series
    └── CRUD操作
        ├── Create/增：s.append(s2, ignore_index, verify_integrity)
        ├── Read/查：布尔索引、条件表达式
        ├── Update/改
        │   ├── 改值：s['A'] = 10
        │   ├── 改索引：s.reset_index(drop=True)
        │   └── 改类型：s.astype('str') → object类型
        └── Delete/删：s.drop('A') → 返回新Series，不修改原对象
```

## 关系与依赖

```
numpy（底层支撑）
    ↓
pandas（数据处理层）
    ├── Series（一维） ← 本P核心
    └── DataFrame（二维）→ 下节内容
```

## 输入 / 输出 / 前置 / 支撑

| 类别 | 内容 |
|---|---|
| **前置知识** | Python基础语法、列表/字典操作 |
| **底层依赖** | numpy（Series底层即numpy数组，可调用.max/.min/.mean/.sum） |
| **输入** | list、dict、标量、range对象、CSV/Excel文件 |
| **输出** | Series对象、numpy数组、标量值 |
| **支撑工具** | PyCharm（IDE）、pandas 1.3.2（版本锁定避免API差异） |

## 易错点

1. **append只接受Series或DataFrame**：传入list/range会报错，必须先用pd.Series()包装
2. **切片与标签索引的区别**：切片基于整数位置，标签索引基于自定义字符串
3. **drop不改变原对象**：必须赋值接收返回值
4. **drop不支持切片语法**：删除只能传标签列表
5. **类型转object后不可数值比较**：astype('str')后执行`>`会报错
6. **索引数量必须匹配**：创建时index长度与data长度不一致会报错
7. **ignore_index默认为False**：append后索引不连续需手动处理

## 外部资源与对象

| 资源/对象 | 角色 |
|---|---|
| **PyCharm** | 本课代码演示环境 |
| **pandas 1.3.2** | 指定版本，锁定API一致性 |
| **numpy** | pandas底层依赖，Series.values返回numpy数组 |
| **CSV** | pandas擅长处理的数据格式（爬虫输出常用） |
| **xlrd/xlwt** | pandas操作Excel的模块 |
| **驼峰命名法（camelCase）** | 代码规范，如userName，业界约定 |
