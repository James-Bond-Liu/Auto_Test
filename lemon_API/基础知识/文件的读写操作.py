# -*- coding: utf-8 -*-
# @Time :2020/6/2 21:38
# @Author : liufei
# @File :class_0601.PY

# from class_one import class_func#导入的过程中，最少具体到模块名又叫文件名
# class_func.add(5,1)

#file操作

file1=open("../class_one/demo.txt", "r", encoding='utf-8')
s1=file1.read(3) #读取三个字节,此时光标移动到第三个字节后面
s2=file1.seek(0) #移动光标到第一位
s3=file1.read(3)

with open("../class_one/demo.txt", "r", encoding="utf-8") as file2:
    s2=file2.read() #读取文件中的全部内容
    print(s2)

file3=open("../class_one/demo.txt", "r", encoding='utf-8')
s3=file3.readline()
print(s3)

file4=open("../class_one/demo.txt", "r", encoding='utf-8')
s4=file4.readlines() #按行读取文件中的内容，返回一个列表，一行作为一个元素。
print(s4)

file5=open("../class_one/demo.txt", "w", encoding='utf-8')
s5=file5.write("china,my country\n中国，我的祖国") #写入文件
print(s5)

file6=open("../class_one/demo.txt", "w", encoding='utf-8') #写入多行，以列表的形式写入
s6=file6.writelines(["china,my coutry\n","中国，我的祖国"])
print(s6)

file7=open("../class_one/demo.txt", "a", encoding='utf-8') #以追加的方式打开文件
s7=file7.writelines(["I am chinese","我是中国人"])
print(s7)

'''
                                                    文件读写操作
r 只能读
r+可读可写，不会创建不存在的文件。如果直接写文件，则从顶部开始写，覆盖之前此位置的内容（并不是原文件内容全部消失，
    仅代表原位置的内容被覆盖掉，其余文件内容依然存在不受影响），如果先读（无论读取文件中几个字节，指针都会移动到文末）后写，则会在文件最后追加内容。

w+ 可读可写 如果文件存在 则覆盖整个文件（原文件中的所有内容均被覆盖），不存在则创建，必须先写后读，且要移动文件指针

w 只能写 覆盖整个文件 不存在则创建

a 只能写 从文件底部添加内容 不存在则创建

a+ 可读可写  永远从文件底部添加内容 不存在则创建，文件指针在最后，读需要移动文件指针

'''