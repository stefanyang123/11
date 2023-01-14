'''
一个属性（一般指实例属性）,只能读取，不能写入
具体实现方法1：
1.将属性私有化 外界将不能访问（读和写）
2.设置实例方法，让外界能读取  公开一个读取的方法给外界
'''
class Person:
    def __init__(self):
        self.__age=18

        pass

    def getAge(self):
        return self.__age
        pass
    # @property 主要作用就是，可以 以使用属性的方式，来使用这个方法
    @property
    def age(self):
        return self.__age

p1=Person()

'''
p1.__age=999
注意
这里不是私有化了一个属性，而是给p1，又增加了一个实例属性__age
想要私有化一个属性必须在类的内部进行
'''

# 用这种方式去访问一个属性 没有之前p1.age 方便
# 因为外界是以使用函数的形式来操作属性的
print(p1.getAge())

# 当我们设置了 用@property装饰的age方法后,就不用在后边加上小括号了
# 用以前读取属性的方式来使用这个方法
# 外界就是以使用属性的方式来操作属性了
print(p1.age)

# 但是此时age属性是不能修改的，有没有什么办法能让它修改呢？
try:
    p1.age=1
except Exception as e:
    print(e)

'''
补充property的其他用处：

property 可以将一些 属性的操作方法（删改查） 关联到某一个属性中
操作一个属性 无非属性的增删改查

例如：将属性的操作方法fget,fset,fdel 关联到某一个属性x中
class Person(object):
    def fget（self）:
        return self._x
    
    def fset（self,value）:
        self._x=value
    
    def fdel（self）:
        del self._x
    
    x = property(fget,fset,fdel,doc)

property有四个参数  最终你会得到一个属性
将几个属性的操作方法关联到 一个属性里面  用于定义和管理一个属性x

如果想要读取属性x
    property它会自动调用它的第一个参数fget，fget是一个函数，用来获取属性的值

'''