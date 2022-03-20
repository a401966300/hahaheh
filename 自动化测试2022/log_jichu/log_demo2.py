import logging.handlers

#  log 底层学习

#获取logger
logger = logging.getLogger()
#设置级别
logger.setLevel(logging.INFO)
# 输出到文件 根据时间切割
th = logging.handlers.TimedRotatingFileHandler(filename='./test.txt',
                                          when='S',   # 时间的单位
                                          interval=1,  # 间隔
                                          backupCount=3)   # 保留文件的个数
# 设置处理器级别  设置为ERROR级别，那么只有ERROR以上信息会输出到文件
th.setLevel(logging.ERROR)
# 获取处理器handler
sh = logging.StreamHandler()


# 添加格式器
fmt = '%(asctime)s - %(levelname)s - %(filename)s - [%(funcName)s:%(lineno)d] -%(message)s'
#logging.basicConfig(level=logging.INFO, format=fmt, filename='./test_log.log')
fm = logging.Formatter(fmt)

# 将格式器添加到处理器中
sh.setFormatter(fm)
th.setFormatter(fm)

#添加处理器handler
logger.addHandler(sh)
logger.addHandler(th)

logger.info('info')
logger.debug('debug')
logger.error('error')
logger.warning('warning')




