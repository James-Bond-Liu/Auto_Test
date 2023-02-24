# 接口自动化

## 一、Python基础

interpreter：解释器，Python中一般用的解释器为CPython，是Python程序运行的环境

package：代码一般放到包里，包里有一个初始化文件，`__init__.py`

模块即Python文件，模块名即Python文件名，字母与数字以下划线分隔开

注释：#，注释单行 ctrl+/，注释快捷键，"""....."""，注释多行

数字：整型，浮点型

布尔值：True，False

### 1、字符串

* 字符串里的元素：单个字母，单个符号都算一个元素。且元素索引正序从0开始，反序从-1开始

* 列表里的元素根据“，”来确定元素个数，列表的子元素均为字符串类型
* 字符串支持切片

#### 1.字符串的切割函数

​	字符串.split("指定的分割符"，指定切割次数-默认为1)，分割符被切走不再存在。

#### 2.字符串的替换

​	字符串.replace（old，new，指定替换次数）

#### 3.字符串去除指定字符

只能去除首尾两处的字符，只作用于首尾。字符串.strip（指定字符-默认为空格）

#### 4.字符串的拼接

​	+，保证+号两边的数据类型要一致。

#### 5.数据类型的强制转换

​	目标数据类型（原数据）

#### 6.查询字符串中的子字符或子字符串

​	find（"子字符或子字符串"），如若存在，返回子字符所在的索引。若存在多个子字符，则返回第一个索引。找不到不存在子字符，返回-1.

#### 7.字符串切片

```python
s = "hello,world!"
n = s[1,5,2]
print(n)  # el,
```



#### 8.字符串的格式化输出

1. <u>.format()</u>，特点用{}来占位

   ```python
   age = 4
   name = 'panda'
   print("{}岁的{}在爬".format(age, name))
   print("{1}岁的{0}在爬".format(name, age))
   ```

2. %，特点用%来占位

   %s——字符串，可以填任何类型数据

   %d——只能是数字整型，如若是浮点型数据则会被强制转换成整型。

   %f——浮点数，%.2f即代表保留两位小数

#### 9.type(对象)，输出对象的数据类型，或者`对象.__class__`，同理

### 2、列表list[]

* 可以存在空列表，列表可以存储任何类型的数据，用“，”分割每个元素。
* 当存储同一类型的数据时建议用列表
* 列表索引从0开始
* 列表支持切片

#### 1.列表追加元素

​	list.append（），在列表末尾追加元素，每次只能追加一个

#### 2.列表插入数据

​	list.insert（索引值，插入元素），可以在列表的任意位置插入元素

#### 3.列表删除元素

1. list.pop（索引值），默认删除最后一个元素，被删除的元素会返回回来，可以用一个变量接收
2. list.remove（元素值），根据列表中的元素值来删除元素

#### 4.列表修改元素

​	list[索引] = 新值，赋值运算

#### 5.swapcase()函数，将字符串的大写转为小写，小写转为大写。

​	s='Hello'，swapcase(s)：hELLO

#### 6.字符串的映射translate()

* 先用maketrans()方法制作一个映射表
* 再利用translate()方法进行映射

~~~python
s = 'hello, world'
intab = 'elod'
outtab = '1234'
trantable = s.maketrans(intab, outtab)
s.translate(trantable)  # h1223,w3r24
~~~

#### 7.列表转为字典

~~~python
s1 = ['key1', 'key2']
s2 = ['value1', 'value2']
result = dict(zip(s1,s2))  # {'key1':'value1', 'key2','value2'}
~~~



### 3、元组tuple（）

* 元组可以包含任何类型的数据，可以存在空元组（）
* 元组支持切片，索引从0开始
* 元组不能进行任何的修改（增、删、改）
  * a =(1, 2, "panda", [1, 4])，a\[3][0\]=8，这样就能更改为a =(1, 2, "panda", [8, 4])
  * 元组本身的元素不能更改，可以将元组里面的列表元素修改，字符串不可以
* 如果元组结构的数据只有一个元素，那么必须加“，”。（‘panda’，）

### 4、字典dict{}

* 字典内部结构key:value，key键必须是唯一的。元素之间用“，”分隔
* 字典的value，可以存放任意类型的数据

#### 1.字典取值

​	字典名[key]

#### 2.删除字典元素

​	字典名.pop(key)

#### 3.字典新增元素

​	字典名[新key] = value

#### 4.字典修改元素

​	字典名[老key] = value

#### 5.update修改/新增元素

~~~python
one = {'name':'panda', 'age':4}

one.update(name='tiger', address='中国成都')  # 可以直接修改存在的KEY，若不存在则新增元素

print(one)  # {'name': 'tiger', 'age': 4, 'address': '中国成都'}
~~~





### 5、运算符

* 加+、减-、乘*、除/、模%。模运算-取余运算，一般用来判断奇偶的问题
* 赋值运算，=
* 比较运算，>，<，>=，<=，!=，==。返回结果布尔值
* 逻辑运算，and，or，not。返回结果布尔值
* 成员运算符，in，not in。返回结果布尔值。
  * 对于字典只能判断key是否存在于字典中



### 6、函数

#### 1.判断语句 if

​	一个条件语句里面，只能有一个if，一个else且else后面不能跟条件。

```python
if 条件：
	子语句
elif 条件：
	子语句
.
.
.
else:
	子语句
```

​	没有elif判断语句的另一种写法

~~~python
真 if 条件 else 假

'成年' if age > 18 else '未成年'
~~~



#### 2.input（）函数

​	从控制台获取数据，且获取的数据都会被转换为字符串str类型

​	s = input（“提示信息”）,用变量s来接收

#### 3.random，随机数

* 可以利用random模块随机生成手机号码

​	random.randint(a, b)，生成[a, b]的随机整数

​	random.random()，生成（0，1）的随机浮点数

​	random.uniform(a,b)，生成[a, b]的随机浮点数

​	random.choice(序列)，序列指字典、列表、元组

​	random.randrange(a, b, c)，a=开始，b=结束，c=步长。从指定递增的范围内随机取一个数

​	

#### 4.for 循环

​	for 循环中“in”的作用，遍历可迭代类型数据的元素，一个个的遍历获取然后赋值给变量

* 对字典名进行遍历时，遍历的是字典的Key。s = {'name':'panda', 'age':4, 'sex':'man'}, for i in s:
* 遍历获取字典中所有的key值，for i in s.keys:
* 遍历获取字典中所有的value值，for i in s.values:

~~~python
li = [1, 2, 3, 4]
for i in li:
	print(i)
~~~

#### 5.range(首, 尾, 步长)函数

​	首：默认为0。步长：默认为1.

​	生成一个整数序列，取头不取尾。range(1, 5, 1)=1,2,3,4

#### 6.zip函数

~~~python
s1 = ['key1', 'key2']
s2 = ['value1', 'value2']
result1 = dict(zip(s1,s2))  # {'key1':'value1', 'key2','value2'}

result2 = list(zip(s1,s2))  # [('key1','value1'),('key2','value2')]。返回一个列表嵌套了元组，列表中第i个元组是原列表中第i个元素组合而成。

~~~



### 7、自定义函数

* 关键字，def 函数名（参数）。

#### 1.参数

1. 位置参数

   def func(n, m, k):

   赋值：func(1, 2, 3)

2. 默认参数

   def func(n, m=1, k = 0):	默认参数要放在位置参数后面。

   赋值：func(2, k=3)，当默认参数有值不需要重传时，可以直接给后面的默认参数赋值

3. 动态参数（*args），在不确定传入几个参数时使用。

   def func(*args)

   *args，代表是一个不定长参数，但在函数体中利用这个参数时则不需要加“\*”，引用变量时直接用变量名args即可。

   赋值：func(1, 3, 4, 5)

   动态参数在字典中体现为元组结构

4. 关键字参数（**kwargs）

   def func(**kwargs)：

   赋值：func(name = 'panda', age = 4, sex = 'boy')	或者	dict1 = {"name":'panda', 'age':4, 'sex'='boy'}，func(**dict1)

   关键字参数在函数中体现为字典结构。

#### 2.变量

1. 全局变量

   整个模块都能用这个变量

2. 局部变量

   函数体内部的局部变量，只能作用于函数

* 两者在于作用范围不一样
* 当两者同时存在且同名，优先使用局部变量。当局部变量不存在时，则使用全局变量。
* 在函数体内部若要使用全局变量，需在函数体内使用之前，先声明函数体内的变量是全局变量。global   全局变量名
* 多层函数嵌套，可以使用“nonlocal  变量名”，来使用并修改外层函数变量

#### 3.函数调用

​	def func(): ....

​	func()：函数名后加()，调用的是函数的执行结果，需要等待该函数执行完成。

​	func：函数名后不带()，调用的是整个函数体，调用的是一个函数对象，不用等待函数执行。

### 8、文件操作

#### 1.open(文件路径, mode)

返回一个文件实例对象file

mode：打开文件的模式——r, w, a, r+, w+, a+。默认打开方式r只读

当向文件中写入中文时，可添加参数encoding = 'gbk'/'utf-8'。Python写入文件不支持自动换行。必须手动输入换行符。

1. file.read()：读取文件中的所有内容
2. file.readline()：按行读取
3. file.readines()：多行读取文本内容，并保存在列表中
4. file.writelines()：写入多行，以列表形式写入，file.writelines(['13', 'panda'])

#### 2.文件相对路径

“/”：表示根目录，在windows系统下表示某个盘的根目录，如“E:\”；
“./”：表示当前目录；（表示当前目录时，也可以去掉“./”，直接写文件名或者下级目录）
“../”：表示上级目录。

![image-20210820201446852](Python自动化.assets/image-20210820201446852.png)

xxx.py想要打开a.txt：./b_file/a.txt

ab.py尝试打开b_file下的a.txt：../b_file/a.txt



### 9、os模块

1. os.mkdir(目录名)：在当前项目路径下新建一个目录/文件夹。此方法不允许递归跨级的创建目录。

2. os.mkdirs(路径)：用于递归的创建目录

3.  os.rmdir(目录)：删除目录，必须一层一层的删除，不支持递归。

4. os.removedirs(目录)：支持递归删除目录，某个目录下的所有文件目录全被删除

5. os.remove(文件)：删除文件

6. os.getcwd()：获取当前文件的工作路径，返回的路径不包括文件本身，只到上一级目录。

7. os.path.realth(路径/文件)：返回文件的绝对目录

   * os.path.realth(`__file__`)：输出当前文件的绝对路径

8. 拼接路径（+，join）

   * new_path = os.getcwd() + '\path'+'\python'

     os.mkdirs(new_path)

   * join，连接。new_path = os.path.join(os.getcwd(), *args)

9. os.path.isdir(路径)：判断是否为目录。os.path.isfile(路径)：判断是否为文件

10. os.path.exists(绝对路径)：判断文件/目录是否存在。

11. os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])

    - **top** -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
      - root 所指的是当前正在遍历的这个文件夹的本身的地址
      - dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
      - files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    - **topdown** --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
    - **onerror** -- 可选，需要一个 callable 对象，当 walk 需要异常时，会调用。
    - **followlinks** -- 可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，如果为 False，则优先遍历 top 的子目录。

    ```python
    import os
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
    ```

### 10、异常处理

1. try:

   ​	未报错，执行的动作语句

   except  错误类型:   				  # 错误类型可以为Exception（所有错误类型的基类）

   ​	报错，执行的动作语句								# 或者写具体的错误类型例如TypeErr或者直接不写错误类型。

   ​	

2. try:

   ​    未报错，执行的动作语句

   except：

   ​	报错，执行的动作语句

   findally:

   ​	无论报错与否，都要执行的动作语句。

   

3. try:

   ​    未报错，执行的动作语句

   except：

   ​	报错，执行的动作语句

   else:

   ​	和try下的未报错代码同步，try执行，else执行。

4. try:

   ​	未报错，执行的动作语句

   except  Exception as e:   				  

   ​	报错，执行的动作语句	

   ​	raise e   # 将错误释放出来。raise下方的代码不再执行，findally除外。

### 11、类与对象

1. 命名

   * 关键字—class

   * 类名：首字母大写，驼峰命名
   * 类：一套模板概括出这类事物拥有的共同属性和共同方法。

2. 实例

   * 类实例化：对象名 = 类名（）
   * 实例拥有类里面所有属性和方法的使用权限。调用类下的实例方法：对象名.方法名（）。调用类下的属性：对象名.属性

3. 属性

   * 同一个类中，在类下方法中调用类属性：self.属性名
   * 不同类中，不同文件(模块)调用类属性：类名.属性名

4. 方法

   类中调用属性和方法：self.属性名，self.方法名

   1. 实例方法

      实例方法必须带有self这个形参。self代表实例本身，相当于占位符。我们在通过实例调用这个方法是不需要传入这个实参，但是Python会自动将我们的对象也就是实例给传入，以此才能调用这个方法。

      ~~~python
      class Teacher():
          
      	def coding(self, a, b):
              print("***")
      Teacher().swimming(1, 2)  # 通诺实例调用实例方法
      ~~~

   2. 类方法

      类方法必须带有cls这个形参。cls代表类本身。

      ~~~python
      class Teacher():
      
      	@classmethod
      	def swimming(cls):
      		print("***")
      Teacher.swimming()  # 可以直接通过类名调用类方法。也可以通过实例调用。
      ~~~

   3. 静态方法

      静态方法就是一个普通函数。和在类外创建的函数一样。

      ~~~python
      class Teacher():
      
      	@staticmethod
      	def swimming():
      		print("***")
      Teacher.swimming()  # 可以直接通过类名调用类方法。也可以通过实例调用。
      ~~~

   4. 三者不同点

      * 三种方法均可通过实例名和类名直接调用
      * 静态方法和类方法不能调用类里的属性
      * 静态方法和类方法常用在函数和其他函数\属性没有关系时

   5. 类中的实例方法可以相互调用

      ~~~
      class Teacher():
          
      	def coding(self, a, b):
              print("***")
              
           def swimming(self):
           	self.coding('panda', 4)
      ~~~

      

5. 初始化函数`__init__`

   ~~~python
   def __init__(self, a, b):  # a,b是类在实例化时需要传入的参数
   	self.a = a  # self.a是实例变量。可以让类下的实例方法进行调用。相当于扩大了变量的作用域。
   	self.b = b
   
   ~~~

   * 初始化函数里面可以有默认值参数
   * 每个实例都自动调用初始化函数
   * 每次创建一个实例，需要传递对应的且个数一指的实参
   * 初始化函数可以有形参也可以无形参
   * 形参赋值给实例变量：self.变量名 = 形参

6. 类的继承

   父类：class  One():

   子类(继承类)：class  Two(One):

   * 子类是否需要写初始化函数，关键看父类是否已写。
   * 父类拥有的属性和方法，均可以被子类调用
   * 子类与父类具有相同的函数且函数名相同——重写。子类创建的实例优先调用子类的方法，父类创建的实例只能调用父类的方法
   * 子类中的方法在父类中不存在——拓展

   多继承

   多继承，继承多个父类，且父类之间不能有继承关系。

   class  Three(One, Two):

   * 具有两个父类的属性和方法，调用时采用就近原则

   * 若两个父类具有相同的方法名是，就近原则。One近，Two远
   * 需要注意：括号中父类中的顺序，若是父类中有相同的方法名，而在子类使用中未指定，python从左至右搜索方法。

### 12、python的内置函数

#### 1、all()函数

