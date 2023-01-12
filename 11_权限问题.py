class Person:
    age=0
    def shilifangfa(self):
        '''
        self 其实就是用来接收实例的形参
        通过实例可以访问到它自身的实例属性
        也可以访问到他对应的类的属性
        :return:
        '''
        print(self)
        print(self.num)   #自身的实例属性
        print(self.age)   #它对应的类的属性
        pass
    @classmethod
    def leifangfa(cls):
        '''
        cls 其实就是用来接收类的形参 或者是它的子类
        通过类只能访问到 类属性
        不能访问到 它实例化出来的 实例的实例的属性
        :return:
        '''
        print(cls)
        print(cls.age)
        try:
            print(cls.num)  #num是p实例的实例属性
        except Exception as e:
            print(e)
        pass
    @staticmethod
    def jingtaifangfa():
        '''
        也能访问 实例属性 和类属性
        但是静态方法本身设计出来就是
        不需要用到 类 实例这些
        因而第一个参数 没有设计默认传递类和实例
        :return:
        '''
        print(Person.age)
        pass
    pass

p=Person()
p.num=10

p.shilifangfa()
print('-'*60)
Person.leifangfa()
