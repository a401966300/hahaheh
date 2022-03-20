import re
import parsel
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import threading

headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }

pattern = re.compile(r'magnet:\?xt=urn:btih:\w+',re.I)


def one():
    lst1 = []
    try:
        for i in range(1,11):
            lst1.append(i)
            print(i)
            url = 'https://rtretyrytre.xyz/search.php?mod=forum&searchid=576233&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page={}'.format(i)
            req = requests.get(url,headers=headers)
            #print(req.status_code)
            if req.status_code == 200:
                response = req.text
                #print(response)
            else:
                print('请求网页失败')
            selector = parsel.Selector(response)
            items = selector.css('.xs3 a::attr(href)').getall()
            for item in items:
                it = 'https://rtretyrytre.xyz/' + item
                resp = requests.get(it,headers = headers)
                resp.encoding = resp.apparent_encoding
                response1 = resp.text
                #response_2 = get_url(li_url)
                selector_2 = parsel.Selector(response1)
                cili_url = selector_2.css('.blockcode li::text').get()
                if cili_url:
                    # cili_url = pattern.findall(cili_url)[0]
                    # if cili_url:
                    print(cili_url)
                    with open('guochang.txt','a',encoding = 'utf-8') as f:
                        f.write(cili_url + '\n')
            print(lst1)
    except Exception as e:
        print(i,e)
def two():
    lst2 = []
    try:
        for i in range(60,101,2):
            lst2.append(i)
            print(i)
            url = 'https://rtretyrytre.xyz/search.php?mod=forum&searchid=567861&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page={}'.format(i)
            req = requests.get(url,headers=headers)
            #print(req.status_code)
            if req.status_code == 200:
                response = req.text
                #print(response)
            else:
                print('请求网页失败')
            selector = parsel.Selector(response)
            items = selector.css('.xs3 a::attr(href)').getall()
            for item in items:
                it = 'https://rtretyrytre.xyz/' + item
                resp = requests.get(it,headers = headers)
                resp.encoding = resp.apparent_encoding
                response1 = resp.text
                #response_2 = get_url(li_url)
                selector_2 = parsel.Selector(response1)
                cili_url = selector_2.css('.blockcode li::text').get()
                if cili_url:
                    # cili_url = pattern.findall(cili_url)[0]
                    # if cili_url:
                    print(cili_url)
                    with open('guochang.txt', 'a',encoding = 'utf-8') as f:
                        f.write(cili_url + '\n')
        print(lst2)
    except Exception as e:
        print(i,e)


if __name__ == '__main__':
    t1 = threading.Thread(target=one, )
    #t2 = threading.Thread(target=two, )
    t1.start()
    #t2.start()