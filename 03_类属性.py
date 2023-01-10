'''
类本质上也是一个对象
    1.让类拥有属性
        方式1： 类名.类属性=值
        方式2： class Money:
                    count=10
                    pass

'''
class Test:
    sex='nan'
    pass

class Money:
    age=14
    pass

Money.conut = 1

print(Money.conut)
print(Money.__dict__)

one=Money()
print(one.__class__)  #实例对象 跟类对象是通过__class__属性 进行关联的

# 通过类的实例对象也能访问类的属性
# 和python对象的属性查找机制有关
#   优先到对象自身去查找属性 找到则结束并返回属性值
#   在对象中没有找到 根据__class__找到实例对象对应的类
#   到类里面去查找
print(one.age,'通过对象也能访问类的属性')

print('-'*20,'如果把one实例对象的__class__修改了','-'*20)

one.__class__=Test   #把one实例对象 指向的类 改为Test
try:
    print(one.age)
except Exception as e:
    print(e,'此时不能访问到属性age')
    pass
print(one.sex,'此时能访问到Test类中的sex属性')

print('-'*20,'如果我们给实例对象one中加入一个sex=1','-'*20)
one.sex=1
print(one.sex,'此时访问的不是Test类中的sex属性，而是one实例对象自身的sex属性')

print('-'*20,'类属性的修改','-'*20)
'''
1.通过 类名.属性 修改
2.能否通过对象修改
'''
Money.age='新的值'
print('类Money的age属性被赋予',Money.age)
two=Money()
two.age=10
print(f'two.age的值是{two.age}，Money.age的值是{Money.age}')

print('-'*40)

print('由此可见，想要给一个类增加或修改属性\n'
      '不能通过它的对象来进行操作\n'
      '一定是 类.类属性 的方式进行操作')

print('-'*20,'类属性的删除 del 类.类属性 ','-'*20)
del Money.age
try:
    print(Money.age)
except Exception as e:
    print(e)
print('-'*20,'del语句 只能删除直系属性 所以不可能通过实例对象往上把类属性删除','-'*20)






