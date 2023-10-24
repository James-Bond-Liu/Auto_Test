# -*- coding: utf-8 -*-
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import pymysql
from common.out_log import OutLog

logger = OutLog().out_log()


class DoMysql():
    """封装数据库的相关操作"""

    def __init__(self, db_info):  # db_info数据库的连接信息必须以字典形式传入
        self.link = pymysql.connect(**db_info)
        self.cursor = self.link.cursor()

    def select(self, sql):  # 查询操作
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            logger.error('数据库查询失败，报错{}'.format(e))
        finally:
            self.cursor.close()
            self.link.close()

    def insert(self, sql):  # 插入操作
        try:
            self.cursor.execute(sql)
            self.link.commit()
        except Exception as e:
            self.link.rollback()
            logger.error('数据库插入失败，报错{}'.format(e))
        finally:
            self.cursor.close()
            self.link.close()

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.link.commit()
        except Exception as e:
            self.link.rollback()
            logger.error('数据库更改失败，报错{}'.format(e))
        finally:
            self.cursor.close()
            self.link.close()

    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.link.commit()

        except Exception as e:
            self.link.rollback()
            logger.error('数据库删除失败，报错{}'.format(e))
        finally:
            self.cursor.close()
            self.link.close()

    # def do_db(self, sql, stat = 'all'):
    #     self.cursor.execute(sql)
    #     try:
    #         if stat == 'all':
    #             res = self.cursor.fetchall()  # 多条数据，列表嵌套元祖
    #         elif stat == 1:
    #             res = self.cursor.fetone()  # 一条数据，元祖
    #         else:
    #             logger.error('stat模式只能为1或者all')
    #         self.cursor.close()
    #         self.link.close()
    #         return res
    #     except Exception as e:
    #         logger.error(e)
    #         raise e
