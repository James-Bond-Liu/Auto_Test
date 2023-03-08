import argparse

"""argparse--位置参数, 传入参数必须按照顺序传入"""
# 创建一个解析对象
parser1 = argparse.ArgumentParser(description='位置参数')

# 向对象中添加位置参数-形参
# nargs是用来说明传入的参数个数，'+' 表示传入至少一个参数，'*' 　表示参数可设置零个或多个，'?'　表示参数可设置零个或一个
parser1.add_argument('param1', type=int, nargs='+', help='需要传入的数字')  # param1-参数名称，type-指定参数类型list str tuple set dict

parser1.add_argument('param2', type=str, help='姓')  # help 参数的提示信息，在命令行可以通过-h展示提示信息help

parser1.add_argument('param3', type=str, help='名')

# 对添加的参数进行解析
args1 = parser1.parse_args()  # args1类似于python的字典



# 使用 args1.参数名来提取传入的参数
print(args1.param1[1])  # 在命令行中输入 python argument.py 5 2 4 5 liu fei  # 输出 2
print(args1.param1)  # 在命令行中输入 python argument.py 5 2 4 5 liu fei  # 输出 [5 2 4 5]