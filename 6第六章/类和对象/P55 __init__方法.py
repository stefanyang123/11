class People:
    def eat(self):
        """
        吃的行为
        :return: 
        """
        print('喜欢吃榴莲')
    pass

xq=People()
xq.eat()
xq.name='小倩'   #可以在class外，添加实例属性name
xq.sex='女生'
print(xq.name,xq.sex)

xl=People()
xl.name='小丽'
xl.sex='女生'
print(xl.name,xl.sex)

#如果有n个这个对象 被实例化 那么需要添加很多次这样的属性了，很不方便
print('--------__init__(self)---------')
# __init__(self)初始化方法，实例化对象的时候自动调用，完成一些初始化设置
class Dog:
    def __init__(self):     #__init__凡是这样的形式的 属于魔术方法
        """
        实例属性
        """
        self.name='旺财'
        self.colour='黄色'
    pass

xg=Dog()         #__init__在创建对象的时候是自动执行的
xg.name='财神'    #这里相当于重新给变量name赋值  name初始值为'旺财'
xg.colour='绿色'
print(xg.name,xg.colour)


print('--------__init__(self，参1，参2...)传参---------')
class Peolll:
    def __init__(self,name,age):     #__init__凡是这样的形式的 属于魔术方法
        """
        实例属性
        """
        self.name=name
        self.age=age
    pass
    def eat(self,food):   #不止是__init__可以传递参数，其他方法也可以
        print(self.name+'喜欢吃'+food)
        #在另外一个函数里,使用事先已经定义好的实例属性self.name
p1=Peolll('小明',12)
p1.eat('苹果')
print(p1.name,p1.age)
p2=Peolll('小花',18)
p2.eat('梨子')
print(p2.name,p2.age)


# 总结__init__
# 1.python 自带的内置函数 具有特殊的含义，用双下划线包起来的[魔术方法]
# 2.是一个初始化的方法，用来定义实例属性和初始化数据的，在创建对象时自动调用的，不用手动调用
# 3.利用传参的机制，可以让我们定义 功能更加强大并且方便的 类














