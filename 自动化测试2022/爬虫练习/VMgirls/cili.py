
import parsel
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver


headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }

for i in range(1,11):
    print(i)
    url = 'https://rtretyrytre.xyz/forum-2-{}.html'.format(i)
    req = requests.get(url,headers=headers)
    if req.status_code == 200:
        response = req.text
    else:
        print('请求网页失败')
    selector = parsel.Selector(response)
    items = selector.css('.icn a::attr(href)').getall()
    for item in items:
        item = 'https://rtretyrytre.xyz/' + item
        resp = requests.get(item,headers = headers)
        # print(response1.status_code)
        resp.encoding = resp.apparent_encoding
        response1 = resp.text
        # #response_2 = get_url(li_url)
        selector_2 = parsel.Selector(response1)
        cili_url = selector_2.css('.blockcode li::text').get()
        if cili_url:
            print(cili_url)
            with open('guochang.txt','a',encoding='utf-8') as f:
                f.write(cili_url + '\n')
