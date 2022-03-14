
import json

# 字典转换为JSON
# data1 = {'name':'haha','age':18}
# data = json.dumps(data1)
# print(data)
#
# # JSON转换为字典
# aa = '{"name":"haha","age":18}'
# bb = json.loads(aa)
# print(bb)

# # JSON写
# cc = {'name':'zhangsan','age':55}
# with open('write.json', 'w', encoding='utf-8') as f:
#     json.dump(cc,f,ensure_ascii=False)


if __name__ == '__main__':

    # JSON读
    with open('write.json','r',encoding='utf-8') as f:
        data = json.load(f)
    print(data)
    arrs = []
    for x in data.values():
        arrs.append((x['a'],x['b'],x['c']))

    print(arrs)





