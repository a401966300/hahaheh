import logging.handlers


class GetLogger():
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger == None:
            # 设置日志器
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            # 设置处理器输出到文件，控制台
            sh = logging.StreamHandler()
            th = logging.handlers.TimedRotatingFileHandler(filename='./log.txt',when='midnight',interval=1,backupCount=30,encoding='utf-8')
            th.setLevel(logging.ERROR)

            # 设置格式器
            fmt = '%(asctime)s -%(levelname)s -%(filename)s [%(funcName)s -%(lineno)d] -%(message)s'
            fm = logging.Formatter(fmt)

            #将设置好的格式器添加到处理器
            sh.setFormatter(fm)
            th.setFormatter(fm)
            #添加处理器到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        return cls.logger


