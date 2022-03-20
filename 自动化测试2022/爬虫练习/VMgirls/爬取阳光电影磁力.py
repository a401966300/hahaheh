import re
import requests
import parsel
import xlwt

url = 'https://www.ygdy8.com/html/gndy/china/list_4_1.html'
pattern = re.compile('<b>.*?<a class="ulink" href=.*?</a>.*?<a href="(.*?)" class="ulink">(.*?)</a>.*?</b>',re.S)
pattern_2 = re.compile('<a target="_blank" href="(.*?)".*?</a>',re.S)


def get_url(url):
    req = requests.get(url)
    req.encoding = req.apparent_encoding
    if req.status_code == 200:
        return req.text


def exe_main():
    datalist = []
    responese = get_url(url)
    selector = parsel.Selector(responese)
    url_list = selector.css('b').getall()
    #print(url_list)
    for item in url_list:
        data = []
        item = str(item)
        #print(item)
        herf = 'https://www.ygdy8.com/' + re.findall(pattern,item)[0][0]
        title = re.findall(pattern,item)[0][1]
        data.append(title)
        responese_2 = get_url(url=herf)
        cili = re.findall(pattern_2,responese_2)[0]
        data.append(cili)
        datalist.append(data)
    print(datalist)



    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    cols = ['电影名称','磁力链接']
    for i in range(0,2):
        sheet.write(0,i,cols[i])
    for i in range(len(datalist)):
        Data = datalist[i]
        for j in range(0,2):
            sheet.write(i+1,j,Data[j])
    workbook.save('.\\电影.xls')




exe_main()