---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 75-【网络爬虫】jsonpath数据提取和案例
page_index: 75
page_title: 【网络爬虫】jsonpath数据提取和案例
type: 讲解过程
tags:
  - 网课
  - 讲解过程
---

# P75 讲解过程 - 【网络爬虫】jsonpath数据提取和案例
## 本P定位

本P是网络爬虫章节中 JSONPath 数据提取技术的讲解与实战。前置知识为 Xpath 提取和简单的 HTTP 请求，本P在此基础上处理**多层级嵌套、结构复杂的 JSON 数据**如何选择性提取目标字段。

---

## 讲解过程

### 1. 问题引入：从简单数据到复杂 JSON

**教学推进：**

- 回顾前几P的腾讯社招案例，指出其数据结构简单（每条数据在同一层级）。
- 提出问题：如果遇到**返回数据层级深、嵌套多、且只想要部分字段**的情况怎么办。
- 明确本P任务：从复杂的 JSON 后台数据中有选择地提取目标字段。

**演示对象：**

- 打开小饭桌网站（金融投资资讯平台），演示其数据通过 AJAX 异步加载。
- 在开发者工具中抓包，找到返回的 JSON 数据。
- 展示数据结构：外层 `code`、`data`，`data` 内每条资讯字段众多（标题、作者、日期、正文、图片等），但目标只取标题、作者、日期三个字段。

**关键结论：** 对于深层嵌套的 JSON 数据，需要专门的路径定位工具来提取，即 JSONPath。

---

### 2. JSONPath 概念引入与类比

**教学推进：**

- 解释 JSONPath 的本质：**对 JSON 数据进行路径定位的工具**。
- 与 Xpath 进行类比：

| 工具 | 适用场景 |
|------|----------|
| Xpath | 提取 HTML / XML 文档内容 |
| JSONPath | 提取 JSON 数据内容 |

- 概括爬虫数据来源的两种格式：

| 类型 | 格式 |
|------|------|
| 结构化数据 | JSON / XML |
| 非结构化数据 | 嵌在网页中的原始文本 |

**关键结论：** 非结构化数据用 Xpath 或正则；结构化 JSON 数据用 JSONPath。

---

### 3. JSON 与 Python 数据格式对照（前置知识铺垫）

**教学推进：**

- 对照讲解 JSON 和 Python 的数据类型对应关系：

| JSON 格式 | Python 格式 |
|-----------|-------------|
| 对象 `{key: value}` | 字典 `dict` |
| 数组 `[val1, val2]` | 列表 `list` |
| 布尔值 `true / false` | 布尔值 `True / False`（**首字母大写**） |
| 空值 `null` | 空值 `None` |
| 字符串必须用**双引号** | 字符串可用单/双引号 |

- 强调 JSON 的强制规范：**字符串必须用双引号**，单引号会报错。
- 演示在 JSON 文件中写一个示例数据（含对象、数组、布尔值、空值、中文），格式化后展示。
- 强调 `true / false / null` 在 JSON 中**全部小写**，与 Python 不同。

**关键结论：** JSON 数据本质是字符串（JSON 字符串），需转换为 Python 对象后才能在代码中处理。

---

### 4. Python json 模块：数据格式互转

**教学推进：**

- 引入 Python 内置模块 `json`（无需安装，直接 import）。
- 讲解该模块的核心方法：

| 方法 | 作用 |
|------|------|
| `json.loads(JSON字符串)` | JSON 字符串 → Python 对象（字典/列表） |
| `json.dumps(Python对象)` | Python 对象 → JSON 字符串 |

**演示一：读取 JSON 文件并转换**

- 新建文件 `data.json`，写入 JSON 数据。
- 用 `open()` 读取文件内容得到字符串，赋值给变量 `json_data`。
- `print(type(json_data))` 确认是字符串类型。
- 调用 `json.loads(json_data)`，得到 Python 字典/列表对象。
- 对比转换前后 `true → True`、`false → False`、`null → None` 的变化。

**演示二：Python 对象转 JSON 字符串**

- 定义一个 Python 字典（含布尔值和中文）。
- 调用 `json.dumps(data2)`，观察输出的变化（True 变回 true、中文默认转为 Unicode）。
- 讲解 `ensure_ascii=False` 参数：设为 False 时保留中文原文输出。

**演示三：文件级读写方法（简化写法）**

| 方法 | 作用 |
|------|------|
| `json.load(文件句柄)` | 从文件直接读取并转换为 Python 对象 |
| `json.dump(数据, 文件句柄)` | 将 Python 数据直接写入文件（无需手动转字符串） |

- 演示 `json.dump(data2, f, ensure_ascii=False, indent=4)`：写入文件并格式化缩进。
- 演示 `json.load(f)`：从文件直接读取为 Python 对象（注意 open 模式用 `r`）。
- 对比两种写入方式：手动转字符串写入 vs 直接用 `json.dump`。
- 对比两种读取方式：手动 read + loads vs 直接用 `json.load`。

**关键结论：** `json.loads` 和 `json.dumps` 处理字符串层面的转换；`json.load` 和 `json.dump` 处理文件层面的直接读写。

---

### 5. JSONPath 语法入门

**教学推进：**

- 安装：`pip install jsonpath`
- 导入：`from jsonpath import jsonpath`
- 语法要素讲解：

| 语法 | 含义 |
|------|------|
| `$` | 根节点（整个 JSON 数据的最外层） |
| `.key` | 取子节点（直接子级） |
| `..key` | 递归搜索（不考虑层级，在任意位置匹配） |
| `[index]` | 数组索引取值 |

