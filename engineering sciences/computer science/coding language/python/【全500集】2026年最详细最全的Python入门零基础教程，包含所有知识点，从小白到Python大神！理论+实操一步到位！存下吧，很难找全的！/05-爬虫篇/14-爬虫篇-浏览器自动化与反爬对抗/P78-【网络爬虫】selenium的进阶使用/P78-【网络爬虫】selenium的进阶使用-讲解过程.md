---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 78-【网络爬虫】selenium的进阶使用
page_index: 78
page_title: 【网络爬虫】selenium的进阶使用
type: 讲解过程
tags:
  - 网课
  - 讲解过程
---

# P78 讲解过程 - 【网络爬虫】selenium的进阶使用
## 本P定位

本P承接 P77 的"领导留言板自动登录"案例，进入 selenium 的数据抓取与等待机制教学。前半段完成建议留言板列表页面的基础抓取，后半段系统讲解 selenium 三种等待方式（强制等待、隐式等待、显式等待），并引出 iframe 嵌套问题，为下P的 iframe 切换做铺垫。

## 讲解过程

### 一、开启新案例：建议留言板数据抓取

1. **任务说明**：上P已完成领导留言板的自动登录，接下来要抓取"建议留言板"中的数据，包括建言信息、标题、时间、内容。

2. **新建文件**：创建文件 `C06_数据抓取案例.py`，将上 P 的登录代码（初始化 Chrome、打开页面、登录操作）完整复制过来。

3. **确认目标页面**：复制建议留言板的 URL，打开后确认进入目标页面。

### 二、分析页面结构与元素定位

1. **打开开发者工具**：右键检查页面，进入 Elements 面板查看 HTML 源码。

2. **定位数据容器**：
   - 所有留言数据都在 `<ul>` 标签内，class 属性为 `animal-list`（或类似值）
   - 每一条留言是 `<li>` 标签
   - 目标：先定位到包含所有数据的 `<ul>`，再获取其下所有的 `<li>`

3. **XPath 定位思路**：
   ```python
   li_list = driver.find_elements(By.XPATH, "//ul[@class='animal-list']/li")
   ```
   - 使用 `find_elements`（复数）而不是 `find_element`（单数）
   - 强调：find_element 只返回第一个匹配元素，find_elements 返回所有匹配元素组成的列表

### 三、提取每条数据的内容

1. **循环遍历**：
   ```python
   for item in li_list:
       title = item.find_element(By.XPATH, ".//div[@class='list-content']/h1").text
       time = item.find_element(By.XPATH, ".//div[@class='list-content']/div/p").text
       content = item.find_element(By.XPATH, ".//p[@class='list-desc']").text
   ```

2. **与 LXML 的核心区别**：
   - LXML 用 `.text` 获取文本
   - Selenium 的 WebElement 对象用 `.text` 属性获取文本（注意不是方法，是属性）
   - 注意 XPath 前面加点 `.` 表示"从当前元素开始往下找"

3. **添加休眠**：由于页面数据加载需要时间，在关闭浏览器前添加 `time.sleep(3)` 等待。

4. **运行验证**：
   - 第一次运行报错：定位表达式无效，原因是漏写了 `By.` 前缀
   - 修复后运行，发现内容全部是第一条数据的问题
   - 检查发现 XPath 少写了一个点（`.`），导致定位路径错误
   - 修正后再运行，数据抓取成功，每条记录的标题、时间、内容均正确

5. **后续扩展说明**：页面底部有"查看更多"按钮，涉及分页抓取和页面滚动，将放在 selenium 高级用法部分讲解，本 P 先完成单页基础抓取。

### 四、讲解等待机制（重点）

**为什么需要等待？**
Selenium 模拟人工操作网页，网页加载受网络影响，有时页面或元素还未加载完成就直接定位会报错，导致爬虫中断。

#### 4.1 强制等待（第一种）

- 使用 Python 标准库的 `time.sleep(秒数)`
- 特点：程序执行到此处强制休眠指定秒数，不管页面是否加载完成
- 缺点：不智能，即使页面已加载完成也要等满设定时间
- 示例：
  ```python
  import time
  time.sleep(3)  # 强制等待3秒
  ```

#### 4.2 隐式等待（第二种）

- 使用 `driver.implicitly_wait(秒数)`
- 特点：设置一次，永久生效（在整个 driver 生命周期内）
- 工作原理：查找元素时，如果元素未找到，每隔一小段时间（如 0.5 秒）重新查找，直到找到或超过最长等待时间
- 优势：比强制等待智能，元素一旦出现立即继续执行
- 比喻：让你在门口等外卖，等一分钟，一分钟内外卖到了你就拿，外卖没到超过一分钟你就走人
- 示例：
  ```python
  driver.implicitly_wait(10)  # 设置最长等待10秒
  ```

