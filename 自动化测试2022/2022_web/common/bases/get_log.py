import os
import logging

project_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


def logger():
    logging.basicConfig(level=logging.INFO,format= '%(asctime)s %(levelname)s %(filename)s [line: %(lineno)d] %(message)s')
    logger = logging.getLogger(project_name)
    return logger


if __name__ == '__main__':
    logger = logger()
    logger.info('this is info')