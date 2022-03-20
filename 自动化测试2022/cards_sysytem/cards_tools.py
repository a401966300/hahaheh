# 1.定义显示菜单功能函数
def show_menu():
    print('')
    print('*'*50)
    print('欢迎使用【名片管理系统】 v1.0')
    print('')
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print('')
    print('0. 退出系统')
    print('*'*50)
#定义全局变量，名片列表
card_list = []

#2. 定义新建名片功能函数
def new_card():
    print('[功能] 新建名片')
    # 1.取用户输入
    name_str  = input('请输入姓名:')
    phone_str = input('请输入电话:')
    qq_str    = input('请输入QQ号:')
    email_str = input('请输入邮箱:')
    # 2.将获取的输入信息保存到字典中去
    new_dict = {
            'name': name_str,
            'phone':phone_str,
            'qq':   qq_str,
            'email':email_str
    }
    # 3.将字典添加到列表中去
    card_list.append(new_dict)
    #4. 打印新建名片成功
    print('新建 %s 名片成功!' % name_str)
    print('名片列表,card_list: ',card_list)
    return card_list


#3.定义显示全部名片功能函数
def show_all_card():
    if len(card_list) ==0:
        print('无记录')
        return
    print('[功能] 显示全部名片')
    print('_'*50)
    print('姓名'.ljust(10),'电话'.ljust(10),'QQ号'.ljust(10),'邮箱'.ljust(10),sep='\t\t')
    print('_' * 50)
    for card_dict in card_list:
        print(card_dict.get('name').ljust(10),card_dict.get('phone').ljust(10),
              card_dict.get('qq').ljust(10),card_dict.get('email').ljust(10),sep='\t\t')
#4。定义查询名片功能函数
def search_card():
    find_name = input('[功能')
    for key in card_list:
        if key.get('name') ==find_name:
            print('您想要找的人信息为：\n姓名 %s 电话 %s QQ号 %s 邮箱 %s' % (key.get('name'),key.get('phone'),key.get('qq'),key.get('email')))
            break
    else:
        print('没有找到，请重新输入')