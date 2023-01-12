'''
元类
创建类对象的类
对象的产生是 是由类创建出来的
因为类 本质上也是对象 所以 有一类创建类对象的类 叫元类

'''
# 我们可以通过 对象的 __class__ 属性 来访问到它的类
p=10
print(p.__class__)  #<class 'int'>

# 因为类也是对象 所以
print(int.__class__)  #<class 'type'>

# type 就是元类

#-----------------------------------类创建的方式-----------------------------------
print('-'*60)
# 自动创建
class Person:
    count=0
    def run(self):
        print('将实例打印出来',self)
        pass
    pass

p1=Person()
print(p1.__class__)
p1.run()

print('-'*60)

# 手动创建
def run():
    print('函数被运行')

xxx = type('Dog',(),{"count":0,"run":run})

a=xxx()
print(a.__class__)   #<class '__main__.Dog'>
print(a.count)       # 0











