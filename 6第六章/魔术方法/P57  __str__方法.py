# python中，有一些内置好的特定方法，方法名是'__XXX__',在进行特定的操作是会被自动调用，这些方法称之为魔法方法
# __str__方法  自定义格式输出
class Person:
    """
    定义类
    """
    def __init__(self,name,food,pro):   #pro在这里是用来传递参数的改成pr也行
        """

        :param name: 姓名
        :param food: 食物
        :param pro: 专业
        """
        self.name=name
        self.pro = pro  # xw=self  相当于xw. pro实体属性 = pr参数
        self.food=food
    # 如果你想后来想修改name food用
    def eat(self,name,food):
        print('%s喜欢吃%s,它的专业是%s'%(name,food,self.pro)) # xw=self
        pass
    #如果你想遵照默认值 用
    # def eat(self,name,food):
    #     print('%s喜欢吃%s,它的专业是%s'%(self.name,self.food,self.pro)) # xw=self
    #     pass

    def __str__(self):   #常用于需要查看对象时
        """
        打印对象  自定义对象的内容格式
        :return:
        """
        return '%s喜欢吃%s,它的专业是%s'%(self.name,self.food,self.pro)
        pass




xw=Person('小明','西瓜','宿管')
print('----如果类里没有__str__这里会输出xw的内存地址----')
print('常用于需要查看对象时')
print(xw)
# 为什么每个方法第一个参数约定俗成都用self？
# 1.因为他们都指向同一个对象，虽然它们不一定要命名为self， 但为了统一，方便，还是都叫self好点，(你也可以都叫a)当然每个实例方法里的self的作用域只是在本方法里。
# 2.每次调用方法(类中的函数)时，self会自动将对象传入方法里，因此这样的方法也叫实例方法
# 3. 对象.方法/属性 的形式在，类，里都可以使用，用来调用实例方法，或者实例属性 。self在实例函数里只是替代了对象的位置,成为负责传递对象的参数