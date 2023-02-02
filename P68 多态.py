# 多态  多种状态，形态
# 同一种行为，对于不同的子类（对象）有不同的行为表现
# 要想实现多态 必须有两个前提需要遵守
# 1.继承：多态必须发生在父类和子类之间
# 2.重写：子类重写父类的方法
# 案例：
class Animal:
    """
    父类（基类）
    """
    def say_who(self):
        print('我是一个动物.....')
        pass
    pass
class Duck(Animal):
    """
     鸭子类（子类）派生类
    """
    def say_who(self):
        """
        这里重写父类的方法
        :return:
        """
        print('我是一只鸭子')
        pass
    pass
class Dog(Animal):
    """
     狗子类（子类）派生类
    """
    def say_who(self):
        """
        这里重写父类的方法
        :return:
        """
        print('我是一只狗子')
        pass
    pass
class Cat(Animal):
    """
     猫子类（子类）派生类
    """
    def say_who(self):
        """
        这里重写父类的方法
        :return:
        """
        print('我是一只猫子')
        pass
    pass



# dog1=Dog()
# duck1=Duck()
# cat1=Cat()
# dog1.say_who()
# duck1.say_who()   #同一个say_who方法在不同子类之间有不同的表现

def commonInvoke(obj):  #定义一个函数统一调用对象的方法
    """
    同一调用的方法
    :param obj:
    :return:
    """
    obj.say_who()
    pass

listobj=[Dog(),Duck(),Cat()]  #新建对象用 类() 的形式  这里相当于item=Dog()
for item in listobj:
    """
    循环调用函数
    """
    commonInvoke(item)

#多态的好处
# 增加程序的灵活性，增加程序的扩展性
#
# 不管你是哪个类生成的对象，继承谁，只要你有say__who方法我都可以统一调用
# 关注的不是对象类型的本身，而是它是如何使用的








