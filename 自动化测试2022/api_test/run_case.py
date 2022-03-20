# 批量运行测试用例，生成测试报告
import unittest
from HTMLTestRunner import HTMLTestRunner
from api.base import Base
from setting import username,password

if __name__ == '__main__':
    Base().login(username,password)
    suite = unittest.TestLoader().discover('./cases','test*case.py')

    test_report_file = 'test_report.html'

    with open(test_report_file,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告')
        runner.run(suite)



