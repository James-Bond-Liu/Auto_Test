import sys
for i in sys.argv:  # sys.argv是一个列表，用来存储py文件传入的参数，不限个数，但是顺序在提取时要一致
    print(i)


# 在命令行终端执行 python argv列表.py 1 liu 4
# 1
# liu
# 4