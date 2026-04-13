---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 97-【数据分析】pandas入门
page_index: 97
page_title: 【数据分析】pandas入门
type: 讲解过程
tags:
  - 网课
  - 讲解过程
---

# P97 讲解过程 - 【数据分析】pandas入门
## 本P定位

本P是pandas数据分析系列的入门第一课。老师首先介绍pandas的概念与功能，明确学习目标（版本1.3.2），随后在PyCharm中通过代码演示的方式，带领学生从零认识Series对象的基本用法，包括创建、索引访问、切片、布尔过滤，以及增删改查四项基本操作。本P为后续学习DataFrame打下基础。

---

## 讲解过程

### 一、开场与本课目标说明

- 自我介绍为小肖老师，宣布正式进入pandas学习。
- 回顾上节课已安装pandas，指定本课统一使用版本 **1.3.2**，强调版本一致性是为了避免API调用和参数差异导致的排错困难。
- 预告本课四大模块：**pandas简介** → **pandas安装（已安装）** → **Series入门** → **DataFrame入门**。

### 二、pandas是什么——概念与能力介绍

- pandas是建立在numpy之上的第三方包，核心优势在于**处理任意类型数据**，而numpy只能处理数值数组。
- 列举pandas能处理的数据类型：数字、字符串、时间序列、分组、排序等。
- 重点强调**表格处理能力**：CSV文件（爬虫常用存储格式）、Excel文件（xlrd/xlwt），能够同时管理**行标签和列标签**。
- 数据可以直接放入结构中，无需预先标记。

### 三、Series的基本用法——PyCharm代码演示

#### 1. 环境准备与导入规范

- 打开PyCharm，新建Python文件（命名如`pandas-series创建.py`）。
- 导入语句：`import pandas as pd`，说明`pd`是业界约定俗成的别名，虽可自定义但应遵循规范，便于团队协作时他人阅读代码。

#### 2. 命名规范穿插讲解

- 提到驼峰命名法（camelCase）：多个单词拼接，每个单词首字母大写，如`userName`。
- 说明：规范不是强制，但遵循约定能大幅提升代码可读性，减少协作障碍。

#### 3. Series对象的创建

- 基本语法：`pd.Series(data, index, dtype, name)`
- 演示用list创建Series：
  ```python
  lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  s = pd.Series(lst)
  ```
- 运行后观察输出结构：**左侧是索引（默认0起）**，**右侧是数据值**，**无列名**（因为Series是一维结构）。
- 指定自定义索引：`index=['A', 'B', 'C', 'D', 'E', 'F']`
- 强调：索引数量必须与数据长度匹配，否则报错。
- 补充：Series也支持直接传入字典创建，但老师指出这种用法意义有限，因为Series的长处在于一维顺序结构，字典更适合后续的DataFrame场景。

#### 4. Series的索引与切片

- **索引访问**：通过索引标签取值，如`s['D']`。
- **行号访问**：通过整数下标取值，行为与numpy数组一致。
- **布尔索引**：演示筛选大于3的元素 `s[s > 3]`，返回满足条件的Series。
- **切片操作**：`s[1:4]`，遵循左闭右开原则。老师特别指出切片与标签索引的区别：切片使用整数位置，标签索引使用自定义标签。

#### 5. Series的属性

- `.index`：查看索引，返回RangeIndex类型（自动生成的整数序列）或自定义索引对象。
- `.values`：查看数据值，返回numpy一维数组对象。
- 说明Series的数据底层是numpy数组，因此可以调用numpy的统计函数如`.max()`、`.min()`、`.mean()`、`.sum()`等。
- `.dtype`：查看数据类型。
- `.sort_values()`：对值排序，返回排序后的新Series（老师演示时补充，可能因时间未完整展开）。

### 四、Series的增删改查——完整操作演示

#### 1. 增加（append）

- 查找Series的添加方法：尝试寻找`insert`方法，发现不存在，最终定位到`append`方法。
- 错误尝试1：传入`range(7, 9)`，报错 *"cannot concatenate object of type '<class 'range'>'; only Series and DataFrame are valid"*。说明**append只接受Series或DataFrame对象**。
- 正确写法：先将数据包装为Series，再append：
  ```python
  temp = range(7, 9)
  s2 = pd.Series(temp)
  s = s.append(s2)
  ```
- 讲解`append`的参数：
  - `ignore_index`：默认为**False**。设为**True**时，合并后自动生成0起的连续整数索引，忽略原Series的自定义索引。
  - `verify_integrity`：默认为**False**。设为**True**时，如果新Series中存在与原Series重复的索引标签，则报错，确保索引唯一性。

#### 2. 删除（drop）

- Series对象**没有`delete`方法**，删除需使用`drop`。
- 传入索引标签删除单个或多个：`s.drop('2')`、`s.drop(['3', '2'])`。
- **不支持切片语法**作为删除条件，只接受标签列表。
- 删除后返回新Series，原Series不变（需要赋值接收）。

#### 3. 修改

- **修改索引**：`s.reset_index()`，将当前索引重置为列，原数据不变。
  - `drop=True`：删除原索引列，生成0起的新索引。
- **修改值**：直接通过索引赋值，如`s['1'] = 3`。
- **修改类型**：使用`astype()`方法。
  - 演示将int转为string：`s = s.astype('str')`，类型变为object（老师解释：object在pandas中等价于string，代表任意类型）。
  - 强调：类型修改后，原有的数值比较运算（如`>`）会报错，因为字符串不支持算术运算符。

#### 4. 查询

- 主要是**布尔索引**，即通过条件表达式筛选数据，如`s[s > 5]`。
- 老师在修改类型后演示：若Series已是object类型，再做数值比较会触发错误 *"'>' not supported between instances of 'str' and 'int'"*。

### 五、本课收尾与下节预告

- 总结本课内容：pandas简介、安装版本、Series基本用法（创建、索引、切片、布尔过滤）、增删改查操作。
- 预告下一P将正式学习**DataFrame**对象，这是pandas的核心数据结构。

---

## 提到的外部资源与对象

| 外部资源/对象 | 角色与说明 |
|---|---|
| **PyCharm** | 本课代码演示的IDE环境，老师全程在PyCharm中新建文件、编写代码、运行调试。 |
| **pandas 1.3.2** | 明确指定的安装版本，用于避免版本差异导致的API不一致问题。 |
| **numpy** | pandas建立在numpy之上；Series的底层数据是numpy数组，可以调用numpy函数。 |
| **CSV文件** | 爬虫常用数据存储格式，pandas擅长处理。 |
| **xlrd / Excel文件** | pandas处理Excel表格的模块，说明pandas的表格处理能力。 |
| **驼峰命名法（camelCase）** | 编程命名规范，老师穿插讲解，提到`userName`等示例。 |

---

## 本P结论

1. **pandas定位**：建立在numpy之上的高级数据分析包，核心优势是能处理任意类型数据（数字、字符串、时间序列等），尤其擅长表格操作（CSV、Excel）和带标签的数据管理。
2. **安装版本统一**：建议使用1.3.2版本，减少因版本差异导致的排错成本。
3. **Series对象**：一维带索引的数据结构，底层是numpy数组。支持创建（list/dict）、索引访问、切片、布尔过滤、增（append）、删（drop）、改（值/索引/类型）、查（布尔索引）。
4. **append注意事项**：只能拼接Series或DataFrame；`ignore_index=True`可重置索引；`verify_integrity=True`可强制索引唯一。
5. **类型转换**：`astype()`可改类型；object类型等价于字符串，执行数值比较会报错。
6. **下节预告**：DataFrame是pandas的核心二维数据结构，下一P将系统学习。
