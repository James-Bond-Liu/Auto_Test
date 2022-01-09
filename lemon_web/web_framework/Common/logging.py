# -*- coding: utf-8 -*-
# @Time :2020/7/15 21:09
# @Author : liufei
# @File :do_logging.PY

import logging
from lemon_web.web_framework.Common import dir_config

class Logging():

    def do_logging(self):
        logger = logging.getLogger('BIG_BANG')
        logger.setLevel('DEBUG')
        if not logger.handlers:
            ch = logging.StreamHandler()
            fh = logging.FileHandler(filename=dir_config.log_dir, encoding='utf-8',mode='a')
            formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(filename)s %(levelname)s %(message)s",
                                        datefmt="%Y-%m-%d %H:%M%S")
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)
            logger.addHandler(ch)
            logger.addHandler(fh)
        return logger


