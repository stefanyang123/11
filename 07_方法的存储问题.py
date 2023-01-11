class Person:
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

p=Person()

print(p.__dict__)
print(Person.__dict__)
'''
不管是哪一种类型的方法 都是储存在类当中的__dict__属性里，没有在实例当中的
'''

print('\n','-'*20,'字典里为啥能放方法','-'*20)
def run():
    print('run')
    pass

p.age=run
print(p.__dict__)