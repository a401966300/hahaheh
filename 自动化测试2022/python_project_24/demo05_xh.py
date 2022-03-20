# for循环
"""
for 变量 in 序列:
    代码块
"""
# 1.需求 ： 循环出字符串中的每一个字符

s = "abcdefg"
for z in s:
    print(z)

# while 循环
"""
while 条件语句:
    代码块
"""
# 2. 打印1~5的所有整数
a = 1
while a<=5:
    print(a)
    a += 1      #  a = a + 1


# range()方法： 生成一个数字序列
"""
range(start,end,step)
    start:代表的是开始位置，默认是从0
    end：代表的是结束位置，默认不包括最后一个数
    step:代表的是步长，默认的步长是1
"""
# 需求： 循环1-10内的整数
for x in range(1,11):
    print(x)
