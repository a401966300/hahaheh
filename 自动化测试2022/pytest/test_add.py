#自动化测试
import pytest

def add(x,y):
    return x + y

@pytest.mark.run(order=2)     #标记，-m加标记名称smoke.last，最后一个运行,run(num)设置执行顺序
def test_case01():
    print('============ test_case01 =========')
    assert  add(3,5) == 4   #assert 断言语句，判断数据测试结果是否正确,成功的话返回值会显示一个点，失败会显示一个F
class TestAdd():
    @pytest.mark.run(order=3)
    def test_case02(self):
        print('=========test_case02 ======')
        assert add(5,5) == 11

    @pytest.mark.run(order=1)
    def test_case03(self,handle):
        print('=========test_case03 ======')
        assert add(6,6) == 12


if __name__ == '__main__':
    args = ['-s','-q','-k','test_add','--maxfail=2']   #设置一个列表，将列表作为一个参数传入main方法，-v:打印日志信息，-s，打印出print语句，-x，遇到失败用例停止测试
    pytest.main(args)     #-k 后加类型，选择运行某一个测试类下的所有测试用例,加方法就是指定测试某一个测试方法
                            #--maxfail=具体数字，当运行失败的用例达到设定数值时，停止继续测试

