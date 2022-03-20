#encoding=utf-8
import re   # 正则表达式，进行文字匹配
from bs4 import BeautifulSoup  # 网页解析，获取网页数据后解析数据
import urllib.request,urllib.error   #指定URL，获取网页数据
import xlwt   # 进行excel操作，存储数据

baseurl = 'https://movie.douban.com/top250?start='
findlink = re.compile(r'<a href="(.*?)">',re.S)
findImgsrc = re.compile(r'<img.*?src="(.*?)".*?/>',re.S)
findMovieName = re.compile(r'<span class="title">(.*?)</span>',re.S)
findScore = re.compile(r'<span class="rating_num".*?>(.*?)</span>',re.S)
findPingjia = re.compile(r'<span>(.*?)评价</span>',re.S)
findInq = re.compile(r'<span class="inq">(.*?)</span>',re.S)
findRbq = re.compile(r'<p class="">(.*?)</p>',re.S)

def main():
    #1.爬取网页
    print('开始爬取')
    datalist = getData(baseurl)
    #3.保存数据
    savepath = ".\\豆瓣电影Top250.xls"
    saveData(datalist,savepath)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)

    # 2.解析数据
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_="item"):
            #print(item)  #查看电影ITEM
            data = []
            item = str(item)
            link = re.findall(findlink,item)[0]
            data.append(link)
            imgsrc = re.findall(findImgsrc,item)[0]
            data.append(imgsrc)
            title = re.findall(findMovieName,item)
            if len(title) == 2:
                ctitle = title[0]
                data.append(ctitle)
                etitle = title[1].strip('/')
                data.append(etitle)
            else:
                data.append(title[0])
                data.append(' ')
            score = re.findall(findScore,item)[0]
            data.append(score)
            pingjia = re.findall(findPingjia,item)[0]
            data.append(pingjia)
            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].strip('.')
                data.append(inq)
            else:
                data.append(' ')
            rbq = re.findall(findRbq,item)[0]
            rbq = re.sub('<br(\s+)?/>(\s+)?','',rbq)
            rbq = re.sub('/',' ',rbq)
            data.append(rbq.strip())
            datalist.append(data)
    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/60.0.3100.0 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=head)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html
#保存数据
def saveData(datalist,savepath):
    print('开始保存数据')
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col = ('电影详情链接','图片链接','影片中文名','影片外国名','评分','评价数','概况','相关信息')
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print('第%d条'%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)

if __name__ == '__main__':
    main()


