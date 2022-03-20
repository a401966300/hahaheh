# 界面层，用户界面上的操作
from services.user_services import UserService

if __name__ == '__main__':

    us = UserService()

    text = input("请输入数据：")

    if text in ['1','新增']:
        print('调用新增功能')
        abc = input()
        lst = abc.split(' ')
        us.add_stu(*lst)

    elif text in ['2','修改']:
        print('调用修改功能')
        abc = input()
        lst = abc.split(' ')
        us.mod_stu(*lst)
    elif text in ['3','删除']:
        print('调用删除功能')
        abc = input()
        lst = abc.split(' ')
        us.del_stu(*lst)
    else:
        print('调用查询功能')
        name = input()
        result = us.get_stu(name)
        print(result)
