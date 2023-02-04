# __new__方法
# 创建并返回一个实例对象，如果__new__只调用了一次，就会得到一个对象。继承自object的新式类才有new这一魔术方法
# __new__至少要有一个参数cls,代表要实例化的类，此参数在实例化时由python解释器自动提供，其他的参数时用来直接传递给__init__方法
# __new__决定是否要使用该__init__方法，因为__new__可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例
# 如果__new__没有返回实例对象，则__init__不会被调用
# 在__new__方法中，不能调用自己的__new__方法，即：return cls.__new__(cls),否则会报错(超过最大递归深度)
class Animal:
   def __init__(self):
       self.color='红色'
       pass

   #如果在python中如果不重写  new 默认结构如下
   def __new__(cls, *args, **kwargs):
       return super().__new__(cls,*args, **kwargs)  #super是调用父类
       # return object().__new__(cls, *args, **kwargs)  或者用object()去创建
   pass
tigger=Animal()   #默认情况下，实例化的过程会自动调用  new 去创建实例
# 在新式类中，__new__ 才是真正的实例化的方法，它为类提供外壳制造出实例框架，然后调用该框架内的构造方法__init__进行丰满操作
# __new__ 负责开发地皮打地基，并将原料存放在工地。__init__ 负责从工地取材料，建造出地皮开发图纸规定的大楼，负责细节设置

# 单例模式
# 单例模式是常用的软件设计模式，单例就比如我们打开电脑的回收站，在系统中只能打开一个回收站，也就是说这整个系统中只有一个实例。重复打开也是使用这个实例
# 简单的说就是不管创建多少次对象，类返回的都是最初创建的，不会再新建其他对象

# 创建单例对象  __new__去实现 （推荐的一种）
class DataBaseCass(object):  #继承一个超类 object
    def __new__(cls, *args, **kwargs):
        # cls._instance=_instance=cls.__new__(cls)  不能使用自身的new方法
        # 容易造成一个深度递归，应该调用父类的new方法
        if not hasattr(cls,'_instance'):  #如果不存在对象_instance就开始创建
            cls._instance=super().__new__(cls, *args, **kwargs)  #调用一个父类__new__方法生成一个实例对象
        return cls._instance
    pass
ab1=DataBaseCass()
print(id(ab1))
ab2=DataBaseCass()
print(id(ab2))    #发现出现了两个对象，我们的目的是要一个对象




















