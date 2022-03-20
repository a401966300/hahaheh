import pytest

#scope = function,class,module，选择一个范围，将打开或者关闭操作在选择的范围内只调用一次
@pytest.fixture(scope='class')   #scope='class'
def login():
    print('=======login==========')

class Testfixturqq():
    def test_case06(self,handle):
        print('=========test_case06 ======')
        assert True

    def test_case07(self):
        print('=========test_case07 ======')
        assert False

if __name__ == '__main__':
    args = ['-q','-s','-k','test']
    pytest.main(args)
