'''
主要完成管理员接口的实现
'''
from api.base import Base
from loguru import logger


class UserManager(Base):

    def __init__(self):
        self.add_user_path = '212121'
        self.delete_user_path = ''
        self.edit_user_path = ''
        self.get_user_path = ''
        self.login('admin123','admin123')   # 临时用来测试

    def add_user(self,username,password,**kwargs):
        user_data = {'username':username,'password':password}
        if kwargs:
            logger.info('添加管理员接收可选参数:{}'.format(kwargs))
            user_data.update(**kwargs)
        add_path = self.get_url(self.add_user_path)
        return self.post(add_path,user_data)

    def delete_user(self,id,**kwargs):
        del_data = {'id': id}
        if kwargs:
            del_data.update(**kwargs)
        del_path = self.get_url(self.delete_user_path)
        return self.delete_user(del_path,del_data)

    def edit_user(self,id,username,password,**kwargs):
        edit_data = {'id':id,'username':username,'password':password}
        if kwargs:
            edit_data.update(**kwargs)
        edit_path = self.get_url(self.edit_user_path)
        return self.edit_user(edit_path,edit_data)

    def get_user(self):
        get_path = self.get_url(self.get_user_path)
        return self.get(get_path)

if __name__ == '__main__':
    um = UserManager()
    um.add_user('admin888','admin999')