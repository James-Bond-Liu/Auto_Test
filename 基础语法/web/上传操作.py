# -*- coding: utf-8 -*-
# @Time :2020/8/4 19:40
# @Author : liufei
# @File :上传操作.PY

''''
上传操作有两种情况：
1、如果是input可以直接输入路径的，那么直接调send_keys输入路径。（如果input标签是readonly属性，可以利用“日期输入框”的方法先改属性再传值）
2、非input标签的上传，则需要借助第三方工具（MAC/Linux--利用AutoIt,调用生成的au3或exe文件，python pywin32库，识别对话句柄，进行操作）
'''
'''
函数解析
win32gui.FindWindow(IpClassName, IpWindowName)
自顶层窗口开始寻找匹配条件的窗口，并返回这个窗口的句柄
IpClassName：类名
IpWindowName：窗口名（window caption）

win32gui.FindWindowEx(hwndParent=0,hwndChildAfter=0,IpszClass=None,IpsWindow=None)
搜索类名和窗体名匹配的窗体，并返回这个窗体的句柄。找不到就返回0
hwndParent：若不为0，则搜索句柄为hwndParent的窗体的子窗体
hwndChildAfter：若为0，从第一个子窗体开始搜索，若不为0，则从索引为hwndChildAfter开始向后搜索子窗体
IpszClass：字符型的窗体类名
IpsWindow：字符型的窗口名

win32gui.SendMessage(hWnd,Msg,wParam,IParam)
hWnd:整形，接收消息的窗体句柄
Msg：整形，要发送的消息，这些消息都是Windows预先定义好的
wParam：整形，消息的wParam参数
IParam：整形，消息的IParam参数
'''
import win32gui
import win32con

#Chrome浏览起的上传操作（不同浏览器，上传文件操作有细微的差别）
def upload_file(filepath):
    # 顶层窗口（一级窗口）
    dialog = win32gui.FindWindow('#32770', '打开')

    # 二级窗口
    comboxex32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)

    # 三级窗口
    combox = win32gui.FindWindowEx(comboxex32, 0, 'ComboBox', None)

    # 四级窗口-文本输入框
    edit = win32gui.FindWindowEx(combox, 0, 'Edit', None)

    # 二级窗口-打开按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&O)')

    # 输入文件地址
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, 0, filepath)  #在edit窗口上输入文件filepath

    # 点击打开按钮，提交文件
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  #在dialog窗口上点击button按钮
