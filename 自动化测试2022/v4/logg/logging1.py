import logging

# 调用 指定级别，输入日志信息
# fmt = '%(asctime)s - %(levelname)s - %(filename)s - [%(funcName)s:%(lineno)d] -%(message)s'
# logging.basicConfig(level=logging.INFO,format=fmt,filename='./test_log.log')

# logging.info('this is info...')
# logging.warning('this is warning')
# logging.error('this is error....')
# logging.critical('this is critical')

def get_logg():
    fmt = '%(asctime)s - %(levelname)s - %(filename)s - [%(funcName)s:%(lineno)d] -%(message)s'
    logging.basicConfig(level=logging.INFO, format=fmt, filename='./test_log.log')
    return logging



