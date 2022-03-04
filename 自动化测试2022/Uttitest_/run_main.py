import unittest
from Uttitest_.demo1 import Test01

# TestLoader,将测试用例文件夹加入到测试套件中

# 测试套件,组装多个用例
suite = unittest.TestLoader().discover('../cases',pattern='test*.py')
# defaultTestLoader = TestLoader()
suite = unittest.defaultTestLoader.discover('../cases')
#执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)





