# break 语句

# 示例：循环1-10的数并打印，当等于7时退出循环
# for x in range(1,11):
#     if x == 7:
#         break
#     print(x)


# continue
# 示例：循环1-10的数并打印，当等于7时跳过本次循环
# for z in range(1,11):
#     if z == 7:
#         continue
#     print(z)

# 练习：定义一个变量 ，这个变量的值是1~100内的整数 。循环一个数列，然后判断这个变量值否是在这个数列中，如果找到了的话，打印该数字
"""
a = 25
for x in range(1,101):
    if a == x:
        print(x)
        break
"""

# 练习：用户输入一个整数 。判断是否是100内的整数，如果是打印，如果不在给出提示 。
# input()方法：接收用户的输入
# a = input()
# print(a)
user_value = input()
user_value = int(user_value)
print(type(user_value))

for x in range(1,101):
    if user_value == x:
        print("输入的值是:",x)
        break

else:
    print("没有找到此值")


while True:
    x = input("请输入值：")
    x = int(x)
    if x == 20:
        break



