# 函数 及调用
def eat():
    print(1)
    print(2)
    print(3)
    pass

eat()

# 方法 (类中的函数) 及调用

class Person:
    def eat2(self): #方法 是描述一个目标的行为动作
        print(1)
        print(2)
        print(3)
        pass
    pass

p=Person()
p.eat2()

'''
实例方法:默认第一个参数 需要接收到一个实例
类方法:默认第一个参数需要接收到一个类
静态方法:第一个参数啥也不默认接收

不管是哪一种类型的方法 都是储存在类当中，没有在实例当中的


'''

class Person1:
    def eat(self):
        '''
        self 仅仅是一个形参名称而已,这个名称想咋写咋写,
        只不过约定俗成的 是self
        :return:
        '''
        print('这是实例方法','打印self',self)
        pass

    @classmethod
    def leifangfa(cls):
        print('这是类方法','打印cls',cls)
        pass

    @staticmethod
    def jingtaifangfa():
        print('这是静态方法')
        pass
    pass

print('\n','-'*20,'实例方法的调用及第一个参数self是什么','-'*20)

p1=Person1()
p1.eat()
print('打印p1实例对象',p1)

print('\n','-'*20,'类方法的调用及第一个参数cls是什么','-'*20)

Person1.leifangfa()
print('打印Person1类',p1)

print('\n','-'*20,'静态方法的调用','-'*20)

Person1.jingtaifangfa()


