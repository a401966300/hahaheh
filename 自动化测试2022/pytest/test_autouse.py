import pytest

#
@pytest.fixture(autouse=True)  #当定义了一个方法使用autouse=True后，后面的测试方法执行前都会调用装饰后的方法
def login():
    print('=======login==========')

class Testfixture():
    def test_case08(self):
        print('=========test_case08 ======')
        assert True

    def test_case09(self):
        print('=========test_case09 ======')
        assert False

if __name__ == '__main__':
    args = ['-q','-s','-k','test_autouse']
    pytest.main(args)
