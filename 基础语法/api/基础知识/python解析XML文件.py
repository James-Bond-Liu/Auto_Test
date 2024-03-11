# -*- coding: utf-8 -*-
# @Time :2021/3/12 23:14
# @Author : liufei
# @File :python解析XML文件.PY
import xml.etree.ElementTree as ET

tree = ET.parse('D:\Python_files\lemon_API\基础知识\country_data') #解析XML文档
root = tree.getroot() #获取根节点
print('root-tag:', root.tag, ',root-attrib:', root.attrib, ',root-text:', root.text)#显示根节点的标签名，属性名，文本内容
'''
<tag attrib1=1>text</tag>tail
  1    2        3         4
tag：string对象，表示数据代表的种类，当为节点时为节点名称。
 
text：string对象，表示element的内容。
 
attrib：dictionary对象，表示附有的属性。
 
tail：string对象，表示element闭合之后的尾迹。
'''

# 对根节点下的所有元素进行遍历，然后打印
for child in root:
     print('child-tag是：',child.tag,',child.attrib：',child.attrib,',child.text：',child.text)
     for sub in child:
          print('sub-tag是：',sub.tag,',sub.attrib：',sub.attrib,',sub.text：',sub.text)

# find/findall方法搜寻匹配的节点
animNode = root.find('country') #查找root节点下第一个tag为country的节点
animNode = root.findall('country') #查找并返回root节点下包含所有tag为country的列表，如果没有匹配元素则返回空列表
print(animNode.tag,animNode.attrib,animNode.text)

#直接使用索引寻找子节点
print(root[0][1].tag,root[1][1].attrib,root[2][1].text)#返回'''year {} 2011'''


# 删除指定的节点以及保存
animNode = root.find('country')
if animNode.attrib['name'] == 'Liechtenstein':
     root.remove(animNode)
tree.write('finish.xml')#保存修改后的XML文件

'''
针对属性的操作
  clear()                     清空元素的后代、属性、text和tail也设置为None。
  get(key, default=None)      获取key对应的属性值，如该属性不存在则返回default值。
  items()                     根据属性字典返回一个列表，列表元素为(key, value）。
  keys()                      返回包含所有元素属性键的列表。
  set(key, value)             设置新的属性键与值。
 
针对后代的操作
  append(subelement)       添加直系子元素。
  extend(subelements)      增加一串元素对象作为子元素。＃python2.7新特性
  find(match)              寻找第一个匹配子元素，匹配对象可以为tag或path。
  findall(match)           寻找所有匹配子元素，匹配对象可以为tag或path。
  findtext(match)          寻找第一个匹配子元素，返回其text值。匹配对象可以为tag或path。
  insert(index, element)   在指定位置插入子元素。
  iter(tag=None)           生成遍历当前元素所有后代或者给定tag的后代的迭代器。
  iterfind(match)          根据tag或path查找所有的后代。
  itertext()               遍历所有后代并返回text值。
  remove(subelement)       删除子元素。
'''

# parse(source, parser=None)：将外部xml加载到树中。source为文件名或文件句柄。parser是可选的解析器实例，默认为XMLParser解析器。
# 函数返回树的根元素，如果解析器无法解析文档，则会产生ParseError错误。

# makeelement(tag, attrib)：创建与此元素类型相同的新Element对象。tag为元素名。attrib为元素属性字典。
#
# append(subelement)：将subelement添加到Element内部子元素列表的末尾。subelement必须是Element类实例，否则会产生TypeError。
#
# extend(elements)：Python3.2新增，将elements添加到Element内部子元素列表的末尾。elements为0到多个Element类实例序列，否则会产生TypeError。
#
# insert(index，subelement)：将subelement添加到Element内部子元素列表的指定索引处。subelement必须是Element类实例，否则会产生TypeError。index为要插入subelement的索引位置。
#
# remove(subelement)：删除匹配的子元素。此函数比较的是内存地址而不是tag值和元素内容。如果找不到匹配的元素，则会产生ValueError。
#
# getchildren：返回所有直接子元素，Python3.2起弃用，使用list（ele）或迭代替代。
#
# getiterator(tag=None)：Python3.2起弃用，使用iter函数替代。
#
# find(path, namespaces=None)：查找并返回第一个匹配的元素，如果未找到则返回None。path为标签名或xpath字符串。namespaces是一个命名空间前缀到全名的映射的字典，默认为None。此函数实际上是调用的ElementPath的find方法。
#
# findall(path, namespaces=None)：查找并返回包含所有匹配元素的列表，如果没有匹配元素则返回空列表。path为标签名或xpath字符串。namespaces是一个命名空间前缀到全名的映射的字典，默认为None。此函数实际上是调用的ElementPath的findall方法。
#
# iterfind(path, namespaces=None)：Python3.2新增，与findall功能相同，只不过返回的是generator实例而不是列表。此函数实际上是调用的ElementPath的iterfind方法。
#
# findtext(path, default=None, namespaces=None)：查找并返回第一个匹配的元素的文本。path为标签名或xpath字符串。default为当找不到path指定的元素时返回的默认文本，namespaces是一个命名空间前缀到全名的映射的字典，默认为None。此函数实际上是调用的ElementPath的findtext方法。
#
# clear：重置元素。删除所有子元素，元素属性字典，text和tail字段设置为None。
#
# get(key, default=None)：获取元素属性。key为要查找的属性名，default为可选的，要查找的属性不存在时的默认返回值，默认为None。
#
# set(key, value)：设置元素属性。key为要设置的属性名。value为要设置的属性值。
#
# keys：获取元素属性名列表。
#
# items：返回包含元素属性的（名称、值）元组的列表。
#
# iter(tag=None)：Python3.2新增，创建并返回一个以当前元素为根的树迭代器。迭代器按文档顺序遍历这个元素和它下面的所有元素。如果tag不为None或“*”，则迭代器只返回名称与tag相同的元素。如果在迭代期间树结构发生变化，则可能包含也可能不包含新增或删除的元素。要获得一个稳定的集合，可以在迭代器上使用list()函数，并循环得到的列表。
#
# itertext：Python3.2新增，创建并返回一个文本迭代器。按文档顺序循环元素和所有子元素，并返回他们的内部文本。

