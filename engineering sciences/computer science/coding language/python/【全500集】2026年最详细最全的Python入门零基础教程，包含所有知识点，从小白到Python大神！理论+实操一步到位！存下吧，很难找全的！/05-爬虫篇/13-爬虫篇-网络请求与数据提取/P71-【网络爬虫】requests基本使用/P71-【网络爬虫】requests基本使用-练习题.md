---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 71-【网络爬虫】requests基本使用
page_index: 71
page_title: 【网络爬虫】requests基本使用
type: 练习题
tags:
  - 网课
  - 练习题
---

# P71 练习题 - 【网络爬虫】requests基本使用
---

## 结构识别

**题目**：以下哪一行代码正确获取了响应内容但未处理编码问题？

A. `response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})`<br>
B. `text = response.text`<br>
C. `content = response.content.decode('utf-8')`<br>
D. `print(response.status_code)`

<details>
<summary>参考答案</summary>
C。`.content`返回bytes，`decode('utf-8')`将其转为字符串，主动处理了编码。其他选项均未获取或解析响应内容。
</details>

---

## 机制理解

**题目**：某网站返回的HTML中包含中文，使用`.text`读取出现乱码。最可能的原因是？

<details>
<summary>参考答案</summary>
网页实际编码与`.text`自动推断的编码不一致（如实际是GBK但被识别为UTF-8）。解决方法是改用`.content.decode('gbk')`显式指定解码字符集。
</details>

---

## 最小实践

**题目**：写出完整的requests代码，实现以下目标：

- 向 `https://www.example.com` 发送GET请求
- 携带User-Agent请求头
- 将返回的HTML文本保存到变量 `html` 中（处理中文编码）
- 打印HTTP状态码

<details>
<summary>参考答案</summary>

```python
import requests

response = requests.get(
    'https://www.example.com',
    headers={'User-Agent': 'Mozilla/5.0'}
)
html = response.content.decode('utf-8')
print(response.status_code)
```

</details>

---

## 扩展思考

**题目**：对比浏览器请求与爬虫代码请求：

1. 为什么爬虫代码不设置User-Agent往往拿不到完整响应？
2. 如果需要下载一张PNG图片并保存到本地，以上代码结构需要做哪些修改？

<details>
<summary>参考答案</summary>

1. 服务器根据User-Agent判断请求来源。浏览器访问时发送的UA包含浏览器标识，爬虫代码默认UA是`python-requests/x.x`，服务器可能返回简化内容或直接拒绝。

2. ① 用`.content`获取bytes而非`.text`；② 不解码，直接以二进制写入模式`open('image.png', 'wb')`保存；③ 通过`response.content`写入文件。

</details>

---

## 最小替代练习

**题目**：如果不使用requests库，仅使用Python标准库，能否完成同样的HTTP请求？写出核心代码思路。

<details>
<summary>参考答案</summary>

```python
from urllib import request

req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = request.urlopen(req)
html = response.read().decode('utf-8')
```

requests是对urllib的封装，核心原理相同，但requests的API更简洁（链式调用、自动异常处理）。本P的核心是理解HTTP请求的本质，标准库能实现相同功能，只是代码量稍多。

</details>
