# -*- coding: utf-8 -*-
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import configparser
from conf.path import Path


class ReadConfig():

    def readconfig(self, section, option):
        conf = configparser.ConfigParser()
        conf.read(filenames=Path.conf_path, encoding='utf-8')
        return conf.get(section=section, option=option)


if __name__ == '__main__':
    a = ReadConfig().readconfig('MODE', 'data_essApi')
    print(a)
    print(type(eval(a)))
