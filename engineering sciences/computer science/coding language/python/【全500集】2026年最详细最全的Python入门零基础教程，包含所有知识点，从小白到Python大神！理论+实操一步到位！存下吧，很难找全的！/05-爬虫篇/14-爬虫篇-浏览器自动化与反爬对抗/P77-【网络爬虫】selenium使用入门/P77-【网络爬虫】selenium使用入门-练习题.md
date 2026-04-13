---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 77-【网络爬虫】selenium使用入门
page_index: 77
page_title: 【网络爬虫】selenium使用入门
type: 练习题
tags:
  - 网课
  - 练习题
---

# P77 练习题 - 【网络爬虫】selenium使用入门
---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 77-【网络爬虫】selenium使用入门
page_index: 77
page_title: 【网络爬虫】selenium使用入门
type: 练习题
tags:
  - 网课
  - 练习题
---

# P77 练习题 - 【网络爬虫】selenium使用入门

---

## 一、结构识别

**Q1：填写下图中的空白节点，描述 Selenium 的三层依赖关系。**

```
[ Python代码 ]
     ↓ 调用
[    ①    ]  ← pip安装的库
     ↓ 驱动
[    ②    ]  ← 需与浏览器版本完全一致的可执行文件
     ↓ 控制
[    ③    ]  ← 实际渲染页面的程序
```

> 填完后，解释为什么缺少②就无法运行，即使①和③都已就绪。

---

**Q2：判断以下场景中，应优先用 requests 还是 Selenium，并说明理由。**

| # | 场景描述 | 选择 | 理由 |
|---|---------|------|------|
| A | 爬取静态 HTML 博客的文章列表 | | |
| B | 爬取需要登录后才显示、且登录由 JS 动态渲染的页面 | | |
| C | 爬取返回纯 JSON 的公开 API 接口 | | |
| D | 目标网站部署了穿云盾，requests 返回 403 | | |

---

## 二、机制理解

**Q3：以下代码有两处易错点，请指出并说明会产生什么后果。**

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
html = driver.page_source
print(html)
```

> 提示：对照本P的"易错点"部分，关注"时序"和"资源释放"两个维度。

---

**Q4：为什么说"XPath 是万能解"，而 ID 定位不是？**

请从以下两个角度各写 1～2 句话：
1. 网站结构的实际情况（id 的存在性）
2. XPath 的表达能力（相对于其他定位方式）

---

## 三、最小实践

**Q5：补全下方代码，使其能完成"打开百度首页 → 等待2秒 → 打印页面标题 → 关闭浏览器"的完整流程。**

```python
from selenium import webdriver
import time

# 1. 创建 driver 对象（假设 chromedriver 已在系统 PATH 中）
driver = _______________

# 2. 访问百度首页
_______________("https://www.baidu.com")

# 3. 等待 JS 渲染完成
time.sleep(_______)

# 4. 打印页面标题（不是 page_source，是 driver 的 title 属性）
print(driver._______)

# 5. 关闭浏览器并释放资源
_______________
```

> 完成后，在本地实际运行一次，观察 Chrome 是否自动打开又关闭。

---

**Q6：在百度搜索框中自动输入"Python selenium"并提交，补全关键操作行。**

```python
# 假设 driver 已创建并已 get 到百度首页
# 百度搜索框的 id 为 "kw"，提交按钮 id 为 "su"

search_box = driver.find_element("id", "kw")
search_box._______________("Python selenium")   # 填写输入文字的方法

submit_btn = driver.find_element("id", "su")
submit_btn._______________()                     # 填写点击的方法

time.sleep(2)
print(driver.page_source[:500])  # 打印前500字符确认页面已跳转
```

---

## 四、扩展思考

**Q7：time.sleep() 是本P用于等待页面加载的方案，但它是"盲等"——不管页面是否加载完成，都固定等待指定秒数。**

请思考：这种方式在什么情况下会出问题？你能设想一种"更聪明"的等待方式是什么样的？（不要求写出代码，描述思路即可。）

> 参考方向：Selenium 的 `WebDriverWait` + `expected_conditions` 是进阶解法，可在后续自行探索。

---

## 五、最小替代练习

> 本P涉及 chromedriver 的下载与版本匹配，以下练习验证你的环境配置是否正确。

**Q8：完成 Selenium 环境的完整验证，按步骤记录结果。**

| 步骤 | 操作 | 预期结果 | 你的实际结果 |
|------|------|---------|------------|
| ① | 查看本机 Chrome 版本（地址栏输入 `chrome://version`） | 获得完整版本号，如 `124.0.6367.82` | |
| ② | 前往 `chromedriver.chromium.org` 下载对应版本驱动 | 下载到 `chromedriver.exe`（Windows）或 `chromedriver`（Mac/Linux） | |
| ③ | 运行 `pip install selenium` | 安装成功，无报错 | |
| ④ | 运行 Q5 中补全的代码 | Chrome 自动打开百度，控制台打印标题后关闭 | |

> 若官方下载速度慢，可尝试淘宝镜像（本P知识框架中有备注）。若 Chrome 版本过新找不到对应驱动，可改用 `webdriver-manager` 库自动管理驱动版本（进阶替代方案）。

---

## 答题自查清单

完成本P练习后，确认你能做到以下几点：

- [ ] 能说清 Selenium 三层依赖各自的作用
- [ ] 能判断何时用 requests、何时换 Selenium
- [ ] 能写出"创建driver → 访问页面 → 等待 → 取源码 → 关闭"的完整骨架
- [ ] 能用 `find_element` + `send_keys` / `.click()` 操作页面元素
- [ ] 本地环境已配置完成并成功运行过一次
