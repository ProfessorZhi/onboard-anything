---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 72-【网络爬虫】Xpah数据提取和案例
page_index: 72
page_title: 【网络爬虫】Xpah数据提取和案例
type: 练习题
tags:
  - 网课
  - 练习题
---

# P72 练习题 - 【网络爬虫】Xpah数据提取和案例
## 结构识别

### 1.1 表达式功能判断

请指出以下 XPath 表达式能够匹配什么内容：

(1) `//div[@class="movie"]//text()` → 获取________________
(2) `//a[@href]/@href` → 获取________________
(3) `//ul/li[last()]` → 获取________________
(4) `//span[contains(@class, "rating")]` → 获取________________

### 1.2 语法要素归类

请将左侧的 XPath 语法要素与右侧的作用一一对应：

| 术语/符号 | 作用 |
|---|---|
| text() | ( A ) |
| @class | ( B ) |
| [1] | ( C ) |
| contains() | ( D ) |

作用选项：
A. 获取属性值
B. 模糊匹配
C. 索引定位
D. 获取标签文本

## 机制理解

### 2.1 索引差异

Python 列表使用 0-based 索引，但 XPath 使用 1-based 索引。请解释为什么 XPath 的第一个元素用 `[1]` 而不是 `[0]` 表示。

### 2.2 路径差异

在HTML文档树中，`/` 和 `//` 的作用有什么区别？请各举一个适用场景。

### 2.3 数据源判断

在 XPath 中，数据要么来自标签文本，要么来自标签属性。请判断以下数据用哪种方式获取：

(1) 电影评分（如"9.0分"）→ 从 `<span class="score">9.0</span>` 中获取，属于______
(2) 图片URL → 从 `<img src="xxx.jpg">` 中获取，属于______
(3) 页面链接 → 从 `<a href="xxx">` 中获取，属于______
(4) 章节标题 → 从 `<h1>标题</h1>` 中获取，属于______

A. text() 获取
B. @attr 获取

## 最小实践

### 3.1 基础解析

假设已通过 requests 获取了某个网页的 HTML 内容，变量名为 `html_text`。请写出使用 lxml 解析该 HTML 并提取所有 class 为 "title" 的元素的文本内容的完整代码。

### 3.2 批量提取改进

有位同学写了以下代码来提取多个电影信息：

```python
from lxml import etree

html = etree.HTML(html_text)
titles = html.xpath('//div[@class="movie"]//span[@class="name"]/text()')
scores = html.xpath('//div[@class="movie"]//span[@class="score"]/text()')

for i in range(len(titles)):
    print(f"{titles[i]}: {scores[i]}")
```

请分析这段代码的潜在问题，并提出改进方案。

## 扩展思考

### 4.1 批量提取对应问题

在爬取豆瓣电影时，需要同时提取电影名称和评分。如果用两段独立的 XPath 分别提取，两个列表的顺序可能会错位。请设计一个方案，保证名称和评分的对应关系不丢失。

### 4.2 浏览器复制的问题

浏览器开发者工具可以"复制 XPath"，但课程建议手写 XPath。请从以下角度分析原因：
(1) 复制的 XPath 通常包含哪些问题？
(2) 手写 XPath 能带来哪些优势？

## 最小替代练习

### 5.1 XPath Helper 安装与使用

请在你的 Chrome 浏览器中安装 XPath Helper 插件，然后在任意一个网页（如百度首页）上使用以下操作：
(1) 按 Shift+Ctrl+X 打开插件面板
(2) 在输入框中输入 `//title/text()`
(3) 记录页面返回的标题内容

### 5.2 开发者工具定位

不使用插件，仅靠浏览器自带的开发者工具：
(1) 打开任意新闻网站（如腾讯新闻）
(2) 使用 Elements 面板定位一篇文章的标题元素
(3) 写出该标题元素的 XPath 路径

---

答案说明：
本次练习的答案请参考对应的《答案解析》文档。
