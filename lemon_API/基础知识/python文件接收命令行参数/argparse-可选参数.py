import argparse

"""argparse--可选参数， 相当于关键字传参，不必考虑顺序，当参数有默认值或者非必填时可以不传"""

parser2 = argparse.ArgumentParser(description='可选参数')

parser2.add_argument('--name', type=str, default='Edger', help='姓名')  # type，指定参数的数据类型；default,对可选参数name设定默认值为Edger

parser2.add_argument('--age', type=int, required=True, help='年龄')  # required设定可选参数path为必填参数

args2 = parser2.parse_args()

print(args2.name+str(args2.age))  # 命令行python argparse-可选参数.py --age=12 --》 输出Edger12
                                  # 命令行python argparse-可选参数.py --name=liufei --age=27 --》 输出liufei27