# 实现业务逻辑层，对学生进行增删改查的业务逻辑实现
from mode.base import Mysql

class UserService():

    def __init__(self):
        self.m = Mysql()

    def add_stu(self,*args):
        # 实现思路
        # 1。确定用户数据，最终组装成sql语句
        lst = list(args)
        while len(lst) <= 6:
            lst.append(' ')
        sql = "insert into students(name,age,sex,class,card,city) values('{}',{},'{}','{}','{}','{}')".format(*lst)
        # 2 。调用update（）方法，实现插入学生操作
        result2 = self.m.update(sql)
        # 3.给用户提示信息（插入成功）
        if not result2:
            print('添加信息成功')
        else:
            print('添加信息失败')

    def del_stu(self,column,value):
        if str(value).isdigit():   # 判断字符串是否只由数字组成  str.isdigit()
            sql = "delete from students where {} = {}".format(column,value)
        else:
            sql = "delete from students where {} = '{}'".format(column, value)
        result = self.m.update(sql)
        if not result:
            print('打印信息成功')
        else:
            print('打印信息失败')

    def mod_stu(self,column,value,name):
        if str(value).isdigit():
            sql = 'update students set {} = {} where name like "%{}%"'.format(column,value,name)
        else:
            sql = "update students set {} = '{}' where name like '%{}%'".format(column, value, name)
        result3 = self.m.update(sql)
        if not result3:
            print('添加信息成功')
        else:
            print('添加信息失败')

    def get_stu(self,value):
        if str(value).isdigit():
            sql = "select * from students where name like '%{}%'".format(value)
        else:
            sql = "select * from students where name like '%{}%'".format( value)
        result = self.m.get_all(sql)
        return result

if __name__ == '__main__':
    us = UserService()
    us.add_stu('张三',25,'man','5','123456','上海')
    # us.mod_stu()
    # us.del_stu()
    # us.get_stu()

