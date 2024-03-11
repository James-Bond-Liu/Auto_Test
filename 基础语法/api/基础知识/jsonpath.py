# -*- coding: utf-8 -*-
# @Time :2021/2/15 16:21
# @Author : liufei
# @File :练习.PY
'''
Jsonpath表达式
JSONPath	Description
$	        表示根元素
@	        当前元素
. or []	    子元素
..	        递归下降，JSONPath是从E4X借鉴的。
*	        通配符，表示所有的元素
[]	        子元素操作符
[,]	        连接操作符在XPath 结果合并其它结点集合。JSONP允许name或者数组索引。
[start:end:step]	数组分割操作从ES4借鉴。
?()	        应用过滤表示式
()	        脚本表达式，使用在脚本引擎下面。
'''
import jsonpath
data = {
    "lemon": {
        "teachers": [
            {
                "id": "101",
                "name": "华华",
                "addr": "湖南长沙",
                "age": 25
            },
             {
                "id": "102",
                "name": "韬哥",
                "age": 28
            },
            {
                "id": "103",
                "name": "Happy",
                "addr": "广东深圳",
                "age": 16
            },
             {
                "id": "104",
                "name": "歪歪",
                "addr": "广东广州",
                "age": 29
            }
        ],
        "salesmans": [
            {
                "id": "105",
                "name": "毛毛",
                "age": 17
            },
             {
                "id": "106",
                "name": "大树",
                "age": 27
            }
        ]
    },
 "avg": 25
}
'''
                                          Jsonpath实例
JsonPath	                     路径说明
$.lemon.teachers[*].name	     获取所有老师的的名称
$..name	                         获取所有人的名称
$.lemon.*	                     所有的老师和销售
$.lemon..age	                 所有人的年龄
$..age	                         所有人的年龄
$.lemon.teachers[*].age	         所有老师的年龄
$.lemon.teachers[3]	             索引为 3（第 4 个）老师的信息
$..teachers[3]	                 索引为 3（第 4 个）老师的信息
$.lemon.teachers[-2]	         倒数第 2 个老师的信息
$..teachers[-2]	                 倒数第 2 个老师的信息
$..teachers[1,2]	             第 2 到第 3 个老师的信息
$..teachers[:2]	                 索引 0（包含）到索引 2（不包含）的老师信息
$..teachers[1:3]	             索引 1（包含）到索引 3（不包含）的老师信息
$..teachers[-2:]	             最后的两个老师的信息
$..teachers[2:]	                 索引 2 开始的所有老师信息
$..teachers[?(@.addr)]	         所有包含地址的老师信息
$.lemon.teachers[?(@.age < 20)]	 所有年龄小于 20 的年龄信息
..teachers[?(@.age<=['avg'])]]	 小于或等于平均年龄的老师信息
$..teachers[?(@.name =~ /.*PPY/i)]	所有名称满足正则表达式的老师信息 (忽略大小写)
$..*	                         所有的信息
$.lemon.teachers.length()	     老师的数量
'''
result1 = jsonpath.jsonpath(data, '$.store.book[*].author')
result2 = jsonpath.jsonpath(data, '$..author')
result3 = jsonpath.jsonpath(data, '$.store.*')
result4 = jsonpath.jsonpath(data, '$..book[?(@.isbn)]')
print(result4)