'''
描述器 descriptor

在拦截的过程当中，针对于所传过来的数据，做数据过滤，数据验证
一个类里面有一个属性，这个属性指向着一个特殊的对象
只要这个对象实现了__set__ __get__ __delete__，就可以把这个对象称为描述器
外界对属性的操作(增删改查) -> 描述器 -> 属性被操作

'''

# ------------------------ 定义方式一  @property ------------------------------------
# 把属性的修改方法 查看方法 删除方法 封装起来变成一个属性
# 这个属性其实就是描述器

class Person:
    def __init__(self):
        self.__age=10
        pass

    def get_age(self):
        return self.__age
        pass

    def set_age(self,value):
        if value < 0:
            value = 0
        self.__age = value
        pass

    def del_age(self):
        del self.__age
        pass

    # 这个age就是个描述器
    age = property(get_age,set_age,del_age)

    # 或者这样写 效果是一样的
    # @property
    # def age(self):       #名字为了保持一直，就命名为age了，其实可以命名成其他的
    #     return self.__age
    #     pass
    #
    # @age.setter
    # def age(self,value):
    #     if value < 0:
    #         value = 0
    #     self.__age = value
    #     pass
    #
    # @age.deleter
    # def age(self):
    #     del self.__age
    #     pass
    #
    # pass

p = Person()
p.age=19
print(p.age)

print('-'*20,'方法二','-'*20)
# --------------------------------- 定义方式二 -------------------------------------
# 一个变量我们需要有三个操作方法，那么很多变量的时候，类的定义就显得很臃肿 因此 有描述器的第二种定义
# 专门开辟一个新的类  描述器类 在新式类才会生效 Age Person 都必须继承object 才可以 python3 默认继承object

# 资料描述器 实现了get set方法
# 非资料描述器 仅仅实现了get 方法
# 执行优先级 资料描述器 > 给实例赋值同名属性 > 非资料描述器
class Age:
    def __get__(self, instance, owner):
        print('get')
        return instance.v
        pass

    def __set__(self, instance, value):
        """
        self:是Age类的对象 Age object
        :param instance:  是Person类的对象 Person object
                          每执行一次会产生不同的 Person对象
                          不同的Person对象才能存储不同的数据 age对象是共享的
        :param value:  赋的值
        :return:
        """
        print('set',self,instance,value) #age实例 person实例 18
        instance.v = value

        pass

    def __delete__(self, instance):
        print('delete')
        pass

    pass

class Person:
    age = Age()   #描述器

    # 给实例赋值同名属性
    # def __init__(self):   #资料描述器 > 给实例赋值同名属性 > 非资料描述器
    #     self.age = 10

    # def __getattribute__(self, item):
    #     print('会覆盖描述器的__get__方法')

    pass
# 当我们定义好描述器时候，通常是通过实例来操作这个属性，而不是Person类
p1=Person()
p2=Person()

p1.age=18
print(p1.age)

p2.age=12
print(p2.age)