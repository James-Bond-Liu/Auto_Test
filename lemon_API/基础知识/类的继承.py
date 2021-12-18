# -*- coding: utf-8 -*-
# @Time :2020/6/6 18:24
# @Author : liufei
# @File :class_0606.PY

class RobotOne():#父类
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def walking_on_ground(self):
        print(self.name+"只能在平地上行走")
    def robot_info(self):
        print("{0}年生产的机器人{1}，是中国研发的".format(self.year,self.name))

class RobotTwo(RobotOne):#继承类
    def walking_on_ground(self):#重写
        super(RobotTwo,self).walking_on_ground()
        print(self.name + "可以在平地上行走")
    def walking_aviond_block(self):#拓展
        self.robot_info()#在一个方法里面调用其他方法时，必须加上self关键字。
        print(self.name+"可以避开障碍物")

t1=RobotTwo('星河',2000)#创建实例
t1.walking_on_ground()#通过实例调用方法

t2=RobotTwo('星河二号',2004)
t2.walking_aviond_block()
t2.walking_on_ground()
