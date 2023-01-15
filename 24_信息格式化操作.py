# ----------------------------------  __str__方法 --------------------------------------
class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
        pass

    def __str__(self):
        '''
        信息格式化
        :return:
        '''
        return '这个人的姓名是%s,年龄是%s'%(self.name,self.age)
        pass

    pass

p1=Person(18,'ybw')
print(p1.age,p1.name)

# 使用print函数  来触发__str__方法
print(p1)   #<__main__.Person object at 0x0000020F0BEB9FD0>  打印实例时，如果没有__str__方法

# 使用str函数   来触发__str__方法
s=str(p1)
print(s,type(s))

# ----------------------------------  __repr__方法 --------------------------------------
class Animal:
    def __init__(self,size,long):
        self.size=size
        self.long=long
        pass

    def __str__(self):
        '''
        信息格式化
        :return:
        '''
        return '调用了__str__方法，这个动物的大小是%d,长度是%d'%(self.size,self.long)
        pass

    def __repr__(self):
        '''
        __str__ 方法比 __repr__ 优先实现

        :return:
        '''
        print('调用了__repr__方法')
        return 'Animal({},{})'.format(self.long,self.size)
    pass

a1=Animal(20,23)

print()
print(repr(a1))

print()
print(a1)

"""
总结
这两个方法都是通过字符串来描述一个实例
__str__ 面向的是用户
__repr__ 1.面向的是程序员  这个对象本质的信息
         2.面向解释器  通过eval 再次转换为相关的实例
"""

print()
# 用eval函数 将字符串变成可以执行语句，前提是语法正确
tmp=eval(repr(a1))  #repr(a1)=Animal(23,20)    tmp=Animal(23,20) 创建了一个tmp实例

print()
print(tmp)  #调用__str__方法



