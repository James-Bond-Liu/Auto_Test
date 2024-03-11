# -*- coding: utf-8 -*-
# @Time :2020/6/26 2:56
# @Author : liufei
# @File :test_http_request.PY

import unittest
from framework.api.tools.http_request import HttpRequest
from framework.api.tools.get_data import GetData
from ddt import ddt,data
from framework.api.tools.do_excel import DoExcel
from framework.api.tools.output_log import OutPutLog
from framework.api.tools.do_mysql import DoMysql

test_data=DoExcel.get_data(test_data_path)
logger=OutPutLog.out_log()
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self,item):
        if item['data'].find('${loan_id}')==-1:
            if getattr(GetData,'loanId')==None:
                query_sql='select max(Id) from loan where MemberID={0}'.format(getattr(GetData,'loan_member_id'))
                loan_id=DoMysql().do_mysql(query_sql)[0][0]
                item['data']=item['data'].replace('${loan_id}',str(loan_id))
                setattr(GetData,'loanId',loan_id)
            else:
                item['data'] = item['data'].replace('${loan_id}', str(getattr(GetData,'loanId')))
        logger.info('获取到的请求数据是：{0}'.format(item['data']))
        if item['check_sql'] != None:
            logger.info('此条用例数据需要做数据库校验：{0}'.format(item['title']))
            query_sql=eval(item['check_sql'])['sql']
            Before_Amount = DoMysql().do_mysql(query_sql, 1)[0]
            logger.info('用例:{0}请求之前的余额是{1}'.format(item['title'],Before_Amount))
            logger.info('---------------开始HTTP接口请求-------------------')
            res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'],getattr(GetData, 'Cookie'))
            logger.info('---------------完成HTTP接口请求-------------------')
            After_Amount = DoMysql().do_mysql(query_sql, 1)[0]
            logger.info('用例:{0}请求之后的余额是{1}'.format(item['title'], After_Amount))
            if eval(item['data'])['amount']==abs(Before_Amount-After_Amount):
                logger.info('数据库余额正确')
                check_sql_result='数据库检查通过'
            else:
                logger.error('数据库余额不正确')
                check_sql_result = '数据库检查不通过'
            DoExcel.write_back(test_data_path,item['sheet_name'],item['case_id']+1,10,check_sql_result)
        else:
            logger.info('此条用例数据不需要做数据库校验：{0}'.format(item['title']))
            logger.info('---------------开始HTTP接口请求-------------------')
            res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'],
                                           getattr(GetData, 'Cookie'))
            logger.info('---------------完成HTTP接口请求-------------------')
        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)
        try:
            self.assertEqual(str(item['expected']),res.json()['code'])
            test_result='PASS'
        except AssertionError as e:
            test_result='Fail'
            logger.error('执行用例出错{}'.format(e))
            raise e
        finally:#不管try,expect的执行情况如何，finally里的肯定执行
            logger.info("获取的结果{}".format(res.json()))
            DoExcel.write_back(test_data_path, item['sheet_name'], item['case_id']+1, 8, str(res.json()))
            DoExcel.write_back(test_data_path, item['sheet_name'], item['case_id'] + 1, 9, test_result)
    def tearDown(self):
        pass