* all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
  元素除了是 0、空、None、False 外都算 True。

  ~~~python
  name = 'panda'
  age = None
  data = [name, age]
  if all(data) is None:
  	print("****")
  ~~~



#### 2、encode()和decode()函数

* 以指定的格式对字符串进行编码和解码，默认编码格式为“UTF-8”
* **字符串在Python内部的表示是unicode编码**，因此，在做编码转换时，通常需要以unicode作为中间编码， 即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
* **decode的作用是将其他编码的字符串转换成unicode编码**，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
* **encode的作用是将unicode编码转换成其他编码的字符串**，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
* 总得意思:想要将其他的编码转换成utf-8必须先将其解码成unicode然后重新编码成utf-8,它是以unicode为转换媒介的 如：s='中文' 如果是在utf8的文件中，该字符串就是utf8编码，如果是在gb2312的文件中，则其编码为gb2312。这种情况下，要进行编码转换，都需要先用 decode方法将其转换成unicode编码，再使用encode方法将其转换成其他编码。通常，在没有指定特定的编码方式时，都是使用的系统默认编码创建的代码文件



#### 3、isdigit()方法

- 检测字符串是否只由数字组成，如果字符串只包含数字，则返回true，否则返回false。

  **str.isdigit**()



#### 4、startswith() 方法

* 用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。

  ~~~python
  str.startswith(str, beg=0,end=len(string));
  - str -- 检测的字符串。
  - strbeg -- 可选参数用于设置字符串检测的起始位置。
  - strend -- 可选参数用于设置字符串检测的结束位置。
  ~~~



#### 5、json数据

* json.dumps 用于将 Python 对象编码成 JSON 字符串。

* json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。




### 13、Python接受文件外部传递的参数

#### 1、sys.argv列表

~~~python
# 文件demo.py
import sys

for i in sys.argv:
  print(i)

# 在终端命令行执行该文件
# python demo.py 1 3 5 6 7
# 输出：demo.py 1 3 5 6 7
~~~

* 指定参数时，使用空格隔开就可以，缺点是我们必须脚本的顺序指定参数较多不建议使用。
* sys.argv是一个列表，第一个元素为py文件本身即文件名，后续元素为命令行向文件中传输的参数



#### 2、利用argparse模块

* 位置参数

  ~~~python
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
  print(args1)  # 在命令行中输入 python argument.py 5  # 输出 5
  ~~~

  

* 可选参数（即选项参数）



~~~python
import argparse

"""argparse--可选参数， 相当于关键字传参，不必考虑顺序"""

parser2 = argparse.ArgumentParser(description='可选参数')

parser2.add_argument('--file', type=str, default='demo.txt', help='文件名')  # default,对可选参数file设定默认值为demo.txt

parser2.add_argument('--path', type=str, required=True, help='文件路径')  # 设定可选参数path为必需参数

args2 = parser2.parse_args()

print(args2.path+args2.file)  # 在命令行输入python argument.py --path=c:/workfiles/ESS/ --file=ess_data
~~~



### 14、py文件输出命令至操作系统命令行执行

* https://cloud.tencent.com/developer/article/1445388

#### 1、os.system()

执行操作系统的命令，将结果输出到屏幕，只返回命令的执行状态（0：成功，非 0 ： 失败）

~~~
import os
>>> a = os.system("df -Th")
Filesystem   Type  Size Used Avail Use% Mounted on
/dev/sda3   ext4  1.8T 436G 1.3T 26% /
>>> a
0     # 0 表示执行成功
# 执行错误的命令
>>> res = os.system("list")
sh: list: command not found
>>> res
32512    # 返回非 0 表示执行错误
~~~



#### 2、 os.popen()

将结果保存在内存当中，可以用**read()**方法读取出来

~~~
>>> import os
>>> s = os.popen('ls -l')
>>> print(s)
<os._wrap_close object at 0x7ff7b3c7d5f8>
>>> s.read()
'total 8\n-rw-------. 1 root root 1962 Feb 10 22:48 anaconda-ks.cfg\ndrwxr-xr-x. 2 root root    6 Feb 10 22:51 Desktop\ndrwxr-xr-x. 2 root root    6 Feb 10 22:51 Documents\ndrwxr-xr-x. 2 root root    6 Feb 10 22:51 Downloads\n-rw-r--r--. 1 root root 2010 Feb 10 22:49 initial-setup-ks.cfg\ndrwxr-xr-x. 2 root root    6 Feb 10 22:51 Music\ndrwxr-xr-x. 2 root root    6 Feb 10 22:51 Pictures\ndrwxr-xr-x. 2 root root    6 Feb 10 22:51 Public\ndrwxr-xr-x. 2 root root    6 Feb 10 22:51 Templates\ndrwxr-xr-x. 2 root root    6 Feb 10 22:51 Videos\n'

~~~



#### 3、subprocess.run()

~~~
>>> subprocess.run(["ls", "-l", "/dev/null"])
crw-rw-rw-  1 root  wheel    3,   2  5  4 13:34 /dev/null
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0)
~~~



### 15、pip安装第三方库

#### pip命令常见操作

~~~python
pip install XXX #安装包

pip install XXX==2.2.3 #指定安装包的版本

pip install --upgrade XXX  #更新包

pip uninstall XXX  #卸载包

pip install XXX -i http://pypi.douban.com/simple/   # 指定源

python -m pip install --upgrade pip  # 升级pip命令
~~~



#### 离线安装库

#### 1.pip离线更新安装

1. 在python第三方库官网，将pip的离线安装包*.whl下载到本地，保存在python.exe的目录下
2. 在此目录下执行cmd命令：python -m pip install --upgrade xxx(pip轮子的文件名) 。完成安装

#### 2、离线安装第三方库

1. 将第三方库的离线安装包*whl保存至python的lib目录
2. 命令行窗口用cd命令跳转到whl文件所在目录，然后使用命令python -m pip install ***.whl即可完成whl文件的安装。
   1. 或者在whl文件所在目录执行python setup install *.whl  



## 二、接口

### 1、基础

#### 1.协议

* 接口的本质：传递数据的通道

* 接口分为：内部接口，外部接口
* 按照不同的协议分为：http接口，webservice接口，dubbo接口，socket接口
* 接口与接口之间的协议必须保持一致，否则无法通信
* http请求分为：get（从服务端获取资源）、pos（用于创建资源，提交表单data、提交请求体body-json）、delete（用于删除资源）、put（用于整体更新资源）、head、option

#### 2.请求

一个http request（请求）是指从客户端到服务端的消息。

包括：请求地址、请求方法、http协议版本、请求头、请求参数（请求正文）

get请求的请求参数存在于URL中，“？”后面为参数，&为参数之间的分隔符。

#### 3.返回码

200：正常，状态码200不一定代表操作成功

302：重定向，请求的资源文档已被迁移的别处

304：未修改，客户端的缓存是最新的，客户端应该继续使用它

403：禁止，服务器理解请求，但禁止处理（一般为权限不够）

404：未找到资源，服务器上没有客户端请求的资源

500：内部服务器错误

503：服务器当前不处理

504：超时

#### 4.cookie、session、token、key

1. cookie

   客户端，存储一些用的数据，比如浏览记录

   cookie是登陆成功后获得的，登录失败是没有cookie的

   cookie ！=（不等于）缓存cache，cache包括cookie

   会员卡机制：session_id存在于cookie中，每次请求，cookie中的所有信息都会传递到服务器，服务器通过session_id来判断是否为同一用户

2. session

   服务端，记录用户的请求状态。一般默认时间30min过期。是变化的。

3. token 鉴权

   服务端发给客户端，每次请求再发给服务端验证。变化的。

   用来判断访问的接口是否正常、是否非法访问、是否绕过前端

4. key 授权

   一般key唯一的、全局的、动态的、具备一定的特征。

   用来判断是否具有访问接口的权限。

5. http

   http响应正文（报文）格式：html（标签）、xml（标签）、json等

   请求头与响应头后面的空行是必须的。

### 2、requests简介

* 官方文档：https://docs.python-requests.org/zh_CN/latest/
* Requests是Python语言的第三方的库，专门用于发送HTTP请求。
* Requests支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动响应内容的编码，支持国际化的URL和POST数据自动编码。
* Requests会自动实现持久连接keep-alive，现代，国际化，友好。

#### 1、7个主要方法

**request**
**requests.request(method, url, \**kwargs)**：构造一个请求，支撑以下各方法的基础方法。
**method** ：请求方式，对应get/post等
**url** ：网页链接
***\*kwargs** ：关键字参数，可选，共13个



**get**
**requests.get(url, params, \**kwargs)**：从指定的资源请求数据，是获取HTML网页信息的主要方法，对应HTTP的GET。
**params** ：字典或字节序列格式，将作为参数增加到url中，可选



**post**
**requests.post(url, data, json, \**kwargs)**：向指定的资源提交要被处理的数据，对应HTTP的POST。
**data ：**data参数的对象一般是字典类型，在发出请求时会自动编码为表单形式
**json ：**json参数会自动将字典类型的对象转换为json格式



**head**
**requests.head(url, \**kwargs)**：获取HTML网页头部信息的方法，对应HTTP的HEAD。



**put**
**requests.put(url, data, \**kwargs)**：向HTML网页提交PUT请求的方法，对应HTTP的PUT。



**patch**
**requests.patch(url, data, \**kwargs)**：向HTML网页提交局部修改请求，对应于HTTP的PATCH。



**delete**
**requests.delete(url, \**kwargs)**：向HTML页面提交删除指定资源的请求，对应HTTP的DELETE。



#### 2、13个关键字参数

**kwargs：控制访问的参数，均为可选项。

**1. params**
字典或字节序列格式，将作为参数增加到url中。

![img](Python自动化.assets/v2-9625f3b5ca324a3c7afb42bf22ad544e_720w.jpg)


**2. data**

data参数的对象一般是字典类型，在发出请求时会自动编码为表单形式。也可以是字节序列或文件对象，作为Request的内容。

![img](Python自动化.assets/v2-7380e5b4e2a5292ccc684aa3dc3db174_720w-16414492773804.jpg)


**3. json**
JSON格式的数据，作为Request的内容。json参数会**自动**将字典类型的对象转换为json格式。

![img](Python自动化.assets/v2-f7f6f1f991d6971217b37010991f61b8_720w-16414492773806.jpg)


**4. headers**
字典格式，为请求添加 HTTP 头部信息，模拟浏览器进行访问。headers是解决requests请求反爬的方法之一。 headers中有很多内容，常用的是user-agent 和 host。

![img](Python自动化.assets/v2-e38ff9c5ced54cdb451def61a345e813_720w.jpg)


**5. cookies**
cookies参数为字典格式的数据或CookieJar
**什么是cookie？**
当用户通过浏览器首次访问一个域名时，访问的web服务器会给客户端发送数据，这些数据就是cookie，它是为了辨别用户身份而储存在用户本地终端上的数据。cookie大部分都是加密的，cookie存在于缓存中或者硬盘中，在硬盘中的是一些文本文件，当访问该网站时，就会读取对应的网站的cookie信息。一般来说，一旦将cookie保存在计算机上，则只有创建该cookie的网站才能读取它。

![img](Python自动化.assets/v2-894ea0003172738bd5ae50a6be1271ca_720w.jpg)


**6. auth**
身份验证。将用户名和密码以元组形式传递给auth参数时，rqeuests 将使用HTTP的认证功能来应用凭据。

![img](Python自动化.assets/v2-5d64266cb16a4095e8ee3adf3acf79ac_720w.jpg)


**7. files**
传输文件。支持在一个请求中发送多个文件。

![img](Python自动化.assets/v2-23a87d61989c244d786004b9c22a43c5_720w.jpg)


**8. timeout**
用于解决请求超时的问题。以秒为单位限制请求时间，如果服务器在设定的请求时间内没有应答，将引发一个异常。

**9. proxies**
字典类型，设定访问代理服务器，可以增加登陆认证。

![img](Python自动化.assets/v2-212d2cf4d334d3429d69f9cc21d8e0d8_720w.jpg)


**10. allow_redirects**
重定向开关：True / False。默认为True，允许重定向；False禁止重定向。

![img](Python自动化.assets/v2-f33a37a2c462935529ea5f437d132c7d_720w.png)

**11. stream**
获取内容立即下载开关：True / False，默认为True。

**12. verify**
请求验证SSL证书开关：True / False，默认为True。

**13）cert**
本地SSL证书路径。用于指定一个本地有效安全证书作为客户端证书。

![img](Python自动化.assets/v2-59c3441b73afef94069cedc64789bd24_720w.jpg)



#### 3、响应对象的5种属性

**① r.status_code**
HTTP请求的返回状态，200为正常，404为错误。

**② r.raw**
HTTP响应内容的原始形式。

**③ r.text**
HTTP响应内容的字符串形式，即url对应的页面内容。获取文本一般使用 r.text。

**④ r.content**
HTTP响应内容的字节形式（二进制形式 ）。获取图片或文件一般使用 r.content。

**⑤ r.encoding**
HTTP响应正文的编码，它的值可能是从HTTP响应头部或正文中解析出来的。
当解析的编码方式不准确时，可以手动指定一种编码方式。如，r.encoding = ' utf-8 ' 。





### 3、requests实战

#### 1.requests模块之get请求

1. get请求参数解析。   requests.get(url, params=None, **kwargs)

   * url：请求url地址
   * params：请求参数
   * headers：请求头(在kwargs中)

2. 简单使用

   - 获取响应状态码: res.status_code
   -  获取响应消息: res.content
   -  获取请求头: res.request.headers
   -  获取响应头: res.headers
   -  获取响应数据 res.text。响应结果一般有三种格式：html、json、text；

   - 获取cookie res.cookies。cookie是一种类字典的数据格式，若想打印字典的值，可以根据key；

   -  res.json()：如果返回结果是json格式，可以把响应结果利用json()来进行解析;


#### 2.requests模块之post请求

1. post请求参数解析。requests.post(url, data=None, json=None, **kwargs)

   * url，必填
   * data，选填，请求参数
   * json，选填，请求参数
   * kwargs，选填关键字参数，可以传入headers、cookies等
2. 请求参数，data和json的区别

   * 不管是json是str还是dict，如果不指定 headers中的content-type，默认为application/json
   * data为dict时，如果不指定content-type，默认为applicaton/x-www-form-urlencoded，相当于普通form表单的形式
   * data为str时，如果不指定content-type，默认为application/json
3. post请求参数到底是传data还是json，这时候我们要看请求头里的content-type类型

   1. 如果请求头中content-type为application/json,  为json形式，post请求使用json参数。
   2. 如果请求头中content-type为application/x-www-form-urlencoded，为表单形式，post请求时使用使用data参数。
   3. 如果请求类型为application/json，我偏要传入data参数呢？

      * 清楚中传入请求头，header = {"content-type":"application/json"}
   4. 请求头中的content-type和响应头中的content-type有什么区别：
      * 请求头中 (如POST 或 PUT)，Content-Type字段用于客户端告诉服务器实际发送的数据类型
      * 响应头中，浏览器会根据 Content-Type 判断响应体的资源类型，然后根据不同文件类型做出不同的展示
* 需要将字典类型数据转换为json字符串。



#### 3.requests模块之session请求

1. 作用以及应用场景
   * requests.session的作用：自动处理cookie，即 **下一次请求会带上前一次的cookie**
   * requests.session的应用场景：自动处理连续的多次请求过程中产生的cookie

