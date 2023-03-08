import sys
"""
指定参数时，使用空格隔开就可以，缺点是我们必须按照脚本的顺序指定，参数较多不建议使用。
sys.argv是一个列表，第一个元素为py文件本身即文件名，后续元素为命令行向文件中传输的参数
"""
params = sys.argv  # sys.argv用来接收外部参数，用列表格式来储存外部传入的参数
print(params)
for i in params:
    print(i)
"""
在终端命令行执行该文件
python demo.py 1 3 5 6 7
输出：demo.py 1 3 5 6 7
"""
