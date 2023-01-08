# 参数分类
# 必选参数，默认参数[缺省参数]，可选参数，关键字参数
# 参数：其实就是函数为了实现某项特定的功能，进而为了得到实现功能所需要的数据



# 1.必选参数
def sum(a,b):    #a,b形式参数：只是意义上的一种参数，在定义的时候是不占内存地址的
    sum=a+b
    print(sum)
    pass
# 函数调用
sum(20,15)       #20和15 是我们的实际参数，实实在在的参数，是实际占用内存地址的
# sum()   不能不写参数，ab是必选参数，是必须要赋值的



# 2.默认参数（缺省参数）始终在参数列表尾部
def sum1(a=20,b=30):   #默认参数a=20 b=30  如果一个有默认值一个没有，默认值要放后面
    print(a+b)
    pass
# 默认参数的调用，这三种都行在调用的时候如果未赋值，就会用定义函数时给定的默认值
sum1()
sum1(10)
sum1(1,2)




# 3.可变参数（当参数的个数不确定时使用）
# 给你的参数加个*  参数是一个元组类型
def getjs(*args):      #可以随意取参数名，一般用args
    '''
    计算累加和
    :param args:可变长的参数类型
    :return:
    '''
    print(args)
    result=0
    for item in args:
        result+=item
        pass
    print('resule={}'.format(result))
    pass

getjs(1,2)
getjs(1)          #gs是一个元组
getjs(1,2,3,4,5)
a=(1,)            #声明一个元组，要想将元组传进去，变量前必须加*
getjs(*a)
getjs(*(2,))



# 关键字可变参数
# **来定义
# 在函数体内  参数是一个字典类型且字典的key是一个字符串
def keyFunc(**kwargs):   #可以随意取参数名，一般用kwargs
    print(kwargs)
    pass
# 调用
# keyFunc(1,2,3)  这样的参数不可以传递
dictA={'name':'he','age':35}
keyFunc(**dictA)      #想要将字典型传进去，变量前必须加**
keyFunc(name='he',age=35)      #想要将字典型传进去，通过键值对来传
keyFunc()             #不传也可以，因为可变可以是0-n个




# 组合的使用
def complexFunc(*args,**kwargs):
    '''
    可选参数*args必须放到关键字可选参数**kwargs之前
    可选参数*args,接收的是一个元组类型
    关键字可选参数**kwargs，接收的是一个字典类型
    :param args:
    :param kwargs:
    :return:
    '''
    print(args)
    print(kwargs)
    pass
complexFunc(1,2,3,4,name='刘德华')
complexFunc()
complexFunc(age=36)


# def complex(**kwargs,*args):   会报错 可选参数必须放到关键字可选参数之前
#     print(args)
#     print(kwargs)
#     pass
# complex(1,2,3,4,name='刘德华')
# complex()
# complex(age=36)



