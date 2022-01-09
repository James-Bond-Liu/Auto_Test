# -*- coding: utf-8 -*-
# @Time :2020/7/15 21:09
# @Author : liufei
# @File :do_logging.PY

import logging
from lemon_item.API2.common.get_path import *

class Dologging():
    def do_logging(self):
        logger = logging.getLogger('BIG_BANG')
        logger.setLevel('DEBUG')
        if not logger.handlers:
            ch = logging.StreamHandler()
            fh = logging.FileHandler(filename=test_log_path, encoding='utf-8',mode='a')
            formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(filename)s %(levelname)s %(message)s",
                                        datefmt="%Y-%m-%d %H:%M%S")
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)
            logger.addHandler(ch)
            logger.addHandler(fh)
        return logger


