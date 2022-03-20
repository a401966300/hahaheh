import pytest

#fixture和params相结合使用，不常用
@pytest.fixture()
def login_user(request):
    print(f'got date: {request.param}')
    return request.param

@pytest.mark.parametrize('login_user',['tom','chen'], indirect =True)
def test_multi_param(login_user):
    print('=======test_multi_param========')
    print(f'got date: {login_user}')
    assert login_user == 'chen'


if __name__ == '__main__':
    args = ['-s','-q','-k','test_multi_params']
    pytest.main(args)