# 函数的4种基本类型
"""
1.无参数，无返回值
一般用于打印信息
def myprint():
    print("-"*20)
2.无参数，有返回值
多用在数据采集，比如获取信息系统
def mycpu():
    #获取cpu信息
    return info
3.有参数，无返回值
多用在设置某些不需要返回值的参数设置
def set(a):
    pass
4.有参数，有返回值
一般是计算型的，需要参数，最终也要返回结果
def cal(a,b)
    c=a+b
"""



#局部变量(在函数内部定义的变量，【作用域仅仅局限在函数内部】)
# 不同函数内可定义相同的局部变量,各自用各自的不会产生影响
# 作用：为了临时的保存数据，需要在函数中定义来进行存储
# 当全局变量和局部变量出现重复定义时，程序会优先执行使用函数内部定义的变量
# 如果在函数内部要想对全局变量进行修改的话，必须用global关键字进行声明，不修改直接拿来用也没问题
overvalue='全局变量'
def printInfo():
    name='局部变量1'
    print('{}'.format(name))
    pass
# print(name)会报错，因为name是在函数里定义的，属于局部变量
printInfo()    #name变量的作用域仅限于函数printInfo内
print(overvalue)
def textInfo():
    name='局部变量2'
    print('{}'.format(name))
    pass
textInfo()     #两个name变量虽然名字相同，但没有关系互不干扰


print('--'*20)
# 全局变量   作用域的范围不同
overvalue='全局变量1'
def printInfo1():
    name='局部变量3'
    print('换行输出\n{}\n{}'.format(name,overvalue))
    pass
printInfo1()

# 当全局变量和局部变量出现重复定义时，程序会优先执行使用函数内部定义的变量
print('-'*10+'全局变量与局部变量名一致时，优先用函数内的变量'+'-'*10)
name='全局变量1'
def printInfo2():
    name='局部变量3'
    print('换行输出\n{}\n{}'.format(name,overvalue))
    pass
printInfo1()

print('-'*10+'修改全局变量'+'-'*10)
def changeGlobal():
    """
    要修改全局变量
    :return:
    """
    # name='修改全局变量1'  之这样写修改不了，这个相当于定义了个局部变量，跟外部没有关系
    global name         #这里用global关键字告诉解释器，要修改的是全局的name变量
    name='修改全局变量'
    pass
changeGlobal()
print(name)









