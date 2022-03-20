'''pymysql的作用：
通过pymysql操作数据的步骤：
 1.导包：import pymysql
 2.建立连接：conn = pymysql.connect()
 connect()参数：
      1).user : 代表连接数据库的用户名
      2).password:连接数据库的密码
      3).host:连接数据库的主机名字
      4).database：连接的数据库
      5).port:连接的端口
      6)charst:设置编码

 3 建立游标对象：cursor = conn.cursor()
 4.执行sql语句：cursor.execute(sql)

 查询一条数据：cursor.getone()
 查询所有数据：cursor.getall()

 5.关闭游标对象：cursor.close()
 6.关闭连接对象：conn.close()



