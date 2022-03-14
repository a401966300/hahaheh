import json

def read_json(filename):
    file = '../data/' + filename
    with open(file,'r',encoding='utf-8') as f:
        datas = json.load(f)
        #print(datas)
        return datas

#read_json('write.json')