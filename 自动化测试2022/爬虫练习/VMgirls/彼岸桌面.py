import requests
import parsel
import os

url = 'http://www.netbian.com/1920x1080/index_{}.htm'


def mkdir_file():
    savepath = 'img\\'
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    return savepath


def get_url(url):
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        return response.text
    else:
        return None
#response = get_url(url)


def data_parse():
    savepath = mkdir_file()
    for i in range(15,16):
        print('正在爬取第%d页的图片' % i)
        URL = url.format(i)
        response = get_url(URL)
        #print(response)
        #把获取下来的网页源码HTML转换为SELECTOR对象
        selector = parsel.Selector(response)
        #href = selector.css('.list li a::attr(href)').getall()
        #print(href)
        lis = selector.css('.list li')
        for li in lis:
            title = li.css('b::text').get()
            if title:
                li_url = 'http://www.netbian.com'+li.css('a::attr(href)').get()
                #print(li_url)
                #对壁纸的详情页发情请求
                response_2 = get_url(li_url)
                selector_2 = parsel.Selector(response_2)
                img_url = selector_2.css('.pic img::attr(src)').get()
                img_content = requests.get(url=img_url).content
                #保存壁纸到文件夹
                with open(savepath + title + '.jpg',mode='wb') as f:
                    f.write(img_content)


data_parse()
