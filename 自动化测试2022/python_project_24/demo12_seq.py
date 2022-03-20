# 序列 - 索引
lst = ['abc','bcd','efg']
s = "abcdefg"
tp = (1,2,3,4)
print(lst[2])
print(lst[-1])
print(s[3])
print(tp[0])

# 序列 -切片
lst5 = ['red','green','blue','black','gold','orange']
print(lst5[1:3:1])
print(lst5[1:3])

print(lst5[0:4:1])
print(lst5[:4:])

print(lst5[0:6:1])
print(lst5[::])
print("=" * 50)


# 序列 - 相加| 相乘
a_lst = ['12']
b_lst = [23]
c_lp = ('jdx',)
print(a_lst + b_lst)
# print(b_lst + c_lp)
print(a_lst * 5)
c_lst = [None] * 5
print(c_lst)



# 序列 - 检查元素
lst8 = ['red', 'yellow', 'cream', 'blue', 'gunmetal']
print('green' in lst8)


# 列表生成式

# 需求 ： 生成一个0~10的偶数 。
lst9 = []
for x in range(0,11):
    if x % 2 == 0:
        lst9.append(x)
print(lst9)


print([x+1 for x in range(0,11) if x % 2 == 0 ])


for x in range(1,10):   # 外层循环
    for y in range(1,10):   # 内层循环
        print(x ,'*', y ,"=" , x * y,end=' ')
    print()
lst10 = [1,2,34,56]
for x in lst10:
    print(x)

for index,value in enumerate(lst10):
    print(index,"====",value)