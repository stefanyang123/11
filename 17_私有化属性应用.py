class Person:
    # 主要作用，当我们创建号一个实例对象之后，会自动的调用这个方法
    # 来初始化对象
    def __init__(self):
        self.age=10
        self.__age=18  #__age被系统改名为 _Person__age
        pass

    # 这个私有属性__age只能在类的内部进行访问，在外部访问不了
    # 我们可以在类里面提供两个方法，专门用来操作这个私有属性

    # 类的外部是访问不到私有属性的
    # 我们又需要操作私有属性__age时，可以设置一个方法来实现
    def setAge(self,value):
        # 将value 的 值赋值给私有属性__age,这样类的外部就能通过调用实例方法来进行修改了

        # 判断value是否是数值型  isinstance(对象,类型) 判定前面一个对象，是否是后面给的类型
        # 且value大于0小于200
        if isinstance(value,int) and 0<value<200:  #满足条件才赋值
            self.__age=value
        else:
            print('请输入正确的值')
        pass

    # 同时我们又想访问修改后的值，同样可以设置一个方法来实现
    def getAge(self):
        return self.__age
    pass

p1=Person()
p2=Person()
p3=Person()

print(p1.age,p2.age,p3.age)
print('虽然age的值都是10，但是这些age分别属于不同的实例')

print()

p1.__age=19
# 这个p1.__age不是私有属性，在类的内部添加的__age 才是私有属性
print(p1.__dict__)  #{'age': 10, '_Person__age': 18, '__age': 19}

print('-'*20,'在外部使用 实例方法 对 私有属性 进行修改和访问','-'*20)
p1.setAge(20)
print(p1.getAge())

'''
补充:
给变量添加下划线的规范

xx_ 这样可以使 变量名与系统内置的关键字做区分
现在就需要命名一个变量 为class 这样就与系统关键字冲突了
我们可以这样写 class_ 这个变量

__xx__  系统内置的变量  避免这种命名方式


'''


