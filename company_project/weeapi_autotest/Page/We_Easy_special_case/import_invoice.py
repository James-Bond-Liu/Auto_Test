# !@coding  :utf-8 
# !@Time    :2021/2/2 22:53
# !@Author  :liulei
# !@coding  :utf-8
# !@Time    :2021/1/5 19:45
# !@Author  :liulei
from Page.BasePage import BasePage
from element.WeEasy import el_login
from data.config import business_data
from data.config import login_data
from element.WeEasy import el_business_manager, el_home_page
from element.WeEasy.el_account_set import process_income_invoice, account_home
import requests
import json
from selenium import webdriver

add_url = "https://www.mi-guo.com/company/customer/add?cjbz=1"


class Login(BasePage):
    """
    登录操作

    """
    enter_account = '//tbody[1]/tr[%s]/td[13]/a[5]'
    page_limit = ('xpath', '//*[@class="limit-select"]')
    jxfp1 = r'C:\Users\weeasy\Desktop\WEAutoTest\测试数据\自动化测试数据\发票查验，自动补全进项校验\FPMX_XX (1).xls'
    jxfp2 = r'C:\Users\weeasy\Desktop\WEAutoTest\测试数据\自动化测试数据\发票查验，自动补全进项校验\FPMX_XX (1).xls'
    fp_list = [jxfp1, jxfp2]
    check = ('xpath', '//*[@id="list"]/table/thead/tr/th[6]')

    def login(self):
        case_name = '客户登录'
        print(case_name, "|开始执行")
        try:
            self.load_url(login_data.login_url)
            self.click(*el_login.f_login_btn)
            self.sleep(2)
            self.send_keys(*el_login.email, login_data.username)
            self.send_keys(*el_login.password, login_data.password)
            self.click(*el_login.s_login_btn)
            self.sleep(5)
        except Exception as why:
            print('why', why)

    def add_costomer(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        sever = '40efc2a71e897652c8b32a2cce39d1a8|1612536859|1612536565'
        dzappck = 'e514d44e2e0f686eb105249066c186a0'
        JSESSIONID = '23399A48D04F7FA5AD0637FC5D7DA781'
        # print(dzappck)
        # print(JSESSIONID)
        a = list(range(53, 300))
        headers = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                   "cookie": "JSESSIONID=%s;dzappck=%s;SERVERID=%s" % (JSESSIONID, dzappck, sever),
                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
        response = ''
        for i in a:
            data = {"qymc": str(i), "province": "370000", "city": "370200", "county": "370201", "nsrzg": "201",
                    "kjzddm": "03", "qynf": "2021", "qyyf": "1", "gs_sbwz": "4", "gs_dlfs": "6", "gs_ca_u_pwd": "",
                    "gs_nsrsbh": "", "sd_gs_smdlzh": "", "gs_username": "", "gs_pwd": "", "gs_vpdn_username": "",
                    "gs_vpdn_pwd": "", "gs_klmm": "", "gs_szqmmm": "", "sd_gs_username": "", "sd_gs_pwd": "",
                    "gs_zjlx": "201", "gs_zjhm": str(i), "gs_yzlx": "1", "gs_sjhm": str(i), "gs_qd_pswd": "",
                    "gs_smdlzh": "", "gs_smdlmm": "", "gs_dlryxm": "", "gs_rydlmm": "", "bj_gs_smdlsf": "法定代表人",
                    "bj_gs_smdlzxm": "", "bj_gs_dlsfzh": "", "bj_gs_pwd": "", "gs_dlrzh": "", "gs_dlrmm": "",
                    "hb_gs_dlsf": "法定代表人", "dlrbz": "0", "hebei_gs_dlsf": "法定代表人", "usb_zdid_dlr": "",
                    "usb_dkh_dlr": "", "gs_ca_u_pwd_dlr": "", "ds_sbwz": "1", "ds_ca_u_pwd": "", "ds_username": "",
                    "ds_pwd": "", "gs_dlsf": "法人", "js_gs_dlry": "", "sjtj": "0", "ah_gs_dlryxm": "",
                    "ah_gs_rydlmm": "", "gx_gs_dlsf": "法定代表人", "gx_gs_pwd": "", "gx_dljg_sh": "", "gx_dljg_pwd": "",
                    "gx_dljg_ryxm": "", "ds_jsjdm": "", "grsds_dlfs": "2", "grsds_wtjm_pwd": str(i),
                    "zj_grsds_wlxtyhm": "", "grsds_smdlzh": "", "grsds_smdlmm": "", "ds_sjhsw": "", "ds_klmm": "",
                    "ds_bdsjh": "", "usb_zdid": "", "usb_dkh": "", "wlfpzh": "", "wlfpmm": "", "gd_wlfpzh": "",
                    "gd_wlfpmm": "", "gd_gs_dlsf": "法定代表人", "sbghjfdlzh": "", "sbghjfdlmm": ""}
            print(i)

            response = requests.post(add_url, headers=headers, data=data)
            print(response)
        return response

    def import_invoice(self):
        num = 0
        for i in range(55, 300):
            self.load_url(login_data.login_url)
            self.click(*el_home_page.customer_manager_page)
            self.select_value(*self.page_limit, value='500')
            self.sleep(1)
            self.click('xpath', self.enter_account % i)
            self.enter_page1()
            invoice_type = self.fp_list[num]
            num += 1
            if num == len(self.fp_list):
                num = 0
            self.import_flow(invoice_type, 1)

    def enter_page1(self):
        self.page_refresh()
        self.sleep(2)
        self.move(*account_home.ywcl)
        self.click(*process_income_invoice.jxfp)
        self.switch_to_frame(*process_income_invoice.change_iframe)

    def import_flow(self, invoice, choose=None):
        self.click(*process_income_invoice.ipt_jxfp)
        self.sleep(2)
        self.send_keys(*process_income_invoice.upload, invoice)
        self.sleep(2)
        self.click(*process_income_invoice.next_step)
        if choose:
            self.click(*process_income_invoice.operation_tips)
        else:
            self.click(*process_income_invoice.tips)
            self.click(*process_income_invoice.confirm)
        self.check_data(self.check, '销方名称')

    def add_flow(self, business):
        self.click(*el_business_manager.add_business)
        self.sleep(1)
        self.select_value(*el_business_manager.select_province, business_data.business_province)
        self.select_value(*el_business_manager.select_city, business_data.business_city)
        self.send_keys(*el_business_manager.ipt_business_name, business)
        self.send_keys(*el_business_manager.identity_num, business_data.business_num)
        self.send_keys(*el_business_manager.telephone_num, business_data.business_num)
        self.send_keys(*el_business_manager.gssb_pwd, business_data.business_num)
        self.click(*el_business_manager.save_btn)
