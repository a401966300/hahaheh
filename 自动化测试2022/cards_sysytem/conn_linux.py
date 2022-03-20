
import paramiko

# 创建SSHClient 实例对象
ssh = paramiko.SSHClient()
# 调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程机器，地址，端口，用户名密码
ssh.connect(hostname='192.168.217.129', port=22, username='chenyong', password='a19940122')
# 输入linux命令
cmd = "ll -h"
stdin, stdout, stderr = ssh.exec_command(cmd)
# 输出命令执行结果
result = stdout.read().strip()
new_result = str(result)
print(result)
print(type(result))
print(type(new_result))
# 关闭连接
ssh.close()