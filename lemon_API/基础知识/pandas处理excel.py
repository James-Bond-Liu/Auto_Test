# -*- coding: utf-8 -*-
# @Time :2020/7/2 21:19
# @Author : liufei
# @File :do_pandas.PY

import pandas as pd
#pandas处理execl行列的索引是从“0”开始的
#openpyxl处理execl行列的索引是从“1”开始的

df=pd.read_excel('test_data.xlsx')#默认打开第一个表单
df1=pd.read_excel('test_data.xlsx',sheet_name=0,header=0)#指定表单打开，0索引表示第一个表单.
# header表示指定作为列名的行，默认0，即取第一行，数据为列名行以下的数据；若数据不含列名，则设定 header = None；

df2=pd.read_excel('test_data.xlsx',sheet_name=[0,1])#指定表单打开，用列表表示打开多个表单
df3=pd.read_excel('test_data.xlsx',sheet_name='login')#根据表单名打开表单

print(df.values())  #获取表单中所有的数据，读取的数据是列表嵌套列表的格式，每一行作为一个子列表嵌套在一个大列表中。
'''
利用pandas读取数据时，当行信息为一行或者列信息为一列时仅需要一个列表即可，当行数为多行或者列数为多列时需要单独将行数（列数）写成一个列表
形成列表嵌套列表的形式。
'''
data1 = df.loc[0].values  # 读取指定的单行，数据会存在列表里面；0表示第一行 这里读取数据并不包含表头，要注意哦！

data2 = df.loc[[1, 2]].values   #读取指定的多行，数据会存在嵌套的列表里面,行列索引都是0开始。

data3 = df.iloc[1, 2]   #读取指定的行列

data4 = df.loc[1, ['case_id','url','http_method']].values  #读取指定的某一行多列值：

data5 = df.loc[[1, 2], ['case_id','url','http_method']].values  #读取指定的多行多列值：

data6 = df.loc[:, ['case_id','data','title','http_method','expected']].values    #获取所有行的指定列,得到的是嵌套列表

data7 = df.loc[:, ['case_id','data','title','http_method','expected']]    #获取所有行的指定列,得到二维矩阵

data7_1 = df.loc[:, ['case_id','data','title','http_method','expected']].to_dict()  #获取所有行的指定列的数据，并将其转化成字典类型

data8 = df.head(n=5) #获取前几行数据，默认5行

data9 = df.tail(n=5)    #获取后几行数据，默认5行

print("输出行号列表:", df.index.values)   #获取行号并打印输出,从0开始,返回一个列表,不包括列名

print("输出标题列名:", df.columns.values)   #获取列名并打印输出['case_id','data','title','http_method','expected']

print("输出值:\n", df.sample(3).values)  # 随机抽取3行查看，这个方法类似于head()方法以及df.values方法

print("输出值:\n", df['url'].values)    #获取指定列的值：


                                        #pandas处理Excel数据成为字典

print("\npandas处理Excel数据成为字典")
df = pd.read_excel('ceshi.xlsx', sheet_name=0)
test_data = []
for i in df.index.values:  # 获取行号的索引，并对其进行遍历
    # 根据i来获取每一行指定的数据 并利用to_dict转成字典
    row_data = df.loc[i, ['case_id','data','title','http_method','expected']].to_dict()
    test_data.append(row_data)
print(test_data)
