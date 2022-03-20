# 字典

# 1.字典的定义
dt = {}
dt1 = {'city':'北京','wd':27}
print(dt)
print(dt1)

# 2.字典的取值 : 字典名称['key']
print("获取字典中城市的值:",dt1['city'])

# 字典的更新或添加
dt1['city'] = '上海'
print(dt1)

dt1['area'] = '2300Km'
print(dt1)

# 3.字典中常用的方法
dt2 = {'name':'zhangsan','age':27}

# 获取字典中键名对应的值 : get()
print(dt2.get('name1'))

# 1) get()和dt[key]的区别

# 获取字典中所有的键 ： keys()
print(dt2.keys())

# 获取字典中所有的值 ： values()
print(dt2.values())

# 获取字典中所有键值对 : items()
print(dt2.items())

for x in dt2.keys():
    print(x)

# 循环键值对
for k,v in dt2.items():
    print('字典key:',k,'对应的值:',v)