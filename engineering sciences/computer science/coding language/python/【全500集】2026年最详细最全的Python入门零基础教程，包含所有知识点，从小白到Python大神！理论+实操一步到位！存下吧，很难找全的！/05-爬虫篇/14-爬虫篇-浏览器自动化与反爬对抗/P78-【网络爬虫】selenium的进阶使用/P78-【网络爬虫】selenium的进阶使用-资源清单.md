---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 78-【网络爬虫】selenium的进阶使用
page_index: 78
page_title: 【网络爬虫】selenium的进阶使用
type: 资源清单
tags:
  - 网课
  - 资源清单
---

# P78 资源清单 - 【网络爬虫】selenium的进阶使用
---

## 一、网站与平台

### 1.1 领导留言板网站

- **类型**：目标网站
- **在本P中的作用**：上P自动登录的目标站，本P的登录代码继承自P77
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 访问登录后的个人中心或其他需要登录权限的页面

### 1.2 建议留言板页面

- **类型**：目标网站 / 案例页面
- **在本P中的作用**：本P数据抓取的具体目标页面，包含留言列表（标题、时间、内容），URL需手动复制确认
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 尝试抓取不同分类的留言板（如投诉、咨询等），对比页面结构差异

### 1.3 QQ邮箱登录页面 (mail.qq.com)

- **类型**：演示网站
- **在本P中的作用**：作为演示等待机制的案例网站，同时暴露iframe嵌套问题（密码登录按钮在iframe内），引出下P的switch_to.frame()讲解
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在模拟登录QQ邮箱场景中练习iframe切换

---

## 二、Python库与模块

### 2.1 time（Python标准库）

- **类型**：标准库
- **在本P中的作用**：提供 `time.sleep()` 函数实现强制等待，程序执行到此处时阻塞指定秒数
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在需要固定延时的场景（如等待弹窗、等待动画完成）中练习使用

### 2.2 selenium (webdriver)

- **类型**：第三方库
- **在本P中的作用**：浏览器自动化框架，本P的所有操作（定位元素、提取数据、配置等待）均围绕selenium展开
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在其他需要浏览器自动化的场景（如自动化测试、表单填写）中练习

### 2.3 selenium.webdriver.common.by.By

- **类型**：Selenium常量类
- **在本P中的作用**：提供定位方式的常量，如 `By.XPATH`、`By.CSS_SELECTOR`、`By.ID` 等，定位元素时必须使用
- **来源**：基于上下文推断（讲解中多次使用 `By.XPATH`，但未显式说明导入语句）
- **后续可练习方向**：建议方向 — 练习使用不同的定位方式（ID、CSS、XPath）定位同一元素，对比优缺点

### 2.4 selenium.webdriver.support.ui.WebDriverWait

- **类型**：Selenium等待类
- **在本P中的作用**：显式等待的入口类，实例化时传入driver、超时时间、轮询频率，配合 `until()` 方法实现按条件等待
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在动态加载页面上练习配置不同的超时时间和轮询频率

### 2.5 selenium.webdriver.support.expected_conditions (EC)

- **类型**：Selenium条件模块
- **在本P中的作用**：提供预定义的等待条件，如元素可见、可点击、存在于DOM等，供 `WebDriverWait.until()` 调用
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 查阅官方文档，尝试更多EC条件，如 `EC.text_to_be_present_in_element()`、`EC.invisibility_of_element_located()` 等

---

## 三、Selenium API 与方法

### 3.1 driver.find_element() vs driver.find_elements()

- **类型**：Selenium方法
- **在本P中的作用**：定位页面元素，前者返回单个WebElement，后者返回元素列表（list）；混淆两者会导致方法调用错误
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在列表页中练习区分使用场景：需要操作单个元素时用前者，需要遍历批量处理时用后者

### 3.2 driver.implicitly_wait()

- **类型**：Selenium方法
- **在本P中的作用**：设置隐式等待，在driver生命周期内全局生效；查找元素时自动轮询，超时则抛出NoSuchElementException
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 练习在初始化driver时统一配置，替代散落在各处的time.sleep()

### 3.3 WebElement.text

- **类型**：Selenium属性（注意不是方法）
- **在本P中的作用**：获取元素的文本内容，与LXML的 `.text` 方法形成对比，selenium中无需括号
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在抓取商品信息、新闻列表等场景中练习提取多字段文本

### 3.4 driver.switch_to.frame()

- **类型**：Selenium方法
- **在本P中的作用**：切换到iframe内部上下文，本P仅引出该问题，详细用法待下P讲解
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 先预习该方法的三个参数形式（frame_name/id、WebElement、索引），为P79做准备

---

## 四、等待条件 (EC)

### 4.1 EC.presence_of_element_located()

- **类型**：Selenium等待条件
- **在本P中的作用**：等待元素存在于DOM中（不要求可见），适合不在意可见性的场景
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在页面有隐藏元素但需要操作时验证其行为

### 4.2 EC.visibility_of_element_located()

- **类型**：Selenium等待条件
- **在本P中的作用**：等待元素可见（display不为none且有尺寸），适合需要用户能看到元素才能操作的场景
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在需要等待元素渲染完成才能点击的按钮场景中练习

### 4.3 EC.element_to_be_clickable()

- **类型**：Selenium等待条件
- **在本P中的作用**：等待元素可点击（存在且可见且启用），适合点击操作前的等待
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在验证码弹窗、登录按钮等需要确保可点击才能提交的表单场景中练习

