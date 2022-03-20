
# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
# # 2. 打印1~100内被3整除的所有数的和 。
# # 3. 使用range()输出1~10内的所有奇数 。
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
o_sum = 0
q_sum = 0
for x in range(1,101):
    if x % 2 == 0:
        o_sum += x
    else:
        q_sum += x
last_sum = o_sum - q_sum
print(last_sum)

# 5. 求1+2+3+...+100的和
sum = 0
for x in range(1,101):
    sum += x
print(sum)


# 6. 判断一个数n能同时被3和5整除
"""
n = int(input("输入一个整数"))
if n % 3 ==0 and n % 5 == 0:
    print("能同时被3和5整除")
else:
    print("不能同时被3和5整除")
"""

# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
a = 136
for x in range(1,101):
    if x == a:
        print("整数在100内")
        break
else:
    print("此整数不在100以内")


# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
"""
lst = []
for x in range(3):
    z = int(input("请输入一个整数"))
    lst.append(z)
lst.sort()
print(lst)
"""
# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
score = 34
if score >=90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")

# 10. 将一个列表的数据复制到另一个列表中。
lst1 = ['abc','bcd',23]
lst2 = lst1[:]
print(lst2)


# 11. 输出 9*9 乘法口诀表。
for x in range(1,10):
    for y in range(x,10):
        print(x,'*',y,'=',x*y,end=' ')
    print()

# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
letter = 0
number = 0
space = 0
other = 0
z = input("请输入一个字符串")
for x in z:
    if x.isspace():
        space += 1
    elif x.isdigit():
        number += 1
    elif x.isalpha():
        letter += 1
    else:
        other += 1
print("字母:",letter,"数字:",number,"空格:",space,"其它:",other)
"""
# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""
a = int(input("请输入一个小于10的正整数"))
n = int(input("请输入一个数"))
s = 0
temp = 0
for x in range(n):
     temp += a
     a *= 10
     s += temp

print(s)
"""

# 14. 题目：打印出如下图案（菱形）:
"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""
t = '*'
sp = " "
s = 4
index = 1
for x in range(1,8):
    if x <= 4:
        vls1 = t * (2 * x - 1)
        vls2 = (s-x) * sp
        ta = vls2 + vls1 + vls2
        print(ta)
    else:
        vls3 = sp * (x-4)
        vls4 = t * (7 -2*index)
        index += 1
        ta1 = vls3 + vls4 + vls3
        print(ta1)