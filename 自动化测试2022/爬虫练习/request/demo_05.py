import re
import requests
from lxml import etree

from lxml import etree
text = '''
<div>
<Ul>
<li class="item-O"><a href=”linkl.html”>first item</a><li>
<li class="item-1"><a href=”link2.html”>second item</a><li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a><li>
<li class="item-5"><a href="link5.html">fifth item</a>
</ul>
</div>'''

html = etree.HTML(text)   # 构造XPATH解析对象
#result = etree.tostring(html)   # 输出修正后的HTML代码
#ww = result.decode('utf-8')  #  decode()方法将bytes数据转换为str

# HTML = etree.parse('./test.html',etree.HTMLParser())
# result = HTML.xpath('//li/a')  # //可以获取子孙节点  //ul/a无法获取结果，因为a不是ul的直接子节点
# qq = HTML.xpath('//li/a/@href')
# print(qq)
#print(result[0])

# result = html.xpath('//li[1]/a/text()')
# aa = html.xpath('//li/a/@href')
# print(result)
# print(aa)
headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }
aa = requests.get('https://up.enterdesk.com/edpic/56/c9/e0/56c9e06c045e1ff43b91e7f6dee71736.jpg',headers=headers)
print(aa.status_code)
print(aa.text)

