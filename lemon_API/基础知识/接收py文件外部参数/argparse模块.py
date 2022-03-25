import argparse

"""argparse--位置参数, 传入参数必须按照顺序传入"""
# 创建一个解析对象
parser1 = argparse.ArgumentParser(description='位置参数')

# 向对象中添加位置参数
# integers 参数名
# type 传入参数的数据类型, 该关键词可以传入list, str, tuple, set, dict等
# help 该参数的提示信息
# nargs是用来说明传入的参数个数，'+' 表示传入至少一个参数，'*' 　表示参数可设置零个或多个，'?'　表示参数可设置零个或一个
parser1.add_argument('param1', type=int, nargs='+', help='需要传入的数字')

parser1.add_argument('param2', type=str, help='姓')

parser1.add_argument('param3', type=str, help='名')

# 对添加的参数进行解析
args1 = parser1.parse_args()  # args类似于python的字典

# 使用 arg.参数名来提取传入的参数
print(args1)  # 在命令行中输入 python argparse模块.py 5，输出 5


"""argparse--可选参数， 相当于关键字传参，不必考虑顺序"""

parser2 = argparse.ArgumentParser(description='可选参数')

parser2.add_argument('--file', type=str, default='demo.txt', help='文件名')  # default,对参数file设定默认值为demo.txt

parser2.add_argument('--path', type=str, required=True, help='文件路径')  # 设定可选参数path为必需参数

args2 = parser2.parse_args()

print(args2.path+args2.file)  # 在命令行输入python argparse模块.py --path=c:/workfiles/ESS/ --file=ess_data

