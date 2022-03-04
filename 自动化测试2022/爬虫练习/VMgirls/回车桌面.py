import requests
import os
import parsel
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if not os.path.exists('img_3\\'):
    os.mkdir('img_3\\')

url = 'https://mm.enterdesk.com/bizhi/64235.html'

headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }


driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(3)
page = driver.page_source
# soup = BeautifulSoup(driver.page_source,'lxml')
time.sleep(3)
# print(driver.page_source)
driver.quit()
#print(page)

# for item in soup.find_all('a',class_="pics_pics"):
#     #print(item.get('src'))
#     img_url = item.get('src')
#     title = item.get('href')
#     title = title.replace('/','')
#     img = requests.get(img_url,headers=headers)
#     # print(title)
#     # print(img)
#     with open('img_3\\'+title +'.jpg','wb') as f:
#         f.write(img.content)

# print('-----------------------------------')


selector_2 = parsel.Selector(page)
img_urls = selector_2.css('.pics_pics')
#print(img_urls)
for i in range(len(img_urls)):
    #print(item.get('src'))
    img_url = img_urls[i].css('img::attr(src)').get()
    img_url = img_url.replace('_360_360','')
    #print(img_url)
    title = img_urls[i].css('img::attr(title)').get()
    img = requests.get(img_url,headers=headers)
    # print(title)
    # print(img)
    with open('img_3\\'+title + str(i) +'.jpg','wb') as f:
        f.write(img.content)


