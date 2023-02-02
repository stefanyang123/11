#类对象所拥有的方法，需要@staticmethod 来表示静态方法，静态方法不需要任何参数,需要的时候也可以传
class People:
    country='中国'
    # 类方法 用@classmethod方法
    @classmethod  #加上这个修饰器后，方法的所有权归类对象所有，实例对象仍有使用权，但无修改权
    def get_country(cls):
        return cls.country  #通过类对象访问这个类属性
        pass

    @classmethod
    def change_country(cls,data):
        cls.country=data
        pass
    pass

    @staticmethod  #设置一个没参数的静态方法
    def getData():
        return People.country #通过类对象去引用
        pass

    @staticmethod  #设置一个有参数的静态方法
    def add(x, y):
        return x + y
        pass

print('通过类对象调用静态方法',People.getData())
p=People()
print('通过实例对象调用静态方法',p.getData())
print(People.add(10,20))
# 既然声明为一个静态方法，它归属于类对象，用类对象访问即可
# 为了减少资源的开销一般情况下我们不会通过实例对象去访问静态方法，因为还有实例化对象
# 当对象执行一个方法时，会先在实例方法里找，找不到去他所属的类去找，类里找不到去它的父类去找
#为什么要是有静态方法
# 由于静态方法主要来存放逻辑性的代码，本身和类以及实例对象没有交互
# 在静态方法中一般不会涉及到类中方法和属性的操作，不需要和实例对象有交互
# 能让数据资源能够得到有效的利用

# demo  返回当前的系统时间
import time    #import引入第三方的时间模块
class TimeTest:
    def __init__(self,hour,min,second):
        self.hour=hour
        self.min=min
        self.second=second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S",time.localtime())
        # strftime格式化时间成 小时 分钟 秒  time.time给系统当前的时间
        pass
    pass
print(TimeTest.showTime())
# 可以看到，这里的功能时独立的，并没有用到我们定义的实例属性
time1=TimeTest(22,10,3)
print(time1.hour)


# 从方法定义的形式可以看出来
# 类方法的第一个参数必须是是类对象 cls 进而去引用类对象的属性和方法
# 必须要用装饰器@classmatheod来修饰

# 实例方法的第一个参数必须是self，通过self 可以去引用类属性或实例属性，
# 若存在相同名称实例属性，类属性的话，优先使用实例属性，实例属性的优先级最高

# 静态方法不需要定义额外的参数，若是要引用静态方法的话，可以通过类对象或是实例对象去引用即可
# 必须要用装饰器@staticmathod来修饰


