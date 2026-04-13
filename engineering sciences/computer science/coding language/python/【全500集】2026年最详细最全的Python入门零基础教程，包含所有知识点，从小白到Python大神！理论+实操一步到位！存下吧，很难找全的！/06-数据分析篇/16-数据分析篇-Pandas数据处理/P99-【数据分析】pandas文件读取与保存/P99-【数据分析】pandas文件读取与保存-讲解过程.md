---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 99-【数据分析】pandas文件读取与保存
page_index: 99
page_title: 【数据分析】pandas文件读取与保存
type: 讲解过程
tags:
  - 网课
  - 讲解过程
---

# P99 讲解过程 - 【数据分析】pandas文件读取与保存
## 本P定位

本P是pandas数据分析章节的延续，聚焦于数据的输入输出（I/O）操作。老师明确指出本P的核心目标是掌握"数据的加载存储"全流程：从外部文件读取数据 → 在Python中处理 → 再保存到指定位置。重点讲解CSV和Excel两类最常用的表格文件格式，以及当数据量巨大时如何通过"逐块读取"来分批处理避免内存溢出。

## 讲解过程

### 一、课程导入与内容概览

老师先进行自我介绍（"我是今天的主讲老师小夏老师"），然后开门见山点明主题：今天讲数据的加载存储，即文本格式的读取和保存。强调"中间的细节还是蛮多的"，提醒学生认真看。

**教学内容四大块：**

1. **读写文本格式的数据**（重点加粗标记）
2. **逐块读取**（针对大文件的分批处理策略）
3. **其他格式的读取与保存**

**支持的数据格式一览：**
老师展示了一张支持格式的汇总图，指出：
- CSV（read_csv）和Excel（read_excel）**加粗标注**，是必须掌握的核心
- JSON（前后端数据传输格式）次之
- HTML、MsgPack、Pickle等"基本上用不到"
- 强调：掌握CSV和Excel之后，其他格式"只是文本数据格式不同，操作流程一致"

---

### 二、read_csv 核心参数讲解

老师打开Jupyter Notebook，新建文件"df文件读取与保存"，开始实战演示。

**代码框架：**
```python
import pandas as pd
df = pd.read_csv(...)
```

老师指出read_csv的参数非常多（"你都得学一天了"），但只需要掌握几个关键参数。

**逐参数解析：**

| 参数 | 作用 | 示例 |
|------|------|------|
| **filepath** | 文件路径（必填） | `'data/数据一.csv'` |
| **sep** | 分隔符（正则表达式） | `,` `\t` |
| **header** | 哪一行作为列名 | 默认第0行；`header=None` 表示不使用 |
| **index_col** | 指定某列作为索引 | `index_col='时间'` |
| **names** | 自定义列名列表 | `names=['时间','姓名','学历','薪资范围','年龄','城市']` |
| **skiprows** | 忽略开头的行数 | `skiprows=1` 跳过第一行 |
| **nrows** | 只读取前N行 | `nrows=5` |

**演示步骤1：基础读取**
```python
df = pd.read_csv('data/数据一.csv')
print(df)
```
效果：默认把第一行数据作为列标签，索引从0开始自动生成。老师指出这样不合理。

**演示步骤2：去掉默认列名**
```python
df = pd.read_csv('data/数据一.csv', header=None)
```
效果：第一行变成普通数据行，列名改为0、1、2、3、4、5。

**演示步骤3：自定义列名**
```python
df = pd.read_csv('data/数据一.csv', header=None, 
                 names=['时间','姓名','学历','薪资范围','年龄','城市'])
```
效果：列名变成有意义的中文标签，数据可读性大幅提升。

**演示步骤4：指定索引列**
```python
df = pd.read_csv('data/数据一.csv', header=None,
                 names=['时间','姓名','学历','薪资范围','年龄','城市'],
                 index_col='时间')
```
效果："时间"列变成索引，不再是普通数据列。

**演示步骤5：跳过前N行**
```python
df = pd.read_csv('data/数据一.csv', header=None,
                 names=['时间','姓名','学历','薪资范围','年龄','城市'],
                 index_col='时间',
                 skiprows=1)
```
效果："张博"那条记录被跳过（忽略掉）。

**演示步骤6：只读取前N行**
```python
df = pd.read_csv('data/数据一.csv', header=None,
                 names=['时间','姓名','学历','薪资范围','年龄','城市'],
                 index_col='时间',
                 nrows=5)
```
效果：只读取5行数据。

