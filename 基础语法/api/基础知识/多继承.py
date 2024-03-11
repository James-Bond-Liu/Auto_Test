# -*- coding: utf-8 -*-
# @Time :2020/6/6 18:24
# @Author : liufei
# @File :class_0606.PY

# 多继承
class RobotOne():
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def walking_on_ground(self):
        print(self.name+"只能在平地上行走")
    def robot_info(self):
        print("{0}年生产的机器人{1}，是中国研发的".format(self.year,self.name))

class RobotTwo():
    def __init__(self,name):
      self.name=name
    def walking_on_ground(self):
        print(self.name + "可以在平地上行走")
    def walking_aviond_block(self):
        print(self.name+"可以避开障碍物")

class RobotThree(RobotTwo,RobotOne):
    def __init__(self, name,year):
        super(RobotThree,self).__init__(name)#超继承父类RobotTwo中的__init__方法
        self.year=year#添加属于自己的特色
    def jump(self):
        print(self.name+"可以单膝跳跃")
t3=RobotThree('星河三号','2004')
t3.walking_on_ground()
t3.robot_info()

t4=RobotThree("星河四号","2008")
t4.jump()
t4.walking_on_ground()
