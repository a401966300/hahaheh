import pymysql
from view.setting import DB_config
class Mysql():
    #构造方法
    def __init__(self):
        self.conn = pymysql.connect(**DB_config)

 # 插入，删除，修改
    def update(self,sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                self.conn.commit()    #  手动提交数据
        except Exception as e:
            self.conn.rollback()   # 回滚操作，SQL语句执行失败后，程序回滚到执行前
            print(e)
        finally:
            if self.conn:
                self.conn.close()
# 查询数据
    def get_all(self,sql):
        try:
            with self.conn.cursor() as cursor:   # 用with代码完成后会自动关闭conn.cursor()
                cursor.execute(sql)
                result = cursor.fetchall()    # fetchall,查询所有数据
                return result
        except Exception as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

if __name__ == '__main__':
# 入口函数，判断程序是否在当前文件，如果是则首先运行此部分代码块：
        sql = "select * from students where name = '项宇'  "
        m = Mysql()
        result_1 = m.get_all(sql)
        print(result_1)

