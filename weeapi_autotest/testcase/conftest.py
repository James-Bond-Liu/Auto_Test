# coding: utf-8

import os
import sys

import pytest
from selenium import webdriver


sys.path.append(os.getcwd())
chrome_driver = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r'\driver\chromedriver89.exe'


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'οnclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot():
    '''截图保存为base64'''
    return driver.get_screenshot_as_base64()


@pytest.fixture(scope='session', autouse=True)
def init_weeasy_programs():
    print('init driver')
    global driver
    option = webdriver.ChromeOptions()
    prefs = {"": ""}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    option.add_experimental_option("prefs", prefs)     # 关闭密码弹窗

    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])     # 防止打印一些无用的日志

    driver = webdriver.Chrome(executable_path=chrome_driver, options=option)

    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {"source": 'var copy = function() {var options, name, src, copy, copyIsArray,'
                                      ' clone,target = arguments[ 0 ] || {},i = 1,length = arguments.length,'
                                      'deep = false;if ( typeof target === "boolean" ) {deep = target;'
                                      ' target = arguments[ i ] || {};i++;}if ( typeof target !== "object"'
                                      ' && !isFunction( target ) ) {target = {};}if ( i === length )'
                                      ' {target = this;i--;}for ( ; i < length; i++ )'
                                      ' {if ( ( options = arguments[ i ] ) != null ) {for ( name in options ) {copy = options[ name ];'
                                      'if ( name === "__proto__" || target === copy ) {continue;}'
                                      'if ( deep && copy && ( jQuery.isPlainObject( copy ) ||( copyIsArray = Array.isArray( copy ) ) ) )'
                                      ' {src = target[ name ];if ( copyIsArray && !Array.isArray( src ) ) {clone = [];}'
                                      ' else if ( !copyIsArray && !jQuery.isPlainObject( src ) ) {clone = {};} else {clone = src;}'
                                      'copyIsArray = false;target[ name ] = jQuery.extend( deep, clone, copy );} '
                                      'else if ( copy !== undefined ) {target[ name ] = copy;}}}}return target;};'
                                      'var a = copy({},navigator);delete navigator;delete a.webdriver;window.navigator = a;'})
    driver.maximize_window()
    yield driver

    print('case执行结束')

    driver.delete_all_cookies()
    driver.close()
