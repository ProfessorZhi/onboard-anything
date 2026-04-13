---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 77-【网络爬虫】selenium使用入门
page_index: 77
page_title: 【网络爬虫】selenium使用入门
type: 讲解过程
tags:
  - 网课
  - 讲解过程
---

# P77 讲解过程 - 【网络爬虫】selenium使用入门
## 本P定位

本P是Selenium网络爬虫的入门讲解，属于爬虫进阶内容的前置课程。目标是让学习者理解Selenium在什么场景下使用、如何安装配置、以及掌握最核心的元素定位方法（XPath）。定位上属于"工具引入 + 环境准备 + 基础操作演示"，为后续更深入的Selenium应用奠定基础。

## 讲解过程

### 一、问题引入：为什么需要Selenium

**1. 场景背景介绍**

老师从领导留言板网站（一个给政府提建议的公开平台）入手，引出真实爬虫需求。老师提到这个需求是接的一个单子，需要爬取该网站的留言数据。

**2. 尝试用requests抓取，遭遇反爬**

老师打开浏览器开发者工具进行抓包分析：
- 发现该网站的数据是通过异步请求（Ajax）加载的
- 原始页面请求返回的响应中不包含实际数据
- 通过F12抓包找到数据接口（一个JSON请求）

老师尝试用Python的requests库模拟请求：
- 使用POST请求，带上URL、请求头、Cookie等参数
- 但请求结果返回"疑似黑客攻击已被穿云盾拦截"的提示

**3. 穿云盾反爬说明**

老师指出目前政府类网站大部分都已接入穿云盾防护，穿云盾不是简单的JS加密或参数加密能破解的，破解成本较高。老师强调requests能搞定的网站就用requests，搞不定的才用Selenium。

**4. Selenium的核心思路**

老师简述Selenium的工作原理：
- 模拟真人操作浏览器
- 可以打开浏览器、访问任意页面
- 能够获取JS渲染后的完整页面源码
- 虽然速度慢，但能绕过大部分反爬检测

老师演示了用Selenium成功获取领导留言板数据的过程：
- 等待10秒让页面JS数据加载完成
- 通过Selenium获取页面源码
- 搜索"书记你好"等关键词，验证数据确实拿到了

**核心结论**：Selenium是爬虫的最后手段，99%的网站都能搞定，剩下1%有更高级的反爬手段（但Selenium也有对应的破解方法）。

### 二、Selenium环境安装

**1. 安装Selenium库**

```
pip install selenium
```

老师说明Selenium是Python的第三方库，跨平台支持Windows、Mac、Linux，支持Python、Java等多种语言。老师本地已安装好，演示了安装命令。

**2. 安装Chrome浏览器驱动**

老师演示如何获取Chrome驱动：
- 首先确认自己Chrome浏览器的版本（老师的是122版本）
- 访问驱动下载页面，下载与浏览器版本完全一致的驱动
- 驱动下载来源包括Chrome官方地址、淘宝镜像等

**3. 驱动配置方法**

老师介绍了三种配置方式，推荐最简单的第三种：
- **方式一**：在代码中通过参数指定驱动路径
- **方式二**：把驱动路径配置到系统环境变量
- **方式三（推荐）**：直接把chromedriver.exe放到Python安装目录下

老师解释原理：Selenium通过浏览器驱动来操作浏览器，调用方法后由驱动发送指令给浏览器执行，所以库和驱动两个都要安装好才能用。

### 三、Selenium基础使用

**1. 代码模板**

```python
from selenium import webdriver

# 第一步：创建浏览器对象
driver = webdriver.Chrome()

# 第二步：访问页面
driver.get("https://www.baidu.com")

# 第三步：操作页面（如果有需要）

# 第四步：获取页面数据
page_source = driver.page_source

# 第五步：关闭浏览器
driver.quit()
```

老师演示了运行效果：Selenium启动的浏览器窗口顶部会显示"Chrome正在受到自动化测试软件的控制"的提示，这是Selenium的标志性特征。老师提到有些网站会通过这个特征检测Selenium，但有对应的规避手段，后续课程会讲。

**2. 窗口操作**

```python
# 窗口最大化
driver.maximize_window()

# 窗口最小化
driver.minimize_window()

# 刷新页面（相当于点击浏览器刷新按钮）
driver.refresh()
```

