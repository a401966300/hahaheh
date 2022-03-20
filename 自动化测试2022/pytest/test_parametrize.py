import pytest

#传递数据给测试用例的另外一种方法，比设定方法接收测试数据相对简单一些
#当想实现多组数据组合测试时，比如账号密码的测试，可以添加多个参数序列
@pytest.mark.parametrize('y',[1,3,5])
@pytest.mark.parametrize('x',[2,4,6])
def test_case11(x,y):
    print('\n=========test_case11 ======')
    print(f'got x={x},y={y}')
    assert x != 8 and y !=9

if __name__ == '__main__':
    args = ['-q','-s','-k','test_parametrize']
    pytest.main(args)