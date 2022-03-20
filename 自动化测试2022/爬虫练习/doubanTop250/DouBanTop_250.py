import re
import urllib
import requests
from requests.exceptions import RequestException

#url = 'http://movie.douban.com/top250'
url = 'https://movie.douban.com/top250?start={}&filter='

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        #response.encoding = 'utf-8'
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def exe_main(offset):
    ur = url.format(offset)
    result = str(get_one_page(ur))
    #print(result)
    pattern = re.compile(r'<li>.*?class="item".*?class="pic".*?class="info".*?class="hd".*?href="(.*?)".*?class="title">(.*?)</span>',re.S)
    #patt = re.compile('<a href="(.*?)">')
    search = pattern.findall(result)
    print(search)
for i in range(25,101,25):
    exe_main(i)