#encoding=utf-8
import re
import parsel
import requests

url = 'https://www.qb5.tw/book_79575/'
pattern = re.compile(r'div id="content".*?<a href=.*?>斗罗大陆V重生唐三</a>(.*?)</div>',re.S)

def get_url(url):
    req = requests.get(url)
    req.encoding = req.apparent_encoding
    if req.status_code == 200:
        response = req.text
        return response
    else:
        print('请求失败')
        return False

def get_data():
    response = get_url(url)
    selector = parsel.Selector(response)
    capters = selector.css('.zjlist dd')
    #print(capters)
    for capter in capters:
        title = capter.css('a::text').get()
        if title:
            print('开始写入《斗罗大陆V重生唐三》之{}'.format(title))
            capter_url = url + capter.css('a::attr(href)').get()
            print(capter_url)
            response_1 = get_url(capter_url)
            capters = pattern.findall(response_1)[0]
            # print(capters)
            capters = capters.replace('最新章节！<br><br> ', '')
            capters = capters.replace('<br /><br />', '\n')
            capters = capters.replace(' &nbsp;&nbsp;&nbsp;&nbsp;', '')
            capters = capters.replace('&nbsp;&nbsp;&nbsp;&nbsp;', '')
            with open('斗罗大陆V重生唐三.txt', 'a+', encoding='utf-8') as f:
                f.write(title.center(80, ' ') + '\n')
                f.write(capters)
                f.write('\n')

get_data()

def qq():
    response = get_url(url='https://www.qb5.tw/book_79575/50563871.html')
    #selector = parsel.Selector(response)
    capters = pattern.findall(response)[0]
    #print(capters)
    capters = capters.replace('最新章节！<br><br> ', '')
    capters = capters.replace('<br /><br />', '\n')
    capters = capters.replace(' &nbsp;&nbsp;&nbsp;&nbsp;','')
    capters = capters.replace('&nbsp;&nbsp;&nbsp;&nbsp;', '')
    print(capters)
    with open('xiaoshuo.txt','a+',encoding='utf-8') as f:
         f.write('huhu'.center(80,' ') + '\n')
         f.write(capters)
         f.write('\n')


