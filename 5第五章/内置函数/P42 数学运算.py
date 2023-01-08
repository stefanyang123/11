# 内置函数就是python自带的函数
# https://docs.python.org/3/library/functions.html
# 访问这个官网网址，所有内置函数
# abs()求绝对值
# all()获取所有
# any()获取任意一个数据
# ascii()ascii码
# bin()二进制转换
# bool()布尔类型的转换
# chr()查看十进制数对应的ascii码

print('----------abs()--------------')
# 常用数学运算函数
# abs()绝对值
print(abs(-10))


print('------------round()-------------')
# round()对浮点数进行近似取值，保留几位小数
# round(x[,n]) x--数值表达式 n--数值
# 返回X的近似值  四舍六入
print(round(2.56,1))    #2.56保留一位小数2.6
print(round(2.55,1))    #2.55保留一位小数2.5

print('-----------pow()--------------')
# pow()求幂运算
# pow(x,y[,z])返回X的Y次方的值
print(pow(3,3))
print(pow(3,3,9))  #算完三的三次方后再除以九的余数
print(3**3)   #这样也行

print('-----------divmod()--------------')
# divmod()求商和余数
print(divmod(9,3))#返回包含商和余数的元组（3，0）


print('-----------max()--------------')
# max()最大值
# 返回给定的参数的最大值，参数可以是序列
print(max(-1,0,3,4,5,6,))
print(max([12,23,56,89,-12]))

# min()最小值  同理



print('-----------sum()--------------')
# sum()对系列进行求和计算
# sun(iterable[,start])
# iterable--可迭代对象，可以遍历如列表 元组 集合
# start--指定相加的参数，如果没有设置这个值默认为0
print(sum([0,1,2],2))
#0+1+2+2
print(sum((1,2,2),3))  #可迭代对象要放前面

print(sum(range(50),3)) #0+.....+50+3

print('----------eval()--------------')
# eval()动态执行字符串表达式
# eval(expression[,globals,locals])
# expression--表达式
# globals--变量作用域，全局命名空间，如果被提供，则必须是个字典对象
# locals--变量作用域，局部命名空间，可以是任何映射对象
# 返回表达式计算结果
# 去掉字符串最外侧的引号，按照python语句的方式去执行引号内的内容

a,b,c=1,2,3
print(eval('a+b+c'))#文本变代码

def TestFun():
    print('我执行了吗？')
    pass

eval('TestFun()')  #通过eval函数是可以执行我定义函数的，也就是里面字符串形式的代码
print(eval('a+b+c',{'c':3,'a':2,'b':3}))

# 如果直接a=eval('python')会报错
# 因为eval()函数在处理'python'时，字符串去掉了两边的引号，python语句
# 将其解释为一个变量，由于这个变量没有定义，因此报错
# 正确方法
python=3
a=eval('python')
print(a)

# 变量=eval(input(提示性文字))
# 用户输入的数字，包括小数和负数，input()解析为字符串，再由eval()
# 去掉字符串引号，将被直接解析为数字保存到变量中





