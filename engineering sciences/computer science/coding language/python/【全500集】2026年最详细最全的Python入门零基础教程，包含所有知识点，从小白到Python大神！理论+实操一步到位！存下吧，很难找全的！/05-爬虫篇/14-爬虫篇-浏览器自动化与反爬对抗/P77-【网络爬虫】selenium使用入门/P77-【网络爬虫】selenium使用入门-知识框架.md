---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 77-【网络爬虫】selenium使用入门
page_index: 77
page_title: 【网络爬虫】selenium使用入门
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P77 知识框架 - 【网络爬虫】selenium使用入门
## 本P位置

Python入门课程 → 网络爬虫章节 → Selenium工具入门

爬虫技术栈中的定位：**requests的兜底方案**。当requests被反爬拦截（穿云盾等JS渲染反爬）时，用Selenium模拟真人浏览器操作获取完整页面。是爬虫从"发送请求"到"控制浏览器"的转折点。

## 核心问题

- requests无法获取JS动态渲染的数据时怎么办
- Selenium如何模拟浏览器完成页面操作
- 如何准确定位页面元素并提取数据

## 知识骨架

**Selenium = 库 + 浏览器驱动 + 浏览器**

1. **工具定位**：反爬绕过工具，模拟真人操作浏览器，获取JS渲染后的完整页面源码
2. **环境配置**：selenium库 + chromedriver驱动（版本必须与Chrome完全一致） + Chrome浏览器
3. **基础使用流程**：创建driver对象 → get()访问页面 → page_source获取源码 → quit()关闭
4. **元素定位**：8种方式（ID/XPATH/LINK_TEXT/NAME/TAG_NAME/CLASS_NAME/CSS_SELECTOR），**XPATH是万能解**
5. **元素操作**：send_keys()输入、.text取文本、.get_attribute()取属性

## 关系与依赖

```
requests（优先尝试） → 被反爬拦截 → Selenium（兜底方案）
                                       ↓
                              selenium库 ← 需要 → chromedriver驱动
                                              ↓
                                       Chrome浏览器
```

- requests优先：速度快，能搞定就不用Selenium
- XPath优先：万能定位，其他方式只是语法不同
- 驱动版本 = 浏览器版本：差一位都不行

## 输入 / 输出 / 前置 / 支撑

| 类型 | 内容 |
|------|------|
| **输入** | chromedriver.exe（本地）+ 目标URL |
| **输出** | JS渲染后的完整页面源码（page_source）、元素数据（文本/属性） |
| **前置知识** | Python基础、HTTP请求概念、网页结构（HTML/CSS/XPath基础） |
| **支撑工具** | Chrome浏览器、Chrome驱动、开发者工具（F12） |

## 易错点

1. **驱动版本不匹配**：chromedriver版本号必须与Chrome浏览器版本完全一致，差一位都会报错
2. **动态内容未加载完成就取源码**：需要加time.sleep()等待JS执行完毕
3. **XPath表达式错误**：写错会导致找不到元素，需用F12验证表达式
4. **没加quit()关闭浏览器**：程序结束但Chrome进程残留
5. **依赖ID定位**：很多网站元素没有id，必须会用XPath兜底

## 外部资源与对象

| 资源/对象 | 角色 | 说明 |
|---------|------|------|
| **领导留言板网站** | 实战案例 | 反爬场景演示站，用于说明穿云盾拦截和Selenium成功获取 |
| **穿云盾** | 反爬系统 | 拦截requests请求，说明为何需要Selenium兜底 |
| **chromedriver** | 核心组件 | Selenium与Chrome之间的通信桥梁，需与浏览器版本匹配 |
| **Chrome官方驱动页** | 驱动来源 | 下载地址：chromedriver.chromium.org |
| **淘宝镜像（chromedriver）** | 备选来源 | Chrome官方访问慢时使用 |
| **BeautifulSoup** | 关联工具 | Selenium取到源码后配合BeautifulSoup解析（非本P重点，但属于后续工具链） |
