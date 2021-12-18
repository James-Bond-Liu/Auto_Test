Author:LiuLei
********************在使用和编写此测试框架时，请先阅读此文件*********************
使用人员直接看第五点使用说明


唯易自动化测试开发说明
一 开发目的唯易自动化测试开发说明
一 开发目的

自动化测试开发是为了更快、更有效率的完成固有的流程测试，保证固有的功能能够正常的运行，提供给客户更稳定，更好用的唯易软件
二 环境说明
1．	开发语言：python3.8
2．	主要框架：selenium
3．	编程模式：pageobject、单例模式
4．	Svn地址：https://121.43.166.225:8443/svn/taxplus/webtest

三 目录结构说明
1.	WEAutoTest
a)	data：该文件夹用来存放输入的数据和需要比对的数据
	data.py
1.	根据不同的功能创建，例如企业管理：business_data.py。
b)	element：该文件夹用来存放所有的页面元素
	el_element.py
1.	根据不同的页面创建，例如企业管理页面：el_business.py
c)	Page: 该文件夹用来存放所有的功能用例
	Page.py
1.	 WeEasy
	用来存放唯易主流程测试的用例
	根据页面来创建，例如添加企业、删除企业等：business_page.py
	调用data、element中的数据进行case的编写
2.	BasePage
	所有需要用到的方法，如果有新的需要用到的方法也可以往里面加
d)	report: 用于生成报告
	report.html
1.	每次执行完case可以查看执行情况
e)	testcase: 该文件夹下主要用于存放不同类型的测试
	test_WeEasy.py
1.	该文件为唯易的主流程测试
2.	该文件中写入所有page中的对应功能用例，用于固定流程，执行时按此文件中的调用顺序来执行
3.	如果有不同类型的测试再添加，一般不添加
f)	测试数据：存放用于导入的EXCEL，pdf等
四 编写规范
1. 	所有变量名最好用英文/英文缩写
2. 	page中如果有多个用例需要用到的重复操作，都需要单独定义函数去调用，避免过多的重复代码
3.	testcase中需要按照已有的来
4.	提交代码时，需要把testcase中的@pytest.mark.debug 注释掉
5.	提交代码时，要绝对保证写的case是能够正常执行成功的，不成功的代码不要提交
6.	每个人只写自己负责的模块，不要修改别人的，避免提交代码时冲突
7.	保证编写格式正确

五 使用说明
1.	测试开发人员，使用时需要区分用例上的mark标志
a)	debug：调试时使用，调试后会在debug_log中产生记录，提交代码时请关闭注释所有debug的mark
b)	we：主流程运行测试，会在report目录中产生记录
c)	declare: 例行申报测试
2.	测试人员使用时，首先在根目录使用pip install -r requirements.txt 安装所有的依赖环境
a)	如果有失败请多安装几次
b)	最好将python库切换至国内的源,安装的速度快，切失败几率小
c)	方法如下
c.1 Windows系统
直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

c.2Linux系统
修改 ~/.pip/pip.conf 文件， 内容如下：
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
3.	环境安装后，如果在pycharm中，就直接在terminal中直接输入 python main.py+mark标志即可运行对应的测试，mark标志在五.1中已经说明
4.	如果在cmd中直接运行，那就在该项目的根目录直接启动cmd，方法同上