2. requests.session使用方法

   * session实例在请求了一个网站后，对方服务器设置在本地的cookie会保存在session中，下一次再使用session请求对方服务器的时候，会带上前一次的cookie

   * session对象发送get或post请求的参数，与requests模块发送请求的参数完全一致

     ~~~python
     session = requests.session() # 实例化session对象
     response = session.get(url, headers, ...)
     response = session.post(url, data, ...)
     ~~~

     

#### 4.cookie和session的应用

* HTTP 协议是一种无状态协议，即每次服务端接收到客户端的请求时，都是一个全新的请求，服务器并不知道客户端的历史请求记录；Session 和 Cookie 的主要目的就是为了弥补 HTTP 的无状态特性。

1. cookie

   * cookie是服务器发送到用户浏览器并保存在本地（客户端）的一小块数据，它会在浏览器下次向同一服务器再发起请求时被携带并发送到服务器上。通常，它用于告知服务端两个请求是否来自同一浏览器，如保持用户的登录状态。

   1. cookie的应用

      ~~~python
      import requests
      
      # 登录接口
      url = 'http://127.0.0.1:8000/user/login'
      payload = {
          "mobilephone":"1530272****",
          "pwd":"123456"
      }
      login_res = requests.post(url,data=payload)
      print(login_res.json())
      # 获取响应结果的cookies
      cookies = login_res.cookies
      print(cookies)
      
      # 充值接口
      url = 'http://127.0.0.1:8000/recharge'
      payload = {
          "mobilephone":"1530272****",
          "amount":100
      }
      # 充值接口请求时携带cookies
      recharge_res = requests.post(url,data=payload,cookies=cookies)
      print(recharge_res.json())
      ~~~

      

2. session

   * Session是存放在服务器端、用来存放用户数据的（类似于HashTable结构）。
   * 当浏览器第一次发送请求时，服务器自动生成了一个HashTable和一个Session ID用来唯一标识这个HashTable，并将其通过响应发送到浏览器。
   * 当浏览器第二次发送请求，会将前一次服务器响应中的Session ID放在请求中一并发送到服务器上，服务器从请求中提取出Session ID，并和保存的所有Session ID进行对比，找到这个用户对应的HashTable，以此来达到共享数据的目的。

   1. session的应用

      ~~~python
      import requests
      
      # 登录接口
      url = 'http://127.0.0.1:8000/user/login'
      payload = {
          "mobilephone":"1530272****",
          "pwd":"123456"
      }
      # 创建session会话管理
      session = requests.session()
      login_res = session.post(url,data=payload)
      print(login_res.json())
      
      # 充值接口
      url = 'http://127.0.0.1:8000/recharge'
      payload = {
          "mobilephone":"1530272****",
          "amount":100
      }
      recharge_res = session.post(url,data=payload)
      print(recharge_res.json())
      ~~~

      



#### 5.Token

1. token的作用

   为了验证用户登录情况以及减轻服务器的压力，减少频繁的查询数据库，使服务器更加健壮。

2. 什么是token

   Token是服务端生成的一串字符串，以作客户端进行请求的一个令牌，当第一次登录后，服务器生成一个Token便将此Token返回给客户端，以后客户端只需带上这个Token前来请求数据即可，无需再次带上用户名和密码。

3. Token和 Cookie、Session 的选型

   对于只需要登录用户并访问存储在站点数据库中的一些信息的中小型网站来说，Session Cookies 通常就能满足。如果有企业级站点，应用程序或附近的站点，并且需要处理大量的请求，尤其是第三方或很多第三方（包括位于不同域的API），则 token显然更适合。

4. token的获取与使用

   1. 访问登录接口，获取token

      ~~~python
      import requests
      url = 'http://127.0.0.1:8000/user/login/'
      payload = {
          "username":"vivi",
          "password":"123456"
      }
      login_res = requests.post(url,json=payload)
      # 从响应结果中获取token值
      token = login_res.json()["token"]
      print("token:", token)
      ~~~

   2. 项目列表携带token访问

      * token前面加一个前缀，然后将token加在请求头里发起请求

        ~~~python
        mport requests
        url = 'http://127.0.0.1:8000/projects/'
        # 拼接最终的token，注意中间有个空格
        token = "Bearer" + " " + token
        headers={
            "authorization": token
        }
        pro_res = requests.get(url,headers=headers)
        print(pro_res.json())
        ~~~

   3. 通过前端返回的html页面获取token

      ~~~python
      import requests
      from lxml import etree
      res = requests.get('http://www.baidu.com/')
      html = etree.HTML(res.text)
      token = html.xpath('//input[@name="crsf_token"]')[0].get('value')
      print(token)
      ~~~

      




#### 6.获取接口响应时间

elapsed里面几个方法介绍

- total_seconds 总时长，单位秒
- days 以天为单位
- microseconds (>= 0 and less than 1 second) 获取微秒部分，大于0小于1秒
- seconds Number of seconds (>= 0 and less than 1 day) 秒，大于0小于1天
- max = datetime.timedelta(999999999, 86399, 999999) 最大时间
- min = datetime.timedelta(-999999999) 最小时间
- resolution = datetime.timedelta(0, 0, 1) 最小时间单位



~~~python
import requests
res = requests.get("http://www.baidu.com")
print(res.elapsed)
print(res.elapsed.total_seconds())  # 单位为s，最常用的记录返回时间
print(res.elapsed.microseconds)  # 单位微秒ms，当响应时间大于1s时，只截取返回微秒部分
print(res.elapsed.seconds)  # 单位s，响应时间小于1s时，为0
print(res.elapsed.days)
print(res.elapsed.max)
print(res.elapsed.min)
print(res.elapsed.resolution)

# 响应时间输出结果
0:00:00.055914
0.055914
55914
0
0
999999999 days, 23:59:59.999999
-999999999 days, 0:00:00
0:00:00.000001
~~~



#### 7.实现文件的上传下载

* 文件的上传下载都是以二进制的方式打开文件的，**b**

* 上传

  支持在一个请求中发送多个文件。

  ~~~python
  files = {'file':open('D:\\test_data\\summer_test_data_05.txt','rb')}  # 我们操作文件上传的时候，把目标文件以open二进制的方式打开，然后存储到变量file里面存到一个字典里面
  upload_data = {"parentId":"","fileCategory":"personal","fileSize":179,"fileName":"summer_text_0920.txt","uoType":1}
  upload_res = requests.post(url='www.baidu.com',data=upload_data,files=files)  # 将变量files传递给关键字参数files
  ~~~

  



* 下载

  ~~~python
  # 小文件直接下载写入
  import requests 
  
  url = 'http://***/test/demo.zip' 
  res = requests.get(url) 
  with open("demo3.zip", "wb") as code:
  	code.write(res.content)
  ~~~

  

#### 8.HTTP设置短链接、长连接

* HTTP的长连接和短连接本质上是**TCP的长连接和短连接**

* HTTP长连接的优点：

  　　1）通过开启和关闭更少的TCP连接，节约CPU时间和内存。

    　　2）通过减少TCP开启和关闭引起的包的数目，降低网络阻塞

* HTTP长连接的缺点：

  ​    服务器维护一个长连接会增加开销。

* HTTP短连接的优点：

  ​	服务器不用为每个客户端连接分配内存来记忆大量状态，也不用在客户端失去连接时去清理内存，节省服务器端资源，以更高效地去处理业务。

* HTTP短连接的缺点：

  　如果客户请求频繁，将在TCP的建立和关闭操作上浪费时间和带宽。

~~~python
header = {'Connection':'close'}  # 设置HTTP短链接

header = {'Connection':'keep-alive'}  # 设置HTTP长连接，有过期时间

header = {'Connection':'keep-alive', 'Keep-Alive':timeout=60}  # 设置HTTP长连接，无过期时间

~~~



9.HTTPS请求

* 一搬发起https请求会报安全警告

  ~~~
  # 禁用安全请求警告
  import requests
  
  from requests.packages.urllib3.exceptions import InsecureRequestWarning
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  
  
  ~~~

  





## 三、单元测试

### 1、unittest框架

1. 概述

   TestCase()——编写测试用例模块需要继承，TestSuite()——测试用例容器，TestLoader()——测试用例加载器，TextTestRunner()——测试用例执行器，初级测试报告。assert——断言比对实际结果。HTMLTestRunnerNew()第三方生成html测试报告的测试用例执行器

2. 编写测试用例

   * 测试用例类必须继承unittest.TestCase()类。
   * 一条用例就是一个函数，每个用例名/方法名必须以"test_"开头。
   * 每个测试用例不能有任何参数，只有一个self

3. 测试用例执行前环境准备和执行完成后环境清理

   * def setUp(self)——初始化环境，该测试类下的每一条测试用例执行前，先自动执行这个函数
   * def tearDown(self)——清理环境，该测试类下的每一条测试用例执行完成后，自动执行这个函数
   * def setUpClass(cls)——整个测试用例类执行前执行一次这个函数。必须用@classmethod装饰
   * def tearDownClass(cls)——整个测试用例类执行结束后执行一次这个函数。必须用@classmethod装饰

4. 加载测试用例

   * 有三种方式可以往测试用例容器里添加用例
     * 逐条添加测试用例，一条测试用例添加一次
     * 根据测试用例类来添加测试用例
     * 根据测试用例文件（模块）添加测试用例

5. 执行测试用例

   * 执行测试用例的时候，unittest是根据测试用例名称的ASCII码排序来执行的。
   * 如果想固定测试用例的执行顺序，可以在测试用例名定位test_0\*\*，test_1\*\*

6. 断言assert

   * 用于判断用例是否执行通过，编写在测试用例中。self.asserEqual（first, second,msg=None）

     * fist——期望值，second——实际结果，msg——用例执行失败触发

   * 断言语法

     | 语法                  | 释义              |
     | --------------------- | ----------------- |
     | self.assertEqual(a,b) | 判断a,b是否相等   |
     | assertTrue(x)         | 判断x是否为真     |
     | assertFalse(x)        | 判断x是否为假     |
     | assertisNotNone(x)    | 判断x是否不为空   |
     | assertisNone(x)       | 判断x是否为空     |
     | assertNotEqual(x)     | 判断a,b是否不相等 |
     | assertin(a,b)         | 判断a是否属于b    |
     | assertNotin(a,b)      | 判断a是否不属于b  |

   * 断言时经常需要进行异常处理

     ~~~python
     try:
     	self.assertEqual(1,n,'断言失败')
     excep AssertionError as e:
     	print('断言失败')
     	raise e  # 当在异常处理时，若报错，必须将异常抛出，否则无论断言是否成功都不会通过
     ~~~

     

## 四、数据处理

### 1.测试用例之间相互依赖

例如：第二条测试用例需要用到第一条测试用例的结果，返回报文等

* 将第一条测试用例写在setUp函数中
* 将第一条测试用例的执行结果保存在全局变量中
* 利用反射，创建一个反射类，将第一条测试用例的执行结果保存在反射类中

### 2.测试用例的参数化

#### 1.超继承父类TestCase的`__init__`方法

~~~python
class TestHttp(unittest.TestCase):
    def __init__(self,methodName,url,method,data,expected):
        super(TestHttp,self).__init__(methodName) #利用超继承从而进行参数化
        self.url=url
        self.method=method
        self.data=data
        self.expected=expected
    def test_api(self): #测试用例本身不能传入参数
        res=HttpRequest().http_request(self.url, self.method, self.data,getattr(GetData,'cookie'))
       
~~~

#### 2.ddt装饰器装饰测试用例

1. ddt模块包括三个部分：ddt，data，unpack
   * ddt——测试类的装饰器
   * data（*args）——测试用例函数的装饰器。拿到几组数据就执行几次用例。
   * unpack——针对data拿到的每组数据再根据“，”进行拆分，并且必须在测试用例函数除出入同等个数的参数。

### 3.openpyxl处理Excel模块

​	form openpyxl import load_workbook

​	注意：Excel中的数据除数值为int或float类型外，其他数据结构读取出来都变成了str类型。可以利用eval()函数将读取出来的数据还原成字典、列表、元组等原结构。

* 打开Excel文件，wb=load_workbook('file_name')
* sheets = wb.get_sheet_names()，返回Excel文件中所有的sheet表单名，存储在列表中返回
* 定位到某个sheet表单， ws=wb['sheet_name']或者wb.get_sheet_by_name('sheet表单名')
* 定位到某个单元格，ws.cell(行，列)。注意行、列的索引是从1开始的。1即第一行或第一列。
* 取值，result=ws.cell(行，列).value。
* 行数，ws.max_row。列数，ws.max_column。



### 4、ddt+unittest+excel

* 在利用ddt修饰测试用例之后，在往容器里加载测试用例时必须通过loader加载用例方法进行。一条一条的添加用例的方式不可行。



### 5、configparser模块处理配置文件

* 以properties、ini、config结尾的均为配置文件	

* 配置文件分为三部分：section、option、value。注意：section在配置文件中必须以**大写形式，且用[section]中括号包围**

  ~~~python
  from configparser import Configparser
  cf = Configparser()
  cf.read('file_name', encoding='utf-8')
  cf.get(section, option)  # 获取option的value
  cf[section][option]  # 获取option的value
  cf.sections()  # 获取文件中的所有section
  cf.items(section)  # 获取section下的所有option、value。类字典格式
  cf.options(section)  # 获取section下所有的option，返回列表格式
  ~~~

  

### 6、pyMsql模块处理MySQL数据库

```python
import pymysql
#建立数据库连接
db = pymysql.connect(host="数据库地址",
                     user="用户名",
                     password="密码",
                     port=3306,# 端口
                     database="数据库名",
                     charset='utf-8')

cursor = db.cursor()  # 创建游标

query_sql='select * from emp'
cursor.execute(query_sql)  # 执行query_sql的sql语句

res=cursor.fetchall()  # 使用fetchall() 方法获取多条数据。
res=cursor.fetchone()# Python查询Mysql使用 fetchone() 方法获取单条数据

db.commit()  # 提交事务

cursor.close()  # 关闭游标

db.close()  # 关闭数据库连接

```



### 

# UI自动化

## 一、web基础

### 1、web页面组成

* web页面由三部分组成：html、css、JavaScript
  * html：定义页面呈现的内容
  * css：层叠样式表，控制网页如何展示、页面布局等，比如：字体颜色、大小、
  * JavaScript：对网页做一些动态的设置，希望网页依据不同的情形做不同的事情。

### 2、HTML

* HTML是一种超文本标记语言，具体知识学习http://www.sz-seo.org/w3cschool/html/index.html
* HTML独立于平台和编程语言
* HTML是一个树形结构

### 3、DOM对象

* DOM是一套web标准，Document Object Mode。定义访问HTML文档的一套属性、方法、和事件
* DOM对象本质：网页和脚本语言沟通的桥梁。脚本语言通过DOM对象来访问HTML页面，改文档的结构和内容
* 当浏览器载入HTML文档后，它就会成为document对象。document对象也是一个树形结构。

#### 1、DOM对象查找元素

* 通过元素的id属性：document.getElementById(id值)
* 通过元素的class属性：document.getElementsByClassName(类值)
* 通过元素的标签名：document.getElementsByTagName(标签名)
* 通过元素的Name属性：document.getElementsByName(name属性值)

#### 2、DOM对象对元素操作

* DOM对象通过查找元素定位以后，可以对元素进行操作

1. 改变元素属性：

   document.getElementById('78').属性名="新值"

   document.getElementsByClassName('ment').属性名="新值"

