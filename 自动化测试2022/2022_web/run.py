import pytest
import os,sys
from common.bases.get_config import config

json_dir_path = config.json_dir_path
html_dir_path = config.html_dir_path


if __name__ == '__main__':
    args = ['-s','-q','--alluredir',json_dir_path]
    sef = sys.argv[1:]
    pytest.main(args + sef)
    cmd = 'allure generate %s -o %s -c' % (json_dir_path,html_dir_path)
    os.system(cmd)
