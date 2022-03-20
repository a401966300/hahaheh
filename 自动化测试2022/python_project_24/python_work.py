# 1.输入a,b,c,d 4个整数，计算a+b-c*d的结果
"""
a = int(input("请输入一个整数:"))
b = int(input("请输入一个整数:"))
c = int(input("请输入一个整数:"))
d = int(input("请输入一个整数:"))
result = a+b-c*d
print(result)

"""
# 2.打印1~100内被3整除的所有数的和 。
sum = 0
for x in range(1,101):
    if x % 3 == 0:
        sum += x
print(sum)

# 3. 使用range()输出1~10内的所有奇数 。
for x in range(1,10):
    if x % 2 != 0:
        print(x,end=" ")
print()

# 4.打印1~100所有偶数的和 减去 所有奇数的和 的值
total_sum = 0
o_sum = q_num = 0
for x in range(1,101):
    if x % 2 == 0:
        o_sum += x
    else:
        q_num += x
total_sum = o_sum - q_num
print(total_sum)

# 5. 求1+2+3+...+100的和
sum = 0
for x in range(1,101):
    sum += x
print(sum)

# 6.判断一个数n能同时被3和5整除
"""
n = int(input("请输入整数"))
if n % 3 == 0  and n % 5 == 0:
    print("能同时被3和5整数")
else:
    print("不能同时被3和5整数")
"""

# 7.定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
a = 125
for x in range(1,101):
    if a == x:
        print("此变量是100内的正整数")
        break
else:
    print("100内没有此整数")


# 8.输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
"""
lst = []
for x in range(3):
    aa = int(input("请输入一个整数"))
    lst.append(aa)
lst.sort()
print(lst)
"""
# 9.利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
"""
score = int(input("请输入一个整数"))
if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
"""
# 10.将一个列表的数据复制到另一个列表中。
lt = ['a','b','c','d']
new_lst = lt[:]
print(new_lst)

# 11.输出 9*9 乘法口诀表。
for x in range(1,10):
    for y in range(x,10):
        print(x,"*",y,"=",x*y,end=" ")
    print()

# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
letter = 0
num = 0
space = 0
other = 0

x = input("请输入一行字符")
for z in x:
    if z.isalpha():
        letter += 1
        continue
    if z.isdigit():
        num += 1
        continue
    if z.isspace():
        space += 1
        continue
    other += 1
print("字母：",letter,"数字：",num,"空格：",space,"其它:",other)
"""

# 13.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""
n = int(input("请输入一个小于10的数"))
s = int(input("请输入一个相加数的次数"))
sum = 0
last_sum = 0
for x in range(s):
    sum += n
    n *= 10
    last_sum += sum
print(last_sum)
"""

# 14. 打印出如下图案（菱形）:
t = "*"
sp = " "
s = 4
index = 1
for x in range(1,8):
    if x <=4:
        vls1 = (s-1) * sp
        vls2 = t * (2*x-1)
        print(vls1+vls2+vls1)
        s -= 1
    else:
        vls3 = sp * (x-4)
        vls4 = t * (7 - 2*index)
        index += 1
        print(vls3+vls4+vls3)
