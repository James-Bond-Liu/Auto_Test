# -*- coding: utf-8 -*-
# @Time :2020/6/7 11:41
# @Author : liufei
# @File :class_homework.PY

# 按照以下要求定义一个游乐园门票类并创建实例调用函数完成儿童和大人的总票价，统计人数不定由你输入的人数个数来决定
# 平日票价100元，周末票价为平日票价的120%，儿童半价，

class CostTicket():
    def __init__(self):
        self.price=100

    def booking_ticket(self):
            day = int(input("请输入您要购买那天的票，1-7代表星期一到星期日"))
            number1 = int(input("请输入您够买成人票的个数"))
            number2 =int(input("请输入您够买儿童票的个数"))
            if day in range(1,6):
                money=number1*self.price+number2*self.price*0.5
                print(money)
                # break
            elif day in range(6,8):
                money = number1 * self.price*1.2 + number2 * self.price * 0.5
                print(money)
                # break
            else:
                print("您输入的选项有误")
if __name__ == '__main__':
    t1=CostTicket()
    t1.booking_ticket()
