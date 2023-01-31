"""
垃圾回收时机
    1.自动回收
        触发条件
            开启垃圾回收机制
                gc.enable()     开启垃圾回收机制（默认开启）
                gc.disable()    关闭垃圾回收机制
                gc.isenabled()  判定当前垃圾回收机制是否开启
            并且要达到垃圾回收的阈值

    2.手动回收


"""
import gc

# 查看垃圾回收机制是否开启
print(gc.isenabled()) #True默认开启
gc.disable()
print(gc.isenabled()) #False
gc.enable()
print(gc.isenabled()) #True

print('-'*40)
# 查看当前设置的参数
print(gc.get_threshold())
# 修改参数
gc.set_threshold(1000,15,10)  #一般会把数值调大 提升整体程序性能

print('--------------------解决循环引用的两种方式------------------')

class Person:

    def __del__(self):
        print('Person对象被释放了')
    pass

class Dog:

    def __del__(self):
        print('Dog对象被释放了')
    pass

p=Person()
d=Dog()

# # 创造循环引用
# p.pet=d        # 此时Dog()对象的两个引用分别为     d->Dog() p.pet->Dog()
# d.master=p     # 此时Person()对象的两个引用分别为  p->Person()   d.master->Person()
#
# p.pet=None   #手动修改p.pet的指向 p.pet->None ，不再指向Dog()对象 则Dog()对象的引用-1
# del p
# del d
#
# gc.collect()  #不填参数默认 回收全部代垃圾，语句的运行与垃圾回收机制的开关无关


import weakref
import sys
# 通过弱引用直接避免循环引用的产生
# 弱引用  不会使被引用对象的 引用计数加一，但仍可使用引用对象

p.pet = d  # Dog()对象 此时的引用为2   1. d->Dog()  2. p.pet->Dog()
print('Dog()对象被引用了{}次'.format(sys.getrefcount(d)-1))

d.master = weakref.ref(p)  #Person()对象 此时的引用为1    p->Person()
print('Person()对象被引用了{}次'.format(sys.getrefcount(p)-1))

"""
扩展
    如果出现多个对象赋值给一个属性的话 使用弱字典 WeakValueDictionary WeakKeyDictionary
    import weakref
    # p.pets={'dog':weakref.ref(d1),'cat':weakref.ref(c1)}
    p.pets=weakref.WeakValueDictionary({'dog':d1,'cat':c1})

"""














