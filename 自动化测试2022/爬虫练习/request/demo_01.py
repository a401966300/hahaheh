import requests
import re

def echo_type(data):
    print(type(data))
    return True

def first_chart():
    url = 'https://www.maoyan.com/board/4'
    r = requests.get(url)
    echo_type(r)
    print(r.status_code)
    echo_type(r.text)
    print(r.text)
    print(r.cookies)
#first_chart()

def demo_get():
    data = {'name':'black','age':18}
    r = requests.get('http://httpbin.org/get',params=data)
    echo_type(r.text)
    # 将JOSN格式的字符串转换成字典
    print(r.json())
    return True
#demo_get()

def zhihu():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/60.0.3100.0 Safari/537.36'}
    r = requests.get('https://www.zhihu.com/explore',headers = headers)
    print(r.text)
    pattern = re.compile('<a target="_blank" as="[object Object]"class="css-1nd7dqm" href="(.*？)">(.*?)</a>',re.S)
    titles = re.findall(pattern,r.text)
    title = pattern.findall(r.text)
    print(title)
    return True
zhihu()

# 爬取图片
def github():
    r = requests.get('https://github.com/favicon.ico')
    with open('favicon.ico','wb') as f:
        f.write(r.content)
# github()

# 使用Session()可以维持会话
def keep_comminuate():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)
    return True
# keep_comminuate()

