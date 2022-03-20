import cards_tools

#获取用户输入
while True:
    cards_tools.show_menu()
    op =input('请输入您的选择：\n')
    # 根据用户的输入进行判断
    if op in ['1','2','3']:
        print('用户输入的操作是%s' % op)
        # 对OP值进行进一步判断
        if op =='1':
            cards_tools.new_card()
        elif op =='2':
            cards_tools.show_all_card()
        else:
            cards_tools.search_card()
    elif op =='0':
        print('欢迎使用名片管理系统！')
        break
    else:
        print('您的输入有误，请重新输入')
print('>>>>>>>>名片管理系统结束>>>>>>>>')