2. 获取属性

   document.getElementBy***("  ").getAttribute("属性名")

3. 移除属性

   document.getElementBy***("  ").removeAttribute("属性名")

4. 改变元素内容

   1. 包含HTML元素标签即有后代的情况

      document.getElementBy***("  ").innerHTML = newHTML。（将原定位的元素内容替换为新的页面newHTML）

   2. 不含HTML元素标签即没有后代的情况，直接改变文本的内容

      document.getElementBy***("  ").innerText = newText。（将新文本赋值改变文本原来内容）

      注意：有时文本内容不存储在innerText属性中，而是存储在value属性中

5. 改变样式css

   document.getElementBy***("  ").style.样式名 = 新的样式值

   实例：document.getElementBy***("  ").style.visibility = ’hidden’

6. 事件

   * 浏览器和用户事件，触发之后执行js代码带来不同的页面响应。

   1. 页面加载完成事件（一般写在最后）

      ~~~
      window.load = function(){
      	alert('everything is ready')
      }
      ~~~

      

   2. 点击事件

      ~~~
      document.getElementBy***("  ").onlick=function(){
      	,,,,,,,
      }
      ~~~

      

   3. 鼠标悬停事件

      ~~~
      document.getElementBy***("  ").onmouse=function(){
      	,,,,,,,
      }
      ~~~

      

   4. 鼠标离开事件

      ~~~
      document.getElementBy***("  ").onmouseout=function(){
      	,,,,,,,
      }
      ~~~

      



### 4、JavaScript





## 二、selenium

### 1、常见driver操作

* 启动浏览器开启会话：driver = webdiriver.Chrome('驱动地址')
* 访问网页：driver.get('http://www.baidu.com')
* 结束会话，关闭浏览器：driver.quit()，彻底杀死进程
* 关闭打开的浏览器窗口：driver.close()，注意此举并没有杀死进程
* 窗口最大化：dirver.maximize_window()
* 设置窗口的大小：driver.set_window_size(self, width, height, windowHandle='current')
* 回退上一页：driver.back()
* 回到上一页，前进：dirver.forward()
* 刷新：driver.refresh()
* 获取标题：driver.title
* 获取网址：driver.current_url
* 窗口句柄：driver.current_window_handle

### 2、元素定位

* 元素定位成功后，可以获取元素的属性，或者进行实践操作
* find_element_by_id/xpath（元素定位表达式）等方法底层是find_element（定位类型，定位表达式）



#### 1、常见定位方式

* 注意下面的driver.find_element**s**\***方法用来匹配多个符合定位表达式的元素，最终返回一个匹配的webelement对象列表。

  1. 通过属性id定位

     ele=driver.find_element_by_id('id属性值')；元素定位成功后返回的ele是一个webElement对象

     ele.get_attribute('class')；获取属性值

  2. 通过class定位

     * 当class属性有多个值是，只能选一个值作为实参，入参

     driver.find_elements_by_class_name('class属性值')

     driver.find_element_by_class_name('class属性值')

     3. 通过name属性

     driver.find_elements_by_name('name属性值')

     driver.find_elements_by_name('name属性值')

     4. 通过tagname标签名

     driver.find_elements_by_tag_name('标签名')

     driver.find_elements_by_tag_name('标签名')

     5. 通过链接a的文本内容

     driver.find_elements_by_link_text('文本内容')；通过文本的全部内容定位。

     driver.find_elements_by_partial_link_text('部分文本内容')；通过文本的部分内容定位。

#### 2、万能定位方式Xpath

* 在UI界面，F12后Ctrl+F，输入xpath定位表达式辅助定位即可。
* driver.find_element_by_xpath(xpath表达式)

