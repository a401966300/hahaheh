from HTMLTestRunner import HTMLTestRunner
import time
import unittest


def exe_main():
    with open('../report/test_report.html','wb',) as f:
        suite = unittest.defaultTestLoader.discover('./',pattern='test*.py')
        runner = HTMLTestRunner(stream=f,verbosity=2,title='TPshop测试报告')
        runner.run(suite)

if __name__ == '__main__':
    exe_main()