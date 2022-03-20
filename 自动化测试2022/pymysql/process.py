
连接数据库步骤:
1.导包
import pymysql
2.设置连接属性
conn = pymysql.connect(user = 'root',password = 'root',host = 'localhost',charset = 'utf8')
3.建立游标对象
cursor = conn.cursor
4.连接数据库执行sql语句
class Mysql():
    def __init__(self,sql):
        self.sql = sql


    def select(self):











