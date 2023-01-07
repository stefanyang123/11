# 序列
# 是什么？ 在python中，一组按顺序排列的值（一个数据集合）
# python中 存在三种内置的序列类型：字符串，列表，元组。（字典不属于序列的范畴）
# 特征：支持索引和切片的操作
#      第一个正索引为0，指向的是左端，第一个索引为负数，指向的是右端

# 切片
# 是指 截取字符串其中一段 的内容
# 使用方法
# [起始下标:结束下标:步长]
#    截取的内容 不包含 结束下标对应的内容
#    步长指的是 隔几个下标 获取一个字符，默认步长1
# 特性：可以根据下标来获取序列对象的任意[部分]数据

# 字符串使用
# 字符串有自己的下标，从零开始，也就是有索引的

# 字符串常用的函数
# 使用方法  字符串名.函数

# 首字母变大写                 是否以..开始/结束
# capitalize()              endswith/stars with()

# 检测...是否在字符串中         判断是否是字母和数字
# find()                    isalnum()

# 判断是否是字母和数字           判断是否是字母
# isalnum()                  isalpha()

# 判断是否是数字                判断是否是小写
# isdigit()                  islower()

# 循环取出所有值用...去连接       大小写转换
# join()                     lower/upper

# 大写变小写，小写变大写          去除字符串 左/右/两侧空格
# swapcase()                   lstrip/rstrip/strip

# 以...切割字符串                 把每个单词的首字母变成大写
# split(...)                    title()

# old被换字符串，new替换字符串,无count表示全部替换
# replace(old,new,count=None)

# 统计出现的次数
# count()

print('------字符串------')
# 函数的使用
Test='python'             #或者""都行
print(type(Test))
Test[0]   #用一个下标去取第一个字符
print('获取第一个字符%s'%Test[0])
print('获取第二个字符%s'%Test[1])

for item in Test:
    print(item,end=' ')

print('')

print('------常用于字符串的函数------')
print('')
print('首字母变大写')
# 首字母变大写
# capitalize()
name='peter'
print('姓名首字母转换大写%s'%name.capitalize())

print('去除字符串 左/右/两侧空格')
# 去除字符串 左/右/两侧空格
# lstrip/rstrip/strip
a='    hello    '
b=a.strip()    #字符串a去除完两侧空格后赋值给b了
print(a)
print(b)
print(a.lstrip())   #删左
print(a.rstrip())   #删右

print('复制字符串')
# 复制字符串
b=a  #在此只是吧a对象的内存地址赋给了b
print(b)
print('a的内存地址%d'%id(a))      # id()函数可以查看一个对象的内存地址  a的内存地址
print('b的内存地址%d'%id(b))
# 结果显示a,b内存地址一样  因此a,b是同一个对象，因为是对一个内存地址数据的引用（指向同一内存地址）

print('检测...是否在字符串中')
# 检测...是否在字符串中
# find()
data='y byw'    #立面有个空格也算一个字符
data.find('y')
print(data.find('y'))  #会返回首个'y'对应的下标值 找到立马返回  没找到返回-1
# index()
print(data.index('b')) #会返回首个'y'对应的下标值 找到立马返回  没找会报异常，与find不一样

print('是否以..开始/结束')
# 是否以..开始/结束
# endswith/starswith()
print(data.startswith('y'))     #判断是否以y开头，返回布尔类型的数据，属于一个判断
print(data.endswith('y'))       #判断是否以y结尾


print('将字符串全变成大写')
#将字符串全变成大写
print(data.upper())


print('切片')
strMsg='hello world'
print(strMsg)  #输出完整数据
print(strMsg[2:5])  #输出字符串第二个到第5个之间的数据 不包括第五个空格
print(strMsg[2:])  #输出字符串第二个一直取到最后
print(strMsg[:3])  #输出字符串开头到第三个字符串，或者print(strMsg[0:3])
print(strMsg[::-1])  #倒着输出



























