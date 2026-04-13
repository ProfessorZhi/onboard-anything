---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 70-【网络爬虫】http协议
page_index: 70
page_title: 【网络爬虫】http协议
type: 练习题
tags:
  - 网课
  - 练习题
---

# P70 练习题 - 【网络爬虫】http协议
## 一、结构识别

**题目 1.1**  
以下是一段简化的 HTTP 请求报文，请指出①～④分别对应报文结构的哪一部分。

```
① GET /search?q=python HTTP/1.1
② Host: www.example.com
   User-Agent: Mozilla/5.0
   Cookie: session=abc123
③
④ （空）
```

参考答案：① 请求首行　② 请求头　③ 空白行（分隔符）　④ 请求体（GET 请求通常为空）

---

**题目 1.2**  
观察下列 URL，请拆解出「协议、域名、路径、查询参数」四部分。

```
https://api.github.com/repos/python/cpython/issues?state=open&labels=bug
```

参考答案：协议 `https`、域名 `api.github.com`、路径 `/repos/python/cpython/issues`、查询参数 `state=open&labels=bug`

---

## 二、机制理解

**题目 2.1**  
HTTP 与 HTTPS 的核心区别是什么？爬虫在编写代码时，为什么「几乎不需要区分用哪个库」去请求它们？

> 提示：从「加密层」与「报文格式」两个角度思考。

参考答案要点：HTTPS 在 HTTP 下方增加了一层 SSL/TLS 加密层，用于加密传输内容防止中间人窃听；但两者的请求报文格式完全一致，爬虫只需向目标 URL 发送请求，底层加密/解密由操作系统和 SSL 库自动处理，代码层面无感知。

---

**题目 2.2**  
请按顺序写出用户在浏览器中访问一个登录页面 → 完成登录 → 访问个人中心的完整 HTTP 交互流程，重点说明 Cookie 在其中是如何工作的。

参考答案要点：

1. 浏览器 GET 登录页 → 服务器返回 200 + Set-Cookie: session=xxx
2. 浏览器自动存储 Cookie，后续请求自动在请求头中携带 Cookie: session=xxx
3. 浏览器 POST 登录表单（账号密码在请求体）→ 服务器验证后返回 200
4. 浏览器 GET 个人中心 → 自动携带 Cookie → 服务器识别会话，返回个人数据

关键：Cookie 是服务器给浏览器发的「身份凭证」，浏览器负责存储并在同源请求中自动附带。

---

**题目 2.3**  
下列状态码分别代表什么含义？如果你是爬虫工程师，拿到这些响应时应该分别做什么处理？

- 200
- 302
- 403
- 404
- 500

参考答案：200 成功，解析响应体；302 重定向，根据 Location 头跟随跳转或保持原 URL；403 禁止访问，常见反爬，需更换 UA/Cookie/IP 或降速；404 资源不存在，检查 URL 是否正确；500 服务器内部错误，重试。

---

## 三、最小实践

**题目 3.1**  
请使用 `requests` 库发送一个 GET 请求，访问 `https://httpbin.org/get`，并完成以下子任务：

- 设置请求头 `User-Agent` 为 `Mozilla/5.0 (Windows NT 10.0; Win64; x64)`
- 打印响应状态码和响应体内容（JSON 格式）

```python
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get("https://httpbin.org/get", headers=headers)

print("状态码:", response.status_code)
print("响应体:", response.json())
```

---

**题目 3.2**  
延续上题，将请求方法改为 POST，并向 `https://httpbin.org/post` 发送一个登录模拟请求：用户名 `admin`，密码 `python123`。要求：

- 使用 `data` 参数传递表单数据（模拟请求体）
- 打印服务器返回的「你发送了什么」字段（观察参数是否出现在响应体中）

```python
import requests

payload = {"username": "admin", "password": "python123"}
response = requests.post("https://httpbin.org/post", data=payload)

print("状态码:", response.status_code)
print("服务器收到:", response.json().get("form"))
```

---

## 四、扩展思考

**题目 4.1**  
有些网站在 F12 Network 面板中可以看到请求带了 `Referer: https://www.baidu.com/` 这样的请求头。如果你在爬虫中没有设置 Referer，可能会导致什么结果？请给出至少两种可能的场景。

参考答案：① 图片/CSS/JS 等静态资源返回 403，网站使用了 Referer 防盗链；② 某些 API 接口验证来源一致性，缺少 Referer 直接拒绝。爬虫默认不会自动设置 Referer（除非手动指定或从上一个页面跳转），这是容易被识别为爬虫的特征之一。

---

**题目 4.2**  
假设你正在爬取一个需要登录才能访问的页面。请分析：为什么「只模拟一次登录请求获取 Cookie」之后，就能持续访问多个登录态页面？这背后涉及了哪两个关键 HTTP 机制？

参考答案：涉及「Cookie 持久化机制」和「无状态的 HTTP 协议如何维持会话」。服务器为每个会话分配唯一 ID，通过 Set-Cookie 让浏览器保存，浏览器在有效期内所有请求都自动携带，服务器据此识别用户身份，无需每次都重新验证。

---

## 五、最小替代练习

**题目 5.1**（无代码版本）  
如果你暂时不打算写爬虫代码，也可以用浏览器开发者工具完成以下观察练习：

1. 打开任意新闻网站（如 `https://news.baidu.com`），按 F12 打开开发者工具，切换到 **Network** 面板
2. 刷新页面，观察浏览器发了哪些请求，找出发送次数最多的文件类型（如 `.js`、`.css`、图片）
3. 点击任意一个请求，查看 **Headers** 面板，找到并记录以下信息：
   - Request Method（是 GET 还是 POST）
   - Status Code
   - 请求头中的 `User-Agent` 和 `Referer` 字段
4. 如果是 GET 请求，参数在哪里？（Headers → Query String Parameters）如果是 POST 请求，参数在哪里？（Payload / Form Data）

> 练习目标：建立「浏览器发出的请求」与「知识框架中报文结构」的直观对应关系。
