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
        print('-----init-------执行了')
        pass
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
    def __new__(cls, *args, **kwargs):  #在实例化的过程中首先会执行这个函数如果，我们没有声明这个函数时，。编译器会自动创建
        """                             #一旦声明，编译器会执行我们声明的这个函数
        创建对象实例的方法，每调用一次就会生成一个新的对象cls就是class的缩写

        场景:可以控制创建对象的一些属性限定 经常用来做单例模式（单个对象）的时候使用
        :param args:
        :param kwargs:
        """
        print('------new--------执行了')
        # object.__new__(需要新建对象的类)
        # object.__new__(cls)  #cls当前这个类  创建当前这个类的一个对象
        return object.__new__(cls) #创建完要 返回return 后面等着用
        pass
xw=Person('小明','西瓜','宿管')
print(xw)
# 从运行结果也可以看出，是先运行new（第一个被执行的） 再运行init的（第二个）
# new 先有了对象，再返回，给init
#  __new__和__init__的区别
# __new__ 类的实例化方法，必须要返回return实例（对象）否则对象创建不成功
# __init__用来做数据属性初始化工作，可以认为时实例的构造方法，接受类的实例，通过self并对其进行构造
# __new__至少有一个参数时cls，代表要实例化的类,此参数再实例化时有python解释器自动提供
# __new__执行要早于__init__