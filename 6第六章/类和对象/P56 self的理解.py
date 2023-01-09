# self和对象指向同一个内存地址，可以认为self是对象的引用
# 实例化对象时，self 不需要开发者传参，python自动将对象传递给self
class Person:
    """
    定义类
    """
    def __init__(self,pro):   #pro在这里是用来传递参数的改成pr也行
        self.pro=pro        #xw=self  相当于xw. pro实体属性 = pr参数

    def getid(self):  #只要是在类里定义，第一个参数是self的就是 实例方法
        """
        实例方法
        :return:
        """
        print('self=%s'%id(self))      #self是一个Person对象
    def eat(a,name,food):
        print('%s喜欢吃%s,它的专业是%s'%(name,food,a.pro)) # xw=a
        pass
    def run(b):
        print('self的名字可以更改,但总是在参数的第一位')
    pass
xw=Person('信管')

print('xw=%s'%id(xw))
xw.getid()  #内存地址相同 所以 self指向实例对象本身
xw.eat('小王','榴莲')
xw.run()

# 小结
# self只有在类中定义 实例方法的时候才有意义
# 调用的时候不必传入相应的参数 而是有解释器自动去指向
# self的名字可以更改，可以定义成其他的名字，只是约定俗成的定义成了 self
# self 指的是对象本身
