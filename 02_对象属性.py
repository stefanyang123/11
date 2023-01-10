'''
属性和变量的区别
变量是可以改变的量值 属性是属于某个对象的特征
变量根据不同位置，存在不同的访问权限 全局变量 局部变量
属性只能通过对象来进行访问 所以必须先找到对象 对象也是通过变量名来引用 也存在对应的访问权限
判断依据：这个变量是否存在宿主
    没有 普通变量
    有 属性 宿主是一个类 类属性
           宿主是一个对象  对象属性
'''

'''
怎样让对象拥有一些属性（增）
    1.直接通过对象动态添加
        对象.属性=值
    2.通过类的初始化方法（构造方法）添加
        __init__方法
'''

# 1. 定义一个类
class Person:
    pass

# 2.根据类，创建一个对象，将对象赋值给一个变量
p = Person()

# 3.给p对象，增加一些属性
p.age = 18

# 4.验证是否有添加成功
print(p.age)


# 查询当前对象里面所有的属性  p.__dict__
print(p.__dict__)   #{'age': 18}  键 属性名 值 属性的值

try:
    print(p.sex)
except Exception as e:
    print(e,'报错，对象没有属性sex')
    pass

print('-'*20,'修改对象的属性','-'*20)
p.age=20
print(p.age,'age属性值被修改为20')


print('-'*20,'删除对象的属性','-'*20)

del p.age
try:
    print(p.age)
except Exception as e:
    print('age属性已经被删除')
    print(e,'报错，对象没有属性sex')
    pass

print('-'*20,'不同对象之间不能互相的访问对方的属性','-'*20)
p1=Person()
p2=Person()

p1.age=22
p2.address='上海'

try:
    print(p1.address)
except Exception as e:
    print(e)
    pass
