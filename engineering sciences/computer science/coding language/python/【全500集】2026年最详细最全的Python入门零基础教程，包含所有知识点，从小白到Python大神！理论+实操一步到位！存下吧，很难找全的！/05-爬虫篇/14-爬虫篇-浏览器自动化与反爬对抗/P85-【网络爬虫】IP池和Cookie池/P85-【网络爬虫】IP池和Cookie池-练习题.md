---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 85-【网络爬虫】IP池和Cookie池
page_index: 85
page_title: 【网络爬虫】IP池和Cookie池
type: 练习题
tags:
  - 网课
  - 练习题
---

# P85 练习题 - 【网络爬虫】IP池和Cookie池
## 一、结构识别

**题目 1.1** 补全流程
请根据下面的简化流程图，在空格处填入正确的组件名称或数据对象：

```
请求 → 【  ①  】 → 目标服务器 → 代理IP → 响应
```

```
Cookie池 → 【  ②  】参数 → requests请求 → 【  ③  】提取
```

- ① 的作用是：随机选取代理IP转发请求
- ② 是requests中注入Cookie的参数名
- ③ 是从登录响应中获取Cookie对象的方式

**题目 1.2** 组合方案识别
阅读下面的伪代码，标注每一行属于IP池、Cokkie池还是组合使用的范畴：

```python
1  proxy = ip_pool.get_random()          # ___
2  cookie = cookie_pool.get_random()     # ___
3  response = requests.get(url, proxies={"http": proxy}, cookies=cookie)  # ___
```

---

## 二、机制理解

**题目 2.1** 场景匹配
高并发爬虫请求目标网站时，以下两个问题分别应该由哪个池解决？请说明原因。

| 问题描述 | 对应池 | 选择原因 |
|----------|--------|----------|
| "当前IP请求过于频繁" | ① | ② |
| "检测到异常用户行为" | ③ | ④ |

**题目 2.2** 工作原理
请用自己的语言解释以下三个概念：

- **代理IP**：__
- **HTTP代理 vs HTTPS代理**：__
- **Cookie轮换**：__

**题目 2.3** 易错点分析
以下代码运行时可能出错，请指出每行代码对应哪个易错点：

```python
proxies = {"http": "http://123.45.67.89:8080"}
response = requests.get("https://example.com", proxies=proxies)
```

---

## 三、最小实践

**题目 3.1** 代理配置
使用requests发送一次带代理的请求，目标URL为`http://httpbin.org/ip`，代理为`{"http": "http://1.2.3.4:5678"}`。请补全代码：

```python
import requests

url = "http://httpbin.org/ip"
proxy = "http://1.2.3.4:5678"
proxies = 【代码】

response = requests.__(url, proxies=__)
print(response.text)
```

**题目 3.2** Cookie获取
模拟登录后从响应中提取Cookie，请补全代码：

```python
import requests

login_url = "http://example.com/login"
login_data = {"username": "test", "password": "123456"}

response = requests.post(login_url, data=login_data)
# 获取Cookie对象
user_cookie = 【代码】
print(user_cookie)
```

**题目 3.3** 随机轮换
请实现一个简化版的IP池类，包含初始化IP列表和随机获取方法：

```python
import random

class SimpleIPPool:
    def __init__(self, ip_list):
        self.ips = ip_list
    
    def get_random(self):
        【代码】
        return 【代码】

# 测试
pool = SimpleIPPool(["1.1.1.1:8080", "2.2.2.2:8080", "3.3.3.3:8080"])
print(pool.get_random())
```

---

## 四、扩展思考

**题目 4.1** 池耗尽处理
假设IP池在高峰期耗尽，所有代理IP都用完了。请设计一个兜底策略，说明在获取不到代理IP时程序应如何处理，并给出代码思路。

我的兜底策略：__
代码思路：__

**题目 4.2** 绑定策略
组合方案中提到"每个Cookie与一个代理IP一一绑定"，请思考：

- 这种绑定策略相比随机独立选取有什么优势？
- 如果某个代理IP失效（比如被封），是否需要解绑对应Cookie？为什么？

**题目 4.3** 实践局限
本P中使用了付费代理服务商（IPOK、快代理）和特定网站（中华网、百度）作为演示。请分析在实际个人项目中可能遇到的限制，并提出替代方案。

---

## 五、最小替代练习

**题目 5.1** 免费代理获取
练习从公开免费代理网站（如 https://www.proxy-list.download/ 或 https://free-proxy-list.net/ ）获取代理IP，并验证其可用性。

目标网站：任何可测试的HTTP站点（如 http://httpbin.org/ip）
任务要求：
1. 抓取至少3个免费代理IP
2. 编写代码验证每个代理是否可用
3. 记录哪些代理可用、哪些已失效

**题目 5.2** 开发者工具抓Cookie
使用浏览器开发者工具（Network面板）访问一个无需登录的网站（如 https://www.baidu.com ），完成以下任务：

1. 找到请求头中的Cookie字段
2. 使用requests携带该Cookie重新请求，对比携带前后的响应差异
3. 说明Cookie在本次实验中起到了什么作用

**题目 5.3** 白名单配置模拟
由于调用代理API需要本机IP在白名单中，请在本地完成以下模拟练习：

1. 查询本机公网IP
2. 模拟一个"白名单检查"函数，判断调用IP是否在白名单列表中
3. 如果不在，打印提示信息"当前IP不在白名单内"

---

## 参考答案概要

> 本节练习题答案将在下期公布。提示：
> - 结构识别题关注API参数名（proxies、cookies）和响应对象（response.cookies）
> - 最小实践题的代码均可直接运行，注意字典键的写法（"http" vs "https"）
> - 扩展思考题无标准答案，言之成理即可
