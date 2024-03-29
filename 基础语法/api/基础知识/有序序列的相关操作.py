# -*- coding: utf-8 -*-
# @Time :2020/5/29 19:30
# @Author : liufei
# @File :class_0527.PY

#列表
a=[]
a.append('liufei') #追加

b=[1,2,3,4,5,'liufei',['京东','淘宝','拼多多']]
b.append('网易考拉')
b.insert(2,"苏宁易购") #插入
c=len(b) #统计元素个数
s=b.pop(2) #删除索引值为2的元素。默认删除最后元素，会返回被删除元素
b[1]='soft' #更改索引值1的元素
b.remove('liufei') #根据元素的值来删除元素

#元组
x=(1,2,"刘菲",[1,2,3])
x[3][2]="china" #更改元组中的列表中的值
e=x[::2] #元组切片

f=("enen",) #当元组中只有一个元素时，元素后面一定要加一个“,逗号”。否则不是元组格式。
print(type(f))

#字典
g={"马云":"淘宝","刘强东":"京东","黄峥":"拼多多"}
g.pop("马云") #删除字典中的元素
g["马云"]="阿里巴巴" #更改字典中的元素

#列表的切片
'''
                                                列表的切片操作

切片操作不是列表特有的，python中的有序序列都支持切片，如字符串，元组。

切片的返回结果类型和切片对象类型一致，返回的是切片对象的子序列，如：对一个列表切片返回一个列表，字符串切片返回字符串。

切片生成的子序列元素是源版的拷贝。因此切片是一种浅拷贝。
'''
li = ["A", "B", "C", "D"]
#格式：
#li[start: end: step]    start是切片起点索引，end是切片终点索引，但切片结果不包括终点索引的值。step是步长默认是1。

t1 = li[0:3]    #["A", "B", "C"]  起点的0索引可以省略，t=li[:3]
t2 = li[2:] #["C", "D"]  省略end，则切到末尾
t3 = li[1:3]    #["B", "C"]
t4 = li[0:4:2]  #["A", "C"]  从li[0]到li[3],设定步长为2。
t5 = li[::-1]   #['D', 'C', 'B', 'A']  倒序输出
t6 = li[3:0:-1]
print(t6)

#有序序列 range(strat,end,step)  start是起点索引,默认值为0，end是终点索引,但是结果不包括终点索引的值，step是步长默认是1。
for i in range(1,10):
    print(i)
