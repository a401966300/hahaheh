import unittest

# 编写求和函数
def add(x,y):
    return x+y

class Test01(unittest.TestCase):



    def test_01(self):
        result = add(2,5)
        print('1---',result)

    def test_add_02(self):
        result1 = add(3,3)
        print('2---',result1)


# 测试套件
# suite = unittest.TestSuite()
# suite.addTest(Test01('test_add'))
# #suite.addTest(Test01('test_add_01'))
# # 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(suite)

