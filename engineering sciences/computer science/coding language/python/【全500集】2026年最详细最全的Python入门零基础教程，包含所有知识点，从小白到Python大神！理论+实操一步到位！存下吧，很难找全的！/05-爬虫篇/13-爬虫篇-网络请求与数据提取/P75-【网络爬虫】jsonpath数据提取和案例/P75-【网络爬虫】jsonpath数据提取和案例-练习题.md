---
course: 【全500集】2026年最详细最全的Python入门零基础教程，包含所有知识点，从小白到Python大神！理论+实操一步到位！存下吧，很难找全的！
level: page
chapter: 75-【网络爬虫】jsonpath数据提取和案例
page_index: 75
page_title: 【网络爬虫】jsonpath数据提取和案例
type: 练习题
tags:
  - 网课
  - 练习题
---

# P75 练习题 - 【网络爬虫】jsonpath数据提取和案例
---

## 一、结构识别

**1.1** Python内置json模块提供四个核心方法，请将以下方法与其功能一一对应：

| 方法 | 功能 |
|------|------|
| json.loads() | ① 从JSON字符串得到Python对象 |
| json.dumps() | ② 从Python对象得到JSON字符串 |
| json.load() | ③ 从文件读取JSON数据 |
| json.dump() | ④ 将Python对象写入文件 |

---

**1.2** 已知JSONPath表达式 `$.data.items[0].title` 和 `$..name`，请判断以下说法是否正确：

| 说法 | 正确/错误 |
|------|----------|
| 两个表达式都以根节点为起点 |  |
| `.items[0]` 表示取items数组的第一个元素 |  |
| `..name` 表示递归搜索所有层级的name字段 |  |
| `$..name` 和 `$.name` 效果完全相同 |  |

---

## 二、机制理解

**2.1** 某API返回的JSON片段如下：

```json
{
  "code": 200,
  "data": {
    "total": 100,
    "items": [
      {"id": 1, "title": "项目A", "visible": true},
      {"id": 2, "title": "项目B", "visible": false}
    ]
  }
}
```

请判断执行以下代码后的输出：

```python
result = json.loads(response_text)
titles = jsonpath(result, '$.data.items[*].title')
print(type(titles))
```

- A. `<class 'str'>`
- B. `<class 'list'>`
- C. `<class 'dict'>`

---

**2.2** 某同学写了如下代码，运行时发现 `print(item['author'])` 抛出 `KeyError`，但数据明明存在。请问最可能的原因是什么？

```python
for item in data['items']:
    print(item['author'])
```

---

## 三、最小实践

**3.1** 补全代码：使用jsonpath从以下JSON数据中提取所有文章的作者名字。

```python
import json
from jsonpath import jsonpath

data = {
    "articles": [
        {"id": 1, "author": "张三", "content": "内容1"},
        {"id": 2, "author": "李四", "content": "内容2"}
    ]
}

# 补全这行代码，使用JSONPath提取所有作者名
authors = jsonpath(data, '___')

# 期望输出：['张三', '李四']
print(authors)
```

---

**3.2** 根据下方JSON结构，写出能提取「所有层级中所有status值」的JSONPath表达式：

```json
{
  "result": {
    "status": "active",
    "details": {
      "status": "pending",
      "items": [
        {"status": "completed"}
      ]
    }
  }
}
```

---

## 四、扩展思考

**4.1** 翻页爬取时，某接口返回的数据从第1页开始，每页20条，总共5页。当前代码只能抓第1页：

```python
url = "https://api.example.com/news?p=1"
response = requests.get(url)
data = response.json()
```

请描述如何修改代码实现完整翻页抓取，并写出核心循环结构的伪代码。

---

**4.2** 如果JSON响应中某些记录缺少某个字段（如 `"author"` 字段缺失），直接访问 `item['author']` 会报错。请设计一个安全的数据提取方案，既能提取存在的字段，又能跳过缺失的字段。至少写出两种思路。

---

## 五、最小替代练习

**5.1** jsonpath官方提供在线测试页面：`https://jsonpath.com/`

请访问该工具，使用以下JSON数据验证表达式是否正确：

```json
{
  "store": {
    "book": [
      {"category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century"},
      {"category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour"}
    ],
    "bicycle": {"color": "red", "price": 19.95}
  }
}
```

请分别验证以下三个JSONPath表达式的匹配结果，并截图或记录输出：

| 表达式 | 预期匹配内容 |
|--------|-------------|
| `$.store.book[*].author` | 所有书籍作者 |
| `$..price` | 所有价格（包含bicycle） |
| `$.store.book[?(@.category=="fiction")]` | 分类为fiction的书籍对象 |

---

## 参考答案概要

| 题号 | 答案要点 |
|------|---------|
| 1.1 | ①→loads、②→dumps、③→load、④→dump |
| 1.2 | 对、对、对、错（递归与直接子节点不同） |
| 2.1 | B（list类型） |
| 2.2 | 部分items元素缺少author字段，或字段名拼写不一致 |
| 3.1 | `'$.articles[*].author'` 或 `'$.articles[].author'` |
| 3.2 | `'$..status'` |
| 4.1 | 循环改变p参数值，range(1,6)，直到数据为空break |
| 4.2 | 思路1：dict.get()方法；思路2：try-except捕获；思路3：提前判断 `if 'author' in item` |
| 5.1 | 自行验证，重点观察返回的是数组还是单个值 |
