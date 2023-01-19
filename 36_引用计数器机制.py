# 引用计数器机制
# 不能处理循环引用的情况

import sys

class Person:
    pass

# p1指向着一个Person实例对象内存地址  这个对象被引用 计数加一
p1=Person()  #引用次数1
print(sys.getrefcount(p1))  #p1传递给函数之后引用会自动加一 实际的引用次数是1

# 将p1的值赋值给p2 p2也指向着同一个对象内存地址  这个对象再次被引用 计数加一
p2=p1   #引用次数2
print(sys.getrefcount(p1))

# 对象的引用减一
del p2   #引用次数1
print(sys.getrefcount(p1))

# 对象的引用减一
del p1   #引用次数0

"""
引用计数+1的场景
    对象被创建 p1=Person()
    对象被引用 p2=p1
    对象被作为参数，传入到一个函数中 sys.getrefcount(p1) +1
                 函数内部有两个属性 都引用着对象  +2
    对象作为一个元素，储存在容器中 list=[p1]

"""
print('-'*40)
class Person1:
    pass

p=Person1()
print(sys.getrefcount(p))

def log(obj):
    print(sys.getrefcount(obj))

    pass

log(p)

# 查看log里的
# for attr in dir(log):
#     print (attr,getattr(log,attr))  #获得 键attr 值getatter

"""
引用计数-1的场景
    对象的别名被显示销毁 del p1
    对象的别名被赋予新的对象 p1=123
    一个对象离开它的作用域   一个函数执行完毕时                      
                        内部的局部变量关联的对象
    对像所在的容器被销毁，或从容器中删除对象

"""

# 循环引用问题
# objgraph库
# objgraph.count() 可以查看，垃圾回收器，跟中的对象个数

class Person:
    pass

class Dog:
    pass

p = Person()
d = Dog()

p.pat=d
d.master=p

# 删除 p d 之后，对于的对象是否被释放掉
del p
del d


