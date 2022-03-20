# 列表
"""
定义列表
    变量名 = []
    变量名 = [数据1,数据2,...]
"""
# lst1 = []
# lst2 = ['red',10,None,True,23.89,['xxxx','hello']]
# print(lst1)
# print(lst2)

# 需求： 使用列表打印1-10的数
for x in [1,2,3,4,5,6,7,8,9,10]:
    print(x)

# 问题 ： 想要往列表中插入元素 ? 进行修改操作 ？

# 需求 ： 实现列表中的增删改
lst = ['red','gold','orange','blue']
# 向列表lst中插入一个元素 ： append(元素)
lst.append('green')
print(lst)
lst1 = ['java','python','go']
# 向列表lst中插入一组元素 ： extend(seq)
lst.extend(lst1)
print(lst)
# 修改列表中第二个元素的值为'hello' ： 列表的索引
lst[1] = 'hello'
print(lst)

# 删除列表中最后的一个值 ： pop()
lst.pop()
print(lst)

# 列表的翻转reverse()和排序sort()
lst.reverse()
print(lst)
lst.sort()
print(lst)

