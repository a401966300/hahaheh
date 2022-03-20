from HTMLTestRunner import HTMLTestRunner
import unittest
import logging.handlers
#
# def main1():
#     suite = unittest.defaultTestLoader.discover('./', pattern='test*.py')
#     with open('./report.html','wb') as f:
#         runner = HTMLTestRunner(title='登录测试报告',stream=f)
#         runner.run(suite)
# if __name__ == '__main__':
#     main1()


def get_lo():
    # 获取日志器
    logger = logging.getLogger()
    # 设置日志器输出级别
    logger.setLevel(logging.INFO)
    #获取处理器
    sh = logging.StreamHandler()
    th = logging.handlers.TimedRotatingFileHandler(filename='./test.log',when='midnight',interval=1,backupCount=30,encoding='utf-8')
    # 设置处理器输出格式
    th.setLevel(logging.ERROR)
    # 格式器
    fmt = "%(asctime)s-%(levelname)s-%(filename)s-[%(funcName)s-%(lineno)d]-%(message)s-"
    fm = logging.Formatter(fmt)

    sh.setFormatter(fm)
    th.setFormatter(fm)

    #添加格式器
    logger.addHandler(sh)
    logger.addHandler(th)

    return logger

haha = get_lo()
haha.info('hhhhhhhhhhhh')