### 4.4 EC.frame_to_be_available_and_switch_to_it()

- **类型**：Selenium等待条件
- **在本P中的作用**：等待iframe可用并自动切换到该iframe，是处理iframe问题的首选等待方式
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在需要进入iframe后才能操作的复杂页面（如在线编辑器、第三方嵌入内容）中练习

### 4.5 EC.title_contains()

- **类型**：Selenium等待条件
- **在本P中的作用**：等待页面标题包含指定字符串，常用于验证页面跳转成功
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在多步骤操作（如注册流程）后验证页面状态

### 4.6 EC.new_window_is_opened()

- **类型**：Selenium等待条件
- **在本P中的作用**：等待新窗口打开，适合点击链接后触发新标签页的场景
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在需要处理弹窗广告、新窗口跳转等场景中练习窗口切换

---

## 五、开发工具

### 5.1 Chrome DevTools (Elements面板)

- **类型**：浏览器开发者工具
- **在本P中的作用**：右键“检查”打开，用于查看页面HTML结构、定位目标元素的class/XPath，是数据抓取前期分析的核心工具
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在不同类型网站上练习分析DOM结构，理解页面渲染方式

### 5.2 Chrome浏览器

- **类型**：浏览器
- **在本P中的作用**：Selenium控制的浏览器载体，本P使用Chrome实例（driver = webdriver.Chrome()）进行自动化操作
- **来源**：基于上下文推断
- **后续可练习方向**：建议方向 — 熟悉Chrome的开发者工具快捷键、隐身模式等辅助调试功能

---

## 六、代码文件

### 6.1 C06_数据抓取案例.py

- **类型**：Python代码文件
- **在本P中的作用**：本P新建的练习文件，继承P77的登录代码结构，完整实现建议留言板的数据抓取
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在此文件基础上逐步添加分页抓取、iframe处理等扩展功能

---

## 七、技术概念

### 7.1 XPath（相对路径）

- **类型**：定位语言
- **在本P中的作用**：在 `find_element` / `find_elements` 中用于定位元素；强调相对路径需以 `.` 开头表示从当前节点往下查找
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 练习手写XPath和使用浏览器复制XPath的对比，理解两者的差异与优化

### 7.2 iframe（内联框架）

- **类型**：HTML技术
- **在本P中的作用**：网页嵌套技术，本P引出iframe导致元素“看得见但定位不到”的问题，为下P的switch_to.frame()做铺垫
- **来源**：字幕直接提到
- **后续可练习方向**：建议方向 — 在实际网站上（F12开发者工具）识别哪些元素位于iframe内部，理解iframe的工作原理

---

## 八、资源汇总表

| 资源名称 | 类型 | 在本P中的作用 | 来源 |
|---|---|---|---|
| 领导留言板网站 | 网站/目标站 | 上P登录目标站 | 字幕直接提到 |
| 建议留言板页面 | 网站/目标站 | 本P数据抓取目标 | 字幕直接提到 |
| QQ邮箱登录页面 | 网站/演示站 | 演示等待失败+引出iframe | 字幕直接提到 |
| time | Python标准库 | 提供time.sleep()强制等待 | 字幕直接提到 |
| selenium | 第三方库 | 浏览器自动化框架 | 字幕直接提到 |
| selenium.webdriver.common.by.By | Selenium常量类 | 提供定位方式常量 | 基于上下文推断 |
| selenium.webdriver.support.ui.WebDriverWait | Selenium等待类 | 显式等待入口 | 字幕直接提到 |
| selenium.webdriver.support.expected_conditions (EC) | Selenium条件模块 | 预定义等待条件集合 | 字幕直接提到 |
| driver.find_element/find_elements | Selenium方法 | 元素定位（单个vs列表） | 字幕直接提到 |
| driver.implicitly_wait() | Selenium方法 | 隐式等待配置 | 字幕直接提到 |
| WebElement.text | Selenium属性 | 获取元素文本（非方法） | 字幕直接提到 |
| driver.switch_to.frame() | Selenium方法 | iframe切换（下P详解） | 字幕直接提到 |
| EC.presence_of_element_located() | Selenium EC条件 | 等待元素在DOM中 | 字幕直接提到 |
| EC.visibility_of_element_located() | Selenium EC条件 | 等待元素可见 | 字幕直接提到 |
| EC.element_to_be_clickable() | Selenium EC条件 | 等待元素可点击 | 字幕直接提到 |
| EC.frame_to_be_available_and_switch_to_it() | Selenium EC条件 | 等待iframe可用并切换 | 字幕直接提到 |
| EC.title_contains() | Selenium EC条件 | 等待标题包含字符串 | 字幕直接提到 |
| EC.new_window_is_opened() | Selenium EC条件 | 等待新窗口打开 | 字幕直接提到 |
| Chrome DevTools (Elements面板) | 浏览器开发者工具 | 定位元素、查看HTML结构 | 字幕直接提到 |
| Chrome浏览器 | 浏览器 | Selenium自动化载体 | 基于上下文推断 |
| C06_数据抓取案例.py | Python代码文件 | 本P练习文件 | 字幕直接提到 |
| XPath（相对路径） | 定位语言 | 元素定位 | 字幕直接提到 |
| iframe | HTML技术 | 网页嵌套，引出切换问题 | 字幕直接提到 |
