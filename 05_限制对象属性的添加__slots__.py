
class Person:
    # 限制类的属性添加 只能添加__slots__列表里的
    __slots__ = ['age']
    pass

p1=Person()
p1.age=1

try:
    p1.num=2
except Exception as e:
    print(e)
























