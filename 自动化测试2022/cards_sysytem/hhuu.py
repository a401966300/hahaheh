import time
# lst = (1,2,3,4)
# gg=list(lst)
# print(gg)
#
# bb =[]
# aa = {'name':'小明','age':25}
# for key in aa.items():
#     bb.append(key)
# print(bb)
#
# c=[1,2,3]
#
# print(id(c))
# c[0] = 4
# print(c)
# print(id(c))

tt = 'a=1 b=2 c=3'
haha = dict([x.split('=') for x in tt.split(' ')])
print(haha)