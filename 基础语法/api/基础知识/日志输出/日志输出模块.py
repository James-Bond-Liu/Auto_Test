import logging

class OutPutLog():
    def __init__(self, file_name):
        self.file_name = file_name

    def out_log(self):
        logger=logging.getLogger('BANG')  #设定日志器，并取名
        logger.setLevel('DEBUG')  #用来设定日志级别
        if not logger.handlers:
            ch=logging.FileHandler(self.file_name,encoding='utf-8')
            # ch.setLevel('ERROR')  #创建的handler也可以调用setlevel函数，
                                    #日志器先对日志级别进行过滤，如果处理器也设计了级别，处理器handler也会进行一次过滤日志级别
            fh=logging.StreamHandler()
            # fh.setLevel('INFO')

            # 设定格式器
            formatter=logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s %(filename)s %(message)s",
                                        datefmt="%Y-%m-%d %H:%M:%S") # 注意格式器中的参数fmt的实参每个参数后面都要加”s“
            ch.setFormatter(formatter)   #将格式器加入到处理器中
            fh.setFormatter(formatter)
            logger.addHandler(ch)
            logger.addHandler(fh)
        return logger

'''
日志流处理简要流程
总的来说：日志器、处理器、格式器三个是相互独立创建的，
然后，利用addHandler方法给日志器添加处理器实例，利用setFormatter方法给处理器添加格式器
1、创建一个logger

2、设置下logger的日志的等级

3、创建合适的Handler(FileHandler要有路径)

4、设置下每个Handler的日志等级

5、创建下日志的格式

6、向Handler中添加上面创建的格式

7、将上面创建的Handler添加到logger中

8、打印输出logger.debug\logger.info\logger.warning\logger.error\logger.critical
'''