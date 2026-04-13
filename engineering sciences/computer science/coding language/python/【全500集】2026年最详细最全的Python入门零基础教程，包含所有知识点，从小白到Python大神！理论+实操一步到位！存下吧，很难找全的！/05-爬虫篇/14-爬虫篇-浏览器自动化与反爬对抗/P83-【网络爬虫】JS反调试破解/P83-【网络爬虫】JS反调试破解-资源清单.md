---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 83-【网络爬虫】JS反调试破解
page_index: 83
page_title: 【网络爬虫】JS反调试破解
type: 资源清单
tags:
  - 网课
  - 资源清单
---

# P83 资源清单 - 【网络爬虫】JS反调试破解
---

## 1. Tampermonkey（油猴）

- **类型**：浏览器扩展
- **在本P中的作用**：核心绕过工具，用于编写和执行自定义JavaScript脚本，覆盖网站禁用的函数、事件监听器和定时器，从而绕过各种反调试机制
- **来源**：字幕直接提到
- **建议方向**：系统学习油猴脚本的元数据块格式（==UserScript==标记块）、@match匹配规则、常见API（GM_setValue、GM_getValue、GM_xmlhttpRequest），参考官方文档和社区脚本库

---

## 2. 浏览器开发者工具（DevTools）

- **类型**：工具
- **在本P中的作用**：JS逆向的主要工作环境，提供Elements面板分析DOM、Console面板执行命令、Sources面板设置断点调试、Network面板监控网络请求；同时也是网站检测的目标对象
- **来源**：字幕直接提到
- **建议方向**：深入掌握Sources面板的条件断点、XHR/Fetch断点，Console的snippets功能，以及使用"停靠到窗口右侧"模式避免宽高检测

---

## 3. Selenium / webDriver

- **类型**：自动化框架
- **在本P中的作用**：用于自动化控制浏览器抓取网页内容，但网站会检测其特征（如navigator.webDriver属性、ChromeOptions参数）判断是否为机器人访问
- **来源**：字幕直接提到
- **建议方向**：学习Selenium的反检测配置（undetected-chromedriver、stealth插件），了解webDriver属性检测的实现原理及常见绕过思路

---

## 4. debugger 语句

- **类型**：JavaScript关键字
- **在本P中的作用**：无限debugger断点是网站常用的反调试手段，通过Function构造函数动态生成或定时循环触发，使代码停在断点处无法继续执行
- **来源**：字幕直接提到
- **建议方向**：学习在开发者工具中取消"在此处暂停"、使用Event Listener Breakpoints拦截，以及通过油猴脚本覆盖window.debugger函数

---

## 5. console.clear()

- **类型**：JavaScript方法
- **在本P中的作用**：网站通过setInterval定时调用console.clear()清空控制台输出，干扰调试人员观察变量值和代码执行结果
- **来源**：字幕直接提到
- **建议方向**：在油猴脚本中覆盖console.clear为空函数，或使用Object.defineProperty重定义console对象

---

## 6. setInterval / clearInterval

- **类型**：JavaScript全局函数
- **在本P中的作用**：setInterval用于创建定时器执行无限debugger、清屏等反调试逻辑；clearInterval用于清除这些定时器以停止干扰
- **来源**：字幕直接提到
- **建议方向**：学习通过开发者工具的Event Listener面板或代码分析定位定时器句柄，编写清除脚本

---

## 7. Function 构造函数

- **类型**：JavaScript内置构造函数
- **在本P中的作用**：网站使用new Function()动态创建包含debugger的函数，使反调试代码在源码中不可见，增加逆向分析难度
- **来源**：字幕直接提到
- **建议方向**：理解Function构造函数的执行机制，学习通过重写Function构造函数或在调用处打断点来追踪动态代码

---

## 8. Date.prototype

- **类型**：JavaScript对象原型
- **在本P中的作用**：网站利用debugger断点前后的时间戳差值判断是否处于调试状态（通常设定阈值为50ms），需要hook Date.prototype.getTime等方法绕过检测
- **来源**：字幕直接提到
- **建议方向**：学习原型链修改技术，通过Object.defineProperty重定义getTime方法，或使用setTimeout延迟修改确保数据先加载完成

---

## 9. iframe

- **类型**：HTML元素
- **在本P中的作用**：网站通过iframe嵌套加载真实数据页面，形成独立的防护层级，需要针对iframe内页面的域名单独编写油猴脚本
- **来源**：字幕直接提到
- **建议方向**：学习识别iframe嵌套结构的方法（如开发者工具Elements面板查看），理解iframe与父页面的作用域隔离及通信机制

---

## 10. Canvas API / Canvas指纹

- **类型**：浏览器API + 检测技术
- **在本P中的作用**：网站通过Canvas API生成独特的图形指纹，识别Selenium等自动化工具的渲染环境差异
- **来源**：字幕直接提到
- **建议方向**：了解Canvas指纹的生成原理，学习通过修改Canvas渲染参数（如toDataURL结果）实现指纹伪装

---

## 11. navigator.webDriver 属性

- **类型**：浏览器属性
- **在本P中的作用**：Selenium控制的浏览器会暴露navigator.webDriver为true，网站检测该属性判断是否为自动化访问，进而阻止数据加载
- **来源**：字幕直接提到
- **建议方向**：在油猴脚本中重写Object.defineProperty(navigator, 'webDriver', {get: () => false})覆盖该属性

---

## 12. 窗口宽高检测（outerWidth/innerWidth）

- **类型**：检测技术
- **在本P中的作用**：网站通过window.outerWidth - window.innerWidth和outerHeight - innerHeight的差值判断是否打开了开发者工具（通常阈值300px），据此执行反调试逻辑
- **来源**：字幕直接提到
- **建议方向**：将开发者工具设置为"停靠到窗口右侧"等模式，或通过油猴脚本覆盖相关属性返回值

---

## 13. 快捷键禁用（F12、右键、Ctrl+S）

- **类型**：JavaScript事件拦截
- **在本P中的作用**：网站通过监听keydown/keyup事件拦截F12、Ctrl+S等调试快捷键，通过contextmenu事件阻止右键菜单显示
- **来源**：字幕直接提到
- **建议方向**：编写油猴脚本在document上重定义onkeydown、oncontextmenu等事件处理函数返回正常结果

---

## 资源速查表

| 资源名称 | 类型 | 核心用途 |
|---------|------|---------|
| Tampermonkey | 浏览器扩展 | 执行自定义绕过脚本 |
| DevTools | 调试工具 | JS逆向工作环境 |
| Selenium | 自动化框架 | 批量抓取（会被检测） |
| debugger | JS关键字 | 无限断点干扰 |
| console.clear() | JS方法 | 清空调试输出 |
| setInterval/clearInterval | JS函数 | 定时检测与清除 |
| Function构造函数 | JS内置对象 | 动态生成不可见代码 |
| Date.prototype | 原型对象 | 时间差检测hook目标 |
| iframe | HTML元素 | 分层防护载体 |
| Canvas指纹 | 检测技术 | 自动化环境识别 |
| webDriver属性 | 浏览器属性 | Selenium特征检测 |
| 窗口宽高检测 | 检测技术 | 控制台开启判断 |
