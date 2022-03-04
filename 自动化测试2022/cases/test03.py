import unittest

# 编写求和函数
def add(x,y):
    return x+y

class Test03(unittest.TestCase):



    def test_05(self):
        result = add(2,5)
        print('5---',result)

    def test_add_05(self):
        result1 = add(3,3)
        print('6---',result1)


# 测试套件
# suite = unittest.TestSuite()
# suite.addTest(Test01('test_add'))
# #suite.addTest(Test01('test_add_01'))
# # 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(suite)

