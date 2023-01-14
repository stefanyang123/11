'''
经典类：没有继承(object)  object类
新式类：继承(object)
python2.x 版本定义一个类时，默认不继承(object)  必须显示的继承自object才是新式类
python3.x 版本定义一个类时，默认继承(object)
建议使用新式类

创建类对象的类是元类，子类继承的父类是基类
为了兼容起见，建议定义类的时候这样 class Person(object) 去定义
'''

class Person:
    pass

# 查看Person类的基类
print(Person.__bases__)   #(<class 'object'>,)

# 因为Person类是继承object类的，所以object类是Person类的基类
# 他俩的元类 都是type
# print(Person.__class__)  <class 'type'>
# print(object.__class__)  <class 'type'>

