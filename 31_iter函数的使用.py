# 方法一  iter(可迭代对象)
class Person:
    def __init__(self):
        self.age=1
        pass

    def __getitem__(self, item):
        self.age += 1
        if self.age >= 6:
            raise StopIteration('停止迭代')
        return self.age
        pass

    pass

p=Person()

for i in p:
    print(i)
    pass
pt=iter(p)

print(pt) #<iterator object at 0x000001DC4F0DCF70>

# 方法二  iter(可调用对象,参数)
class Person1:
    def __init__(self):
        self.age=1

    def __iter__(self):
        self.age=1
        return self

    # def __next__(self):
    #     self.age+=1
    #     if self.age>=6:
    #         raise StopIteration
    #     return self.age

    def __call__(self, *args, **kwargs):
        self.age += 1
        if self.age >= 6:
            raise StopIteration
        return self.age

    pass


p1=Person1()
# 判断为4的时候会自动终止
# pt1=iter(p1.__next__,4)

pt1=iter(p1,4)   #当pt1 具有__call__方法后，就可以被调用

for i in pt1:
    print(i)
    pass


