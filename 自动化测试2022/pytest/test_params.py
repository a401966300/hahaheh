import pytest

#传递测试数据给测试用例，首先装饰要传递数据的方法，将数据写入，然后用request接收数据，返回数据后就可以传递给用例了
@pytest.fixture(params=[1,3,5])
def pass_date(request):
    return request.param

def test_case10(pass_date):
    print('=========test_case10 ======')
    print(f'got date:',{pass_date})
    assert pass_date != 8

if __name__ == '__main__':
    args = ['-q','-s','-k','test_params']
    pytest.main(args)