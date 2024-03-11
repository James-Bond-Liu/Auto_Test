# -*- coding: utf-8 -*-
# @Time :2020/6/26 19:20
# @Author : liufei
# @File :read_config.PY

import configparser

class ReadConfig():
    @staticmethod
    def get_config(filepath,section,option):
        cf=configparser.ConfigParser()
        cf.read(filepath)
        return cf.get(section,option)

if __name__ == '__main__':
    from API_item.tools.project_path import *
    print(ReadConfig.get_config(test_config_path,'MODE','mode'))