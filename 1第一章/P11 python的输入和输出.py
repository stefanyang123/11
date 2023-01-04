print('python的格式化输出')  #运行结果分行，方便复习看
# python 有一个简单的字符格式化方法，使用%做占位符，%后面跟的是变量的类型
# 格式化输出 用%占位符  %s   这个s是跟在%后面的变量类型str
#                   %d   数字类型
#                   %f   浮点实数
# 在输出的时候，如果有\n那么，此时\n后面的内容会在另外一行显示
name='杨博文'
classpro='黑科技'
age=103
print('我的名字是%s：来自[%s],今年%d岁了'%(name,classpro,age))
# \n 换行输出  \转义符号  \\n 则不会换行
print('我可以\n换行吗？')
print('我可以\\n换行吗？')
print('我叫%s'%name)
"""
格式符号     转换  
%c         字符
%s         通过str()字符串转换来格式化
%i         有符号十进制整数
%d         有符号十进制整数
%u         无符号十进制整数
%o         八进制整数
%x         十六进制整数（小写字母）
%e         索引符号（小写e）
%E         索引符号（大写E）
%f         浮点实数
%g         %f和%e的简写
%G         %f和%E的简写
"""
print('')
print('练习题')  #运行结果分行，方便复习看
# 尝试输出
# =========================
# 姓名：小杨
# QQ:1520719580
# 手机号码：15816807958
# 公司地址：广东
# =========================
# 答案
Name='小杨'
QQ=1520719580
phoneNumber=15816807958
addr='广东'
print('=========================')
print('姓名：%s\nQQ:%d\n手机号码：%d\n公司地址：%s'%(Name,QQ,phoneNumber,addr))
print(addr,type(addr))
print('=========================')

# print(变量1,变量2,....变量n)输出后的各变量用空格分割
value=123.45
print(value,'python',value,value)

#print()函数子啊输出文本时默认会在最后增加一个换行
# 如果不希望换行 可以用print()函数的end参数进行赋值
print('待输出的内容',end='增加的输出结尾')
a=10
print(a,end='$')
print(a,end='%')
print(a)     #以上三行在同一行输出
print(a)     #另开一行输出

print('')
print('格式化输出的其他方式 .format() 不需要再去指定数据类型了方便些')  #运行结果分行，方便复习看
# 格式化输出的其他方式  .format(变量1,变量2,....变量n)
print('===========format输出形式==============')
print('姓名：{} 年龄是：{}'.format(name,age))
print('QQ：{}'.format(QQ))
print('手机号：{}'.format(phoneNumber))
print('地址：{}'.format(addr))
print('===========format输出形式==============')


print('')
print('python的输入')  #运行结果分行，方便复习看
# python中提供了input方法来获取键盘输入
# input 接收的键盘输入结果都是str类型的，如果接收数字类型需要将str转成int


Name=input("请输入您的姓名")
QQ=input("请输入您的QQ")
phoneNumber=input("请输入您的电话号码")
addr=input("请输入您的地址")
print('===========报告单如下==============')
# 注意这里都改成了%s,因为input接收的键盘输入结果都是str类型的
print('姓名：%s\nQQ:%s\n手机号码：%s\n公司地址：%s'%(Name,QQ,phoneNumber,addr))
print('=================================')
# 若用%d则代码应是这样
# QQ=int(input("请输入您的QQ"))
# phoneNumber=int(input("请输入您的电话号码"))
# print('姓名：%s\nQQ:%d\n手机号码：%d\n公司地址：%s'%(Name,QQ,phoneNumber,addr))
