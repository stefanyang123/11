class Person:
    """
    这是类的文档
    """
    age=19
    def __init__(self):
        self.name='ybw'
        pass

    def run(self):
        print('run')
        pass

    pass
print('-'*20,'__dict__ 类的属性','-'*20)
print(Person.__dict__)

print('-'*20,'__bases__ 当前类的所有父类 构成的元组','-'*20)
print(Person.__bases__)  #只有一个父类object

print('-'*20,'__doc__ 类的文档字符串','-'*20)
print(Person.__doc__)
print('与help() 的区别')
help(Person)

print('-'*20,'__name__ 查看类名','-'*20)
print(Person.__name__)

print('-'*20,'__module__ 查看类定义的模块','-'*20)
print(Person.__module__)

print('\n','-'*80)
p1=Person()
p1.name='ybw'

print('\n','-'*20,'__class__ 查看实例对应的类名','-'*20)
print(p1.__class__)

print('\n','-'*20,'__dict__ 查看实例的属性','-'*20)
print(p1.__dict__)










