import json
import yaml

def get_json(filename):
    filepath = '../data/' + filename
    with open(filepath,'r',encoding='utf-8') as f:
        datas = json.load(f)
    arrs = []
    for data in datas.values():
        arrs.append((data['a'],data['b'],data['c'],data['d'],data['e']))
    return arrs

def get_yaml():
    arrs = []
    with open('../data/login_data.yaml','r',encoding='utf-8') as f:
        datas = yaml.safe_load(f).values()
        for data in datas:
            arrs.append(tuple(data.values()))
        print(arrs)

get_yaml()




