---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 71-【网络爬虫】requests基本使用
page_index: 71
page_title: 【网络爬虫】requests基本使用
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P71 知识框架 - 【网络爬虫】requests基本使用
## 本P位置

Python入门 → 网络爬虫章节 → 爬虫四步骤之「发请求」实操

前置：爬虫四步骤理论（发请求→获取响应→提取数据→存储数据）
本P任务：掌握requests库发送HTTP请求，建立反爬意识
后续：数据提取（BeautifulSoup/正则）、存储持久化

## 核心问题

如何用Python代码替代浏览器发送HTTP请求并获取响应？

## 知识骨架

```
requests.get(url, headers)
        ↓
   response对象
    /      \
.text     .content
  ↓          ↓
字符串(乱码风险)  bytes → .decode() → 字符串
                              或
                        直接写入二进制文件
```

三个关键决策点：
1. 选.text还是.content → 文本内容用.decode()，二进制媒体用.content直接写入
2. 是否设置User-Agent → 几乎所有网站都需要，否者返回简化内容
3. 解码用UTF-8还是GBK → 先试UTF-8，失败换GBK

## 关系与依赖

requests库是Python标准库urllib的封装，作者Kenneth Reitz，API更简洁

知识链条：HTTP协议基础 → requests发送请求 → response解析 → 文件IO存储

依赖关系：Python基础语法 → requests库 → 反爬应对策略

## 输入 / 输出 / 前置 / 支撑

输入：目标URL + 可选headers字典
输出：response对象（包含text/content/status_code/headers/cookies）
前置：Python基础语法、HTTP请求概念（可选）
支撑：浏览器开发者工具（获取UA、抓取媒体URL）、PyCharm Terminal（安装requests）

## 易错点

.text自动解码字符集与网页实际编码不符 → 导致乱码 → 改用.content.decode()
不设置User-Agent → 服务器识别为爬虫 → 返回不完整响应
二进制文件用"w"模式写入 → 应使用"wb"模式
.decode()不传参数默认UTF-8 → 遇到GBK编码中文网站会失败

## 外部资源与对象

requests库：Python HTTP请求核心工具，安装命令pip install requests
浏览器开发者工具：获取User-Agent字符串（Network面板）、抓取媒体文件真实URL（media类型筛选）
PyCharm Terminal：执行pip命令安装requests的IDE内嵌终端
Kenneth Reitz：requests库作者
