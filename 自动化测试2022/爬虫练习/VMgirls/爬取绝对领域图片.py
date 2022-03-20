#encoding=utf-8

import os
import parsel
import requests
import re

if not os.path.exists('img_4\\'):
    os.mkdir('img_4\\')

url = 'https://www.jdlingyu.com/tuji/page/'


def get_url(url):
    req = requests.get(url)
    req.encoding = req.apparent_encoding
    response = req.text
    if req.status_code == 200:
        return response
    else:
        print('请求失败')
        return False


def req_data(resp):
    selector = parsel.Selector(resp)
    lis = selector.css('.post-info')
    for li in lis:
        href = li.css('a::attr(href)').get()
        title = li.css('a::text').get()
        response_2 = get_url(href)
        if not response_2:
            return False
        selector_2 = parsel.Selector(response_2)
        img_urls = selector_2.css('.entry-content img::attr(src)').getall()
        #print(img_urls)
        #print('------------------')
        for x in range(len(img_urls)):
            #print(img_urls[x])
            img_content = requests.get(img_urls[x]).content
            with open('img_4\\' + title + '_{}'.format(x) + '.jpg',mode='wb') as f:
                 f.write(img_content)
    return True


def exe_main():
    for i in range(2,6):
        print('开始获取第{}页的图片链接'.format(i))
        response = get_url(url+str(i))
        if not response:
            return False
        result = req_data(response)
        if not result:
            print('获取图片失败，请检查')
            return False
        print('第{}页的图片获取完毕'.format(i))
    print('获取图片成功')
    return True

if __name__ == '__main__':
    exe_main()