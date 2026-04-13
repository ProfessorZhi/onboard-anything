---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 78-【网络爬虫】selenium的进阶使用
page_index: 78
page_title: 【网络爬虫】selenium的进阶使用
type: 练习题
tags:
  - 网课
  - 练习题
---

# P78 练习题 - 【网络爬虫】selenium的进阶使用
---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 78-【网络爬虫】selenium的进阶使用
page_index: 78
page_title: 【网络爬虫】selenium的进阶使用
type: 练习题
tags:
  - 网课
  - 练习题
---

# P78 练习题 - 【网络爬虫】selenium的进阶使用

## 结构识别

**Q1：区分三种等待机制的作用域与触发条件**

下表列出了三种等待方式，请补全空白列：

| 等待方式 | 代码入口 | 作用范围 | 等待条件 | 适用场景 |
|---|---|---|---|---|
| 强制等待 | `time.sleep(n)` | _____ | _____ | _____ |
| 隐式等待 | `driver.implicitly_wait(n)` | _____ | _____ | _____ |
| 显式等待 | `WebDriverWait + EC` | _____ | _____ | _____ |

> 提示：重点区分"等待的是什么"与"设置一次还是逐句配置"。

---

**Q2：判断以下 XPath 的差异**

给定一个已定位到的 `<li>` 元素存储在变量 `item` 中，以下两行代码的结果有何不同？

```python
# 写法 A
driver.find_element(By.XPATH, "//span[@class='title']")

# 写法 B
item.find_element(By.XPATH, ".//span[@class='title']")
```

请说明：
1. 写法 A 和写法 B 的查找起点分别是哪里？
2. 在遍历多条 `<li>` 时，哪种写法会出现"每次都返回第一条数据"的 bug？原因是什么？

---

## 机制理解

**Q3：隐式等待的两个隐藏限制**

阅读以下场景，判断隐式等待能否解决问题，并给出原因：

- **场景 A**：页面正在加载，目标 `<div>` 还未插入 DOM，`driver.find_element()` 立即调用。
- **场景 B**：目标 `<button>` 已在 DOM 中，但被 CSS 设置为 `display: none`，代码尝试点击它。
- **场景 C**：目标元素在 `<iframe>` 内部，主文档 DOM 中不存在该元素。

每个场景请回答：隐式等待是否会让代码通过？通过后操作会不会报错？

---

**Q4：为什么 iframe 内的元素无法直接定位**

用一句话解释：`NoSuchElementException` 在 iframe 场景下的本质原因是什么（从"selenium 默认操作上下文"角度回答）？并说明本 P 留下了这个问题，P79 将用什么方法解决。

---

## 最小实践

**Q5：批量抓取列表数据**

参考本 P 建议留言板案例，在任意含有重复列表结构的页面上完成以下代码骨架：

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("你选定的目标页面 URL")

# 1. 定位所有列表项
items = driver.find_elements(By.XPATH, "___填入列表项 XPath___")

# 2. 遍历每一项，提取至少两个字段
results = []
for item in items:
    field_1 = item.find_element(By.XPATH, "___相对 XPath___").___  # 注意：text 是属性
    field_2 = item.find_element(By.XPATH, "___相对 XPath___").___
    results.append({"field_1": field_1, "field_2": field_2})

print(results)
driver.quit()
```

完成后检查：
- [ ] `find_elements` 返回的是列表，`find_element` 返回的是单个元素，是否用对？
- [ ] `.text` 后面没有加括号 `()`？
- [ ] 第二层 XPath 以 `.` 开头，从 `item` 节点往下查找？

---

**Q6：三种等待的最小对比实验**

打开任意加载稍慢的网页，分别用以下三种方式等待某个元素出现，记录结果：

```python
# 方式一：强制等待
import time
time.sleep(3)
driver.find_element(By.XPATH, "目标元素 XPath")

# 方式二：隐式等待
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "目标元素 XPath")

# 方式三：显式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "目标元素 XPath"))
)
```

记录并对比：三种方式实际等待时长是否不同？哪种最早返回？哪种在元素不可见时仍然通过？

---

## 扩展思考

**Q7：隐式等待与显式等待混用会怎样**

查阅 selenium 官方文档或可靠资料，回答：selenium 官方是否推荐同时使用隐式等待和显式等待？如果混用会出现什么问题？你会在项目中采用哪种策略，理由是什么？

---

## 最小替代练习

**Q8（替代练习）：无真实登录站点时的 iframe 引出实验**

本 P 使用 QQ 邮箱登录页演示 iframe 导致的定位失败。若无法访问该页面，请：

1. 在本地新建一个 `test.html`，内容如下：

```html
<!DOCTYPE html>
<html>
<body>
  <p id="outside">主文档段落</p>
  <iframe id="myframe" srcdoc="<p id='inside'>iframe 内部段落</p>"></iframe>
</body>
</html>
```

2. 用 selenium 打开该本地文件，分别尝试：
   - 直接 `find_element` 定位 `id='inside'` 的元素，观察报错信息
   - 直接 `find_element` 定位 `id='outside'` 的元素，确认成功
3. 记录报错信息，思考：报错类型是否和本 P 描述的 `NoSuchElementException` 一致？

> 此实验结果将直接对应 P79 `switch_to.frame()` 的动机。
