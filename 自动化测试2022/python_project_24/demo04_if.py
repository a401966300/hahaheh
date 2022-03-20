# if语句

# 1.if单分支语句

# 需求 ： 如果今天下雨，打印 带雨伞
a = "今天下雨学习"
if a == "今天下雨":
    print("带雨伞")

# 2. if多分支语句
# 需求 ： 定义一个分数，判断分数是不及格,及格，良，优秀
score = 88
if score > 90:
    print("优秀")
elif score >= 80:
    print("良")
elif score >= 70:
    print("及格")
else:
    print("不及格")

# 各种数据类型的返回值
a = 1  # 变量的赋值
if a:
    print("hello world")
    print("hello world")
    print("hello world")

if 2:
    print("==============")

b = "xx"
if b:
    print("hello hello")

c = None
if not c:
    print("hello hello hello")

d = 2
if d:
    print("hello xxx")


# is和 in
x = "hello"
y = "hello python"
if x in y:
    print("x元素在y元素里")
else:
    print("x元素不在y元素里")

h = 56788889999999
p = 56788889999999
print(h==p)
print(h is p)
