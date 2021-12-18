# -*- coding: utf-8 -*-
# @Time :2020/6/7 11:41
# @Author : liufei
# @File :class_homework.PY

# 人和机器猜拳游戏写成一个类，有如下几个函数
# 函数一，选择角色 1 曹操 2 张飞 3 刘备
# 函数二，角色猜拳，1 剪刀 2 石头 3 布 输入1~3的数字
# 函数三，电脑出拳随机产生一个1~3的数字，提示电脑出拳
# 函数4，角色和机器出拳对战，对战结束后最后出示本局最后对战结果 赢 输 ，然后提示用户是否继续，y继续n退出，
# 最后结束的时候，输出结果,角色赢几局,电脑赢几局,平局几局，游戏结束，

import random
class Ganme():
    role_dict={1:'曹操',2:'张飞',3:'刘备'}
    fist_dict={1:'剪刀',2:'石头',3:'布'}
    def get_role_name(self):
        role_num=input("请选择角色'1':'曹操','2':'张飞','3':'刘备'")
        return self.role_dict[int(role_num)]
    def get_role_fist(self):
        fist_num=input("角色请出拳'1':'剪刀','2':'石头','3':'布'")
        return int(fist_num)
    def get_computer_fist(self):
        fist_num=random.randint(1,3)
        return fist_num

    def play_games(self):
        role_win=0
        cp_win=0
        draw=0
        role_name=self.get_role_name()

        while True:
            role_fist = self.get_role_fist()
            compuer_fist = self.get_computer_fist()
            print(role_name+"出拳为{0}，电脑出拳为{1}".format(role_fist,compuer_fist))
            if role_fist - compuer_fist == 1 or role_fist - compuer_fist == 2:
                role_win+=1
                print("角色赢了")
            elif role_fist - compuer_fist == -1 or role_fist - compuer_fist == -2:
                cp_win+=1
                print("电脑赢了")
            elif role_fist - compuer_fist == 0:
                draw+=1
                print("双方平局")
            chocie=input("是否还继续，y继续，n退出")
            if chocie=='n':
                break
        print("角色赢了{}局，电脑赢了{}局，平局{}".format(role_win,cp_win,draw))
s=Ganme()
s.play_games()