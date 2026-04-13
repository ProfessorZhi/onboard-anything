---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 85-【网络爬虫】IP池和Cookie池
page_index: 85
page_title: 【网络爬虫】IP池和Cookie池
type: 讲解过程
tags:
  - 网课
  - 讲解过程
---

# P85 讲解过程 - 【网络爬虫】IP池和Cookie池
## 本P定位

本P从多线程并发爬虫的痛点出发，引出两个核心解决方案：**IP池**（应对IP限流）和**Cookie池**（应对用户维度的反爬检测）。前半部分重点演示如何在代码中接入代理IP并构建动态IP池，后半部分讲解Cookie池的设计思路与实现，并最终将两者结合使用。

---

## 讲解过程

### 一、问题引入：多线程并发爬虫面临的风险

老师首先回顾了上一P讲的多线程并发爬虫，指出这种爬虫最大的问题在于**同一时间请求太密集**。具体风险包括：

- 集中请求会给目标服务器造成压力，可能导致服务器崩溃
- 目标网站查看日志后发现请求来源单一，轻易识别为爬虫行为
- 网站会采取反扒措施，包括**针对IP做限流**（同一IP不让频繁请求）和**校验用户token**（同一用户不允许持续高频请求）

> 老师用“狂飙”来形容这种情况被限制后的狼狈。

### 二、解决方案概览：IP池 + Cookie池

老师提出应对思路：

- **IP池**：预先准备大量代理IP，请求时随机选取，分散请求来源
- **Cookie池**：预先准备多个Cookie或多个登录账号，请求时轮换使用

### 三、IP池原理讲解（画图演示）

老师通过画图解释IP池的工作机制：

1. **原有方式**：客户端直接向目标服务器发送请求，如果100个并发请求都直接打过去，服务器能轻易识别
2. **改进方式**：找“中间人”即代理，请求先发到代理，再由代理转发到目标服务器
3. **效果**：服务器看到的是不同的代理IP，虽然并发量很大，但每个代理只分摊少量请求，伪装成正常用户访问

老师强调代理IP需要付费，但成本不高，“爬数据还是划得来的”。

### 四、代理IP平台介绍与操作演示

老师列举了常见的代理IP服务商：**快代理**、**IPOK**等。

以**IPOK**平台为例演示操作步骤：

1. 注册账号，平台赠送5000天启币额度
2. 进入个人中心配置**白名单**（将本机IP加入白名单，否则无法调用API）
3. 在控制台选择代理类型（HTTP）、IP时长（5分钟、10分钟等）、提取数量
4. 点击生成API链接，复制该链接用于代码请求

老师演示了提取1个5分钟有效期的代理IP，费用为10天启币。

### 五、代码实现：获取代理IP

老师新建文件编写代码：

```python
import requests

def get_proxy_ip():
    # 从代理IP平台生成的API地址
    api_url = "你的API链接"
    response = requests.get(api_url)
    result = response.json()
    return result
```

运行后遇到错误提示“当前IP不在白名单内”，老师随即演示如何在平台添加白名单，再次运行后成功返回代理IP数据。

### 六、代码实现：在requests中配置代理

老师演示在`requests.get()`中使用`proxies`参数：

```python
import requests

# 直接请求（无代理）
response = requests.get("https://www.baidu.com")
print(response.text)

# 通过代理请求
proxies = {
    "http": "http://代理IP:端口",
    "https": "https://代理IP:端口"
}
response = requests.get("https://www.baidu.com", proxies=proxies)
print(response.text)
```

成功请求百度后返回正常内容，老师指出请求链路为：**客户端 → 代理IP → 目标服务器 → 代理IP → 客户端**。

### 七、构建动态IP池类

老师定义一个爬虫类，包含以下结构：

```python
import requests
import random

class DemoSpider:
    def __init__(self):
        # 初始化时获取一批代理IP
        self.ip_api_url = "你的API链接"
        self.ip_list = self._get_proxy_ip()
    
    def _get_proxy_ip(self):
        response = requests.get(self.ip_api_url)
        result = response.json()
        return result['data']
    
    def _get_random_proxy(self):
        item = random.choice(self.ip_list)
        return item
    
    def get_html(self, url):
        proxy = self._get_random_proxy()
        proxies = {
            "http": f"http://{proxy['ip']}:{proxy['port']}",
            "https": f"http://{proxy['ip']}:{proxy['port']}"
        }
        response = requests.get(url, proxies=proxies)
        return response
```

