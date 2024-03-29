#### 文件的基本操作：

**open（）** --打开 **注：**在括号里填入绝对路径（或者相对路径)/文件名，需要在前边给变量名赋值，才可以去操作文件，在open传入的参数都是以字符串方式传入进去。

**文件对象去点close（）** --关闭，打开文件后执行完代码需要去关闭 如果不关闭会对内存有影响

**注：**在打开文件open（）括号走除了文件还要写入执行的方法（只读取 写入），

**r** --以读取模式打开文件 在打开命令中后边参数中不填写r也会默认是r
**r+** --读取写入模式，同w+一样但不会创建新文件
**w** --写入模式，在打开命令产生中填入w是以写的模式去打开这个文件。注：w模式是只写入模式 不可以读取
**w+** --写入读取模式，读取光标后边的内容，如果写入内容后 需要读取应先调整光标位置，如果没有这个文件会创建文件，这个命令会覆盖掉里边的内容。
**a** --追加模式，没有文件同样会创建，没有读取的功能只能追加内容，如果文件已存在光标会防止文件结尾，如果没有这个文件，会创建文件进行写入。
**a+** --追加写入读取模式
**注：**在追加模式中用write命令可以在文件后边增加内容

**变量名点read（）**  --读取，读取文件的所有内容，需要定义变量赋值，括号里可以填入数值指定读取几个，
**变量名点readline（）** --只读取一行。
**变量名点readlines（）** --读取所有，**注：** 把每行作为列表中的值返回给变量，读取模式中光标是在第一行的位置，如果前边执行过读取的命令，光标会跳到读取过内容的后边 这个命令只会执行光标后边的内容去返回。
**变量名点seek（）** --设置光标的位置 **注：**括号里默认为0 也就是文件第一个字符前边
**变量名点write（）** --写入 括号里边填入写入的内容。
**变量名点flush（）** --刷新缓存，有时候调整光标位置或增加内容后会出现没执行问题可以刷新缓存来解决 。
**变量名点tell（）** --或得光标所在位置，返回数字，数字表示在第几个字符
**rb，rb+，wb，wb+，ab，ab+** 以二进制去操作文件

**注：**在以读的模式用二进制打开文件，如果放的是字符串格式，就以字符串显示，如果是二进制写的就以二进制打开（写入二进制需要在字符串前边的引号加b）



#### **StringIO流:**

**导入io模块（io为小写）**
**io,StringIo（）** --定义变量去接收，不需要绝对路径，它是虚拟的只存在于内存中，只是个临时文件，一但关闭写入的文件直接没有了。文本文件
**变量名点getvalue（）** --赋值给另一个变量，打印赋值给的变量可以直接查看其中内容，不用在去调整光标去查看
**io,BytesIO（）** --定义变量去接收，二进制文件

#### 上下文件管理：

**with open（‘文件名’，‘模式’）as 变量名：** --冒号下边缩进写执行代码，**注：**变量名就是open（）赋值给的变量名。会自动关闭文件 不用在close去写文件关闭
**注：**在写代码的时候，在with命令中变量名后边冒号前边加逗号（或直接回车，回车后需要自己在反斜杠前边加逗号）写上 **open('文件名‘，’模式‘） as 第二个文件变量名**，可以同时管理第二个文件，多个文件同理在冒号前边加逗号回车。不要在打开一个文件的时候在一个with中写 会出现一些问题

#### 常见问题处理：

在with open（文件名，模式，encoding=‘编码‘） as  f：--中的编码属于执行with命令中代码规定安什么编码去执行
**注：**如果用两个with命令去打开一个文件如果编码不一样会出现报错 报编码错误。
**注1:**在with括号里边后边在加上errors=’ignore‘ 忽略编码模式 不会报错  但读取的会出现乱码

**os模块的目录及文件操作：**

**导入os模块（os小写）**
**os点system（）** --系统，括号里输入执行的命令字符串，会执行命令
**os点getcwd（）** --获取当前路径
**os点listdir（path）** --展示当前目录
**os点chdir（path）** --改变当前路径
**os点mkdir（文件名）** --创建目录
**os点rmdir（文件名）** --删除目录
**os点remove（文件）**--删除文件
**os点rename（）** --重命名

#### os点path模块：

**os点path点join（’文件名‘，文件名’，‘文件名’）** --自动在文件名和文件名之间加个斜杠也就是路径，只会把两文件名变量拼接如果是最顶层的目录前边需要 / 需要自己去写
**dirname**  --所在目录/父级目录
**basename**  --基本短路径
**abspath** --绝对路径
**relpath** --相对路径
**getsize** --资源大小
**getctime** --创建资源时间
**getatime** --访问资源时间
**getmtime** --修改资源时间
**isfile** --括号里是丢路径，判断是不是文件
**isdir** --判断是不是文件夹（目录）
**isabs** --判断是否是绝对路径


