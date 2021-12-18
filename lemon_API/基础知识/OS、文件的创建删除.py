# -*- coding: utf-8 -*-
# @Time :2020/6/5 15:03
# @Author : liufei
# @File :class_0603.PY

import os
os.mkdir("python2") #在当前文件所在目录创建目录（文件夹）

os.mkdir(r"python2/code") #跨级创建目录，必须保证上一级目录必须存在

os.makedirs("python3/jkds") #批量创建目录，创建递归目录

os.rmdir("python2/code") #删除目录文件，注意必须一级一级的删除

os.rmdir("python2") #错误示范，不能直接删除带有文件的目录

os.removedirs('python2')#删除递归目录

os.remove(os.path.realpath(__file__))#删除文件

path1=os.getcwd() #获取获取当前工作文件路径/工作目录

# __file__作为参数代表当前文件
path2=os.path.realpath(__file__) #获取当前文件所在的绝对路径，包括文件名

path3=os.path.join(os.getcwd(),"python4","china","jiangsu") #拼接路径
os.makedirs(path3) #将拼接出的路径创建出来

path4=os.path.split(__file__) #将当前文件的绝对路径的最后一级和上级分割开来，以列表的形式返回。

a=os.path.isdir(os.getcwd()) #判断是否是目录

b=os.path.isfile(os.path.realpath(__file__)) #判断是否是文件

c=os.path.exists(r"D:\\test_technical_data\\51testing\刘菲博为峰上课笔记\第二阶段\Python") #判断此路径（文件/目录）是否存在

d1=os.listdir(os.getcwd()) #列出当前路径下的所有文件和目录,返回一个列表
d2=os.listdir(r"D:\\test_technical_data")

e1=os.path.abspath(os.getcwd()) #返回path的绝对路径
e2=os.path.abspath("software")

'''
os.walk(top, topdown=True, onerror=None, followlinks=False)
os.walk() 方法是一个简单易用的文件、目录遍历器
top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
    root 所指的是当前正在遍历的这个文件夹的本身的地址
    dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
onerror -- 可选，需要一个 callable 对象，当 walk 需要异常时，会调用。
followlinks -- 可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，如果为 False，则优先遍历 top 的子目录。
'''
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print('遍历目标文件夹root下的所有文件', os.path.join(root, name))
    for name in dirs:
        print('遍历目标文件夹root下的所有目录', os.path.join(root, name))