老师解释工作流程：

- 对象初始化时一次性获取一组代理IP存入列表
- 每次发送请求前，从列表中随机选取一个IP
- 每次请求使用不同的代理IP，降低被识别概率

### 八、Cookie池讲解：为什么需要Cookie池

老师分析Cookie在反爬中的作用：

- 一个Cookie对应一个用户身份信息
- 网站不仅限制IP，还限制用户维度——同一用户请求太频繁也会被识别为爬虫
- 识别方式：读取请求中的Cookie信息

解决方案分两种场景：

1. **需要登录的网站**：准备多个账号，批量登录获取多个Cookie
2. **不需要登录的网站**：手动多次访问目标网站，复制不同的Cookie值保存

### 九、Cookie池实现：手动获取未登录Cookie

老师以百度为例演示手动获取Cookie（未登录场景）：

1. 用浏览器访问百度，打开开发者工具找到Network中的请求
2. 复制Cookie值，保存到本地
3. 清空浏览器Cookie，再次访问百度，重新复制Cookie
4. 多次重复，获取多组不同的Cookie值

> 老师指出：未登录Cookie每次值会有部分相同、部分不同，积累足够多后可用于轮换。

### 十、Cookie池实现：代码编写Cookie管理类

老师定义Cookie管理类：

```python
import requests
import random

class CookieManager:
    def __init__(self):
        self.login_url = "中华网登录地址"
        self.users = [
            {"username": "账号1", "password": "密码1"},
            {"username": "账号2", "password": "密码2"},
            # 可准备更多账号
        ]
        self.cookie_list = []
        self._login_all()
    
    def _login(self, user):
        response = requests.post(self.login_url, data=user)
        if response.status_code == 200:
            self.cookie_list.append(response.cookies)
    
    def _login_all(self):
        for user in self.users:
            self._login(user)
    
    def get_cookie(self):
        return random.choice(self.cookie_list)
```

老师解释流程：

- 初始化时遍历用户列表，批量登录各账号
- 登录成功后从响应中提取Cookie，存入列表
- `get_cookie()`方法随机返回一个Cookie

### 十一、Cookie池与爬虫结合使用

老师演示在爬虫类中使用Cookie池：

```python
class SpiderDemo:
    def __init__(self):
        self.ck = CookieManager()  # 初始化Cookie管理器
    
    def fetch_html(self, url):
        cookie = self.ck.get_cookie()  # 每次获取随机Cookie
        response = requests.get(url, cookies=cookie)
        return response.text
    
    def parse_data(self, html):
        # 解析页面提取数据
        pass
    
    def save_data(self, data):
        # 保存数据
        pass
```

### 十二、IP池 + Cookie池组合使用

老师最后指出：当前代码仍是单线程、同一IP频繁请求，即使轮换Cookie，服务器仍能通过IP限流识别。

**解决思路**：将IP池与Cookie池组合，每个Cookie与一个代理IP一一对应，每次请求同时更换IP和Cookie，模拟真实用户从不同地点、不同账号访问的效果。

---

## 提到的外部资源与对象

| 资源名称 | 类型 | 在本P中的作用 |
|---------|------|-------------|
| **快代理** | 代理IP服务商 | 列举的代理IP购买渠道之一 |
| **IPOK** | 代理IP服务商 | 演示平台：注册账号、配置白名单、提取代理IP、生成API链接 |
| **中华网** | 登录案例网站 | 用于演示Cookie池的登录与Cookie获取 |
| **百度** | 目标网站 | 用于演示代理IP请求成功、未登录Cookie手动获取 |
| **requests库** | Python库 | 用于HTTP请求、配置proxies参数、获取响应Cookie |

---

## 本P结论

1. **IP池核心思想**：通过代理IP“中间人”机制，将集中请求分散到多个出口IP，降低单一IP的请求频率，避免被限流
2. **Cookie池核心思想**：通过多个账号或手动采集的多组Cookie，请求时随机轮换，避免基于用户维度的反爬检测
3. **代码要点**：
   - requests通过`proxies`字典配置代理IP
   - 通过API从代理平台动态获取IP列表
   - 用`random.choice()`从IP池/Cookie池中随机选取
   - Cookie可从登录响应的`response.cookies`属性中获取
4. **进阶方案**：将IP池与Cookie池组合，每个IP与Cookie一一对应，每次请求同时轮换，进一步提升伪装效果
