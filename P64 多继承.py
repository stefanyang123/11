# 多继承 （一个子类继承多个父类）
# class C(父类A,父类B) 父类A是亲爹，B是干爹 如果AB有相同的方法，C在调用此方法时，优先执行亲爹A的方法

class Shenxian:   #类的命名规范，首字母一定要大写！！！！
    def fly(self):
        print('神仙都会飞')
    pass
class Monkey:
    def chitao(self):
        print('猴子喜欢吃桃')
        pass
class Sunwukong(Shenxian,Monkey):
    pass

swk=Sunwukong()
swk.chitao()
swk.fly()
# 问题是 当多个父类中 存在相同方法时 应该取调用哪一个？
class D:
    def eat(self):
        print('D.eat')
        pass
    pass
class C(D):
    def eat(self):
        print('C.eat')
        pass
    pass
class B(D):
    pass
class A(B,C):  #你可以把B看成A的亲爹 C是干爹 亲爹里找不到方法找干爹
               #A的爹们B，C 他们继承了同一个爹D  所以先在A中找方法，找不到，先找B再找C，找不到再从B，C的同一个爹D 里去找
               # 顺序就是A-B-C-D
               #如果A的爹们B，C继承于不同的爹，则先找亲爹B，找不到再找B的爹D，如果找不到，再去干爹C找，找不到再去C的爹找
               # 顺序就是A-B-D-C
    pass

a=A()
a.eat()
print(A.__mro__)   #可以显示类的依次继承关系
# 结果执行了C.eat  为啥？
# 执行eat的方法时 查找方法的顺序是 A-B-C-D 也是A继承的顺序！
# 只要在中间哪一个类找到了eat方法，就不会往后去查找了

# 首先到A里面去查找，如果A中没有 则继续的去B类中去查找，如果B中没有，则去C中去查找
# 平级的去查找，也就是广度优先的去查找
# 如果C中没有，则取D类中查找，如果D类中还没有，则会报错


# 当对象a执行eat方法时，先在类A里找，发现没有此方法
# 因此先去A的父类B里找，发现父类B里也没有定义eat方法
# 然后接着取A的另一个父类C里找，发现父类C有定义eat方法，执行！

print('----------间接继承---------')
class GrandFather:
    def eat(self):
        print('爷爷的吃')
        pass
    pass
class Father(GrandFather):
    # def eat(self):   #因为它继承的父类里已经存在了这个方法，在这里相当于方法重写（即方法覆盖）
    #     print('爸爸的吃')
    #     pass
    pass
class Son(Father):
    # def eat(self):
    #     print('儿子的吃')
    #     pass
    pass
son1=Son()
print(son1.eat())
print(Son.__mro__)    #类.__mro__ 显示引用它的 类 的继承顺序

# 总结
# 类的传递过程中，我们把父类又称为基类，子类又称为派生类，父类的属性和方法可以一级一级的传递到子类。
# 一般不超过三级，三级就能基本上满足需求
# 当父类方法中有跟子类方法重名的，会被子类方法覆盖















