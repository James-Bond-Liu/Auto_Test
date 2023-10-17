import os
class Path():
    project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
    data_essApi = os.path.join(project_path, 'data_essApi')
    data_thirdApi = os.path.join(project_path, 'data_thirdApi')
    log_path = os.path.join(project_path, 'log', 'running_log.txt')
    txt_report_path = os.path.join(project_path, 'report', 'test_report.txt')
    conf_path = os.path.join(project_path, 'conf', 'conf.ini')
    report_essApi_html=os.path.join(project_path, 'report', 'report_essApi', 'html_report', 'test_report.html')
    report_essApi_allure = os.path.join(project_path, 'report', 'report_essApi', 'allure_report', 'test_report')
    report_thirdApi_html = os.path.join(project_path, 'report', 'report_thirdApi', 'html_report', 'test_report.html')
    report_thirdApi_allure = os.path.join(project_path, 'report', 'report_thirdApi', 'allure_report', 'test_report')

if __name__ == '__main__':
    print(Path().data_thirdApi)









