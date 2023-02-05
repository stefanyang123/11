# python是动态语言，在运行的时候可以动态添加属性。如果要限制在运行的时候给类乱添加属性，
# python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# 只有在__slots__变量中的属性才能被添加，没有在其中的会添加失败。可以防止其他人子啊调用类的时候胡乱添加属性或方法。
# __slots__变量不会继承，只有在当前类中有效

# 作用
# 限制要添加的实例属性
# 解约内存空间
class Student(object):
    __slots__ = ('name','age')  #里面变量的类型是个字符串的类型,只能创建里面的属性
    def __str__(self):
        return '{}...{}'.format(self.name,self.age)
    pass

xw=Student()
xw.name='ybw'
xw.age=123
print(xw)
# xw.score=11    score会添加失败

# print(xw.__dict__)   #所有xw的属性都在这里存储，不足的地方就是占用的内存空间大
# 在定义了 slots变量后Student类的实例已经不能随意创建  不在__slots__里定义的属性了
# 同时还可以看到实例当中也不再有__dict__了(要用dict必须注销掉slots)


# 在继承关系中slots的使用
# 子类未声明__slots__时，那么是不会继承父类的__slots__，此时子类是可以随意的属性赋值的
# 如果子类声明了__slots__，那么父类中__slots__里的属性范围会被继承下来，其自身的+父类的  子类尽量不要与父类的重复
class subStudent(Student):
    __slots__=()    #继承父类的__slots__
    pass
ln=subStudent()
ln.gender='男'
print(ln.gender)   #报错 说明slots不会被继承











