# -*- coding: utf-8 -*-

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
