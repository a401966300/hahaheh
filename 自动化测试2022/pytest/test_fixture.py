import pytest

#装饰函数，如果某个测试用例需要先进行登录操作，可以把登录函数先装饰一下，然后将其作为一个参数传入具体的测试用例中。
@pytest.fixture()
def login():
    print('=======login==========')

class Testfixture():
    def test_case04(self,login):
        print('=========test_case04 ======')
        assert True

    def test_case05(self,login):
        print('=========test_case05 ======')
        assert False

if __name__ == '__main__':
    args = ['-q','-s','-k','test_fixture']
    pytest.main(args)
