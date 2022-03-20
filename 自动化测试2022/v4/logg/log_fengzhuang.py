import logging.handlers

class GetLog:

    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger == None:
            #获取日志器
            cls.logger = logging.getLogger()
            # 设置日志器级别
            cls.logger.setLevel(logging.INFO)
            #获取两个处理器，控制台加文件
            sh = logging.StreamHandler()
            th = logging.handlers.TimedRotatingFileHandler(filename = './test.txt',
                                                           when = 'midnight',
                                                           interval= 1,
                                                           backupCount= 30,
                                                           encoding='utf-8'
                                                            )
            # 设置处理器级别
            th.setLevel(logging.ERROR)

            # 设置格式器
            fmt = '%(asctime)s -%(levelname)s -%(filename)s [%(funcName)s:%(lineno)s] -%(message)s'
            fm = logging.Formatter(fmt)

            # 将格式器添加到处理器中
            sh.setFormatter(fm)
            th.setFormatter(fm)

            #将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger

if __name__ == '__main__':

    logger = GetLog().get_logger()
    logger.info('this is info')
    logging.debug('this is debug')
    logging.warning('this is warning')
    logging.error('this is error--错误')
    logging.critical('this is critical')