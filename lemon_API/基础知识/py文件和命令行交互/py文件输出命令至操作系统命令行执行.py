
import os
"""
使用os.system模块将命令输出至操作系统命令行执行
"""
os.system('')


import subprocess
"""
subprocess 模块首先推荐使用的是它的 run 方法，更高级的用法可以直接使用 Popen 接口。

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

args：表示要执行的命令。必须是一个字符串，字符串参数列表。

stdin、stdout 和 stderr：子进程的标准输入、输出和错误。其值可以是 subprocess.PIPE、subprocess.DEVNULL、一个已经存在的文件描述符、已经打开的文件对象或者 None。subprocess.PIPE 表示为子进程创建新的管道。subprocess.DEVNULL 表示使用 os.devnull。默认使用的是 None，表示什么都不做。另外，stderr 可以合并到 stdout 里一起输出。

timeout：设置命令超时时间。如果命令执行时间超时，子进程将被杀死，并弹出 TimeoutExpired 异常。

check：如果该参数设置为 True，并且进程退出状态码不是 0，则弹 出 CalledProcessError 异常。

encoding: 如果指定了该参数，则 stdin、stdout 和 stderr 可以接收字符串数据，并以该编码方式编码。否则只接收 bytes 类型的数据。

shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。
"""
subprocess.run(["ls", "-l", "/dev/null"])  # 返回 CompletedProcess实例，CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0)
                                           # 通常返回状态为0则表明它已经运行完毕，若值为负值 "-N",表明子进程被终。

def runcmd(command):
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
    if ret.returncode == 0:
        print("success:",ret)
    else:
        print("error:",ret)


runcmd(["dir","/b"])#序列参数
runcmd("exit 1")#字符串参数