1. 相对定位的xpath表达式

   * 以"//"开头，不依赖页面的顺序和位置，只看整个页面有没有符合表达式的元素
   * 绝对定位：以**/**开头，非常依赖页面位置和顺序

   ~~~python
   //标签名[@属性=‘值’]  # 单个属性定位
   //标签名[@属性=‘值’ and @属性=‘值’]  # 通过多个属性定位
   //标签名[@属性=‘值’ or @属性=‘值’]
   
   ~~~

   

2. 层级定位的xpath表达式

   ~~~python
   //标签名[@属性名=‘值’]//标签名[@属性名=‘值’]
   ~~~

   

3. 通过text（）函数进行文本定位

   ~~~python
   //标签名[text()=“文本内容”]  # 此处的文本内容必须用双引号括起来
   //标签名[@属性名=‘值’]//标签名[text()="sjdfj"]
   ~~~

   

4. 通过contains（）函数进行部分文本、部分属性值进行元素定位

   * contains(@属性，’值‘)
   * contains(text(), “值”)

   ~~~python
   //input[contains(@class,'username') and @id='32']//*[@id='99']	
   ~~~

5. 模糊定位

   ~~~python
   //标签名[starts-with(@属性名，‘属性值’)]  # 以。。。开始的元素
   //标签名[ends-with(@属性名，‘属性值’)]  # 以。。。结束的元素
   ~~~

   

#### 3、轴定位

| 轴名称            | 描述                                       |
| ----------------- | ------------------------------------------ |
| ancestor          | 祖先节点                                   |
| parent            | 父节点                                     |
| child             | 子节点                                     |
| preceding         | 当前元素节点标签之前的所有节点             |
| preceding-sibling | 当前元素节点标签之前的所有兄弟（同级）节点 |
| following         | 当前元素节点标签之后的所有节点             |
| following-sibling | 当前元素节点标签之后的所有兄弟（同级）节点 |

* 轴定位语法

  ~~~
  /轴名称：：节点名称[@属性=’值‘]  # 绝对定位方式。节点名称即标签名
  //span[text()="python"]/ancestor::a/following-sibling::div//a
  ~~~


#### 4、特殊元素的定位

* web界面有一种情况，弹窗一闪而过，出现很短时间，然后就消失。如何定位：

  F12，选择sources工具，弹窗元素出现后，立即点击暂停pause。然后进入Elements定位元素。



### 3、元素等待

#### 1、强制等待

* 利用time.sleep（）模块

#### 2、隐性等待

* 利用implicitly_wait（时间）
* 设置最长元素等待最长时间，在这个时间内加载完成，则执行下一步。
* 整个driver的会话周期内，设置一次即可，全局通用。

#### 3、显性等待

* 利用webDriverwait类（显性等待类）、expected_conditons类（期望条件类）、By类（元素定位类型类）组合实现

* 明确等到某个条件满足之后再执行下一步操作

* 程序每隔**秒查看一下，如果条件成立，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出“TimeOutException"

  webDriverWait(driver，最长等待时长，轮训周期).until（成立条件）/until_not(否定条件)

  expected_conditons类提供了一系列期望发生的条件：

  ​	presence_of_element_located：元素存在

  ​	visibility_of_element_located：元素可见

  ​	element_to_bi_clickable：元素可点击

* WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((定位类型, 定位表达式)))

* 实例

  ~~~python
  from selenium import webdriver
  from selenium.webdriver.support.wait import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  from selenium.webdriver.common.by import By
  
  driver = webdriver.Chrome()
  WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, 'id属性值')))  # 定位表达式必须以元组格式传入。
  ~~~


### 4、iframe切换

* 当对html页面进行元素操作时，如果操作元素为iframe元素（另一个HTML页面）下，注意需要先切换至iframe下。
  * 先找到要切换的iframe
  * 再切换
  * 再定位元素

#### 1、iframe切换方法一

* 切换iframe代表进入另一个HTML页面
  * driver.swith_to.frame(name的属性值)
  * driver.swith_to.frame(索引值-从1开始计算)
  * driver.swith_to.frame(通过元素定位表达式定位返回的**webelement对象**)

#### 2、iframe切换方法二

* 通过元素显性等待至iframe元素出现，然后同时切换过去

  ~~~python
  from selenium.webdriver.support import expected_conditions as EC
  
  WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it((定位类型, '定位表达式')))
  
  ~~~

#### 3、iframe其他操作

* 从iframe页面切换默认页面（访问网页默认加载的页面）

  driver.switch_to.default_content()

* iframe页面只能一级一级的切换

* html页面切换至上一级页面

  driver.switch_to.parent_content()



### 5、窗口切换

* 思路
  * 目前有多少窗口打开
  * 窗口句柄是什么
  * 找到句柄切换过去

* 最新打开的窗口，句柄在返回的列表最后
* 显性等待新的窗口出现
  * WebDriverWait(driver, 10, 0.5).until(EC.new_window_is_opened(入参为未打开新窗口之前的句柄数))

#### 1、获取窗口句柄

~~~python
handles = dirver.window_handles  # 获取目前窗口总数，返回一个句柄列表
hanle = driver.current_window_hanle  # 获取当前窗口的句柄
~~~



### 6、Alert弹框

* alert不是html元素
* 弹出框分两种
  * 页面弹出框：等待弹出框出现后，再去定位弹框，然后在操作弹框元素
  * Windows弹出框（alert弹框）

#### 1、切换至弹框

* driver.switch_to.alert

#### 2、操作弹框

* alert类提供了弹框的操作方法

  * dismiss（）：点击否，拒绝
  * accept（）：点击是，接受
  * text（）：获取弹框内的内容
  * send_keys（）：往弹框内输入内容

* 显性等待弹框出现

  * WebDriverWait(driver, 10, 0.5).until(EC.alert_is_present（）)。这注意alert的等待条件不需要输入参数

* 实例

  ~~~python
  driver = webdriver.Chrome()
  driver.get('网址')
  WebDriverWait(driver, 10, 0.5).until(EC.alert_is_present（）)  # 显性等待弹框出现
  alert = driver.switch_to.alert  # 切换至弹框
  alert.accept()  # 相当于鼠标点击弹框“是”
  
  ~~~

  

### 7、常见元素操作

* 针对元素定位成功后的后续常见操作
* 当对鼠标操作传入一个webelement对象参数时，则会在该对象处进行操作，不传入参数时，则在鼠标当前位置进行操作。
  * 模拟鼠标点击：click（）
  * 往文本框发送文本：send_keys（）
  * 清空文本框信息：clear（）
  * 提交表单/模拟回车：submit（）

* webelement对象的四个基本操作
  * driver.find_element_by_xpath(“***“).click()
  * driver.find_element_by_xpath(“***“).send_keys('文本信息')
  * driver.find_element_by_xpath(“***“).text()  # 获取文本信息
  * driver.find_element_by_xpath(“***“).get_attribute('属性名')

### 8、鼠标操作

* 由selenium的ActionChains类来完成模拟鼠标操作
  * from selenium.webdriver.common.action_chains import ActionChains
* 流程
  * 以列表形式存储鼠标操作
  * 利用perform（）执行操作

#### 1、ActionChains类支持的操作

​	double_click()——双击；context_click（）——右击；drag_and_drop（）——拖拽，相当于鼠标左键按住然后拖动到另一区域释放；mover_to_element（）——鼠标悬停；。。。。。。





### 9、下拉框操作

* 操作下拉框两种方案
  * 先通过文本内容定位，然后操作
  * 先获取所有下列表值，再利用for循环匹配，操作

#### 1、select类

* select类是专用于处理select/option 标签下拉框
  * from selenium.webdriver.support.ui  improt select
* 如何通过select类定位下拉框中的元素？
  * 通过下表选择：select_by_index(索引值-从0开始计算)
  * 通过value属性：select_by_value(value属性值)
  * 通过文本内容：select_by_visible_text(文本内容)



### 10、键盘操作

* 通过Keys类和send_keys（）来实现模拟键盘操作
  * from selenium.webdriver.common.keys import Keys
* 键盘也可以利用pywin32来实现模拟

#### 1、组合键

* Keys.CONTROL相当于ctrl键

​	复制：send_keys（Keys.CONTROL，"c"）

​	全选：send_keys（Keys.CONTROL，"a"）

​	剪切：send_keys（Keys.CONTROL，"x"）

​	粘贴：send_keys（Keys.CONTROL，"v"）

​	。。。。。。



#### 2、非组合键

​	回车键：send_keys（Keys.ENTER）

​	删除键：send_keys（Keys.BACK_SPACE）

​	空格键：send_keys（Keys.SPACE）

​	制表键：send_keys（Keys.TAB）



### 11、执行JavaScript

#### 1、滚动滚动条

* 当页面中的元素不在可见区域内时，需要滚动条操作。滚动条不是HTML页面中的元素，是浏览器利用JavaScript实现。
* 利用JavaScript实现滚动滚动条

1. scrollIntoView()参数为Boolean型参数，传入false,移动WebElement对象至与当前窗口的底部对齐

   driver.execute_script("arguments[0].scrollIntoView(false);", WebElement对象)

2. scrollIntoView()参数为Boolean型参数，传入true.默认值为true,移动WebElement对象至与当前窗口的顶部对齐

   driver.execute_script("arguments[0].scrollIntoView();", WebElement对象)

3. 滑动滚动条至页面底部
   driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

4. 滑动滚动条至页面顶部
   driver.execute_script("window.scrollTo(0,0)")

5. scrollIntoViewIfNeeded()方法也是用来将不在浏览器窗口的可见区域内的元素滚动到浏览器窗口的可见区域

   但如果该元素已经在浏览器窗口的可见区域内，则不会发生滚动。

   driver.execute_script("arguments[0].scrollIntoViewIfNeed(true);", ele)	#true为默认值，但不是滚动到顶部，而是让元素在可视区域中居中对齐；false时元素可能顶部或底部对齐，关键看元素靠哪边更近。



#### 2、日期输入框

日期输入框的input标签是readonly属性，然后又不想在弹出框中选择具体日期时，可以通过利用DOM更改元素的属性，使readonly的值由ture变为false然后就可以直接编辑输入日期了。

```python
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
driver.maximize_window()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='train_date']")))

#利用JavaScript(DOM对象)来修改readOnly属性的值，将readOnly的值变为false后，便可以进行编辑了
#或者也可以利用JavaScript(DOM对象)来移除readOnly属性，然后就可以进行编辑了
js = 'var ele = document.getElementById("train_date");ele.readOnly = false;ele.value = "2020-09-12";'
driver.execute_script(js)

driver.find_element_by_link_text('查    询').click()
```







### 12、上传操作

* 上传操作有两种情况：

  * 如果是input可以直接输入路径的，那么直接调send_keys输入路径。（如果input标签是readonly属性，可以利用“日期输入框”的方法先改属性再传值）
  * 非input标签的上传，则需要借助第三方工具（MAC/Linux--利用AutoIt,调用生成的au3或exe文件，python pywin3操2库，识别对话句柄，进行作）

* 利用pywin32模块和spy++工具来实现

  import win32gui 

  import win32con

#### 1、定位顶级窗口

win32gui.FindWindow(IpClassName, IpWindowName)
自顶层窗口开始寻找匹配条件的窗口，并返回这个窗口的句柄
IpClassName：类名
IpWindowName：窗口名（window caption）

#### 2、定位子级窗口

win32gui.FindWindowEx(hwndParent=0,hwndChildAfter=0,IpszClass=None,IpsWindow=None)
搜索类名和窗体名匹配的窗体，并返回这个窗体的句柄。找不到就返回0
hwndParent：若不为0，则搜索句柄为hwndParent的窗体的子窗体
hwndChildAfter：若为0，从第一个子窗体开始搜索，若不为0，则从索引为hwndChildAfter开始向后搜索子窗体
IpszClass：字符型的窗口类名
IpsWindow：字符型的窗口名

#### 3、执行上传操作

win32gui.SendMessage(hWnd,Msg,wParam,IParam)
hWnd:整形，接收消息的窗体句柄
Msg：整形，要发送的消息，这些消息都是Windows预先定义好的
wParam：整形，消息的wParam参数
IParam：整形，消息的IParam参数



## 三、Pytest

### 1、pytest概述

1. pytest的所有命令均在终端命令行执行
2. pytest是基于unittest之上的单元测试框架
3. 自动发现测试模块和测试方法
4. 断言使用 assert + 表达式即可
5. 可以设置会话级（session）、模块级（module）、类级（class）、函数级（function）的fixture，用于数据清理和准备工作
6. 有丰富的插件库

### 2、pytest收集测试用例规则

* 默认从当前目录下收集测试用例。即在哪个目录下运行pytest命令，则从哪个目录下收集，pytest可以递归搜集目录
* 规则：
  * 测试用例文件命名规则：test\_*.py或\*_test.py
  * 测试用例函数名规则：以test_开头命名
  * 测试用例类以Test开头，并且测试用例类没有init函数。
  * python包规则：需要有`__init__.py`文件

### 3、对测试用例打标签

* 在运行测试用例时，可以根据标签名过滤测试用例
* 使用方法：
  * 在测试用例/测试类前加上：**@pytest.mark.标签名**。例如@pytest.mark.smoke
  * 可以在一个测试用例/测试类上加多个标签
* 单独执行带有某种标签的测试用例
  * 在该用例文件下执行pytest.main(['-m=smoke']) 无效，不会筛选带有标签的用例
  * 单独写一个执行pytest的文件，执行pytest.main(['-m=smoke'])函数，会筛选带有标签的用例
  * pytest -m 标签名（在终端执行命令），也会筛选带有标签的用例



### 4、创建fixture方法

1. 在测试用例文件的同级目录下创建conftest.py。（必须和测试用例文件同级）

2. 在conftest.py中定义函数，并用**@pytest.fixture(scope=" 此fixture函数的作用域session、class、function等 ")**标记

3. 在测试用例方法、测试用例类中引用conftest.py中的fixture。

   * 注意在测试用例模块文件中引用fixture时，不需要将conftest.py文件导入。

   * 给需要用fixture的测试用例/测试类前直接标签标注。**@pytest.mark.usefixture("fixture函数名")**

4. 在conftest.py文件中，fixture函数里有“yeild"作为前置操作、后置操作的分割线。

   * yeild可以用来返回fixture函数中的变量、值，用元组/列表的形式返回。
   * 在测试用例函数中，加入形参-fixture函数名来接收返回值，以便后续调用

* conftest.py文件实例

  ~~~python
  import pytest
  
  driver = None
  @pytest.fixture(scope='class')   #声明此函数是一个fixture,参数scope代表此fixture的作用域。作用域为类。整个测试类只执行一次。
  def access_web():
      #前置操作
      global driver
      driver = webdriver.Chrome()
      driver.get(CD.web_login_url)
      lg = LoginPage(driver)
      yield (driver, lg)  #yield 分隔线，代表前置条件与后置操作的分隔，并且还用来返回（相当于return）变量参数
                          # 返回参数有的格式为元组或列表形式
      #后置操作
      driver.quit()
      
  @pytest.fixture(scope='function')   #作用域为每一个函数，每个函数均会执行一次本函数。
  def refresh_page():
      global driver
      yield  #yield不是不许存在的，当存在后置操作时则需要输入yield分割线
      #后置操作
      driver.refresh()
  ~~~

* 测试用例调用fixture实例

  ~~~python
  import pytest  #pytest和unittest不要放在一起用
  
  @pytest.mark.usefixtures('access_web')  #在运行测试用例的时候会先去运行access_web函数
  @pytest.mark.usefixtures('refresh_page')    #同理，类下面的每个函数都会执行这个fixture
  class TestLogin():
      # 传入需要接收返回值的fixture的函数名用来接收返回值。用fixture函数名称作为参数接收conftest.py文件中的函数的返回值。
      def test_1_login_success(self, access_web):
          # 步骤：输入用户名密码点击登录
          access_web[1].login(LD.success_data['user'], LD.success_data['password'])
          # 断言：页面中能否找到**元素,pytest中直接利用assert进行判断，后面表达式为Ture则返回Ture,False返回False
          assert IndexPage(access_web[0]).isExist_logout_element()
  ~~~

  

### 5、pytest、unittest

1. unittest中可以根据用例名称（含有数字，`_0_、_1_`）来决定用例加载执行顺序。否则用例执行时无序的。
2. pytest中只能通过用例的位置，即用例在文件中靠前就先执行，用例在文件中靠后就后执行。
3. pytest和unittest测试用例文件的加载顺序，可以通过给测试用例文件命名来决定。（test_01_login.py；test_02_invest.py）



### 6、pytest测试用例参数化

* 数据驱动自动化测试，相当于实现unittest中的ddt。在自动化测试中，一个测试用例对应一个测试点，通常一组测试数据无法完全覆盖测试范围，所以，需要参数化来传递多组数据。

* 在测试用例的前面加上：**@pytest.mark.paramertize('参数名'，‘列表数据’)**
  * 在使用`pytest.mark.parametrize()`传递参数化数据时，测试用例本身必须有参数。
  * 参数名：以字符串的形式标识用例函数的参数，且和用例函数中的参数名必须相同。以逗号分隔的字符串
  * 列表数据：参数值列表。若有多个形参，列表嵌套元组的形式。一组实参以元组形式存在，包含多组形参的所有实参

~~~python
phone_data = [
    {"user": 1389045372123, "password": "iphone12", "check": "请输入正确手机号"},
    {"user": 13890453, "password": "iphone12", "check": "请输入正确手机号"},
    {"user": 111389045372, "password": "iphone12", "check": "请输入正确手机号"},
    {"user": "", "password": "iphone12", "check": "请输入手机号"},
    {"user": 1389045372123, "password": "", "check": "请输入密码"}
]

@pytest.mark.parametrize('data1', phone_data)    #pytest模块中不能使用ddt进行测试用例的参数化
def test_0_login_user_wrongformat(self, data1, access_web):
    # 步骤：输入用户名密码点击登录
    access_web[1].login(data1['user'], data1['password'])
    # 断言：页面中提示请输入正确的手机号
    assert access_web[1].get_errorMsg_from_loginArea() == data1['check']
~~~



#### 1、参数化之一个参数（形参）

* 一个参数，多个值

~~~python
@pytest.mark.parametrize("arg_1", [4399, 2012])
def test_add_by_func_aaa(arg_1):
	print(arg_1)
	
# test_case/test_func.py::test_add_by_func_aaa[4399] 4399
PASSED
# test_case/test_func.py::test_add_by_func_aaa[2012] 2012
PASSED

~~~



#### 2、参数化之多个参数（形参）

* 多个参数，多个值

~~~python
@pytest.mark.parametrize("arg_1, arg_2", [(4399, 'AAAA'), (2012, 'BBBB')])
def test_add_by_func_aaa(arg_1,arg_2):
	print("arg_1:{}  arg_2:{}".format(arg_1, arg_2))
    
# test_case/test_func.py::test_add_by_func_aaa[4399-AAAA] arg_1:4399  arg_2:AAAA
PASSED
# test_case/test_func.py::test_add_by_func_aaa[2012-BBBB] arg_1:2012  arg_2:BBBB
PASSED

~~~



#### 3、多个参数混合使用

* 笛卡尔乘积

~~~python
@pytest.mark.parametrize("arg_1", [4399,  2012, 1997])
@pytest.mark.parametrize("arg_2", ['AAAA', 'BBBB', 'CCCC'])
def test_add_by_func_aaa(arg_1,arg_2):
	print("arg_1:{}  arg_2:{}".format(arg_1, arg_2))

# test_case/test_func.py::test_add_by_func_aaa[AAAA-4399] arg_1:4399  arg_2:AAAA
PASSED
# test_case/test_func.py::test_add_by_func_aaa[AAAA-2012] arg_1:2012  arg_2:AAAA
PASSED
# test_case/test_func.py::test_add_by_func_aaa[AAAA-1997] arg_1:1997  arg_2:AAAA
PASSED
# test_case/test_func.py::test_add_by_func_aaa[BBBB-4399] arg_1:4399  arg_2:BBBB
PASSED
# test_case/test_func.py::test_add_by_func_aaa[BBBB-2012] arg_1:2012  arg_2:BBBB
PASSED
# test_case/test_func.py::test_add_by_func_aaa[BBBB-1997] arg_1:1997  arg_2:BBBB
PASSED
# test_case/test_func.py::test_add_by_func_aaa[CCCC-4399] arg_1:4399  arg_2:CCCC
PASSED
# test_case/test_func.py::test_add_by_func_aaa[CCCC-2012] arg_1:2012  arg_2:CCCC
PASSED
# test_case/test_func.py::test_add_by_func_aaa[CCCC-1997] arg_1:1997  arg_2:CCCC
PASSED

~~~



### 7、pytest重运行机制

* rerunfailures

* 使用方式：

  pytest --reruns 次数，运行失败用来可以运行几次

  pytest --reruns 重运行次数  --reruns-delay 延时，延时是重运行之间的时间间隔

* 举例：pytest --reruns 2 --reruns-delay 5，表示失败的用例可以重运行2次，每次间隔时间为5秒



### 8、pytest生成测试报告

* 涉及到的路径均为相对路径

1. 生成JunitXml格式报告：--junitxml=path/文件名.xml——常用于dign
2. 生成result log格式报告：--resultlog=path/log.txt
3. 生成HTML格式报告：--html=report/t文件名.html（需要安装pytest-html插件）



### 9、pytest-allure报告

#### 1、安装查看

* 安装插件，allure-pytest

* 生成报告命令：pytest  --alluredir=相对路径(指定测试报告目录即可，不用像上面一样指定文件名)

* 查看allure的测试报告

  * 安装windows的allure插件，并将路径添加到环境变量中
  * allure	serve	allure目录(绝对路径)——在cmd命令行执行

* **方式一：直接打开默认浏览器展示报告（常用）**

  * allure serve ./result/

* 方式二：从结果生成报告

  - 生成报告

    `allure generate ./result/ -o ./report/ --clean` (覆盖路径加--clean)

  - 打开报告

    `allure open -h 127.0.0.1 -p 8883 ./report/`

#### 2、allure测试用例说明

* https://www.cnblogs.com/Zhan-W/p/13141219.html

| Allure用例描述            |                    |                                               |
| :------------------------ | ------------------ | --------------------------------------------- |
| 使用方法                  | 参数值             | 参数说明                                      |
| @allure.epic()            | epic描述           | 定义项目、当有多个项目是使用。往下是feature   |
| @allure.feature()         | 模块名称           | 用例按照模块区分，有多个模块时给每个起名字    |
| @allure.story()           | 用例名称           | 一个用例的描述                                |
| @allure.title(用例的标题) | 用例标题           | 一个用例标题                                  |
| @allure.testcase()        | 测试用例的连接地址 | 自动化用例对应的功能用例存放系统的地址        |
| @allure.issue()           | 缺陷地址           | 对应缺陷管理系统里边的缺陷地址                |
| @allure.description()     | 用例描述           | 对测试用例的详细描述                          |
| @allure.step()            | 操作步骤           | 测试用例的操作步骤                            |
| @allure.severity()        | 用例等级           | blocker 、critical 、normal 、minor 、trivial |
| @allure.link()            | 定义连接           | 用于定义一个需要在测试报告中展示的连接        |
| @allure.attachment()      | 附件               | 添加测试报告附件                              |

只有当用例上使用allure的语法糖，allure的测试报告才能更加仔细详尽的说明。



### 10、执行测试用例

在项目的根目录下创建一个run执行用例的入口

只需要写简单的两行代码

~~~python 
import pytest
# 不带参数，默认运行的是当前目录及子目录的所有文件夹的测试用例
pytest.main()
~~~





# APPUI自动化

## 1、Appium基础

* Appium，开源工具，用于自动化界面。可用于iOS手机、Android手机、Windows桌面上的移动web和混合应用。

### 1、应用分类

* 原生应用：用iOS、Android、Windows SDK编写的应用
* 移动web应用：移动端浏览器访问的应用（Appium支持iOS上的Safari，Chrome和Android上的内置浏览器）
* 混合应用：带有一个“webview”的包装器，比如微信上的（APP+公众号_网页），知乎，Android原生控件+网页web（其实就是HTML页面放在APP上）





## 2、移动端自动化框架

* ios9.3以上：XCUITest
* ios9.3以下：UIAutomation
* Android4.2以上：UIAutomator
* Android2.3以上：Instrumontation



## 3、Android设备相关命令

### 1、aapt命令

* 获取应用包名和入口activity

  aapt 	dump	badging	apk应用名（以apk为后缀）



### 2、adb命令

* adb用来连接安卓手机和PC端的桥梁

  | 命令                                                         | 描述                                                     |
  | ------------------------------------------------------------ | -------------------------------------------------------- |
  | adb  kill-server                                             | 关闭adb服务                                              |
  | adb  start-server                                            | 开启adb服务                                              |
  | adb  devices                                                 | 检测连接到电脑的安卓设备                                 |
  | adb  shell  logcat                                           | 打印log信息                                              |
  | adb  pull  <手机路径>  <电脑路径>                            | 从手机中拉取信息到电脑路径                               |
  | adb  push  <电脑路径><手机路径>                              | 从电脑上推送信息到手机上去                               |
  | adb  shell                                                   | 登录设备的shell（人机交互命令行），进入到Linux命令行环境 |
  | adb  shell  logcat  >  电脑文件路径                          | 将log信息重定向到本机文件中                              |
  | adb  install  **.apk                                         | 安装应用，也可以直接把apk包直接拖进cmd窗口中             |
  | adb  uninstall  包名（应用）                                 | 卸载APP                                                  |
  | adb  shell  dumpsys  activity名  \|  find  "mFocusedActivity" | 查看前台应用Activity名（当前设备活动的activity页面）     |
  | adb  connect/disconnect                                      | 通过WiFi进行远程手机调试                                 |
  | adb  kill-server/adb  start-server                           | 关闭/启动adb服务                                         |
  | adb  shell pm  list  packages                                | 列出所有的包名                                           |
  | adb  shell pm  list  packages  -f                            | 列出所有apk路径及包名                                    |
  | adb  shell pm  list  packages  -s                            | 列出所有系统apk路径及包名                                |
  | adb  shell pm  list  packages  -3                            | 列出用户apk路径及包名                                    |
  |                                                              |                                                          |
  |                                                              |                                                          |

  

## 4、元素定位

* 通过id定位：resrouce-id
* 通过class-name定位：classname
* 通过Accessibilityid定位：content-desc
* 通过AndroidUiAutomator定位：
* 通过Xpath定位（效率低下）

### 1、AndroidUiAutomator定位详解

* 通过UiAutomator中的Uiselector类来进行元素定位
* driver.find_element_by_android_uiautomator(Uiselector类定位元素表达式）

1. Uiselector类定位元素的表达（用java来写）

   注意java中，“	”来表示字符串，'	'来表示单个字符

   new	UiSelector().函数名(“定位表达式”).函数(“定位表达式”)……————Java语法

   new	UiSelector().resrouceid("com.xx2b.fenwoo:id/btn_login")





## 5、滑屏操作

* 滑屏接口：swipe（起始X，起始Y，结束X，结束Y）

  起始X——结束X：X轴滑动的距离

  起始Y——结束Y：Y轴滑动的距离

  

* 滑屏执行原理

  获得屏幕尺寸；设置滑动距离占屏幕比率；调用滑动接口

* 实例

  获得窗口的大小——get_window_size()；返回屏幕的宽和高

  设置滑动距离——X1=\*；Y1=\*；X2=\*；Y2=\*；

  调用接口——swipe（X1，Y1，X2，Y2）





## 6、触屏操作

* 利用TouchAction类，类似于selenium中的ActionChains类

  将一系列的动作放在一个链条中，然后将链条传送给服务器，server接受链条后，会解析，依次执行。

  

  | 命令             | 描述                           |
  | ---------------- | ------------------------------ |
  | press            | 短按                           |
  | longpress        | 长按                           |
  | tap              | 点击                           |
  | move  to  (x，y) | 移动到，相当于上一个坐标的距离 |
  | wait             | 等待                           |
  | release          | 释放                           |
  | perform          | 执行                           |
  | cancel           | 取消                           |
  |                  |                                |

  **注意：press、longPress会与release结合使用**

  **press，longPress可以传入element对象，也可以传入坐标**

  ~~~python
  ele = driver.find_element_by_id("***")
  ele.size  # 获取元素的尺寸，以字典的形式返回元素的尺寸，{’width':'**';'height':'**'}
  ori = ele.location  # 获得元素的起点坐标（元素的左上角）
  					# location方法返回元素的起点坐标，以字典的形式返回{’x':'**';'y':'**'}
  ~~~



## 7、Toast提示信息提取

* 在提取Toast提示信息之前，初始化服务器参数时必须指定自动化测试引擎（automationName）为UiAutomator2

  **版本高时，不需要指定会自动切换至UiAutomator2**

1. Xpath表达式——文本匹配

   appium中的text是元素的属性

   xpath=“//*[contains(@text,'部分文本内容‘)]”

2. 元素等待

   元素wait时，使用presence_of_element_located，不能使用visibility……，toast不支持







## 8、杂七杂八

### 1、如何分辨一个APP是Active还是web？

1. 开发者选项中打开显示布局边界，如果APP有边界显示则为Active，没有则为web

2. 通过UiAutomatoviewer定位，class属性值为webview***，则为web

   混合应用中的web移动网页和原生控件是不同的，不能通过UiAutomatoviewer来识别





### 2、hybird混合应用自动化方案

基于UiAutomator+ChromeDriver

### 3、获取webview页面的三种方式

通过Chrome://inspect,网页获取，需要翻墙

使用driver.page_source，获取HTML页面

找开发要源文件

使用uc-devtools工具获取



### 4、context

类似于web-selenium中的窗口，此处叫做上下文

列出所有可用的上下文：driver.contexts

列出当前的上下文：driver.current_context

切换至默认的上下文：driver.switch_to.context(None)

切换至指定的上下文：driver.switch_to.context(driver.contexts[-1])

当前的Activity：driver.current_activity

当前的包名：driver.current_package





# Python库

https://mp.weixin.qq.com/s/HXw15DV_FxesVOfzblWlnQ



## 库名称简介



Chardet字符编码探测器，可以自动检测文本、网页、xml的编码。



colorama主要用来给文本添加各种颜色，并且非常简单易用。



Prettytable主要用于在终端或浏览器端构建格式化的输出。



difflib，[Python]标准库，计算文本差异



Levenshtein，快速计算字符串相似度。



fuzzywuzzy,字符串模糊匹配。



esmre,正则表达式的加速器。



shortuuid,一组简洁URL/UUID函数库。



ftfy，Unicode文本工具7



unidecode，ascii和Unicode文本转换函数。



xpinyin，将汉字转换为拼音的函数库



pangu.py，调整对中日韩文字当中的字母、数字间距。



pyfiglet，Python写的figlet程序，使用字符组成ASCII艺术图片



uniout，提取字符串中可读写的字符



awesome slugify，一个Python slugify库，用于处理Unicode。



python-slugify，转换Unicode为ASCII内码的slugify函数库。



unicode-slugify，生成unicode内码，Django的依赖包。



ply，Python版的lex和yacc的解析工具



phonenumbers，解析电话号码，格式，存储和验证的国际电话号码。



python-user-agents，浏览器的用户代理（user-agents）的解析器。



sqlparse，SQL解析器。



pygments，一个通用的语法高亮工具。



python-nameparser，解析人名，分解为单独的成分。



pyparsing，通用解析器生成框架。



tablib，表格数据格式，包括，XLS、CSV，JSON，YAML。



python-docx，docx文档读取，查询和修改，微软Word 2007 / 2008的docx文件。



xlwt/xlrd，读写Excel格式的数据文件。



xlsxwriter，创建Excel格式的xlsx文件。



xlwings，利用Python调用Excel



csvkit，CSV文件工具包。



marmir，把Python[数据结构]，转化为电子表格。



pdfminer，从PDF文件中提取信息。



pypdf2， 合并和转换PDF页面的函数库。



Python-Markdown，轻量级标记语言Markdown的Python实现。



Mistune，,快速、全功能的纯Python编写的Markdown解释器。



dateutil，标准的Python官方datetime模块的扩展包，字符串日期工具，其中parser是根据字符串解析成datetime，而rrule是则是根据定义的规则来生成datetime。



arrow,更好的日期和时间处理Python库



chronyk，一个Python 3版函数库，用于解析人写的时间和日期。



delorean，清理期时间的函数库。



when.py，为见的日期和时间，提供人性化的功能。



moment，类似Moment.js的日期/时间Python库



pytz，世界时区，使用tz database时区信息[数据库]



BeautifulSoup，基于Python的HTML/XML解析器，简单易用, 功能很强大,即使是有bug，有问题的html代码，也可以解析



lxml，快速，易用、灵活的HTML和XML处理库，功能超强，在遇到有缺陷、不规范的xml时，Python自带的xml处理器可能无法解析。报错时，程序会尝试再用lxml的修复模式解析。



htmlparser，官方版解析HTML DOM树，偶尔搞搞命令行自动表单提交用得上。



pyyaml，Python版本的YAML解释器。



html5lib，-标准库，解析和序列化HTML文档和片段。



pyquery，类似[jQuery]的的HTML解释器函数库。



cssutils，Python CSS库。



MarkupSafe，XML或HTML / XHTML安全字符串标记工具。



cssutils - ACSS library for Python., MarkupSafe - Implements a XML/HTML/XHTML



bleach，漂白，基于HTML的白名单函数库。



xmltodict，类似JSON的XML工具包。



xhtml2pdf，HTML / CSS格式转换器，看生成pdf文档。



untangle，把XML文档，转换为Python对象，方便访问。



## 文件处理



库名称简介Mimetypes，Python标准库，映射文件名到MIME类型。



imghdr，Python标准库，确定图像类型。python-magic，libmagic文件类型识别库，Python接口格式。path.py，os.path模块的二次封装。



watchdog，一组API和shell实用程序，用于监视文件系统事件。



Unipath，面向对象的文件/目录的操作工具包。pathlib，-（Python 3.4版已经作为Python标准库），一个跨平台，面向path的函数库。



pickle/cPickle,python的pickle模块实现了基本的数据序列和反序列化。通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。



cPickle是[C语言]实现的版本，速度更快。



ConfigParser，Python标准库，INI文件解析器。



configobj，INI文件解析器。config，分层次配置，logging作者编写。



profig，多格式配置转换工具。



logging，Python标准库，日志文件生成管理函数库。



logbook，logging的替换品。



Sentry，实时log服务器。Raven，哨兵Sentry的Python客户端。



Sphinx，斯芬克斯（狮身人面像），Python文档生成器。



reStructuredText，标记语法和解析工具，Docutils组件。mkdocs，Markdown格式文档生成器。



pycco，简单快速、编程风格的文档生成器。



pdoc，自动生成的Python库API文档epydoc，从源码注释中生成各种格式文档的工具



## 图像处理



库名称简介PIL（Python Image Library），基于Python的图像处理库，功能强大，对图形文件的格式支持广泛，内置许多图像处理函数，如图像增强、滤波[算法]等Pillow，图像处理库，PIL图像库的分支和升级替代产品。Matplotlib，著名的绘图库，提供了整套和matlab相似的命令API，用以绘制一些高质量的数学二维图形，十分适合交互式地进行制图。brewer2mpl，有一个专业的python配色工具包，提供了从美术角度来讲的精美配色。



PyGame基于Python的多媒体开发和游戏软件开发模块，包含大量游戏和图像处理功能Box2d，开源的2d物理引擎，愤怒的小鸟就是使用了这款物理引擎进行开发的，Box2d物理引擎内部模拟了一个世界，你可以设置这个世界里的重力，然后往这个世界里添加各种物体，以及他们的一些物理特性，比如质量，摩擦，阻尼等等。



Pymunk，类似box2d的开源物理图形模拟库OpenCV, 目前最好的开源图像/视觉库，包括图像处理和计算机视觉方面、[机器学习]的很多通用算法。SimpleCV，计算机视觉开源框架，类似opencv。VTK，视觉化工具函式库（VTK， Visualization Toolkit）是一个开放源码，跨平台、支援平行处理（VTK曾用于处理大小近乎1个Petabyte的资料，其平台为美国Los Alamos国家实验室所有的具1024个处理器之大型系统）的图形应用函式库。



2005年时曾被美国陆军研究实验室用于即时模拟俄罗斯制反导弹战车ZSU23-4受到平面波攻击的情形，其计算节点高达2.5兆个之多。cgkit,Python Computer Graphics Kit,其module 主要分两个部分，



 \1. 与3d相关的一些python module 例如the vector, matrix and quaternion types, the RenderMan bindings, noise functions 这些模块可以在maya houdini nuke blender 等有Python扩展的程序中直接用;



 \2. 提供完整的场景操作的module， 他类似其他三维软件，在内存中保留完整的描述场景的信息。



不能直接用于maya 等CGAL，



Computational Geometry Algorithms Library，计算几何算法库，提供计算几何相关的数据结构和算法，诸如三角剖分（2D约束三角剖分及二维和三维Delaunay三角剖分），



Voronoi图（二维和三维的点，2D加权Voronoi图，分割Voronoi图等），

多边形（布尔操作，偏置），多面体（布尔运算），曲线整理及其应用，

网格生成（二维Delaunay网格生成和三维表面和体积网格生成等），几何处理（表面网格简化，细分和参数化等），

凸壳算法（2D，3D和dD），搜索结构（近邻搜索，kd树等），插值，形状分析，拟合，距离等。



Aggdraw，开源图像库，几乎涵盖了2d image操作的所有功能，使用起来非常灵活Pycairo,开源矢量绘图库Cairo开罗的python接口，

cairo提供在多个背景下做2-D的绘图，高级的更可以使用硬件加速功能。wand，Python绑定魔杖工具（MagickWand），C语言API接口。



thumbor， -智能成像工具，可调整大小和翻转图像。



imgSeek，查询相似的图像。



python-qrcode，纯Python的二维码（QR码）生成器。



pyBarcode，创建条码，无需PIL模块。



pygram，Instagram像图像过滤器。



Quads，基于四叉树的计算机艺术。



nude.py，裸体检测函数。



scikit-image，scikit工具箱的图像处理库。



hmap，图像直方图工具。



bokeh，交互的Web绘图。



plotly，Web协同的Python和Matplotlib绘制。



vincent，文森特，Python Vega的函数库。



d3py，Python绘图库，基于D3.JS, ggplot -API兼容R语言的ggplot2.Kartograph.py，在Python绘制漂亮的SVG地图。pygal， SVG图表的创造者。



pygraphviz，Graphviz的Python接口。



Fonttlools，ttf字体工具函数包，用于fontforge、ttx等字体软件。



## 游戏和多媒体



库名称简介audiolazy，数字信号处理（DSP）的Python工具包。



audioread，跨平台（GStreamer + Core Audio + MAD + FFmpeg）音频解码库。



beets，音乐库管理。



dejavu，音频指纹识别算法。



Dejavu 听一次音频后就会记录该音频的指纹信息，然后可通过麦克风对输入的音频进行识别是否同一首歌。django-elastic-transcoder,Django +亚马逊elastic转码。eyeD3,音频文件工具，特别是MP3文件包含的ID3元数据。



id3reader，用于读取MP3的元数据。



mutagen，处理音频元数据。



pydub，-操纵音频和简单的高层次的接口。



pyechonest，Echo Nest API客户端。talkbox，语音和信号处理的Python库。



TimeSide，开放的网络音频处理框架。



tinytag，读取音乐文件元数据，包括的MP3，OGG，FLAC和wave文件。



m3u8，用于解析m3u8文件。



moviepy，多格式视频编辑脚本模块，包括GIF动画。



shorten.tv，视频摘要。



scikit视频，SciPy视频处理例程。



GeoDjango,一个世界级的地理Web框架。



geopy,Geo地理编码的工具箱。



pygeoip，纯Python写的GeoIP API。



GeoIP，Python API接口，使用高精度GeoIP Legacy Database数据库。



geojson，GeoJSON函数库django-countries，一个Django程序，提供国家选择，国旗图标的静态文件，和一个国家的地域模型。



Pygame，Python游戏设计模块。



Cocos2d，2D游戏框架，演示，和其他的图形/交互应用，基于pyglet。Cocos2d- cocos2d is a framework for building 2D games, demos, and other graphical/interactive applications. It is based on pyglet.,PySDL2，SDL2的封装库。



Panda3D- 3D游戏引擎，迪士尼开发。



用C++写的，完全兼容Python。PyOgre，OGRE 3D渲染引擎，可用于游戏，模拟，任何3D。



PyOpenGL，绑定OpenGL和它相关的API。



PySFML，Python绑定SFMLRenPy，视觉小说引擎。



## 大数据与科学计算



库名称简介pycuda/opencl，GPU高性能并发计算Pandas，python实现的类似R语言的数据统计、分析平台。基于NumPy和Matplotlib开发的，主要用于数据分析和数据可视化，它的数据结构DataFrame和R语言里的data.frame很像，特别是对于时间序列数据有自己的一套分析机制，非常不错。



Open Mining，商业智能（BI），Pandas的Web界面。blaze，NumPy和Pandas大数据界面。



SciPy，开源的Python算法库和数学工具包，SciPy包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算。



其功能与软件MATLAB、Scilab和GNU Octave类似。



 Numpy和Scipy常常结合着使用，Python大多数机器学习库都依赖于这两个模块。



ScientificPython，一组经过挑选的Python程序模块，用于科学计算，包括几何学（矢量、张量、变换、矢量和张量场），四元数，自动求导数，（线性）插值，多项式，基础统计学，非线性最小二乘拟合，单位计算，Fortran兼容的文本格式，通过VRML的3D显示，以及两个Tk小工具，分别用于绘制线图和3D网格模型。



此外还具有到netCDF，MPI和BSPlib库的接口。



NumPy科学计算库，提供了矩阵，线性代数，傅立叶变换等等的解决方案, 最常用的是它的N维数组对象. NumPy提供了两种基本的对象：



ndarray（N-dimensional array object）和 ufunc（universal function object）。



ndarray是存储单一数据类型的多维数组，而ufunc则是能够对数组进行处理的函数。



Cvxopt，最优化计算包，可进行线性规划、二次规划、半正定规划等的计算。



Numba，科学计算速度优化编译器。pymvpa2，是为大数据集提供统计学习分析的Python工具包，它提供了一个灵活可扩展的框架。



它提供的功能有分类、回归、特征选择、数据导入导出、可视化等NetworkX，复杂网络的优化软件包。zipline，交易算法的函数库。



PyDy， Python动态建模函数库。



SymPy,符号数学的Python库。statsmodels,Python的统计建模和计量经济学。



astropy,天文学界的Python库。



orange，橙色，数据挖掘，数据可视化，通过可视化编程或Python脚本学习机分析。



RDKit,化学信息学和机器学习的软件。



Open Babel，巴贝尔，开放的化学工具箱。



cclib，化学软件包的计算函数库。



Biopython，免费的生物计算工具包。



bccb，生物分析相关的代码集。bcbio-nextgen，提供完全自动化、高通量、测序分析的工具包。



visvis, 可视化计算模块库，可进行一维到四维数据的可视化。



MapReduce是Google提出的一个软件[架构]，用于大规模数据集（大于1TB）的并行运算。



概念“Map（映射）”和“Reduce（归纳）”，及他们的主要思想，都是从函数式编程语言借来的MapReduce函数库。Framworks and libraries for MapReduce.,PySpark，[Spark]的Python API。dpark，Spark的Python克隆，Python中的MapReduce框架。luigi，为批量工作，建立复杂的管道。mrjob，运行在[Hadoop]，或亚马逊网络服务的，MapReduce工作。



## 人工智能与机器学习



库名称简介NLTK（natural language toolkit)，是python的自然语言处理工具包。2001年推出，包括了大量的词料库，以及自然语言处理方面的算法实现：



分词， 词根计算， 分类， 语义分析等。



Pattern，数据挖掘模块，包括自然语言处理，机器学习工具，等等。

textblob，提供API为自然语言处理、分解NLP任务。基于NLTK和Pattern模块。



jieba，结巴，中文分词工具。snownlp，用于处理中文文本库。



loso，中文分词函数库。



genius，中文CRF基础库，条件随机场(conditional random field,简称 CRF),是一种鉴别式机率模型,是随机场的一种,常用于标注或分析序列资料,如自然语言文字或是生物序列Gensim，一个相当专业的主题模型Python工具包，无论是代码还是文档，可用于如何计算两个文档的相似度LIBSVM,是台湾大学林智仁(Lin Chih-Jen)教授等开发设计的一个简单、易于使用和快速有效的SVM模式识别与回归的软件包，他不但提供了编译好的可在Windows系列系统的执行文件，还提供了源代码，方便改进、修改以及在其它[操作系统]上应用；



该软件对SVM所涉及的参数调节相对比较少，提供了很多的默认参数，利用这些默认参数可以解决很多问题；



并提供了交互检验(Cross Validation)的功能。



该软件可以解决C-SVM、ν-SVM、ε-SVR和ν-SVR等问题，包括基于一对一算法的多类模式识别问题。



scikits.learn，构建在SciPy之上用于机器学习的 Python 模块。它包括简单而高效的工具，可用于数据挖掘和数据分析。



涵盖分类，回归和聚类算法，例如SVM， 逻辑回归，朴素贝叶斯，随机森林，k-means等算法，代码和文档都非常不错，在许多Python项目中都有应用。



例如在我们熟悉的NLTK中，分类器方面就有专门针对scikit-learn的接口，可以调用scikit-learn的分类算法以及训练数据来训练分类器模型。PyMC，机器学习采样工具包，scikit-learn似乎是所有人的宠儿，有人认为，PyMC更有魅力。



PyMC主要用来做Bayesian分析。Orange，基于组件的数据挖掘和机器学习软件套装，它的功能即友好，又很强大，快速而又多功能的可视化编程前端，以便浏览数据分析和可视化，包含了完整的一系列的组件以进行数据预处理，并提供了数据帐目，过渡，建模，模式评估和勘探的功能。



侧重数据挖掘，可以用可视化语言或Python进行操作，拥有机器学习组件，还具有生物信息学以及文本挖掘的插件。



Milk，机器学习工具箱，其重点是提供监督分类法与几种有效的分类分析：SVMs(基于libsvm)，K-NN，随机森林经济和决策树。

它还可以进行特征选择。这些分类可以在许多方面相结合，形成不同的分类系统。对于无监督学习，它提供K-means和affinity propagation聚类算法。



PyMVPA(Multivariate Pattern Analysis in Python),是为大数据集提供统计学习分析的Python工具包，它提供了一个灵活可扩展的框架。它提供的功能有分类、回归、特征选择、数据导入导出、可视化等NuPIC，开源人工智能平台。

该项目由Grok（原名 Numenta）公司开发，其中包括了公司的算法和软件架构。



 NuPIC 的运作接近于人脑，“当模式变化的时候，它会忘掉旧模式，记忆新模式”。如人脑一样，CLA 算法能够适应新的变化。Pylearn2，-基于Theano的机器学习库。



hebel，GPU加速，[深度学习]Python库。



gensim，机器学习库。pybrain，机器学习模块，它的目标是为机器学习任务提供灵活、易应、强大的机器学习算法。



pybrain包括神经网络、强化学习(及二者结合)、无监督学习、进化算法。以神经网络为核心，所有的训练方法都以神经网络为一个实例Mahout,是 Apache Software Foundation（ASF） 旗下的一个开源项目，提供一些可扩展的机器学习领域经典算法的实现，旨在帮助开发人员更加方便快捷地创建智能应用程序。



Mahout包含许多实现，包括聚类、分类、推荐过滤、频繁子项挖掘。此外，通过使用 Apache Hadoop 库，Mahout 可以有效地扩展到云中。



Crab，灵活的，快速的推荐引擎。python-recsys，娱乐系统分析，推荐系统。vowpal_porpoise，Vowpal Wabbit轻量级Python封装。



Theano,用来定义、优化和模拟数学表达式计算，用于高效的解决多维数组的计算问题的python软件包。它使得写深度学习模型更加容易，同时也给出了一些关于在GPU上训练它们的选项。



## 系统与命令行



库名称简介threading，Python标准线程库，更高级别的线程接口。

envoy，特使，Python子线程的函数库。



sh，成熟的子线程替换函数库。sarge，封装线程。subprocess,调用shell命令的神器argparse，写命令行脚本必备，强大的命令行差数解析工具timeit，计算代码运行的时间等等unp，命令行工具，解压文件。

eventlet开销很少的多线程模块，使用的是 green threads 概念，例如，pool = eventlet.GreenPool(10000) 这样一条语句便创建了一个可以处理 10000 个客户端连接的线程池。



类似Gevent线程库Gevent，多线程模块pytools,著名的python通用函数、工具包SendKeys, 键盘鼠标操作模块, 模拟键盘鼠标模拟操作。



pyHook,基于Python的“钩子”库，主要用于监听当前电脑上鼠标和键盘的事件。



这个库依赖于另一个Python库PyWin32，如同名字所显示的，PyWin32只能运行在Windows平台，所以PyHook也只能运行在Windows平台。



pstuil,跨平台地很方便获取和控制系统的进程，以及读取系统的CPU占用内存占用等信息.cement，一个轻量级的、功能齐全的命令行工具click，简单优雅的的命令行接口。



clint，Python命令行工具。cliff，创造多层次指令的命令行程序框架。



Clime， 可以转换任何模块为多的CLI命令程序，无任何配置。



docopt，Python命令行参数分析器。



pycli，命令行应用程序，支持的标准命令行解析，测井，单元[测试]和功能测试。



Gooey，打开命令行程序，作为为一个完整的GUI应用程序,cookiecutter，命令行工具，从cookiecutters（项目模板）创建项目。



例如，Python包项目，jQuery插件项目。



percol，为UNIX传统管道pipe命令，添加交互式选择风格。



rainbowstream，聪明和漂亮的推特客户终端。Django Models，Django的一部分SQLAlchemy，Python SQL工具包和对象关系映射。



peewee，小型的ORM解析器。



PonyORM，为ORM提供了一种面向SQL的接口。MongoEngine，Python对象文件映射，使用[MongoDB]。



, Django MongoDB引擎MongoDB , Django后台。



django-mongodb-engine，Django后台.redisco,一个简单的模型和容器库，使用[Redis]flywheel，Amazon DynamoDB对象映射。



butterdb，谷歌电子表格的ORM，Python版。celery，芹菜，异步任务队列/工作，基于分布式消息队列。



huey，休伊，轻量级，多线程任务队列。



mrq，队列先生，分布式任务队列，使用redis & Gevent。rq，简单的工作队列。



Queue,Queue模块可以用来实现多线程间通讯，让各个线程共享数据，生产者把货物放到Queue中，供消费者（线程）去使用。



simpleq，简单的，可扩展的队列，Amazon SQS基础队列。

Psyco，超强的python性能优化工具，psyco 的神奇在于它只需要在代码的入口处调用短短两行代码，性能就能提升 40% 或更多，真可谓是立竿见影！如果你的客户觉得你的程序有点慢，敬请不要急着去优化代码，psyco 或许能让他立即改变看法。



psyco 堪称 Python 的 jit。fn.py，Python函数编程：缺失的功能享受FP的实现。funcy，函数编程工具。



Toolz，函数编程工具：迭代器、函数，字典。CyToolz，Toolz的Cython实现，高性能的函数编程工具。Ansible，安塞波，极为简单的自动化平台。



SaltStack，基础设施的自动化管理系统。



Fabric，织物，一个简单，远程执行和部署的语言工具。



Fabtools，Fabric的工具函数。



cuisine，热门的Fabric的工具函数。



psutil，跨平台的过程和系统工具模块。



pexpect，控制互动节目。



provy，易于使用的配置系统的Python。honcho，Foreman的Python接口，用于管理procfile应用工具。



gunnery，多任务执行工具，与网络接口的分布式系统。



fig，快速。独立的开发环境中使用泊坞窗。



APScheduler，轻量级、但功能强大的在线任务调度程序。



django-schedule,Django日程应用程序。doit,任务流道/生成工具。



Joblib,Python提供的轻量级的流水线工具函数。



Plan，简易生成crontab文件。



Spiff，纯Python实现的，功能强大的工作流引擎。



schedule，Python作业调度。TaskFlow，有助于使任务执行简单。



ctypes，Python标准库，速度更快，Python调用C代码的外部函数接口。cffi，Python调用C代码外部函数接口，类似于ctypes直接在python程序中调用c程序,但是比ctypes更方便不要求编译成so再调用。



Cytoolz，python 加速库SWIG，简化封装和接口生成器。



,Cython，Python优化静态编译器。



PyPy，Python解释器的 Python实现。



Stackless Python，一个增强版本的Python。它使程序员从基于线程的编程方式中获得好处，并避免传统线程所带来的性能与复杂度问题。



Stackless为 Python带来的微线程扩展，是一种低开销、轻量级的便利工具Pyston,使用LLVM和现代JIT技术,对python进行性能优化。



pythonlibs，非官方的Windows（32 / 64位）的Python扩展包scapy，优秀的数据包处理库。



ino，Arduino命令行工具。Pyro，Python的机器人工具包。



pluginbase，一个简单而灵活的Python的插件系统。



itsdangerous，数据安全传输工具。blinker，快速Python中的信号/事件调度系统。



pychievements，用于创建和跟踪成果框架。



python-patterns，Python中的设计模式。



pefileWindows PE文件解析器SIP，自动为C和C++库生成Python扩展模块的工具



## 数据库



库名称简介MySQLdb，成熟的[MySQL]数据库模块,Baresql,SQL数据库包ZODB，Python本地对象数据库。一个K-V对象图数据库。



pickledb,简单和轻量级的K-V键值存储。



TinyDB, 轻量级，面向文档的数据库。



mysql-python，MySQL的Python工具库。



mysqlclient，mysql-python分支，支持Python 3.,PyMySQL,纯Python写的 MySQL驱动程序，兼容mysql-python。mysql-connector-python,MySQL连接器,来自[Oracle]，纯Python编写。



oursql，MySQL连接器，提供本地话指令语句和BLOBs支持。

psycopg2，最流行的Python PostgreSQL适配器。txpostgres，于Twisted的异步驱动，用于PostgreSQL。



queries,psycopg2函数库，用于PostgreSQL。



dataset,存储Python字典数据,用于SQLite，MySQL和PostgreSQL。

cassandra-python-driver，开源分布式NoSQL数据库系统Apache Cassandra系统的Python驱动.pycassa,简化的cassandra数据库Python驱动。



HappyBase，友好的Apache [Hbase]的函数库。



PyMongo，MongoDB官方客户端。



Plyvel，LevelDB快速和功能丰富的Python接口。redis-py,redis客户端。



py2neo,Python客户端(基于Neo4j的RESTful接口).telephus,基于Twisted的cassandra客户端。



txRedis，基于Twisted的Redis客户端。



 【网络】Curl，Pycurl包是一个libcurl的Python接口，它是由C语言编写的。



与urllib相比，它的速度要快很多。



Libcurl是一个支持FTP, FTPS, HTTP, HTTPS, GOPHER, TELNET, DICT, FILE 和 LDAP的客户端URL传输库.libcurl也支持HTTPS认证,HTTP POST,HTTP PUT,FTP上传,代理,Cookies,基本身份验证,FTP文件断点继传,HTTP代理通道等等。



Requests，用Python语言编写，基于 urllib的开源 HTTP 库。



它比 urllib 更加方便，更加 Pythoner。



支持 Python3。httpie，命令行HTTP客户端，用户友好的cURL的替换工具。



s3cmd，命令行工具，用于管理Amazon S3和CloudFront。



youtube-dl，命令行程序，从YouTube下载视频。



you-get，Python3写的视频下载工具，可用于YouTube/Youku优酷/Niconico视频下载Coursera，从coursera.org下载视频，可重新命名文件wikiteam，wiki下载工具。



subliminal，命令行工具，搜索和下载字幕的函数库requests，HTTP函数库，更加人性化。grequests，异步HTTP请求+ Gevent（高性能高并发函数库）。

urllib3，一个线程安全的HTTP连接池，支持文件post。



httplib2，综合HTTP的客户端函数库。treq， Python API接口，Twisted的HTTP客户。



Mininet，流行的网络仿真器,API采用python编写。



POX，基于Python的开源软件定义网络（SDN）控制开发平台的应用，如OpenFlow的SDN控制器。



Pyretic，SDN的编程语言，提供了强大的抽象在网络交换机或仿真器。SDX Platform，基于SDN的IXP实现，利用最小网络，痘和热。inbox.py，Python的SMTP服务器。imbox， Python版本IMAP库。inbox，收件箱，开源邮件工具包。



lamson,SMTP服务器。flanker,侧卫,电子邮件地址和MIME解析库。



marrow.mailer,高性能可扩展邮件交付框架。



django-celery-ses， Django电子邮件后台，使用AWS SES和Celery。



modoboa，邮件托管和管理平台，包括现代和简化Web UI。



envelopes，邮件工具。



mailjet，批量邮寄mailjet API接口，带统计。Talon，利爪，Mailgun库，提取消息和签名。



mailjet- Mailjet API implementation for batch mailing, statistics and more., Talon - Mailgun library to extract message quotations and signatures.,pyzmail，编写，发送和解析电子邮件。



furl，燃料，小型的的URL解析库库。purl，简单的，干净的API，操纵URL。



pyshorteners，纯Python库，URL短网址编辑。



short_url，短网址生成。



Scrapy，快速屏幕截取和网页抓取的框架。



portia，波西亚，Scrapy的可视化扩展。



feedparser，信息源解释器RoboBrowser，简单的网页浏览Python函数库，没有使用Web浏览器。



MechanicalSoup，网站自动化互动测试工具包。



mechanize，网页浏览编程工具。



Demiurge，造物主，-PyQuery的轻量级工具。



newspaper,提取报纸新闻。html2text,转换HTML为 Markdown格式的文本。



python-goose,HTML内容提取器。



lassie,莱西,人性化的网站内容检索。



micawber,通过UR抓提网页的函数库。



sumy，概要，文本和HTML网页的自动文摘模块。



Haul，距离，可扩展的图像爬虫。



python-readability,可读性工具Arc90,快速的Python接口。



opengraph,OpenGraphProtocol协议解析模块,textract，从任何文件，Word，PowerPoint，PDF文件中提取文本，等。



sanitize，消毒，使混乱的数据变的理智。



AutobahnPython， WebSocket和WAMP的函数库，使用 Twisted和PythonWebSocket-for-Python，websocket客户端和服务器端函数库。SimpleXMLRPCServer，python标准库，简单的XML-RPC服务器，单线程。



SimpleJSONRPCServer，JSON-RPC规范实施函数库。



zeroRPC，基于ZeroMQ和MessagePack的RPC实现。



apache-libcloud，所有云服务的Python接口库。



wifi，WiFi -一套个Python库和命令行工具与WiFi，用于[Linux]。



streamparse，运行Python代码和数据的实时流。

集成了Apache Storm。

boto，亚马逊网络服务接口。



twython，Twitter推特API。google-api-python-client，谷歌客户端API。

gspread，谷歌电子表格的Python API。



facebook-sdk，facebook平台Python SDK。



facepy，简易的facebook图形APIgmail，Gmail的Python接口。



django-wordpress，Django的WordPress的模型和视图。



 【Web框架】Django，最流行的Python-Web框架，鼓励快速开发,并遵循MVC设计，开发周期短ActiveGrid企业级的Web2.0解决方案Karrigell简单的Web框架，自身包含了Web服务，py脚本引擎和纯python的数据库PyDBLitewebpy一个小巧灵活的Web框架，虽然简单但是功能强大CherryPy基于Python的Web应用程序开发框架Pylons基于Python的一个极其高效和可靠的Web开发框架Zope开源的Web应用服务器TurboGears基于Python的MVC风格的Web应用程序框架Twisted流行的网络编程库，大型Web框架QuixoteWeb开发框架Flask,轻量级web框架Bottle，快速，简单和轻量级的WSGI模式Web框架。



Pyramid，轻量级，快速，稳定的开源Web框架。



web2py，简单易用的全堆栈Web框架和平台。



web.py，强大、简单的Web框架。TurboGears，便于扩展的Web框架。



CherryPy，极简Python Web框架，支持，HTTP 1.1和WSGI线程池。

Grok，基于Zope3的Web框架。



Bluebream，开源的Web应用服务器，原名Zope 3。



guava，轻量级，高性能的Python-Web框架，采用c语言编写。



django-cms，基于Django企业级开源CMS。



djedi-cms轻量级但功能强大的Django CMS的插件，内联编辑和性能优化。



FeinCMS，基于Django的先进内容管理系统。



Kotte，高层次的Python的Web应用框架，基于Pyramid。Mezzanine，强大，一致，灵活的内容管理平台。



Opps，基于Django的CMS，用于高流量的报纸、杂志和门户网站。



Plone，基于Zope的开源应用服务器Zope。



Quokka，灵活，可扩展的，轻量级的CMS系统，使用Flask和MongoDB。



Wagtail，Django内容管理系统。



Widgy，CMS框架，基于Django。



django-oscar，Django奥斯卡，开源的电子商务框架。



django-shop，基于Django的网店系统。



merchant，支持多种付款处理工具。



money，可扩展的货币兑换解决方案。



python-currencies，货币显示格式。



cornice，Pyramid的REST框架。



django-rest-framework，Django框架，强大灵活的工具，可以很容易地构建Web API。



django-tastypie，创造精美的Django应用程序API接口。



django-formapi，创建JSON API、HMAC认证和Django表单验证。flask-api，提供统一的浏览器体验，基于Django框架。



flask-restful，快速构建REST API支持扩展。



flask-api-utils，flask的扩展。falcon，猎鹰，高性能的Python框架，构建云API和Web应用程序后端。



eve，夏娃，REST API框架，使用Flask，MongoDB和良好意愿。



sandman，睡魔，为现有的数据库驱动的系统，自动生成REST API。restless，类似TastyPie的框架。



savory-pie，REST API构建函数库（Django，及其他）Jinja2，现代设计师友好的语言模板。



Genshi，网络感知输出模板工具包。



Mako，马可，Python平台的超高速、轻型模板。



Chameleon，变色龙，一个HTML / XML模板引擎。



仿照ZPT，优化速度。



Spitfire，快速的Python编译模板。



django-haystack,大海捞针,Django模块搜索。



elasticsearch-py,Elasticsearch官方低级的Python客户端。



solrpy,solr客户端。



Whoosh,呼,快速，纯Python搜索引擎库。



Feedly，建立新闻和通知系统的函数库，使用Cassandra和Redis。



django-activity-stream,Django活动流,从你网站上的行动,产生通用的活动流。



Beaker，烧杯，一个缓存和会话使用的Web应用程序，独立的Python脚本和应用程序库。

dogpile.cache，是Beaker作者的下一代替代作品。HermesCache，Python的缓存库，基于标签的失效及预防Dogpile效果。



django-cache-machine，Django缓存机，自动缓存失效，使用ORM。django-cacheops，自动颗粒事件驱动，ORM缓存失效。johnny-cache,约翰尼高速缓存框架,Django应用程序。



django-viewlet,渲染模板部件扩展缓存控制。pylibmc,在libmemcached接口。



WTForms-JSON,JSON表单数据处理扩展。Deform， HTML表单生成的函数库。



django-bootstrap3，bootstrap3，集成了Django。django-crispy-forms，Django程序，可以创建优雅的表单。django-remote-forms，Django的远程表单，Django表格的序列化程序。



django-simple-spam-blocker，Django简单的垃圾邮件拦截器。



django-simple-captcha，Django简单验证码，简单的和高度可定制的Django应用程序，用于添加验证码图像Ajenti，服务器管理面板。



Grappelli，界面花哨的django皮肤。django-suit，Django替代o界面（仅用于非商业用途）。



django-xadmin，Django管理面板替代工具。



flask-admin，简单的flask管理界面框架flower，实时监控和Web管理面板。



Pelican，鹈鹕，Markdown或ReST，字王内容主题。支持 DVCS, Disqus. AGPL。



Cactus,仙人掌,设计师的网站静态生成器。



Hyde，海德， 基于Jinja2的静态网站生成器。



Nikola，尼古拉-一个静态网站和博客生成器。



Tags，标签，最简单的静态网站生成器。



Tinkerer，工匠，基于Sphinx的静态网站生成器。



asyncio，（在Python 3.4 +是Python标准库），异步I/O，事件循环，协同任务。



gevent，基于Python的网络库。



Twisted，扭曲，事件驱动的网络引擎。



Tornado，龙卷风，Web框架和异步网络的函数库。



pulsar，脉冲星，事件驱动的并行框架的Python。



diesel，柴油，绿色的，基于事件的I/O框架。



eventlet，WSGI支持异步框架。



pyzmq， 0MQ消息库的Python封装。



txZMQ,基于Twisted的0MQ消息库封Crossbar,开源统一应用路由器（WebSocket和WAMP）。



wsgiref，Python标准库，WSGI封装实现，单线程。



Werkzeug，机床，WSGI工具函数库，很容易地嵌入到你自己的项目框架。



paste，粘贴，多线程，稳定的，久经考验的WSGI工具。



rocket，火箭，多线程服务，基于Pyramid。



netius，快速的、异步WSGI服务器，gunicorn，forked前身，部分用C写的。



fapws3，异步网络，用C写的。meinheld，异步WSGI服务器，是用C写的。



bjoern，-快速的、异步WSGI服务器，用C写的。



 【安全】Permissions函数库，允许或拒绝用户访问数据或函数。



django-guardian,Django守护者，管理每个对象的权限，用于Django 1.2 +Carteblanche，管理导航和权限。



Authomatic，简单强大的认证/授权客户端。



OAuthLib， 通用，规范，OAuth请求签约工具。



rauth，用于OAuth 1.0，2.0，的Python库。



python-oauth2，利用全面测试，抽象接口来创建OAuth的客户端和服务器。



python-social-auth，易于安装的社会认证机制。



,django-oauth-toolkit,Django OAuth工具包django-oauth2-provider,Django OAuth2工具包。



django-allauth，Django认证的应用程序。



Flask-OAuthlib，Flask的OAuth工具包sanction，制裁，简单的oauth2客户端。



jose，[JavaScript]对象签名和加密(JOSE)草案实施，标记状态。



python-jwt，JSON的Web令牌生成和验证模块。



pyjwt，JSON的Web令牌草案01。



python-jws，JSON的Web令牌草案02。



PyCrypto，Python的加密工具包。



Paramiko，sshv2协议的实现，提供了客户端和服务器端的功能。



cryptography，密码开发工具包。



PyNac，网络和密码（NaCl）函数库。hashids，hashids的 Python函数库。



Passlib，安全的密码存储/哈希库，非常高的水平。



hashlib,md5, sha等hash算法，用来替换md5和sha模块，并使他们的API一致。



它由OpenSSL支持，支持如下算法：md5,sha1, sha224, sha256, sha384, sha512.



## GUI



PyGtk，基于Python的GUI程序开发GTK+库

PyQt用于Python的QT开发库

WxPythonPython下的GUI编程框架，其消息机制与MFC的架构相似,入门非常简单，需要快速开发相关的应用可以使用这个

TkinterPython下标准的界面编程包，因此不算是第三方库了



PySide，跨平台Qt的应用程序和用户界面框架，支撑Qt v4框架。

wxPython，混合wxWidgets的C++类库。



kivy，创建应用程序GUI函数库，看运行于Windows，Linux，MAC OS X，[Android]和[iOS]。



curse，用于创建终端GUI应用程序。



urwid，创建终端GUI应用程序窗体的函数库，支持事件，色彩丰富。

pyglet，跨平台的窗口和多媒体库的Python。



Tkinter，是Python事实上的标准GUI软件包。



enaml，创建漂亮的用户界面，语法类似QML。



Toga，托加，OS原生GUI工具包。【构建封装】



pyenv,简单的Python版本管理。



virtualenv,创建独立的Python环境，用于同时安装不同版本的python环境。



virtualenvwrapper，是virtualenv的一组扩展。



pew,一套管理多个虚拟环境的工具。



vex，使运行指定的virtualenv命令。



PyRun，一个单文件，无需安装的Python版本管理工具。



PIP，Python包和依赖的管理工具。



easy_install，软件包管理系统,提供一个标准的分配Python软件和 函式库的格式。是一个附带设置工具的模块，和一个第三方函式库。旨在加快Python函式库的分配程式的速度。类似Ruby语言的RubyGems 。



conda，跨平台，二进制软件包管理器。,



Curdling，一个管理Python包的命令行工具。



wheel，Python发行的新标准，旨在替代eggs.



cx-Freeze，跨平台的，用于打包成可执行文件的库



py2exe, Windows平台的Freeze脚本工具，Py2exe ，将python脚本转换为windows上可以独立运行的可执行程序



py2app，MAC OS X平台的Freeze脚本工具



pyinstaller，-转换成独立的可执行文件的Python程序（跨平台）。



pynsist,构建Windows安装程序的工具，用Python编写。



dh-virtualenv,建立和分发virtualenv(Debian软件包格式)

PyPI，新一代的Python包库管理工具。



warehouse,新一代的Python包库（PyPI）管理工具。



devpi，PyPI服务器和包装/测试/发布工具。



localshop，PyPI官方包镜像服务器，支持本地（私人）包上传。



buildout，创建，组装和部署应用程序的多个部分，其中一些可能是非基于Python的。



SCons，软件构造工具。



platformio，一个控制台的工具，构建的代码可用于不同的开发平台。



bitbake，特殊设计的工具，用于创建和部署[嵌入式]Linux软件包

fabricate，自动为任何编程语言，生成依赖包。



django-compressor，Django压缩机，压缩和内联JavaScript或CSS，链接到一个单一的缓存文件。



jinja-assets-compressor，金贾压缩机，一个Jinja扩展，通过编译，压缩你的资源。



webassets，优化管理，静态资源，独特的缓存清除。



fanstatic，球迷，包优化，提供静态文件。



fileconveyor，监控资源变化，，可保存到CDN（内容分发网络）和文件系统。



django-storages，一组自定义存储Django后台。



glue，胶胶，一个简单的命令行工具，生成CSS Sprites。



libsass-python，Sass (层叠样式表)的Python接口。



Flask-Assets，整合应用程序资源。【代码调试】



unittest，Python标准库，单元测试框架。



nose，鼻子，unittest延伸产品。



pytest，成熟的全功能的Python测试工具。



mamba，曼巴，Python的权威测试工具。出自BDD的旗下。



contexts，背景，BDD测试框架，基于C#。



pyshould，should风格的测试框架，基于PyHamcrest.



pyvows，BDD风格测试框架



Selenium，web测试框架，Python绑定Selenium。



splinter，分裂，测试Web应用程序的开源工具。



locust，刺槐，可扩展的用户负载测试工具，用Python写的。



sixpack，语言无关的A/B测试框架。



mock，模拟对象（英语：mock object，也译作模仿对象），模拟测试库。



responses，工具函数，用于mock模拟测试。



doublex-强大的测试框架。



freezegun，通过时间调整，测试模块。



httpretty， HTTP请求的模拟工具。



httmock，mock模拟测试。



coverage，代码覆盖度量测试。



faker，生成模拟测试数据的Python包。



mixer，混频器，产生模拟数据，用于Django ORM，SQLAlchemy，

Peewee, MongoEngine, Pony ORM等



model_mommy，在Django创建测试随机工具。



ForgeryPy，易用的模拟数据发生器。



radar，雷达，生成随机日期/时间。



FuckIt.py，测试Python代码运行。



Code Analysispysonar2，Python类型索引。



pycallgraph,可视化的流量（调用图）应用程序。



code2flow,转换Python和JavaScript代码到流程图。



LinterFlake8，源代码模块检查器

pylama，Python和JavaScript代码审计工具。



Pylint，源代码分析器，它查找编程错误，帮助执行一个代码标准和嗅探一些代码味道。注意：相比于PyChecker，Pylint是一个高阶的Python代码分析工具，它分析Python代码中的错误。



Pyflakes，一个用于检查Python源文件错误的简单程序。Pyflakes分析程序并且检查各种错误。它通过解析源文件实现，无需导入。



pdb,Python标准库,Python调试器。



ipdb,IPython使用的PDB。



winpdb独立于平台的GUI调试器。



pudb，全屏，基于python调试控制台。



pyringe，-可附着于及注入代码到Python程序的调试器。



python-statsd，statsd服务器客户端。



memory_profiler， 内存监视。



profiling，交互式Python分析器。



django-debug-toolbar, Django调试工具栏,显示各种调试信息:当前请求/响应。



django-devserver,Django调试工具。



flask-debugtoolbar,flask调试工具。
