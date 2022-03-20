#encoding=utf-8
import requests
import re
from request.demo_04 import html
import json
# 抓取猫眼电影排行榜
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/60.0.3100.0 Safari/537.36'}
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    return None

def execute_main():
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       + '.*?integer">(.*?)</i>.*?fraction">(.*?)<.*?</dd>',re.S)
    result = pattern.findall(html)
    for ite in result:
        print(ite)
    for item in result:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
def write_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    for item in execute_main():
        print(item)
        write_file(item)
#execute_main()

if __name__ == '__main__':
    main()