---

### 三、逐块读取（Chunked Reading）

老师回到开头提出的问题：数据量很大怎么办？比如1000行、1万行、10万行的Excel表格。

**核心语法：chunksize参数**
```python
pd.read_csv('data/数据一.csv', chunksize=1000)
```
含义：每次读取1000行，返回一个可迭代对象。

**实战演示：切换大数据集**

老师发现演示用的"数据一"只有16行，不够演示效果，改用另一个更大的数据集——"某招聘网站数据"。

```python
df = pd.read_csv('data/某招聘网站数据.csv')
print(df)
```

**数据预览的显示控制：**

老师发现数据量太大时Jupyter会截断显示（中间只显示"..."），于是介绍两个显示控制参数：

```python
# 控制行数显示
pd.set_option('display.max_rows', None)  # 显示全部行

# 控制列数显示  
pd.set_option('display.max_columns', None)  # 显示全部列
```

老师解释：display就是"布局"的意思（前端同学应该熟悉），设置max为None表示不限制。

**逐块读取完整代码：**
```python
number = 25
chunk_iter = pd.read_csv('data/某招聘网站数据.csv', chunksize=number)

for i, item in enumerate(chunk_iter):
    print(f'第{i}块')
    # item是DataFrame对象，可以进行DataFrame操作
```

老师解释数据共105行、52列，分25行一块的话会循环4次（100行），剩余5行单独一块。

---

### 四、数据保存（to_csv）

老师讲解保存操作的对应关系：**读取用read，保存用to**。

**to_csv参数一览：**

| 参数 | 作用 |
|------|------|
| path_or_buf | 保存路径（必填） |
| encoding | 编码格式（常用UTF-8、GBK） |
| index | 是否保留索引列 |
| 其他 | 与读取参数类似，如只保存部分行等 |

**分块保存实战：**

需求：将大数据集按每25行切分成多个文件保存。

```python
number = 25
number2 = 0
chunk_iter = pd.read_csv('data/某招聘网站数据.csv', chunksize=number)

for i, item in enumerate(chunk_iter):
    if number2 >= 100:  # 超过100行就停止
        break
    item.to_csv(f'data/某招聘网站数据_{number2}.csv', index=False, encoding='utf-8')
    print(f'第{i}块保存成功')
    number2 += number
```

**报错排查：**

老师演示时遇到错误"对象不可订阅"——因为之前忘记写`for`循环直接对迭代器调用了某个方法（具体错误信息未完整保留在字幕中）。通过添加`for i, item in enumerate(chunk_iter)`解决了问题。

**输出结果验证：**
- 第0块：0~24行
- 第1块：25~49行
- 第2块：50~74行
- 第3块：75~99行
- （第4块开始被break跳过了）

---

### 五、head/tail切片补充

老师顺便回顾之前学过的DataFrame切片方法，提醒学生注意：

| 方法 | 功能 |
|------|------|
| df.head(n) | 获取前n行（默认5行） |
| df.tail(n) | 获取后n行（默认5行） |

在逐块读取的场景下，chunksize参数本身就是一种切片操作，可以精确控制每次读取的行数。

---

## 提到的外部资源与对象

| 资源名称 | 类型 | 在本P中的作用 |
|----------|------|---------------|
| **数据一.csv** | 示例数据文件 | 用于演示read_csv基础读取 |
| **某招聘网站数据.csv** | 大数据文件（105行52列） | 用于演示逐块读取chunksize |
| **Jupyter Notebook** | 开发环境 | 老师演示代码的IDE |
| **JSON** | 数据格式 | 老师顺带提及是前后端交互的文本传输格式 |

## 本P结论

1. **read_csv是最核心的读取方法**，必须掌握filepath、header、index_col、names、skiprows、nrows这6个常用参数
2. **逐块读取通过chunksize参数实现**，返回可迭代对象，配合for循环分批处理大文件，避免内存溢出
3. **保存操作用to_csv**，读取和保存的参数逻辑高度对称，只是方向相反
4. **编码问题不可忽视**，中文字符集常用UTF-8和GBK两种格式
5. **display选项可控制Jupyter的显示行数列数**，避免大数据被截断显示
6. **分块读取配合break语句**可以精确控制读取范围，防止越界
