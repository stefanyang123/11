# 所谓重写，就是子类中，有一个父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法
# 为什么要重写，父类的方法已经不满足子类的需要了，那么子类就可以重新父类或者完善父类的方法
class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color


    def bark(self):
        print('汪汪叫....')
        pass
    pass
class Kjquan(Dog):
    def __init__(self,name,color,weight): #属于重写父类的方法，保留父类属性的同时，可以扩展子类其他属性
        """
        当你的子类有__init__函数，会覆盖父类__init__
        但你又需要父类中的name,color参数，不想再重新写，又想有子类自己的独有参数时
        要调用父类的函数
        """
        Dog.__init__(self,name,color)#手动调用Dog 调用父类的方法 执行完毕就可以具备name,color这两个父类的实例属性了
        #已经调用了父类的方法了，执行完毕就可以具备name,color这两个实例属性了
        # #拓展子类其他属性
        self.height=90
        self.weight=weight
        # 这是另一种父类构造函数
        # # super是自动找到父类Dog，进而调用方法，假设继承了多个父类，那么会按照继承顺序逐个的去找，找到后再调用
        # super().__init__(name,color)
        # pass

    def bark(self):  #属于重新父类的方法
        super().bark() #调用父类的bark()方法
        print('叫的跟神一样')
        pass
    pass

kj=Kjquan('柯基','红色','80')
kj.bark()
print(kj.name,kj.color,kj.weight)
