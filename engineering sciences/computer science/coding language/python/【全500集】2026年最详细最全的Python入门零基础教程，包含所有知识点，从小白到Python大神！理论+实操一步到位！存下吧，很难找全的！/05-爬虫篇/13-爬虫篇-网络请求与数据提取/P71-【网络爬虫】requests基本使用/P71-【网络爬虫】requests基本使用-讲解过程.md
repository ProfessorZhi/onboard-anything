---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 71-【网络爬虫】requests基本使用
page_index: 71
page_title: 【网络爬虫】requests基本使用
type: 讲解过程
tags:
  - 网课
  - 讲解过程
---

# P71 讲解过程 - 【网络爬虫】requests基本使用
## 本P定位

本P是网络爬虫章节的正式入门课，承接前面对爬虫四步骤的理论介绍，从第一步"发请求"切入，介绍Python的requests库的使用。通过百度首页的抓取演示，引出乱码问题、反爬机制，最终以图片下载、网页下载、音乐下载三个实战案例收尾。本P奠定了后续所有爬虫实战的代码基础。

## 讲解过程

### 一、requests模块引入与基本使用

**背景铺垫**：老师先回顾了爬虫的四个步骤——发请求、获取响应、提取数据、存储数据。指出当前要解决的是第一步：如何通过代码发送HTTP请求，而不是像人一样在浏览器地址栏输入URL。

**模块介绍**：

- requests是Python中的一个HTTP请求库
- 作者是Kenneth Reitz，Python语言的总架构师，30岁左右

**创建文件**：`01_request发送get请求.py`

**需求描述**：使用代码获取百度首页

**实现步骤**（老师写在代码注释中）：

1. 准备URL地址
2. 发送请求
3. 获取返回结果

**安装库**：在PyCharm的Terminal中执行 `pip install requests`

**基础代码演示**：

```python
# 导入request模块
import requests

# 第一步：准备好百度首页URL
url = "https://www.baidu.com"

# 第二步：发送请求——requests.get()方法，参数名是url
response = requests.get(url=url)

# 第三步：获取返回结果
print(response.text)
```

**运行结果**：返回了HTML内容，但出现了乱码（大量\u开头的转义字符或问号符号）。

---

### 二、response对象的两种数据获取方式

老师先预告：接下来要详细讲解response返回的response对象的属性。

**方式一：response.text**

- 获取到的是字符串
- 存在的问题：自动解码时采用的字符集可能不正确，导致乱码

**方式二：response.content**

- 获取到的是原始二进制数据（bytes类型）
- 数据前方有b前缀，表示字节类型
- 需要通过.decode()方法解码成字符串

---

### 三、Python中bytes与字符串的转换（穿插知识讲解）

**创建文件**：`03_字符串和bytes类型转换.py`

老师先铺垫：互联网上的数据传输都是二进制（bytes），requests拿到的原始数据就是bytes。

**bytes转字符串**：使用`.decode()`方法，称为解码（decoding）

**字符串转bytes**：使用`.encode()`方法，称为编码（encoding）

**代码演示**：

```python
# 定义字符串
s = "你好"
# 字符串 → bytes（编码）
res = s.encode()  # 结果：b'\xe4\xbd\xa0\xe5\xa5\xbd'，中文变成十六进制字节

# bytes → 字符串（解码）
res_i = res.decode()  # 结果：你好
```

**结论**：

- `.text`直接获取字符串，但自动解码可能出错
- `.content`获取bytes，要手动`.decode()`解码
- 如果默认UTF-8解码失败，可以尝试指定`decode('gbk')`（GBK是只包含中文的编码方式）
- 三种方式都能获取页面源码

---

### 四、response对象的其他属性（扩展介绍）

老师提示：这些属性后面会用到，先了解即可。

- `response.status_code`：获取HTTP状态码
- `response.headers`：获取响应头
- `response.cookies`：获取响应cookies
- `response.request.headers`：获取本次请求的请求头
- `response.request.cookies`：获取本次请求的请求cookies

---

### 五、反爬虫机制：User-Agent检测与应对

**问题发现**：对比代码请求结果与浏览器直接打开百度页面的返回内容，发现代码拿到的HTML明显少了很多内容。

**原因分析**：

1. 通过`response.request.headers`打印本次请求的请求头，发现User-Agent字段显示的是`python-requests/x.x.x`
2. 浏览器发请求时User-Agent标识自己是浏览器（包含Chrome/Firefox等浏览器信息）
3. 服务器检测到User-Agent不是正常浏览器，就返回了一个简化的HTML，拒绝完整响应
4. 这是第一种反爬虫手段：**检测请求头中的User-Agent，鉴别客户端身份**

**解决方案**：在请求时手动设置请求头，伪装成浏览器。

**代码修改**：

