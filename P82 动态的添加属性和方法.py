# 动态语言：
# 运行时可以改变其结构的语言，例如新的函数，对象，甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化
# 如PHP,JavaScript,Python都是动态语言，C,C#,java是静态语言
# 因此Python可以在程序运行的过程中添加属性和方法


# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     pass
#     def __str__(self):
#         return '{}今年{}岁了'.format(self.name,self.age)
#         pass
#     pass
# zy=Student('张燕',20)
# zy.weight=50  #动态添加的，归zy所有
# print(zy)
# print(zy.weight)
# print('----------另外一个实例对象-------------')
# zm=Student('张明',20)
# print(zm)
# # print(zm.weight)  zm并不具备weight属性，weight是针对zy特意添加的，归zy所有
# print('---------------给类添加属性，通过类对象--------------')
# Student.school='北京大学'
# print(zm.school)


print('----------动态添加实例方法，用types库----------')

import types   #导入添加方法的库
# 先定义一个实例方法
def dymicMethod(self):
    print('{}的体重是{}，在{}读大学'.format(self.name,self.weight,Student.school))  #因为是类属性，所以通过类对象访问
    pass

@classmethod
def classText(cls):
    print('这是一个类方法')
    pass

@staticmethod
def staticMethodTest():
    print('这是一个静态方法')
    pass


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    pass
    def __str__(self):
        return '{}今年{}岁了'.format(self.name,self.age)
        pass
    pass
zy=Student('张燕',20)
zy.weight=50  #动态添加的，归zy所有
# 动态的绑定方法，types.MethodType(要绑定的方法，谁要绑定)
zy.printInfo=types.MethodType(dymicMethod,zy)

print('----------另外一个实例对象-------------')
zm=Student('张明',20)
print(zm)
# print(zm.weight)  zm并不具备weight属性，weight是针对zy特意添加的，归zy所有

print('---------------实例方法的绑定--------------')
Student.school='北京大学' #动态添加了一个类属性，所有实例对象均可访问
print(zm.school)
zy.printInfo()   #printInfo(自己取的名字)动态绑定dymicMethod方法
# zm要动态绑定的话，得给他一个weight属性，因为dymicMethod使用到了weight属性，不然会报错

print('----------类方法的绑定----------')
#先定义一个类方法，如上@classmethod
Student.TestMethod=classText
Student.TestMethod()   #调用方法时，要加括号
# 动态绑定的类方法，实例对象也能用

print('-----------静态方法的绑定------------')
#先定义一个静态方法，如上@staticmethod
Student.mythod=staticMethodTest
Student.mythod()   #调用方法时，要加括号


# # 动态绑定方法
# 1.创建一个实例方法  def xxx(self):
#
#          类方法   @classmethod
#                  def XXX(cls):
#
#          静态方法 @staticmethod
#                  def xxx():
# 2.绑定 实例方法需要 import types 
# 3.调用方法() 记得加括号























