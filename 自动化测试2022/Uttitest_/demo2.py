import unittest
from Uttitest_.demo1 import Test02
from HTMLTestRunner import HTMLTestRunner
import time

def Suite():
    # 测试套件,组装多个用例
    suite = unittest.TestSuite()
    # suite.addTest(Test01('test_add'))
    # suite.addTest(Test01('test_add_01'))
    suite.addTest(unittest.makeSuite(Test02))
    # 执行测试套件
    runner = unittest.TextTestRunner()
    runner.run(suite)
#Suite()


# python自带的assert
def python_assert():
    #assert 'hello' == 'hell'
    assert 'h' in 'hello'
    assert 0

#python_assert()

# 测试报告
def html_report():
    #suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(Test02))
    suit = unittest.defaultTestLoader.discover('../cases/',pattern='test*.py')
    with open('./report_{}.html'.format(time.strftime('%Y-%m-%d %H-%M-%S')),'wb') as f:
        runner = HTMLTestRunner(stream=f,verbosity=2,title='测试报告')
        runner.run(suit)

html_report()