```python
# 第一步：准备好URL
url = "https://www.baidu.com"

# 第二步：准备请求头（字典格式）
headers = {
    "User-Agent": "从浏览器开发者工具Network面板复制的完整User-Agent字符串"
}

# 第三步：发送请求时传入headers参数
response = requests.get(url=url, headers=headers)
```

**效果验证**：再次运行，返回内容与浏览器完全一致，包含"全球领先的中文搜索引擎"等完整内容。

**老师强调**：写爬虫时，发请求一定要加上User-Agent，这是第一个必须掌握的解决反爬的手段。

---

### 六、实战案例一：下载百度图片

**创建文件**：`05_案例_通过request发送请求下载图片.py`

**目标**：下载百度首页的logo图片

**步骤**：

1. 在浏览器中右击图片 → "在新标签打开图片" → 获取图片URL
2. 图片是二进制媒体文件，请求后返回的响应内容是bytes
3. 用`wb`（二进制写入）模式打开文件，将`response.content`写入文件

**代码**：

```python
import requests

# 图片URL
url = "https://www.baidu.com/img/bd_logo1.png"

# 请求头（带User-Agent）
headers = {
    "User-Agent": "从浏览器复制的User-Agent"
}

# 发送请求
response = requests.get(url=url, headers=headers)

# 以二进制写入模式打开文件，保存为.jpg
with open("baidu.jpg", "wb") as f:
    f.write(response.content)

print("图片下载成功")
```

---

### 七、实战案例二：下载百度网页

**创建文件**：`06_案例_发送请求下载网页.py`

**目标**：把百度首页HTML保存到本地文件

**步骤**：

1. 发送请求获取HTML内容
2. 打开HTML文件时指定UTF-8编码
3. 用`response.content.decode()`解码后再写入（因为文件读写的是字符串而非bytes）

**代码**：

```python
import requests

url = "https://www.baidu.com"
headers = {
    "User-Agent": "从浏览器复制的User-Agent"
}

response = requests.get(url=url, headers=headers)

# 以UTF-8编码打开HTML文件，写入解码后的内容
with open("baidu.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())

print("网页下载成功")
```

**验证**：用浏览器打开本地baidu.html文件，确认内容完整可显示。

---

### 八、实战案例三：下载网易云音乐

**创建文件**：`07_案例_通过request下载网易云音乐.py`

**目标**：下载网易云的非VIP歌曲（如《乡愁》）

**前置知识**：视频/音频文件下载思路与图片相同——找到媒体文件的URL，请求后以二进制方式保存。

**获取音乐地址的方法（浏览器控制台抓包）**：

1. 打开网易云音乐网站，按F12或右击 → 检查，打开开发者工具
2. 切换到Network（网络）面板
3. 播放音乐，观察Network中出现的media类型请求
4. 找到音乐请求，复制其URL
5. 在新标签页打开该URL验证是否为正确歌曲

**注意事项**：VIP歌曲只能下载前十几二十秒的试听片段，非VIP歌曲可以完整下载。

**代码结构**（与图片下载完全一致）：

```python
import requests

# 音乐URL（通过抓包获得）
url = "音乐文件的URL地址"

headers = {
    "User-Agent": "从浏览器复制的User-Agent"
}

response = requests.get(url=url, headers=headers)

# 以二进制写入模式保存为.m4a或其他音频格式
with open("乡愁.m4a", "wb") as f:
    f.write(response.content)
```

## 提到的外部资源与对象

| 资源/工具 | 角色 | 说明 |
|---|---|---|
| **requests库** | Python HTTP请求库 | 本P的核心工具，用于发送各种HTTP请求 |
| **PyCharm Terminal** | 安装工具 | 用于执行`pip install requests`命令 |
| **浏览器开发者工具（F12）** | 调试与抓包工具 | 用于查看请求头、复制User-Agent、抓取音乐/视频URL |
| **Kenneth Reitz** | requests库作者 | Python语言总架构师 |

## 本P结论

1. **requests库是Python中发送HTTP请求的基础工具**，核心方法为`requests.get()`，参数包括`url`和`headers`。

2. **response对象的两种数据获取方式**：`.text`直接获取字符串（有乱码风险），`.content`获取bytes需要手动`.decode()`解码。

3. **bytes与字符串的互转**：字符串→bytes用`.encode()`（编码），bytes→字符串用`.decode()`（解码）。

4. **User-Agent是第一个必须掌握的反爬应对手段**：通过在请求头中设置浏览器的User-Agent，伪装成正常浏览器访问。

5. **图片、音频、视频等二进制文件的下载核心**：请求获取bytes后，以`wb`模式写入文件即可。

6. **获取媒体文件URL的方法**：使用浏览器开发者工具的Network面板，按类型筛选media，找到请求的媒体文件URL。
