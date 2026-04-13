---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 79-【网络爬虫】selenium反爬的破解方案
page_index: 79
page_title: 【网络爬虫】selenium反爬的破解方案
type: 资源清单
tags:
  - 网课
  - 资源清单
---

# P79 资源清单 - 【网络爬虫】selenium反爬的破解方案
## 资源总览

本P共涉及 14 项资源，涵盖库/框架、工具、软件、命令行参数、API/方法、代码/脚本、属性、网站等类型。

---

## 库 / 框架

**selenium**
- 类型：Python库 / Web自动化框架
- 在本P中的作用：核心爬虫工具，通过模拟浏览器操作绕过静态页面解析限制；本P的全部破解操作都是针对 selenium 启动的 Chrome 浏览器进行特征伪装
- 来源：字幕直接提到
- 建议方向：对比学习 Playwright、DrissionPage 等同类工具的防检测机制差异

**time**
- 类型：Python标准库
- 在本P中的作用：设置隐式等待或强制休眠，确保页面有足够时间加载
- 来源：基于上下文推断（课程演示中需设置等待时间）
- 建议方向：结合 selenium 的显式等待（WebDriverWait）替代 sleep，提高脚本稳定性

---

## 工具 / 驱动

**chromedriver**
- 类型：浏览器驱动
- 在本P中的作用：selenium 与 Chrome 浏览器之间的通信桥梁；必须与本地 Chrome 版本严格对应，否则启动参数可能不生效
- 来源：字幕直接提到（知识框架部分）
- 建议方向：使用 webdriver-manager 自动管理 chromedriver 版本，避免手动匹配

---

## 软件

**Google Chrome**
- 类型：浏览器软件
- 在本P中的作用：selenium 控制的浏览器环境；所有反爬检测都针对 Chrome 的特征进行
- 来源：字幕直接提到
- 建议方向：了解 Firefox（geckodriver）、Edge（msedgedriver）等其他浏览器的反爬对抗思路

---

## 命令 / 配置参数

**--disable-infobars**
- 类型：Chrome启动参数
- 在本P中的作用：禁用浏览器上方的信息栏，消除"Chrome 正受到自动化测试软件的控制"提示文字
- 来源：字幕直接提到
- 建议方向：查阅 Chromium 官方文档，了解其他 Chrome 启动参数的用途（如 --headless、--no-sandbox）

**--disable-extensions**
- 类型：Chrome启动参数
- 在本P中的作用：禁用浏览器扩展程序，防止扩展特征被反爬系统利用
- 来源：字幕直接提到
- 建议方向：理解扩展对浏览器指纹的影响，扩展了解 --load-extension 参数的用法

**--disable-dev-shm-usage**
- 类型：Chrome启动参数
- 在本P中的作用：禁用开发者模式相关功能，进一步减少可被检测的特征点
- 来源：字幕直接提到
- 建议方向：在 Docker 或 Linux 环境下运行 Chrome 时，该参数的必要性及相关坑点

---

## API / 方法 / 类

**ChromeOptions**
- 类型：selenium配置类
- 在本P中的作用：创建配置对象，通过 add_argument() 添加启动参数，实现浏览器特征的初级伪装
- 来源：字幕直接提到
- 建议方向：学习如何添加实验性选项（add_experimental_option）以及配置代理、用户代理等

**WebDriver**
- 类型：selenium核心接口
- 在本P中的作用：浏览器驱动对象，负责创建和控制浏览器实例；接收 ChromeOptions 配置参数
- 来源：字幕直接提到
- 建议方向：了解 WebDriver 的生命周期管理、上下文切换（switch_to）等进阶用法

**execute_script()**
- 类型：selenium方法
- 在本P中的作用：在当前页面执行 JavaScript 代码，用于注入防检测脚本、修改 DOM、操作滚动等
- 来源：字幕直接提到
- 建议方向：扩展使用 execute_async_script() 处理异步 JS 场景；结合 Page Object 模式组织代码

**WebDriverWait**
- 类型：selenium等待类
- 在本P中的作用：实现显式等待，等待页面特定元素加载完成后再进行操作，避免因网速慢导致的元素定位失败
- 来源：基于上下文推断（课程提到网站加载较慢）
- 建议方向：配合 expected_conditions（EC）使用常见等待条件，掌握 until / until_not 的用法

---

## 代码 / 脚本

**防检测JS脚本**
- 类型：JavaScript脚本
- 在本P中的作用：在页面加载前执行，覆盖或删除 navigator.webdriver 等 selenium 特征属性，使网站无法通过 JS 检测到自动化工具
- 来源：字幕直接提到（课程中直接展示代码内容）
- 建议方向：追踪反爬社区（如 undetected-chromedriver、selenium-stealth）更新防检测脚本；理解其原理后尝试自定制

---

## 属性

**navigator.webdriver**
- 类型：浏览器JS属性
- 在本P中的作用：检测是否使用 selenium 的核心标志位；正常浏览器返回 undefined/false，selenium 启动的浏览器返回 true
- 来源：字幕直接提到
- 建议方向：使用 Chrome DevTools Protocol（CDP）直接修改该属性，或通过浏览器启动参数禁用相关检测

---

## 网站

**空气质量查询网站（演示站点）**
- 类型：目标测试网站
- 在本P中的作用：作为反爬场景演示对象，展示 selenium 被检测后数据区域为空，以及破解后数据正常加载的效果
- 来源：字幕直接提到（视频中直接复制URL使用）
- 建议方向：寻找其他已部署反爬检测机制的公开网站进行实战练习（如某些电商、招聘、房产平台）

---

## 资源关联图

```
chromedriver（驱动）
    ↓
selenium（库） ←→ Google Chrome（浏览器）
    ↓
ChromeOptions（配置参数） → --disable-infobars
                           --disable-extensions
                           --disable-dev-shm-usage
    ↓
WebDriver（控制接口）
    ↓
execute_script() → 防检测JS脚本 → navigator.webdriver（属性）
    ↓
WebDriverWait → 页面加载完成 → 数据提取
```
