# -*- coding: utf-8 -*-
# @Time :2020/7/13 19:45
# @Author : liufei
# @File :test_http_request.PY

import unittest
from lemon_item.API2.common.http_request import HttpRequest
from lemon_item.API2.common.do_excel import DoExcel
from ddt import ddt, data
from lemon_item.API2.common.get_variable import GetVariable
from lemon_item.API2.common.do_mysql import DoMysql
from lemon_item.API2.common.do_logging import Dologging

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    test_data = DoExcel().do_excel(r'D:\Python_files\lemon_item\API\test_data\test_data.xlsx', 'login')
    @data(*test_data)
    def test_api(self, item):
        logger = Dologging().do_logging()
        global test_result
        if item['data'].find('${loanId}') != -1:
            if getattr(GetVariable,'loanId') == None:
                query_sql = 'select max(Id) from loan where MemberID={0}'.format(getattr(GetVariable, 'loan_member_id'))
                loanId = DoMysql().do_mysql(query_sql,1)[0]
                item['data'] = item['data'].replace('${loanId}', str(loanId))
                setattr(GetVariable,'loanId',str(loanId))
            else:
                item['data'] = item['data'].replace('${loan_id}', getattr(GetVariable,'loanId'))

        logger.info('获取到的请求数据是{0}'.format(item[data]))
        if item['check_sql'] != None:
            logger.info('此条用例数据需要做数据库校验：{0}'.format(item['title']))
            query_sql = eval(item['check_sql'])['sql']
            Before_Amount = DoMysql().do_mysql(query_sql, 1)[0]
            logger.info('用例:{0}请求之前的余额是{1}'.format(item['title'], Before_Amount))
            logger.info('---------------开始HTTP接口请求-------------------')
            res = HttpRequest.http_request(item['url'],eval(item['data']),item['http_method'],getattr(GetVariable,'cookie'))
            logger.info('---------------完成HTTP接口请求-------------------')
            After_Amount = DoMysql().do_mysql(query_sql, 1)[0]
            logger.info('用例:{0}请求之后的余额是{1}'.format(item['title'], After_Amount))
            if eval(item['data'])['amount'] == abs(Before_Amount - After_Amount):
                logger.info('数据库余额正确')
                check_sql_result = '数据库检查通过'
            else:
                logger.error('数据库余额不正确')
                check_sql_result = '数据库检查通过'
        else:
            logger.info('此条用例数据不需要做数据库校验：{0}'.format(item['title']))
            logger.info('---------------开始HTTP接口请求-------------------')
            res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'],
                                           getattr(GetVariable, 'cookie'))
            logger.info('---------------完成HTTP接口请求-------------------')
        if res.cookies:
            setattr(GetVariable,'cookie',res.cookies)
        try:
            self.assertEqual(str(item['expected']) , res.json()['code'])
            logger.info('断言通过')
            test_result='PASS'
        except Exception as e:
            logger.error('断言失败{}'.format(e))
            test_result='Filed'
            raise e
        finally:
            logger.info('用力的执行结果为{0}'.format(res.json()))
            DoExcel().write_back(r'/API2\test_data\test_data.xlsx', 'login',
                                 item['case_id'] + 1, 8, res.json())
            DoExcel().write_back(r'/API2\test_data\test_data.xlsx', 'login',
                                 item['case_id'] + 1, 9, test_result)
    def tearDown(self):
        pass