老师加了time.sleep()来让操作可见，否则程序执行太快眼睛反应不过来。

**3. 获取页面属性**

```python
# 获取页面源码（JS渲染后的完整源码）
page_source = driver.page_source

# 获取当前访问的URL
current_url = driver.current_url

# 获取窗口标题
title = driver.title

# 页面截图
driver.get_screenshot_as_file("screenshot.png")
```

老师强调Selenium获取的源码和requests获取的不一样：requests拿到的是服务器返回的原始HTML，Selenium拿到的是JS执行完毕、动态数据渲染完成后的最终页面源码。

### 四、元素定位方法

**1. 八种定位方式概览**

Selenium提供了8种元素定位方式：
- By.ID：通过元素id属性定位
- By.XPATH：通过XPath表达式定位
- By.LINK_TEXT：通过链接文本（全文本匹配）
- By.PARTIAL_LINK_TEXT：通过链接文本（部分匹配）
- By.NAME：通过name属性定位
- By.TAG_NAME：通过标签名定位
- By.CL_NAME：通过class属性定位
- By.CSS_SELECTOR：通过CSS选择器定位

老师明确表态：**只要掌握XPath一种就够了**，其他方式作用相同，不需要全部记住，因为做爬虫提取数据XPath用得最多。

**2. 演示：用XPath定位百度搜索框**

老师在百度页面演示定位输入框的过程：
- 按F12打开开发者工具
- 按Ctrl+F打开搜索框
- 写XPath表达式：`//input[@id="kw"]`
- 验证能唯一匹配到搜索框元素

**3. 元素定位代码**

```python
from selenium.webdriver.common.by import By

# 方式一：通过XPath定位
input_box = driver.find_element(By.XPATH, '//*[@id="kw"]')

# 方式二：通过ID定位（更简洁，但没有id的元素用不了）
input_box = driver.find_element(By.ID, "kw")
```

老师补充说明：通过ID定位更简单，但很多网站开发时不一定会给元素加id，所以不能依赖ID定位，XPath是万能的。

**4. 元素操作方法**

```python
# 往输入框输入内容
input_box.send_keys("人大代表")

# 获取元素文本
element.text

# 获取元素属性
element.get_attribute("属性名")
```

老师用XPath定位到百度搜索框后，调用send_keys方法成功输入了"人大代表"文字，验证了Selenium能完全模拟人的键盘输入操作。

### 五、元素属性获取

**1. 常用属性方法**

- `.text`：获取元素的文本内容
- `.get_attribute("属性名")`：获取元素的指定属性值（如href、src等）
- `.tag_name`：获取元素的标签名
- `.is_displayed()`：判断元素是否可见

老师强调这些方法在用Selenium做爬虫时很重要，因为Selenium不像BeautifulSoup那样可以用CSS选择器直接提取数据，而是需要先定位到元素，再通过这些方法获取数据。

## 提到的外部资源与对象

| 资源/对象 | 角色 | 说明 |
|---------|------|------|
| **领导留言板网站** | 实战案例网站 | 用于演示反爬虫场景和数据抓取效果 |
| **穿云盾** | 反爬虫防护系统 | 拦截了requests请求，引出Selenium的必要性 |
| **Chrome驱动（chromedriver）** | 必要组件 | Selenium操作Chrome浏览器的桥梁，需与浏览器版本匹配 |
| **Chrome官方驱动下载页面** | 驱动下载地址 | 用于下载对应版本的chromedriver.exe |
| **淘宝镜像（chromedriver镜像）** | 备用下载地址 | Chrome官方地址访问慢时可使用 |

## 本P结论

1. **Selenium定位**：当requests请求被反爬机制拦截无法获取数据时，Selenium是最后的兜底手段，能模拟浏览器操作获取JS渲染后的完整页面。

2. **环境配置两步走**：安装selenium库 + 下载与浏览器版本匹配的chromedriver驱动，驱动最简单的配置方式是放到Python安装目录下。

3. **核心方法**：`driver.get()`打开页面、`driver.page_source`获取源码、`driver.quit()`关闭浏览器。

4. **元素定位重点**：8种定位方式只需掌握XPath，`find_element(By.XPATH, "表达式")`可以定位任何元素。

5. **元素操作要点**：`send_keys()`用于输入、`get_attribute()`用于提取属性值、`.text`用于提取文本内容。
