login_url = 'https://sso.jrj.com.cn/sso/ssopassportlogin'

success_data = {'msg': '退出', 'username': '财友2sna6763', 'password': 'Ok654321'}

failed_data = [
    {'name': '登录-反向用例-用户名为空', 'username': '', 'password': '654321', 'error_msg': '账号登录'},
    {'name': '登录-反向用例-用户名错误', 'username': '财友', 'password': '654321', 'error_msg': '账号或密码错误'},
    {'name': '登录-反向用例-密码为空', 'username': 'caiyou', 'password': '', 'error_msg': '账号登录'},
    {'name': '登录-反向用例-密码错误', 'username': '财友2sna6763', 'password': '123456', 'error_msg': '账号或密码错误'}
]