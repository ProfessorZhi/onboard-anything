---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 79-【网络爬虫】selenium反爬的破解方案
page_index: 79
page_title: 【网络爬虫】selenium反爬的破解方案
type: 练习题
tags:
  - 网课
  - 练习题
---

# P79 练习题 - 【网络爬虫】selenium反爬的破解方案
## 一、结构识别

**题目 1.1**
selenium 启动的 Chrome 浏览器可被网站识别，主要依赖哪些检测点？请从下列选项中选出全部正确项。

- A. `infobar` 提示文字
- B. `navigator.webdriver` 属性标志位
- C. CSS 样式中的 `background-color` 值
- D. 开发者工具是否被触发打开

**题目 1.2**
特征伪装需要在两个层面同时生效，请将以下措施正确归类。

| 措施 | 所属层面 |
|------|----------|
| 添加 `--disable-infobars` 启动参数 | ① |
| 执行 JS 脚本覆盖 `navigator.webdriver` | ② |
| 添加 `--disable-extensions` 启动参数 | ① |
| 执行 JS 脚本覆盖 `navigator.plugins` | ② |

## 二、机制理解

**题目 2.1**
某爬虫工程师只给 Chrome 添加了 `--disable-infobars` 启动参数，没有执行任何 JS 脚本。结果：infobar 提示消失了，但目标网站仍然拒绝加载数据。请解释原因。

**题目 2.2**
代码执行顺序对反爬效果有直接影响。判断以下说法是否正确，并说明理由：

> "防检测 JS 脚本既可以在 `get()` 之前执行，也可以在 `get()` 之后执行，效果相同。"

**题目 2.3**
chromedriver 版本与本地 Chrome 版本的关系是反爬成功的隐性前提。请描述当版本不匹配时会发生什么，以及为什么。

## 三、最小实践

**题目 3.1**
请补全以下代码框架中的注释（①②③），实现 selenium 反爬的基本配置流程。

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
# ① 为 options 添加至少两个启动参数，消除 UI 层特征
options.add_argument('__①__')
# 创建驱动
driver = webdriver.Chrome(options=options)
# ② 执行防检测 JS 脚本，覆盖 navigator.webdriver 等属性
driver.__②__
# ③ 访问目标网站
driver.get('https://example.com')
```

**题目 3.2**
某同学编写了以下代码，但脚本执行后网站仍然检测到 selenium。请指出最可能的三处原因。

```python
driver = webdriver.Chrome(options=options)
driver.get('https://air-quality.example.com')  # 立即访问，未留足时间
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})
# 后续元素定位...
```

## 四、扩展思考

**题目 4.1**
反爬与反反爬本质上是**持续迭代的对抗关系**。请思考：如果网站升级检测手段（例如不仅检测 `navigator.webdriver`，还检测浏览器内核版本指纹），你现有的防检测方案需要如何调整？这种调整的方向是什么？

**题目 4.2**
假设你无法使用 selenium，但仍需要绕过基于浏览器特征的反爬检测。你可以考虑哪些替代方案？请列出至少两种思路，并简要说明其原理。

## 五、最小替代练习（可选）

**题目 5.1**
selenium 的主要替代方案之一是使用 requests 配合抓包分析，直接请求数据接口。但这种方法的前提是找到真实的数据接口。

请描述：当你面对一个有反爬保护的网站时，用 selenium 绕过和用 requests + 抓包分析这两种思路，各自的核心挑战是什么？你如何判断哪种方法更适用于当前场景？
