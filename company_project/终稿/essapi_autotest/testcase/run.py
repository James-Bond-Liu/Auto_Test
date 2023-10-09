# -*- coding: utf-8 -*-

import shutil
import time
import pytest
from common.out_log import OutLog
import datetime
from conf.path import Path
import os


class Run():
    logger = OutLog().out_log()

    def clean_up(self):
        # 日志、测试报告等文件清理
        if os.path.exists(Path.log_path):
            with open(Path.log_path, 'w') as file1:
                file1.truncate(0)
        if os.path.exists(Path.html_report_path):
            with open(Path.html_report_path, 'wb') as file2:
                file2.truncate(0)
        if os.path.exists(Path.allure_report_path):
            shutil.rmtree(Path.allure_report_path)
        time.sleep(3)
        Run.logger.info('测试报告、测试日志等数据已清理完毕')

    def run(self):
        self.clean_up()
        # 执行测试用例
        start_time = datetime.datetime.now()
        Run.logger.info('开始执行接口测试，开始时间{}'.format(start_time))
        pytest.main(['--clean-alluredir', f'--html={Path.html_report_path}', f'--alluredir={Path.allure_report_path}'])
        end_time = datetime.datetime.now()
        time_consuming = ((end_time - start_time).seconds) / 60  # 共耗时
        Run.logger.info('完成接口测试，结束时间{}，共耗时{}s'.format(end_time, end_time - start_time))
        zip_path = os.path.split(Path().html_report_path)[0]
        if os.path.exists(zip_path):
            zip_name = shutil.make_archive(zip_path, "zip", zip_path)
            Run.logger.info(f'测试报告{zip_name}已打包完成')

if __name__ == '__main__':
    Run().run()
