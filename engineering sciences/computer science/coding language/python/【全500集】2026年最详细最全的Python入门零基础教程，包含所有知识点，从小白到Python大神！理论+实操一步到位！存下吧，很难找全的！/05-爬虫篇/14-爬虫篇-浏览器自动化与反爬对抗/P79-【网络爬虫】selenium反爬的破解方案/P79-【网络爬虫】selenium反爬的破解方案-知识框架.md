---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 79-【网络爬虫】selenium反爬的破解方案
page_index: 79
page_title: 【网络爬虫】selenium反爬的破解方案
type: 知识框架
tags:
  - 网课
  - 知识框架
---

# P79 知识框架 - 【网络爬虫】selenium反爬的破解方案
## 本P位置

Python 爬虫技术链中，selenium 属于「无头浏览器/自动化模拟」层。本P位于反爬策略体系的「客户端特征对抗」节点，前置依赖是 selenium 基本操作（P78），后续可衔接 Ajax 数据抓取、IP代理轮换等更复杂的反爬对抗手段。

## 核心问题

selenium 启动的 Chrome 浏览器存在可被识别的机器特征，网站据此拒绝加载数据。核心任务：消除特征，使浏览器在 JS 层表现为普通用户浏览器。

## 知识骨架

**反爬检测层**
网站 JS 通过读取浏览器特征属性判断是否 selenium → 检测点包括 infobar 文字、navigator.webdriver 标志位、行为轨迹、开发者工具触发

**特征伪装层**
消除检测点 → 两条路径：
路径A：Chrome 启动参数（disable-infobars / disable-extensions / disable-dev-shm-usage）
路径B：JS 脚本覆盖 navigator.webdriver 等属性

**两者必须同时生效**，参数去 UI 层提示，JS 去属性层检测，缺一则网站仍可识别

## 关系与依赖

反爬检测（网站）→ 识别特征（selenium 浏览器）→ 特征伪装（两重手段）→ 数据获取（爬虫目标）

检测与伪装是一对持续迭代的对抗关系：网站升级检测手段 → 需要更新 JS 脚本参数

## 输入 / 输出 / 前置 / 支撑

- **输入**：目标网站 URL
- **输出**：绕过反爬后正常渲染的页面（可用于后续元素定位与数据提取）
- **前置**：已安装 selenium、chromedriver 版本与 Chrome 匹配
- **支撑**：防检测 JS 脚本（固定参数组合，非自研，直接复用）

## 易错点

1. 只加启动参数不执行 JS 脚本 → infobar 消失但网站仍拒绝加载
2. JS 脚本执行时机错误（须在 get 访问页面之前执行，而非之后）
3. WebDriver 创建后立即 get，未留足脚本注入时间
4. chromedriver 与 Chrome 版本不匹配 → 参数不生效

## 外部资源与对象

- **chromedriver**：Chrome 与 selenium 之间的桥梁，须与本地 Chrome 版本严格对应
- **防检测 JS 脚本**：直接复制使用的现成脚本，负责覆盖 navigator.webdriver 等属性，本质是固定参数组合
- **目标网站（空气质量查询）**：作为检测场景演示，验证破解方案有效性的测试对象
