---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 75-【网络爬虫】jsonpath数据提取和案例
page_index: 75
page_title: 【网络爬虫】jsonpath数据提取和案例
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P75 知识框架 - 【网络爬虫】jsonpath数据提取和案例
## 本P位置

网络爬虫章节 → 数据提取技术 → JSONPath数据提取与实战
前置：Xpath提取基础、简单HTTP请求
后续：可衔接复杂反爬应对、多线程爬虫

---

## 核心问题

如何从深层嵌套的JSON响应中精准提取目标字段？
如何处理JSON数据与Python对象之间的双向转换？

---

## 知识骨架

### 一、JSON与Python数据类型对照

JSON本质是字符串，需解析为Python对象才能操作。

| JSON格式 | Python格式 | 注意事项 |
|----------|------------|----------|
| 对象 {key: value} | dict字典 | |
| 数组 [val1, val2] | list列表 | |
| true / false | True / False | **首字母大写** |
| null | None | |
| 字符串 | 字符串 | **必须双引号** |

### 二、Python json模块（内置，无需安装）

四种方法，处理字符串层面和文件层面的双向转换：

| 方法 | 方向 | 场景 |
|------|------|------|
| json.loads(JSON字符串) | JSON字符串 → Python对象 | 处理API响应文本 |
| json.dumps(Python对象) | Python对象 → JSON字符串 | 构造请求体、输出JSON |
| json.load(文件句柄) | 文件 → Python对象 | 读取JSON文件 |
| json.dump(数据, 文件句柄) | Python对象 → 文件 | 写入JSON文件 |

常用参数：`ensure_ascii=False`（保留中文）、`indent=4`（格式化缩进）

### 三、JSONPath语法

通过路径表达式定位JSON中的目标字段。需安装：`pip install jsonpath`

| 语法 | 含义 | 示例 |
|------|------|------|
| $ | 根节点 | $ |
| .key | 取直接子节点 | $.data.title |
| ..key | 递归搜索（任意层级） | $..author |
| [index] | 数组索引 | $[0].title |

使用：`from jsonpath import jsonpath`，返回列表（即使只有一个值），需索引取值 `[0]`

### 四、实战流程（小饭桌融资资讯爬虫）

1. 开发者工具Network抓AJAX请求 → 获取接口URL和参数
2. requests.get(url) → response.json() 直接解析为Python对象
3. for item in result['data'] 遍历每条记录
4. jsonpath(item, '$.目标字段') 精准提取
5. 翻页：URL中变更分页参数（如p=1→p=2）

---

## 关系与依赖

```
HTTP请求 (requests库)
    ↓ response.text
JSON字符串
    ↓ json.loads() / response.json()
Python对象 (dict/list)
    ↓ jsonpath() 路径表达式
目标字段提取
    ↓ 遍历 + 翻页循环
批量数据采集
```

依赖链：requests → 获取响应 → json模块解析 → jsonpath提取 → 数据清洗存储

---

## 输入 / 输出 / 前置 / 支撑

**输入**：JSON格式的API响应（字符串）
**输出**：Python对象中的目标字段值
**前置**：HTTP请求基础（requests库）、数据类型基础（字典/列表操作）
**支撑**：开发者工具Network面板（抓包）、jsonpath第三方库

---

## 易错点

1. JSON布尔值大小写：JSON用true/false（小写），Python用True/False（大写）
2. JSON字符串强制双引号：单引号会解析报错
3. jsonpath返回值是列表：即使只匹配一个值也返回列表，必须加 `[0]` 取值
4. 字段缺失：部分数据记录可能不存在某个字段，递归搜索会返回布尔值而非列表
5. 第0页无数据：分页通常从第1页开始

---

## 外部资源与对象

| 资源/对象 | 类型 | 作用 |
|-----------|------|------|
| 小饭桌网站（xiaofanzhuo.com） | 目标网站 | 金融投资资讯平台，AJAX异步加载数据，本P实战演示对象 |
| jsonpath库 | Python第三方库 | 通过路径表达式提取JSON字段，pip install jsonpath安装 |
| Python内置json模块 | 标准库 | JSON字符串与Python对象的双向转换，文件级读写 |
| requests库 | 第三方库 | HTTP请求，获取API响应（本P依赖但非本P重点） |
| 浏览器开发者工具Network面板 | 工具 | 抓取AJAX请求包，获取真实数据接口URL和参数 |
| jsonpath在线校验工具 | 在线工具 | 调试JSONPath表达式是否正确匹配目标字段 |
