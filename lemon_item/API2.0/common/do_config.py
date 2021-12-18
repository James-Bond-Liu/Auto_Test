# -*- coding: utf-8 -*-
# @Time :2020/7/15 21:49
# @Author : liufei
# @File :do_cofig.PY

import configparser

class DoConfig():
    def do_config(self, filename, section, option):
        cf = configparser.ConfigParser()
        cf.read(filename)
        res = cf.get(section, option)
        return res

if __name__ == '__main__':
    print(DOConfig().do_config(r'D:\Python_files\lemon_item\API\conf\case.config','MODE','mode'))

