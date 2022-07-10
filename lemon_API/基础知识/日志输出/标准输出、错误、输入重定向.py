import datetime
import sys
from typing import TextIO
from io import TextIOWrapper
from re import compile, sub
import time

"""
参考文献：https://blog.csdn.net/NEKOic/article/details/123268139?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-1-123268139-blog-110044000.pc_relevant_aa2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-1-123268139-blog-110044000.pc_relevant_aa2&utm_relevant_index=2
"""
# 记录初始标准的输出位置，以便于最后恢复
old_stdout = sys.stdout
old_stdin = sys.stdin
old_stderr = sys.stderr


class CustomStream(object):
    """自定义流, 将标准输入输出流进行重新封装, 对输入输出功能进行扩充

    Attribute:
        stream (TextIO): 输入输出流
        log (TextIOWrapper): 日志文件对象
        message (str): 读取的文本信息

    """
    stream: TextIO
    log: TextIOWrapper
    message: str

    def __init__(self, filename, stream: TextIO):
        self.stream = stream
        self.log = open(filename, 'a', encoding="UTF-8")

    def write(self, message):
        self.stream.write(message)
        comp = compile(r"\033\[.*?m|\033\[.*?A|\033\[.*?C|")  # 这里匹配的东西以你用到的转义序列为准
        message = sub(comp, "", message)
        self.log.write(message)
        self.log.flush()

    def readline(self):
        message = self.stream.readline()
        self.log.write(message)
        self.log.flush()
        return message

    def flush(self):
        self.stream.flush()


def setLogger(log_file_path: str):
    """应用日志记录器

    Args:
        logfpath (str): 日志文件路径
    """
    sys.stdout = CustomStream(log_file_path, stream=old_stdout)
    sys.stderr = CustomStream(log_file_path, stream=old_stderr)
    sys.stdin = CustomStream(log_file_path, stream=old_stdin)


def removeLogger():
    """取消日志记录器, 将系统标准流重定向到最初的标准流
    """
    sys.stdout = old_stdout
    sys.stdin = old_stdin
    sys.stderr = old_stderr

setLogger('./日志.log')
print(datetime.datetime.now(), end='')
print(1/0)
print(sys.stdin)
print(sys.stderr)
print(sys.stdout)

removeLogger()
print(sys.stdin)
print(sys.stderr)
print(sys.stdout)