**演示：使用准备好的 JSON 数据（从小饭桌抓取的原始数据）**

- 将 JSON 数据写入 `data.json` 文件。
- 用 `json.load()` 读取到变量 `data`。
- **提取标题**：`jsonpath(data, '$.data[0].title')` → 提取第一条资讯的标题。
- **提取作者**：`jsonpath(data, '$..author')` → 递归搜索所有 author 字段。
- **提取作者图片**：`jsonpath(data, '$.data[0].author.photo')` → 先定位作者，再找其下的图片字段。
- **提取时间**：`jsonpath(data, '$..pubDate')` → 递归搜索所有日期字段。
- 每次提取后 `print` 查看结果，指出返回的都是列表（即使只有一个值），需要索引取值 `[0]`。

**与字典取值的对比：** 字典嵌套深时逐级取值写得很长，JSONPath 用路径表达式一行搞定。

**关键结论：** JSONPath 通过路径表达式精确定位 JSON 中的目标字段，`$` 代表根，`.` 取子节点，`..` 递归搜索。

---

### 6. 实战案例：小饭桌融资资讯爬虫

**教学推进：**

#### 6.1 数据来源分析

- 打开小饭桌网站，找到"融资消息"分类。
- 点击"查看更多"，在开发者工具 Network 中抓取 AJAX 请求包。
- 找到目标接口，复制请求 URL 和参数。
- 解读 URL 参数含义：
  - `p`：页码
  - `n`：每页条数
  - `type`：消息类型（如热点、最新资讯、融资消息）

#### 6.2 单页抓取实现

**代码步骤：**

1. `import requests`
2. `from jsonpath import jsonpath`
3. 定义目标 URL（含分页参数占位）
4. 发起请求，先测试能否直接访问（不带头部）
5. 调用 `response.json()` 直接获取 Python 对象（等同于 `json.loads(response.text)`）
6. 打印 `result` 确认数据结构

**代码示例（简化版）：**

```python
import requests
from jsonpath import jsonpath

url = "https://www.xiaofanzhuo.com/api/xxx?p=1&n=5&type=hot"
response = requests.get(url)
result = response.json()
```

#### 6.3 遍历提取目标字段

- 确认数据在 `result['data']` 中。
- 写 `for item in result['data']` 遍历每条资讯。
- 分别用 JSONPath 提取：

```python
title = jsonpath(item, '$.title')[0]
author_name = jsonpath(item, '$.author.name')[0]
author_photo = jsonpath(item, '$.author.photo')[0]
pub_date = jsonpath(item, '$.pubDate')[0]
print(title, author_name, author_photo, pub_date)
```

#### 6.4 翻页抓取与问题排查

- 外层套 `for i in range(1, 10)` 循环翻页。
- 用字符串格式化拼接 URL：`url.format(i)`。
- **问题一**：第0页无数据。**解决**：从第1页开始。
- **问题二**：`TypeError: 'bool' object is not iterable`。**分析**：某些记录缺少 author 字段，递归搜索时返回了布尔值。**排查方式**：打断点逐条观察，发现部分数据的 author 值为空。
- 强调**断点调试**在爬虫开发中的重要性：通过 Debug 模式逐行执行，观察每一步的变量值，快速定位问题数据。

#### 6.5 最终代码框架

```python
import requests
from jsonpath import jsonpath

for page in range(1, 10):
    url = f"https://www.xiaofanzhuo.com/api/xxx?p={page}&n=5&type=hot"
    response = requests.get(url)
    result = response.json()
    
    for item in result['data']:
        title = jsonpath(item, '$.title')[0]
        author_name = jsonpath(item, '$.author.name')[0]
        author_photo = jsonpath(item, '$.author.photo')[0]
        pub_date = jsonpath(item, '$.pubDate')[0]
        print(title, author_name, author_photo, pub_date)
```

---

## 提到的外部资源与对象

| 资源/对象 | 角色 |
|-----------|------|
| **小饭桌网站**（xiaofanzhuo.com） | 本P演示用目标网站，金融投资资讯平台，数据通过 AJAX 异步加载 |
| **jsonpath 库** | Python 第三方库，通过 `pip install jsonpath` 安装，用于 JSON 路径表达式提取 |
| **Python 内置 json 模块** | 无需安装，用于 JSON 字符串与 Python 对象的互相转换，以及文件级读写 |
| **开发者工具 Network 面板** | 浏览器内置工具，用于抓取 AJAX 请求包，获取真实数据接口 |

---

## 本P结论

1. **JSON 数据本质是字符串**，需要通过 `json.loads()` 转换为 Python 字典/列表才能操作；反过来用 `json.dumps()` 可将 Python 对象转回 JSON 字符串。
2. **JSON 与 Python 的数据类型对应关系**需牢记：JSON 对象→字典、JSON 数组→列表、JSON true/false/null→Python True/False/None（注意大小写差异）。
3. **JSONPath 是提取 JSON 数据的路径定位工具**，核心语法为 `$`（根节点）、`.`（子节点）、`..`（递归搜索）、`[index]`（数组索引）。
4. **复杂 JSON 数据提取思路**：先用 `response.json()` 或 `json.load()` 获取 Python 对象，再通过 JSONPath 路径表达式精准提取目标字段。
5. **翻页爬虫核心**：URL 中携带分页参数（如 `p=1`），循环改变页码即可批量抓取；注意部分数据可能缺少某些字段，需做好异常处理和断点调试。
6. **实战要点**：小饭桌网站数据通过 AJAX 异步加载，接口地址和参数需在开发者工具中抓取；requests 的 `response.json()` 方法可直接完成响应体的 JSON 解析。
