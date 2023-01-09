'''
将一堆变量和方法封装到一个区域 叫类
在类的内部 重新赋值的变量会覆盖本来的变量

'''



class Person:
    name='小杨'
    age='20'
    def eat(self):
        print(self.name+'大口的吃饭')
        pass
    def run(self):
        print('飞速的跑')
        pass
    pass

p=Person()
p.name='小白'
p.eat()

# 改变类中变量name
p1=Person()
p1.eat()

