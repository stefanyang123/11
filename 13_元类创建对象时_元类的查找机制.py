'''

class Person:  # 或 class Person(metaclass=xxx):
    # 类 可以通过 __metaclass__ 来指明创建它的元类
    # __metaclass__ = xxx  # xxx 可以是type 也可以是自己写的元类
    pass

元类的查找机制  __metaclass__

如果类中没有指明 创建它的元类  就会到这个类的父类里找
父类也没指明  就会到模块级别 找 也就是当前这个py文件找
如果都没有指明  直接使用系统内置的type元类 来创建

在这其中每个环节我们都可以去指明元类
通过这个元类 针对于类对象的创建 来做一些事请
在不同的环节 指明 作用范围也不同
'''


# 在模块级别中指明元类
# __metaclass__=xxx      作用范围：模块中所有的类

class Animal():
    # 在父类级别中指明元类
    # __metaclass__=xxx    作用范围：它的所有子类
    pass

class Person(Animal):
    # 在类级别中指明元类
    # __metaclass__=xxx   作用范围：它自己
    pass








