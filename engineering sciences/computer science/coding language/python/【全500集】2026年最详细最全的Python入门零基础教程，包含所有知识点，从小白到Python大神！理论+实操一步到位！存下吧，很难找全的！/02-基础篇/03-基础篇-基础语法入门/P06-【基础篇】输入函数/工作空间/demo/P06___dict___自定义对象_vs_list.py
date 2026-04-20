def show(title):
    print(f"\n===== {title} =====")


show("1. 自定义对象通常有 __dict__")


class Person:
    pass


p = Person()
p.name = "Tom"
p.age = 18

print("p.__dict__ =", p.__dict__)
print("hasattr(p, '__dict__') =", hasattr(p, "__dict__"))
print("p.name =", p.name)
print("p.age =", p.age)


show("2. list 实例通常没有 __dict__")
nums = [1, 2, 3]
print("nums =", nums)
print("hasattr(nums, '__dict__') =", hasattr(nums, "__dict__"))

try:
    print(nums.__dict__)
except AttributeError as e:
    print("访问 nums.__dict__ 报错 =", e)


show("3. 为什么会这样")
print("自定义对象常用 __dict__ 存实例属性。")
print("list 更偏向用内置固定结构存元素，不靠普通实例属性字典。")
