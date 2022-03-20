#encoding=utf-8
import re
from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html = file.read().decode('utf-8')
bs = BeautifulSoup(html,'html.parser')   #'html.parse'是解析器
# print(bs.title)  # 取标签title并将标签和标签内的内容打印出来
# print(bs.a.attrs) # 拿到标签内的所有属性
# print(bs.head)
#1.TAG 标签，找到标签的第一个内容
#2.Navigablestring 标签里的内容
#3.Beautifulsoup 表示整个文档
#4.comment 特殊的Navigablestring，输出的内容不包含注释符号
#print(bs)

#-------------------------
#文档的遍历
#print(bs.head.contents[1])
#文档的搜索
# 查找所有的a标签.字符串过滤，查找与字符串完全匹配的内容
#t_list = bs.find_all('a')
#print(t_list)
#正则表达式搜索，使用search()方法匹配内容
#t_list = bs.find_all(re.compile('a'))

#传入一个函数，根据函数要求来搜索
# def name_is_exist(tag):
#     return tag.has_attr('name')
# t_list = bs.find_all(name_is_exist)
# for item in t_list:
#     print(item)

#2.kwargs 参数
# t_list = bs.find_all(id='head')
# for item in t_list:
#     print(item)

#CSS选择器
# print(bs.select('title'))  #标签
# print(bs.select('.mnav'))  #类名
# print(bs.select('#u1'))  # ID
print(bs.select("a[class='bri']"))  #属性





