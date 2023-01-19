"""
生命周期 指的是对象从诞生到消亡的过程
当一个对象被创建时，会在内存中分配相应的内存空间进行存储
当这个对象不再使用，为了节约内存，就会把这个对象释放

监听对象生命周期
    __new__ 方法
        当我们创建一个对象时，用于给这个对象分配内存的方法
        通过拦截这个方法，可以修改对象的创建过程   如：单例模式

    __init__ 方法


    __del__ 方法
""" 


# class Person:
#
#     # def __new__(cls, *args, **kwargs):
#     #     print('新建了一个对象,被我们拦截了')
#     #     pass
#
#     def __init__(self):
#         print('初始化方法')
#         self.name='sz'
#         pass
#
#     def __del__(self):
#         print('这个对象被释放了')
#
#     pass
#
# p=Person()
# print(p)
# print(p.name)

print('--------------------------小案例----------------------------')
# --------------------------监听对象声明周期方法--小案例-----------------------------
# Person 打印一下，当前这个时刻，由Person类，产生的实例，有多少个
# 创建了一个实例，计数+1，如果，删除了一个实例，计数-1


class Person:

    __personcount = 0

    def __init__(self):
        # 创建实例的时候会自动调用
        print('计数+1')
        #这里 personcount+=1 是错的，因为相当于给实例也添加了一个personcount实例属性
        Person.__personcount += 1
        pass

    def __del__(self):
        # 删除实例的时候会自动调用
        print('计数-1')
        self.__class__.__personcount -= 1   #通过实例拿到对应的类self.__class__
        pass

    @staticmethod
    def log():
        print('当前的人数是%d个' % Person.__personcount)
        pass

    # 或者这样写也行
    # @classmethod
    # def log(cls):
    #     print('当前的人数是%d个' % cls.__personcount)
    #     pass

    pass

p=Person()
Person.log()
del p














