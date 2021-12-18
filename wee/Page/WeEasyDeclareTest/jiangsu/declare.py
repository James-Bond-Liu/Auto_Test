# !@coding  :utf-8 
# !@Time    :2021/2/22 11:31
# !@Author  :LiuLei

from Page.BasePage import BasePage
from element.WeEasy import el_home_page as home
from element.WeEasy import el_declare_page as element
from data.declare_config import declare_config
from element.WeEasy_manager import el_login
import requests
import openpyxl
import datetime


class RoutineCheckDeclare(BasePage):
    """
    例行申报报表检测
    
    """
    total_info = None
    status = []  # 查每个报表的qynbm,dzbdbm,status {qynbm:{dzbdbm:status}}
    declare_status = []  # 查同一个dzbdbm的列表 {dzbdbm:[status1,status2],row:[1,2]}}
    check_info = None
    '''
    传入主表附表对应关系
    '''
    form_xlsx = openpyxl.load_workbook(declare_config.data_path)
    form_ws = form_xlsx['Sheet1']
    max_row = form_ws.max_row
    max_row += 1
    
    zb_list = []
    fb_list = []
    for i in range(2, max_row):
        zb = form_ws['A%s' % i].value
        fb = form_ws['B%s' % i].value
        zb_list.append(zb)
        fb_list.append(fb)
    print('表单对应关系创建成功')
    
    def declare_status_check(self):
        case_name = "申报表例行测试"
        print(case_name, "|开始执行")
        
        self.login(username=declare_config.declare_username, password=declare_config.declare_password)
        self.page_refresh()
        cookie = self.get_url_cookie()  # 获取测试后台的cookie
        self.enter_page_too(home.declare, element.statement_list_btn)  # 进入报表列表界面
        self.select_value(*element.page_limt, value='500')  # 设置界面显示500条
        self.sleep(1)
        self.click(*element.show_error)  # 显示异常原因
        self.sleep(1)
        self.total_info = self.total(element.total)  # 获取报表总数
        self.sleep(1)
        self.check_declare_status(cookie)  # 开始申报流程
        
        result_status = self.check_info
        assert result_status, case_name + '失败'
    
    def check_declare_status(self, cookie):
        declare_success_item = []
        declare_chaobao_item = []
        declare_fail_item = []
        invalid_success_item = []
        invalid_fail_item = []
        
        print('开始检查报表状态')

        while True:
            
            info = False
            mark = False
            start_time = datetime.datetime.now()
            print('开始时间：%s' % start_time)
            for i in range(1, self.total_info):
                
                try:
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    self.switch_to_window(0)
                    self.page_refresh()
                    
                    declare_name, fetch, tax_pay, dzbdbm, qynbm, main_form, declare_status, invalid, name, error = self.collect_data(
                        i)  # 采集每条报表的数据

                    if declare_status != '未申报' and dzbdbm:
                        self.update_status_form(dzbdbm, i, declare_status, mark)
                    elif declare_status == '未申报' and '撤销' in invalid:
                        self.update_status_form(dzbdbm, i, declare_status, mark)
                        
                    if not dzbdbm:
                        print('第%s条无dzbdbm' % i)
                    # 当报表的状态处于申报失败、撤销成功、撤销失败时，该条不检查
                    if {name: dzbdbm} in invalid_success_item or {name: dzbdbm} in invalid_fail_item or {
                        name: [dzbdbm, error]} in declare_fail_item:
                        print({name: dzbdbm})
                        print('当前报表已检查完毕')
                        continue
                    
                    else:
                        # 申报流程
                        self.auto_declare(main_form, qynbm, dzbdbm, fetch, declare_status, tax_pay, i, name, invalid)
                        print('申报状态', declare_status)
                        if '申报中' in declare_status:
                            print('申报中,跳过')
                            info = False
                            continue
                        elif '未申报' in declare_status:
                            if '撤销' in invalid:
                                print('该条申报完毕，进入撤销阶段')
                                info = True
                            else:
                                print('该条未申报，跳过')
                                info = False
                                
                                continue
                        elif '已申报' in declare_status:
                            print('已申报,发送状态检查')
                            self.click('xpath', element.view % i)
                            self.sleep(1)
                            self.click(*element.check_status)
                            info = False
                            continue
                        elif '申报成功' in declare_status:
                            print('申报成功')
                            declare_status = '申报成功'
                            if {name: dzbdbm} not in declare_success_item:
                                declare_success_item.append({name: dzbdbm})
                            
                            for j in self.declare_status:  # 遍历所有状态字典
                                key_list = list(j.keys())  # 获得状态字典的key
                                key = str(key_list[0])
                                if key == dzbdbm:  # 如果状态字典中已经有dzbdbm
                                    print('所有状态 key:', key, ';dzbdbm:', dzbdbm)
                                    for m in j['row']:  # 当该条电子表单申报成功时，检查其他同类型的电子表单是否成功
                                        d_status = self.get_element_text('xpath', element.declare_status % m, open=False)
                                        if '申报成功' in d_status:
                                            d_status = '申报成功'
                                        index = j['row'].index(m)
                                        j[key][index] = d_status
                                        print('状态：', j)
                                    for n in j[key]:
                                        if '申报成功' in n:
                                            info = True
                                            print(info)
                                        else:
                                            info = False
                                            print(info)
                                            break
                                    if info:
                                        self.open_declare_task(dzbdbm, cookie)
                                    print('该条申报成功')
                        elif '申报异常' in declare_status and '未抄' in error or '抄报' in error or '汇总报送' in error:
                            print('申报异常，但异常原因是没有抄报')
                            if {name: dzbdbm} not in declare_chaobao_item:
                                declare_chaobao_item.append({name: dzbdbm})
                            info = False
                        elif '申报异常' in declare_status and '未抄' not in error and '抄报' not in error and '汇总报送' not in error:
                            print('申报异常')
                            if '您的增值税或者消费税还未申报' in error or '主税（增值税）未申报' in error:
                                info = False
                                pass
                            else:
                                if {name: [dzbdbm, error]} not in declare_fail_item:
                                    declare_fail_item.append({name: [dzbdbm, error]})
                                info = False
                        stat = False
                        if info:
                            for j in self.declare_status:
                                key_list = list(j.keys())  # 获得状态字典的key
                                key = str(key_list[0])
                                if key == dzbdbm:  # 如果状态字典中已经有dzbdbm
                                    for l in j['row']:
                                        print(j['row'])
                                        invalid = self.get_element_text('xpath', element.invalid_status % l, open=False)
                                        if '撤销成功' in invalid:
                                            print('撤销成功')
                                            stat = True
                                            pass
                                        elif '撤销中' in invalid:
                                            print('撤销任务执行中，检查下一个')
                                            stat = False
                                            pass
                                        elif '———' in invalid:
                                            stat = False
                                            print('----')
                                            if dzbdbm in self.zb_list:
                                                fbdygx = []  # 当前qynbm中所有表
                                                for o in range(len(self.zb_list)):
                                                    try:  # 找到所有主表关联的附表
                                                        if self.zb_list[o] == dzbdbm:
                                                            (fbdygx.append(self.fb_list[o + 1]) if self.zb_list[o] ==
                                                                                                   self.zb_list[
                                                                                                       o - 1] else fbdygx.append(
                                                                self.fb_list[o]))
                                                    except IndexError:  # 第一轮i-1会出现错误
                                                        print('第一轮')
                                                print(fbdygx)
                                                for p in self.status:  # 找到当前企业内部吗中所有的表单信息
                                                    try:
                                                        fbdm = list(p[qynbm].keys())[0]
                                                        print('附表代码', fbdm)
                                                        fb_status = []
                                                        declare_mark = ''
                                                        for n in fbdygx:
                                                            print(n, fbdm)
                                                            if n == fbdm:
                                                                print(p[qynbm][n])
                                                                fb_status.append(p[qynbm][n])
                                                        for q in fb_status:
                                                            
                                                            print(q, fb_status)
                                                            if '未申报' in q or '申报中' in q:
                                                                print('存在未申报或申报中的附表，暂不撤销%s' % dzbdbm)
                                                                declare_mark = False
                                                                break
                                                            else:
                                                                print(q)
                                                                declare_mark = True
                                                        if declare_mark:
                                                            print('%s的所有附表均已申报完毕' % dzbdbm)
                                                            self.declare_invalid(l)
                                                        elif declare_mark:
                                                            print('%s仍有附表没有检查完毕' % dzbdbm)
                                                    except KeyError:
                                                        print('继续查找%s' % qynbm)
                                            else:
                                                print('%s没有附表' % dzbdbm)
                                                self.declare_invalid(l)
                                        
                                        elif '撤销异常' in invalid:
                                            stat = False
                                            print('撤销失败')
                                            invalid_fail_item.append({name: dzbdbm})
                                        elif '已撤销' in invalid:
                                            print('已撤销')
                                            stat = False
                                            self.click(*element.check_status)
                                    if stat:
                                        
                                        if {name: dzbdbm} not in invalid_success_item:
                                            print(dzbdbm, '撤销成功')
                                            invalid_success_item.append({name: dzbdbm})
                                    else:
                                        pass
                
                except Exception as why:
                    print(why)
                    print('当前条目失败，检查下一条')
            end_time = datetime.datetime.now()
            total_time = end_time - start_time
            
            print('结束时间：%s' % end_time)
            print('一轮共计用时：%s' % total_time)
            print('===================================申报成功=======================================')
            print('declare_success_item', declare_success_item)
            print('===================================申报失败=======================================')
            print('declare_fail_item', declare_fail_item)
            print('declare_chaobao_item', declare_chaobao_item)
            print('===================================撤销成功=======================================')
            print('invalid_success_item', invalid_success_item)
            print('===================================撤销失败=======================================')
            print('invalid_fail_item', invalid_fail_item)
            print('=================================================================================')
            print('已处理表单总数：', len(declare_fail_item) + len(invalid_success_item) + len(invalid_fail_item) + len(
                declare_chaobao_item))
            print('申报状态总数：', len(self.declare_status))
            print('=================================================================================')
            
            # if len(invalid_success_item) + len(declare_chaobao_item) and len(self.declare_status) != 0:
            #     self.check_info = True
            #     break
            # elif len(declare_fail_item) + len(invalid_success_item) + len(invalid_fail_item) == len(
            #         self.declare_status) + len(declare_chaobao_item) and len(self.declare_status) != 0:
            #     break
            self.sleep(60)
            
    def auto_declare(self, main_form, qynbm, dzbdbm, fetch, declare_status, tax_pay, num, name, invalid):
        print('自动申报测试开始')
        mark = False
        # try:
        
        if main_form is not None:  # 说明该条电子表单是有主表的,这个if进来的一定是附表
            for j in self.status:
                try:
                    print('查看申报状态', j)
                    if '申报成功' in j[qynbm][main_form] or '发现已完成申报' in j[qynbm][main_form]:  # 判断主表是否申报成功
                        print('%s的主表已经申报完毕' % name, dzbdbm)
                        mark = True  # 主表申报成功标志，成功了附表才进行申报
                        break
                    else:
                        print('主表未申报成功')
                        mark = False
                        break
                except KeyError:
                    pass
            if '未取数' not in fetch and '未申报' in declare_status and tax_pay == '0' and mark and '撤销' not in invalid:
                print('附表开始申报')
                self.declare_flow(num, declare_status, dzbdbm)  # 当符合条件时进行申报
        elif main_form is None:  # 当电子表单没有主表的时候直接申报
            print('%s无主表' % dzbdbm)
            if '未取数' not in fetch and '未申报' in declare_status and tax_pay == '0' and '撤销' not in invalid:
                self.declare_flow(num, declare_status,
                                  dzbdbm)  # 当符合条件时进行申报  #  # except Exception as why:  #     print('该条申报操作失败')
    
    def get_dzbdbm_qynbm(self, num):
        print('获取电子表单编码,企业内部码')
        self.click('xpath', element.select_box % num)
        self.sleep(1)
        dzbdbm = ''
        qynbm = ''
        try:
            self.click('xpath', element.view % num)
            self.switch_to_window(-1)
            url = self.get_page_url()
            self.sleep(0.5)
            self.close_page()
            self.switch_to_window(0)
            dzbdbm = url.split('dzbdbm=')[1].replace('&sjsy', '')
            qynbm = url.split('qynbm=')[1].split('&')[0]
        except Exception as why:
            print('没有可以获取的url')
        print('获取到的电子表单编码', dzbdbm)
        print('获取到的企业内部码', qynbm)
        if dzbdbm == '':
            pass
        else:
            return dzbdbm, qynbm
    
    def declare_invalid(self, num):
        print('申报作废开始')
        
        self.sleep(1)
        self.click('xpath', element.select_box % num, open=1)
        self.sleep(1)
        self.click(*element.revocation_btn, open=1)
        self.sleep(1)
        self.click(*element.revocation_confirm, open=1)
        self.sleep(1)
        self.click(*element.declare_er, open=1)
    
    def total(self, page_total):
        total = int(self.get_element_text(*page_total, open=False).replace('共[', '').replace(']条', ''))
        print('报表总数为：', total)
        if total == 0:
            self.page_refresh()
            self.sleep(5)
            total = int(self.get_element_text(*page_total, open=False).replace('共[', '').replace(']条', ''))
            print('报表总数为：', total)
        return total + 1
    
    def get_url_cookie(self):
        # 获取后台管理的cookies
        new_url = 'window.open("{}");'.format(declare_config.manager_url)
        self.js_script(new_url)
        self.switch_to_window(-1)
        self.sleep(1)
        self.send_keys(*el_login.ipt_username, declare_config.manager_user)
        self.send_keys(*el_login.ipt_password, declare_config.manager_pwd)
        self.click(*el_login.login_btn)
        self.sleep(3)
        self.switch_to_frame(*el_login.iframe)
        info = self.get_element_text(*el_login.login_info, open=False)
        get_cookie = self.driver.get_cookies()
        print(get_cookie)
        cookie = get_cookie[0]['name'] + '=' + get_cookie[0]['value']
        self.close_page()
        self.switch_to_window(0)
        print(cookie)
        
        return cookie
    
    def open_declare_task(self, dzbdbm, cookie):  # 使用接口放开已经申报成功的报表
        print('放开', dzbdbm)
        url = declare_config.open_declare_url + '?DZBDBM=' + dzbdbm + '&RWZXBZ=0'
        header = {'Content-Type': 'application/json;charset=UTF-8', 'Accept': '*/*', 'cookie': cookie}
        response = requests.get(url, headers=header)
        print(response.text)

        task_status = ''
        try:
            task_status = eval(response.text)['succ']
            if task_status == 'true':
                print(dzbdbm, ':', task_status)
                print(dzbdbm, '放开成功')
            else:
                print(dzbdbm, ':', task_status)
        except:
            print('%s申报任务放开接口返回数据错误' % dzbdbm)
        return task_status
    
    def form_relation(self, dzbdbm, qynbm):  # 查找电子表单对应的主表
        print('开始进行对应关系查找')
        zb_list = []
        sbzt = ''
        n = 0
        exist = False
        for key, value in zip(self.zb_list, self.fb_list):
            
            if dzbdbm == value:  # 如果电子表单编码在对应关系的附表中
                print(dzbdbm, value)
                print(self.zb_list[self.fb_list.index(value)], '找到其对应关系')
                zb_list.append(key)  # 保存当前循环的电子表单编码的主表
                exist = True
        if exist:  # 如果当前电子表单有主表
            for j in self.status:
                print(j)
                try:
                    sbzt = list(j[qynbm].keys())[0]  # 找到当前企业内部吗的电子表单的增值税主表
                    print('报表名称：', sbzt)
                except Exception as why:
                    print('当前企业内部码不存在')
                    continue
                if 'YBNSR' in sbzt or 'XGMNSR' in sbzt:  # 满足条件的必定是增值税
                    print(sbzt)
                    print('查看所有对应的主表')
                    print(zb_list)
                    for k in zb_list:
                        if sbzt == k:  # 如果当前循环的增值税=对应关系中的主表，返回当前循环的增值税，为了判断一般纳税人还是小规模纳税人
                            print(sbzt)
                            return sbzt
                else:
                    print('当前报表的主表是', sbzt)
                    return sbzt
        else:
            print('未找到%s的对应主表' % dzbdbm)
    
    def collect_data(self, num):
        declare_name = self.get_element_text('xpath', element.declare_name % num, open=False)  # 申报表名称
        fetch = self.get_element_text('xpath', element.fetch_status % num, open=False)  # 取数状态
        declare_status = self.get_element_text('xpath', element.declare_status % num, open=False)  # 申报状态
        invalid = self.get_element_text('xpath', element.invalid_status % num, open=False)  # 撤销状态
        name = self.get_element_text('xpath', element.name % num, open=False)  # 公司名称
        error = self.get_element_text('xpath', element.error % num, open=False)  # 异常信息
        
        try:
            tax_pay = \
                self.get_element_text('xpath', element.pay_tax % num, open=False).splitlines(keepends=False)[-1].split(
                    ':')[1]
            print(tax_pay)  # 税额
        except IndexError:
            tax_pay = self.get_element_text('xpath', element.pay_tax % num, open=False)
        if tax_pay == '0.00' or tax_pay == '————':
            tax_pay = '0'
        
        dzbdbm, qynbm = self.get_dzbdbm_qynbm(num)
        main_form = None
        business_declare_dict = {}
        
        if dzbdbm != '' and '撤销成功' not in invalid and len(self.status) != self.total_info - 1:
            print('开始获取对应关系')
            main_form = self.form_relation(dzbdbm, qynbm)  # 要么是none 要么是主表
            business_declare_dict = {qynbm: {dzbdbm: declare_status}}
            self.status.append(business_declare_dict)
        elif len(self.status) == self.total_info - 1 and dzbdbm != '':
            print('开始更新申报状态')
            main_form = self.form_relation(dzbdbm, qynbm)  # 要么是none 要么是主表
            for i in range(len(self.status)):
                if list(self.status[i].keys())[0] == qynbm:
                    if list(self.status[i][qynbm].keys())[0] == dzbdbm:
                        self.status[i][qynbm][dzbdbm] = declare_status
        
        print('-------------------------------------展示获取到的数据------------------------------------')
        print('电子表单编码', dzbdbm)
        print('--------------------------------------------------------------------------------------')
        print('企业内部码', qynbm)
        print('--------------------------------------------------------------------------------------')
        print('第%s条' % num, ';取数状态', fetch, ';申报状态', declare_status, ';税款', tax_pay)
        print('--------------------------------------------------------------------------------------')
        print('公司名称', name, '申报表名称：', declare_name, '撤销状态:', invalid, '异常信息：', error)
        print('--------------------------------------------------------------------------------------')
        print('main_form', main_form)
        print('--------------------------------------------------------------------------------------')
        print('企业各表单申报状态', business_declare_dict)
        print('--------------------------------------------------------------------------------------')
        print('查看所有的报表对应状态', self.status)
        print('--------------------------------------------------------------------------------------')
        print('报表类型及行数：', self.declare_status)
        print('--------------------------------------------------------------------------------------')
        return declare_name, fetch, tax_pay, dzbdbm, qynbm, main_form, declare_status, invalid, name, error
    
    def declare_flow(self, num, status, dzbdbm):
        
        mark = False
        print('第%s条可以申报' % num)
        self.click('xpath', element.select_box % num, open=1)
        self.sleep(1)
        self.click(*element.declare_btn, open=1)
        self.sleep(1)
        self.click(*element.declare_confirm, open=1)
        self.sleep(1)
        self.click(*element.declare_er, open=1)
        self.sleep(1)
        
        print(dzbdbm)
        if not dzbdbm:
            print('该条无dzbdbm')
            return
        if len(self.declare_status) == 0:
            print('状态表为空')
            check_dict = {dzbdbm: [status], 'row': [num]}  # 状态检测字典
            self.declare_status.append(check_dict)
            print(self.declare_status)
        else:
            self.update_status_form(dzbdbm, num, status, mark)
    
    def update_status_form(self, dzbdbm, num, declare_status, mark):
        print('更新已存在的报表')
        for k in self.declare_status:
            key_list = list(k.keys())  # 获得状态字典的key
            key = str(key_list[0])
            try:
                if key == dzbdbm:
                    if num not in k['row']:
                        k['row'].append(num)
                        k[key].append(declare_status)
                    elif num in k['row']:
                        print(k[key][k['row'].index(num)])
                        k[key][k['row'].index(num)] = declare_status
                    mark = True
                    break
                elif key != dzbdbm:
                    mark = False
            except IndexError as why:
                print('更新状态时超出索引')
        if not mark:
            check_dict = {dzbdbm: [declare_status], 'row': [num]}
            self.declare_status.append(check_dict)
