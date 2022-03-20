import os
import configparser   # 解析xx.ini类型的配置文件

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# print(BASE_DIR)
config_file_path = os.path.abspath(os.path.join(BASE_DIR,'common/config/config.ini'))
# print(config_file_path)

class Config:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.img_dir_path = self.read_config('img','img_dir_path')
        self.json_dir_path = self.read_config('report','json_dir_path')
        self.html_dir_path = self.read_config('report', 'html_dir_path')
        #print(self.html_dir_path)
    # 读取INI配置文件，field,key对应【img】和basexxx
    def read_config(self,field,key):
        try:
            self.cf.read(config_file_path, encoding='utf-8')
            path = self.cf.get(field,key).replace('base_dir',str(BASE_DIR))
            if ':' in path:
                path = path.replace('/','\\')
            return path
        except Exception as e:
            print(f'获取配置数据出现错误:{e}')
config = Config()



if __name__ == '__main__':
    haha = Config()
    print(haha.img_dir_path)


