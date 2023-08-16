# -*- coding: utf-8 -*-
from common.http_request import HttpRequest
from common.get_all_testdata import GetRequestData, UpdateData
import pytest
from conf.global_data import GlobalData
from common.out_log import OutLog
from common.do_mysql import DoMysql
from common.read_config import ReadConfig
import os
from common.do_regx import DoRegx

"""
此模块用于封装执行某个Excel文件下所有sheet表单的用例
将登录用例写在Excel文件中，先执行登录用例获取token
"""

logger = OutLog().out_log()
test_data = GetRequestData().get_request_data()


class TestApi():

    @pytest.mark.parametrize('item', test_data)
    def test_api(self, item):
        compare_result = None
        if item['sql_before'] != 'None':
            item['sql_before'] = DoRegx().do_regx(item['sql_before'])
            item['sql_before'] = eval(item['sql_before'])
            result1 = \
                DoMysql(eval(ReadConfig().readconfig('MYSQL_DB', item['sql_before'][0]))).select(item['sql_before'][2])[
                    0]
            setattr(GlobalData, item['sql_before'][1], result1)
            logger.debug(
                f'测试用例---{item["case_name"]}的GlobalData{item["sql_before"][1]}={getattr(GlobalData, item["sql_before"][1])}')
        if item['parameters'] != 'None':
            item['parameters'] = DoRegx().do_regx(item['parameters'])
            logger.debug(f'测试用例---{item["case_name"]}存在parameters')

        item['path_info'] = DoRegx().do_regx(item['path_info'])
        item['path_info'] = getattr(GlobalData, 'login_url') + item['path_info']

        headers = {'Content-Type': 'application/json', 'authorization': getattr(GlobalData, 'token')}
        cookies = getattr(GlobalData, 'cookies')
        logger.info('**********测试用例【{}】，开始请求接口**********'.format(item['case_name']))

        logger.debug(f"测试用例---{item['case_name']}的请求地址：{item['path_info']}")
        logger.debug(f'测试用例---{item["case_name"]}的请求参数：{item["parameters"]}')
        res = HttpRequest().http_request(item['path_info'], eval(item['parameters']), item['method'],
                                         headers=headers,
                                         cookies=cookies)
        logger.info('**********测试用例【{}】，接口请求完成**********'.format(item['case_name']))
        logger.debug(f"测试用例---{item['case_name']}的请求头：{res.request.headers}")

        if res.json().get('data'):
            if 'access_token' in res.json()['data']:
                token = 'Bearer ' + res.json()['data']['access_token']
                setattr(GlobalData, 'token', token)
                logger.debug('测试用例---{}响应报文返回token：{}'.format(item['case_name'], token))
            else:
                logger.debug('测试用例---{}响应报文没有返回token'.format(item['case_name']))
        else:
            logger.debug('测试用例---{}响应报文没有【data】字段'.format(item['case_name']))
        if res.cookies:
            setattr(GlobalData, 'cookies', res.cookies)
            logger.debug('测试用例---{}响应报文携带cookie：{}'.format(item['case_name'], res.cookies))
        else:
            logger.debug('测试用例---{}响应报文未携带cookie'.format(item['case_name']))
        try:
            assert res.status_code == item['expect_status_code']
            logger.info('测试用例---{}status_code为{}校验通过'.format(item['case_name'], res.status_code))
            logger.info(f"测试用例---{item['case_name']}的响应报文为{res.json()}")
            if res.status_code == 400:
                assert res.json()['error'] == item['request_expect_result']
                logger.info('测试用例---{}is bad request'.format(item['case_name'], res.json()['error']))
            elif res.status_code == 500:
                assert res.json()['error'] == item['request_expect_result']
                logger.info('测试用例---{}Internal Server Error'.format(item['case_name'], res.json()['error']))
            elif res.status_code == 200:
                assert res.json()['msg_code'] == item['request_expect_result']
                logger.info('测试用例---{}msg_code为{}'.format(item['case_name'], res.json()['msg_code']))

            if item['sql_after'] != 'None':
                item['sql_after'] = DoRegx().do_regx(item['sql_after'])
                item['sql_after'] = eval(item['sql_after'])
                result2 = \
                    DoMysql(eval(ReadConfig().readconfig('MYSQL_DB', item['sql_after'][0]))).select(
                        item['sql_after'][2])[0]
                setattr(GlobalData, item['sql_after'][1], result2)
                logger.debug(
                    f'测试用例---{item["case_name"]}的GlobalData{item["sql_after"][1]}={getattr(GlobalData, item["sql_after"][1])}')

            if item['database_compare_sql'] != 'None':
                item['database_compare_sql'] = DoRegx().do_regx(item['database_compare_sql'])
                logger.debug(f'测试用例---{item["case_name"]}需要进行数据库校验，校验sql为{item["database_compare_sql"]}')
                item['database_compare_sql'] = eval(item['database_compare_sql'])
                con = ReadConfig().readconfig('MYSQL_DB', item['database_compare_sql'][0])
                database_actual_result = DoMysql(eval(con)).select(item['database_compare_sql'][1])[0]
                logger.debug('测试用例---{}查询数据库结果为{}，期望结果为{}'.format(item['case_name'], database_actual_result,
                                                                  item['database_expect_result']))
                if database_actual_result == item['database_expect_result']:
                    compare_result = 'Pass'
                    logger.info(
                        f'{item["file_name"]}--{item["sheet_name"]}---测试用例---{item["case_name"]}测试结果为{compare_result}')
                else:
                    compare_result = 'Failed'
                    logger.error(
                        f'{item["file_name"]}--{item["sheet_name"]}---测试用例---{item["case_name"]}测试结果为{compare_result}')
            else:
                compare_result = 'Pass'
                logger.info(
                    f'{item["file_name"]}--{item["sheet_name"]}---测试用例---{item["case_name"]}测试结果为{compare_result}')

        except Exception as e:
            compare_result = 'Failed'
            logger.error(
                '{}---{}---测试用例---{}断言过程报错{}'.format(item['file_name'], item['sheet_name'], item['case_name'], e))
            raise e

        finally:
            try:
                file_name = os.path.join(os.path.split((os.path.split(os.path.realpath(__file__)))[0])[0], 'data',
                                         item['file_name'])  # 将item['file_name]拼接成一个绝对路径

                UpdateData().update(file_name, item['sheet_name'], item['case_id'] - 1, 'request_actual_result',
                                    str(res.json()))
                logger.debug(f'{item["case_name"]}响应报文{res.json()}已存档')

                UpdateData().update(file_name, item['sheet_name'], item['case_id'] - 1, 'test_result', compare_result)
                logger.debug(f'{item["case_name"]}的测试结果{compare_result}已存档')
            except Exception as e:
                logger.error('在Excel中写入数据失败，产生错误{}'.format(e))
                raise e