#### 4.3 显式等待（第三种）

- 需要导入：`from selenium.webdriver.support.ui import WebDriverWait`
- 需要导入条件类：`from selenium.webdriver.support import expected_conditions as EC`
- 特点：可指定具体等待条件，最智能、最灵活
- 基本语法：
  ```python
  wait = WebDriverWait(driver, timeout=30, poll_frequency=0.2)
  element = wait.until(EC.presence_of_element_located((By.XPATH, "定位表达式")))
  ```
  - 第一个参数：driver 对象
  - 第二个参数：最长等待时间（如 30 秒）
  - 第三个参数：每隔多久查找一次（默认 0.5 秒）

- 常用等待条件：
  - `EC.visibility_of_element_located()`：等待元素可见
  - `EC.element_to_be_clickable()`：等待元素可点击
  - `EC.presence_of_element_located()`：等待元素存在于 DOM 中（仅在 DOM 中，不要求可见）
  - `EC.title_contains()`：等待标题包含某内容
  - `EC.new_window_is_opened()`：等待新窗口打开
  - `EC.frame_to_be_available_and_switch_to_it()`：等待 iframe 可用并切换

- 与隐式等待的区别：
  - 隐式等待只检查元素是否存在于 DOM
  - 显式等待可检查元素是否可见、是否可点击
  - 某些场景下元素在 DOM 中但不可见（隐藏状态），此时点击会报错

### 五、演示案例：QQ邮箱登录页面

1. **打开目标页面**：访问 QQ 邮箱登录页面

2. **使用强制等待演示**：
   ```python
   time.sleep(3)
   driver.get("https://mail.qq.com")
   time.sleep(10)
   driver.quit()
   ```

3. **使用隐式等待演示**：
   - 设置 `driver.implicitly_wait(10)`
   - 尝试定位页面中的"密码登录"链接（A 标签，id 为 `switcher_plogin`）
   - 直接点击会报错"NoSuchElementException"

4. **发现问题**：即使加了隐式等待，仍然找不到"密码登录"元素。原因是该元素位于 iframe 内部，是一个独立的小页面，讲解了 iframe 是网页嵌套网页的前端技术，将在后续 P 中详细讲解 iframe 切换方法。

### 六、引出 iframe 切换问题

1. **问题根源**：QQ 邮箱登录页面的"密码登录"按钮在 iframe 内部，不在主文档中

2. **解决方案预告**：下 P 将讲解如何使用 `driver.switch_to.frame()` 切换到 iframe 内部进行操作

3. **实战意义**：很多网站会使用 iframe 嵌套，不会切换 iframe 就无法完成抓取

## 提到的外部资源与对象

| 资源/对象 | 角色 | 说明 |
|---|---|---|
| 领导留言板网站 | 案例目标网站 | 上 P 自动登录的目标站 |
| 建议留言板页面 | 案例目标网站 | 本 P 数据抓取的目标站，位于领导留言板下的一个子页面 |
| QQ 邮箱登录页面 (mail.qq.com) | 演示等待机制的案例网站 | 页面包含 iframe 嵌套结构，适合演示等待和切换 |
| `time` 模块 | Python 标准库 | 用于强制等待 `time.sleep()` |
| `selenium.webdriver.support.ui.WebDriverWait` | Selenium 等待类 | 用于显式等待 |
| `selenium.webdriver.support.expected_conditions` (as EC) | Selenium 等待条件模块 | 提供各种等待条件的预定义方法 |
| `find_element` vs `find_elements` | 方法对比 | 前者返回单个元素，后者返回列表 |

## 本P结论

1. **数据抓取基础**：使用 `find_elements` 定位元素列表，通过相对 XPath（加点）逐层提取标题、时间、内容，用元素的 `.text` 属性获取文本。

2. **三种等待方式对比**：
   - 强制等待（time.sleep）：简单粗暴，不智能
   - 隐式等待（implicitly_wait）：设置一次永久生效，智能轮询元素是否出现
   - 显式等待（WebDriverWait + EC）：最灵活，可指定可见、可点击等具体条件

3. **iframe 问题**：遇到"元素在页面上能看到但定位不到"的情况，很可能是该元素在 iframe 中，需要用 `switch_to.frame()` 切换上下文。

4. **下 P 预告**：将详细讲解 iframe 的三种切换方式（通过 name/id、通过索引、通过 WebElement），并在建议留言板案例中实现翻页抓取。
