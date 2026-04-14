# dis 反汇编演示：假注释 vs 真注释
import dis

# 假注释函数
def with_fake_comment():
    '''这是假注释三引号
    第二行
    第三行'''
    a = 1
    return a

# 真注释函数
def with_real_comment():
    # 这是一条真注释
    a = 1
    return a

print("=" * 50)
print("1. 字节码长度对比")
print(f"   假注释函数: {len(with_fake_comment.__code__.co_code)} bytes")
print(f"   真注释函数: {len(with_real_comment.__code__.co_code)} bytes")
print()

print("=" * 50)
print("2. 假注释函数字节码")
print("   （三引号字符串被编译进常量池）")
print("=" * 50)
dis.dis(with_fake_comment)
print()

print("=" * 50)
print("3. 真注释函数字节码")
print("   （完全没有字符串）")
print("=" * 50)
dis.dis(with_real_comment)
print()

print("=" * 50)
print("4. 常量池内容对比")
print("=" * 50)
print(f"   假注释函数常量: {with_fake_comment.__code__.co_consts}")
print(f"   真注释函数常量: {with_real_comment.__code__.co_consts}")
