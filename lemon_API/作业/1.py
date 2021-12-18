# -*- coding: utf-8 -*-
# @Time :2020/6/7 11:41
# @Author : liufei
# @File :class_homework.PY

# 定义一个学生类，
# 有下面的类属性，1 姓名 2 年龄 3 成绩，语文数学英语每课成绩的类型为整数，均放在初始化函数里面为
# 方法
# 获取学生的姓名，get_name()返回类型str，获取学生的年龄get_age()返回类型int，返回三门科目中最高的分数get_course()返回类型int
# 写好了以后，可以定义两个同学测试一下，

class Student():
    def __init__(self,name,age,*course):
        self.name=name
        self.age=age
        self.course=course
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        course1=sorted(list(self.course))
        return course1[2]
if __name__ == '__main__':
    s1=Student('liufei','23',90,56,89)
    print(s1.get_name())
    print(s1.get_age())
    print(s1.get_course())

