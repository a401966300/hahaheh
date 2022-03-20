import requests
import os
import parsel
import selenium


savepath = 'img_2\\'
if not os.path.exists(savepath):
    os.mkdir(savepath)

url = 'https://mm.enterdesk.com/bizhi/63899-347866.html'
headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }
req = requests.get(url,headers=headers)
req.encoding='utf-8'
print(req)
#req.encoding = req.apparent_encoding
response = req.text
print(response)
# selector = parsel.Selector(response)
# li_url_list = selector.css('.egeli_pic_li dd a::attr(href)').getall()
# print(li_url_list)


