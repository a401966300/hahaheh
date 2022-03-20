# 赋值运算符
# a += b
b = 10
a = 8
a += b
print(a)
a -= b   # ==> a = a-b = 18 - 10
print(a)


# 逻辑运算符:
# 1. and 两个条件同时都满足返回真，否则返回假
# 2. or 两个条件满足一个返回真，否则返回假
# 3. not 条件为真时，返回假，否则返回真 。
d = 20
e = 21
f = 20
g = 22

print(d == f and g == f)
print(d == f or g == f)
print(not g == f)