---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 78-【网络爬虫】selenium的进阶使用
page_index: 78
page_title: 【网络爬虫】selenium的进阶使用
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P78 知识框架 - 【网络爬虫】selenium的进阶使用
## 本P位置

- 前置：P77 完成领导留言板自动登录
- 本P：完成建议留言板数据抓取 + selenium 三种等待机制
- 后续：P79 讲解 iframe 三种切换方式 + 翻页抓取

本P是 selenium 爬虫从"登录"到"抓取"再到"等待"的过渡环节，同时承上启下地引出 iframe 问题。

## 核心问题

1. 如何在 selenium 中批量抓取列表页的结构化数据
2. 页面未加载完成时元素定位失败怎么办
3. 为什么元素明明可见却定位不到

## 知识骨架

```
selenium 数据抓取
├── find_elements → WebElement 列表
│   └── .text（属性，非方法）获取文本
├── 相对 XPath（加点 .）
│   └── 从当前 WebElement 往下查找
│
selenium 等待机制
├── 强制等待：time.sleep() → 无差别阻塞
├── 隐式等待：implicitly_wait() → 轮询 DOM，driver 级别设置一次永久生效
└── 显式等待：WebDriverWait + EC → 按条件等待，最灵活
    ├── EC.presence_of_element_located()：在 DOM 中
    ├── EC.visibility_of_element_located()：可见
    └── EC.element_to_be_clickable()：可点击
│
iframe 问题
└── 元素在 iframe 内部 → 无法直接定位 → 需 switch_to.frame()
```

## 关系与依赖

```
P77 登录代码（初始化 driver、打开页面、登录操作）
    ↓ 复用代码结构
C06_数据抓取案例.py（新建文件，继承上P登录逻辑）
    ↓ 登录成功后访问建议留言板 URL
定位列表容器：<ul class='animal-list'> → <li> 列表
    ↓ 遍历每条 <li>
提取字段：标题 / 时间 / 内容
    ↓
遇到页面未加载完成
    → 等待机制介入（三选一）
    ↓
遇到 iframe（QQ邮箱演示）
    → 待 P79 switch_to.frame() 解决
```

## 输入 / 输出 / 前置 / 支撑

| 类型 | 内容 |
|---|---|
| 输入 | 目标页面 URL、目标元素的 XPath |
| 输出 | 结构化文本数据（标题、时间、内容组成的列表） |
| 前置依赖 | P77 driver 初始化与登录代码 |
| 支撑工具 | Chrome DevTools（Elements 面板定位元素） |

## 易错点

- `find_element` vs `find_elements`：前者返回单个，后者返回列表，用错类型导致方法不可用
- `.text` 在 selenium 中是属性，不是方法，不能加括号
- XPath 相对路径必须以 `.` 开头表示从当前节点往下找，漏写则从文档根路径查找，结果错误
- 隐式等待设置一次全局生效，多次调用会覆盖，不等于累加
- 隐式等待只检查元素在 DOM 中，不检查可见性；元素若被隐藏，用隐式等待通过后直接操作仍会报错
- 页面有 iframe 时，元素在 DOM 中但不在主文档里，直接定位必然报 NoSuchElementException

## 外部资源与对象

| 资源 / 对象 | 角色 |
|---|---|
| 领导留言板网站 | 案例背景：登录目标站 |
| 建议留言板页面 | 案例抓取目标：列表页结构化数据 |
| QQ 邮箱登录页 (mail.qq.com) | 演示等待失败 + 引出 iframe 问题的跳板网站 |
| `time` 模块（Python 标准库） | 提供 `time.sleep()` 实现强制等待 |
| `selenium.webdriver.Chrome` | driver 实例，承载隐式等待配置 |
| `selenium.webdriver.common.by.By` | 提供 `By.XPATH` 等定位方式常量 |
| `selenium.webdriver.support.ui.WebDriverWait` | 显式等待入口类 |
| `selenium.webdriver.support.expected_conditions` (EC) | 预定义等待条件集合 |
| `driver.switch_to.frame()` | iframe 切换方法，本P引出，P79 详解 |
