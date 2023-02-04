# 私有变量，一般写两个方法，一个去访问，一个去修改
class Person():
    def __init__(self):
        self.__age=18  #定义一个私有化属性 ，属性名前加__即可
        pass
    def get_age(self):  #写个方法访问私有化属性
        return self.__age
        pass
    def set_age(self,age):  #写个方法修改私有化属性
        if age <0:
            print('年龄不能小于0')
        else:
            self.__age=age
            pass
        pass
    def __str__(self):
        return '年龄是{}'.format(self.__age)
    # 定义一个类属性，实现通过直接访问属性的形式去访问私有的属性
    age=property(get_age,set_age) #必须将方法设置为get_age set_age才能访问



    pass
p1=Person()  #创建实例对象
print(p1.get_age())  #通过方法访问私有化属性
p1.set_age(90)  #通过方法修改私有化属性
print(p1)

print('-------设置property函数-------')
print(p1.age)    #不再是调用方法访问了，而是像访问属性一样访问它
                 #当你调用时 property函数直接自动调用get_age方法
p1.age=19        #修改也一样，不用再去调用方法去修改了
print(p1.age)


print('----------------------')
# 通过装饰器也可以实现property功能
class Person():
    def __init__(self):
        self.__age=18  #定义一个私有化属性 ，属性名前加__即可
        pass

    @property #使用装饰器对age进行装饰，提供一个getter方法
    def age(self):  #写个方法访问私有化属性
        return self.__age
        pass

    @age.setter # 属性名.setter 使用装饰器进行装饰，提供一个setter方法
    def age(self,prms):  #写个方法修改私有化属性
        if prms <0:
            print('年龄不能小于0')
        else:
            self.__age=prms
            pass
        pass
    def __str__(self):
        return '年龄是{}'.format(self.__age)

print(p1.age)
p1.age=16
print(p1.age)





