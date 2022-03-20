from api.user_manager import UserManager
import unittest

class TestUserManagerCase(unittest.TestCase):

    id01 = 1001



    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManager()
        cls.new_user = 'test008'


    # case1:只输入用户名和密码，请求添加管理员
    def test01_add_user(self):
        # 1.初始化数据
        username = 'test03'
        password = 'test03'
        # 2.请求接口（添加管理员），输入参数就是用户名和密码
        result = self.user.add_user(username,password)
        data = result.get('data')
        if data:
            user_id = data.get('id')
        if user_id:
            TestUserManagerCase.id01 = user_id
        # 3. 断言
        self.assertEqual(0,result['errno'])
        self.assertEqual(username, result['data']['username'])

    def test04_del_user(self):
        result = self.user.delete_user(TestUserManagerCase.id01)
        self.assertEqual(0,result['errno'])

    def test02_edit_user(self):
        result = self.user.edit_user(TestUserManagerCase.id01,self.new_user,'55555569')
        self.assertEqual(0,result['errno'])
        self.assertEqual(self.new_user, result['data']['username'])

    def test03_get_user(self):
        result = self.user.get_user()
        self.assertEqual(0, result['errno'])
        # self.assertEqual(self.new_user, result['data']['username'])







if __name__ == '__main__':
    unittest.main()