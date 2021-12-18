# -*- coding: utf-8 -*-
# @Time :2020/6/5 19:15
# @Author : liufei
# @File :class_homework.PY

# # 自动贩卖机只接受 1元 5元 10元的纸币或硬币
# # 可以 1块 5块 10块，最多不超过10块钱
# # 自动贩卖机只接受1元 5元 10元的纸币或硬币可以一块5块10块，最多不超过10块钱，
# # 饮料只有橙汁，椰汁，矿泉水，早餐奶售价分别为3.5 4 2 4.5，写一个函数用来表示范围计的功能，
# # 用户投钱和选择饮料，并通过判断之后给用户吐出饮料和找零，用户投钱和选择饮料，并通过判断之后给用户吐出饮料和找零，
#
# # 思路先选饮料再付钱
# drink={"1":2.5,"2":4,"3":2,"4":4.5}
# total=0
# # 选饮料
# while True:
#     choice=input("请您选择，1橙汁2椰汁3矿泉水4早餐奶，按q退出")
#     if choice in drink.keys():
#         total+=drink[choice]
#     elif choice=="q":
#         print("退出选择饮料")
#         break
#     else:
#         print("您输入的选项不存在")
# # 投币
# toubi=0
# while True:
#     money=input("您只可以投入1元5元10元的纸币或硬币,按q退出投币")
#     if money == "1" or money == "2" or money == "10":
#         toubi+=int(money)
#         if total > toubi:
#             print("你购买{0}元饮料，你投入{1}元，还需投入{2}元".format(total,money,total-toubi))
#         elif total < toubi:
#             print("你购买{0}元饮料，你投入{1}元，找零{2}元".format(total,money, toubi-total))
#         else:
#             print("你购买{0}元饮料，你投入{1}元，支付完毕".format(total,toubi))
#             break
#     elif money=="q":
#         print("退出投币")
#         break
#     else:
#         print("您输入的选项不存在")

# # 输出一个直角三角形
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")

# # 输出一个等边三角形
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("* ",end="")
#     print(" ")