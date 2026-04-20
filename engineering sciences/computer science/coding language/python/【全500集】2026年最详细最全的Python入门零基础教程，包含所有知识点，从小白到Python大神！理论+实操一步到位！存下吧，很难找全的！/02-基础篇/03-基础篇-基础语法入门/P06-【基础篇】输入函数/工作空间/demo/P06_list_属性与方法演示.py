def show(title):
    print(f"\n===== {title} =====")


def show_block(label, text):
    print(f"{label}:")
    print(text)


show("1. list 实例对象")
nums = [1, 2, 3]
print("nums =", nums)
print("type(nums) =", type(nums))
# 预期结果: <class 'list'>
# 为什么: __class__ 表示这个实例对象所属的类型
print("nums.__class__ =", nums.__class__)
# 预期结果: 一段关于 list 的说明文字
# 为什么: 实例对象也能访问到类型提供的帮助文档
show_block("nums.__doc__", nums.__doc__)
# 检查 list 实例是否像很多自定义对象一样带有普通实例属性字典 __dict__
print("hasattr(nums, '__dict__') =", hasattr(nums, "__dict__"))
# 预期结果: <built-in method append of list object at ...>
# 为什么: 这是绑定到当前 nums 实例上的 append 方法
print("nums.append =", nums.append)
# 预期结果: <built-in method sort of list object at ...>
# 为什么: 这是绑定到当前 nums 实例上的 sort 方法
print("nums.sort =", nums.sort)


show("2. list 类型对象")
print("list =", list)
print("type(list) =", type(list))
print("list.__name__ =", list.__name__)
print("list.__bases__ =", list.__bases__)
# 预期结果: (<class 'list'>, <class 'object'>)
# 为什么: list 找属性和方法时, 先找自己, 找不到再沿继承链去 object 里找
print("list.__mro__ =", list.__mro__)
# 预期结果: 一段关于 list 的说明文字
# 为什么: __doc__ 是类型对象自己的帮助文档属性
show_block("list.__doc__", list.__doc__)
# 预期结果: <method 'append' of 'list' objects>
# 为什么: 这里看的不是 nums.append 这种“某个实例绑定后的方法”, 而是 list 类型上定义的 append 方法本体
print("list.append =", list.append)
# 预期结果: <method 'sort' of 'list' objects>
# 为什么: sort 也是定义在 list 类型上的方法, 所有 list 实例都是从这里获得这项能力
print("list.sort =", list.sort)
# 预期结果: [<class 'list'>, <class 'object'>]
# 为什么: mro() 和 __mro__ 表达的是同一条查找链, 只是返回形式不同
print("list.mro() =", list.mro())


show("3. append: 改原对象, 返回 None")
nums = [1, 2, 3]
print("调用前 nums =", nums)
# 这里只是查看“绑定在 nums 实例上的 append 方法对象本身”，还没有真正调用
print("nums.append =", nums.append)
# 这里才是真正调用 append 方法
result = nums.append(4)
print("调用后 nums =", nums)
print("append 返回值 =", result)


show("4. pop: 改原对象, 返回被删除元素")
nums = [10, 20, 30]
print("调用前 nums =", nums)
result = nums.pop()
print("调用后 nums =", nums)
print("pop 返回值 =", result)


show("5. sort: 改原对象, 返回 None")
nums = [3, 1, 2]
print("调用前 nums =", nums)
result = nums.sort()
print("调用后 nums =", nums)
print("sort 返回值 =", result)


show("6. index: 不改原对象, 返回位置")
nums = [10, 20, 30]
print("调用前 nums =", nums)
result = nums.index(20)
print("调用后 nums =", nums)
print("index 返回值 =", result)


show("7. 其他常见方法")
nums = [1, 2, 3]
print("原始 nums =", nums)

nums.extend([4, 5])
print("extend 后 =", nums)

nums.insert(1, 99)
print("insert 后 =", nums)

nums.remove(2)
print("remove 后 =", nums)

count_result = nums.count(1)
print("count(1) 返回 =", count_result)
print("count 后 nums =", nums)

nums.reverse()
print("reverse 后 =", nums)

nums.clear()
print("clear 后 =", nums)


show("8. 重点对比: 类型上的方法定义 vs 实例上的绑定方法")
nums = [1, 2, 3]
print("list.append =", list.append)
print("nums.append =", nums.append)
print("list.sort =", list.sort)
print("nums.sort =", nums.sort)


show("9. type(...) 对照: 普通函数, 类型方法, 绑定方法")


def demo_func():
    pass


nums = [1, 2, 3]
s = "a b"

print("type(demo_func) =", type(demo_func))
print("type(list.append) =", type(list.append))
print("type(nums.append) =", type(nums.append))
print("type(str.split) =", type(str.split))
print("type(s.split) =", type(s.split))
