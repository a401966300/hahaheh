#encoding=utf-8
import urllib.request
import re
import urllib.parse
import xlwt
#request = urllib.request.Request
# result = urllib.request.urlopen("http://www.baidu.com")
# print(result.read().decode('utf-8'))

#获取一个post请求
def demo01():
    data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
    response = urllib.request.urlopen('http://httpbin.org/post',data=data)
    print(response.read().decode('utf-8'))
#demo01()

def demo02():
    response = urllib.request.urlopen('http://www.baidu.com')
    #print(response.read().decode('utf-8'))
    print(response.getheaders())
#demo02()

#添加请求头，伪装浏览器访问
def demo03():
    url = 'http://www.douban.com'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    req = urllib.request.Request(url=url,headers=head)
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))
    #print(response.getheader('User-Agent'))

#demo03()

'''workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0,0,'hello')  #写入数据，第一个0表示行，第二个0表示列
workbook.save('student.xls')'''

# workbook = xlwt.Workbook(encoding="utf-8")
# worksheet = workbook.add_sheet('sheet1')
# for i in range(0,9):
#     for j in range(0,i+1):
#         worksheet.write(i,j,'%d * %d = %d' %(i+1,j+1,(i+1)*(j+1)))
# workbook.save('student.xls')



