import unittest
from parameterized import parameterized
# 编写求和函数
def add(x,y):
    return x+y

data = ([1,2,4],[3,3,6],[4,4,8])
version = 30
class Test01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('执行SETUP')

    def test_add(self):
        result = add(2,5)
        self.assertEqual(result,5)

    def test_add_01(self):
        result1 = add(3,3)
        self.assertEqual(result1,5)

    @classmethod
    def tearDownClass(cls):
        print('执行TEARDOWN')

#测试套件
# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Test01))
# #suite.addTest(Test01('test_add_01'))
# # 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(suite)
class Test02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('执行SETUP')
    @parameterized.expand(data)
    def test_add(self,x,y,z):
        self.assertEqual(x + y, z)

    #@unittest.skip('功能暂未实现')
    def test_add_01(self):
        result1 = add(3, 3)
        self.assertEqual(result1, 6)
    @unittest.skipIf(version > 25,'版本大于25，跳过此方法')
    def test_add_02(self):
        result1 = add(3, 3)
        self.assertEqual(result1, 5)

    @classmethod
    def tearDownClass(cls):
        print('执行TEARDOWN')