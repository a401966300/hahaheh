import pytest
import yaml
import os

#数据驱动，将数据写入到文件（yaml）中，方便数据管理
@pytest.mark.parametrize('x,y', yaml.safe_load(open('data.yaml',encoding='utf-8')))
def test_case_yaml(x,y):
    print('======test_case_yaml=========')
    print(f'got data: x={x},y={y}')
    assert x == 1 and y ==2


if __name__ == '__main__':
    args = ['-s','-q','--alluredir','alluer_result']  #'-k','test_yaml',
    pytest.main(args)
    cnd = 'allure generate %s -o %s -c' % ('alluer_result','test_report')
    os.system(cnd)
