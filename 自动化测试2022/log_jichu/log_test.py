import logging

#  log 底层学习

#获取logger
logger = logging.getLogger()
#设置级别
logger.setLevel(logging.INFO)
# 获取处理器handler
sh = logging.StreamHandler()

#添加处理器handler
logger.addHandler(sh)
#输入信息
logger.info('info')
logger.debug('debug')

