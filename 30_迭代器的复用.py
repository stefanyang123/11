# 自己写一个迭代器，用for in 进行循环
class Person:
    def __init__(self):
        self.age=1
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.age += 1
        if self.age >= 6:
            print('停止了循环')
            raise StopIteration('遍历停止')

        return self.age

    pass

p=Person()

"""
迭代器iterator类型的定义
    1.当类中定义了 __iter__ 和 __next__  两个方法
    2.__iter__方法 需要返回对象本身 即self
    3.__next__方法 返回下一个数据，如果没有数据了，则需要抛出一个StopIteration的异常

for item in 迭代器对象  循环的内部机制
    首先会执行迭代器对象的 __iter__ 方法并获取返回值
    并会一直回去反复的执行next(迭代器对象) 而next()函数 又会执行迭代器对象的 __next__方法，并把执行的结果赋值给item
    
可迭代对象interable的定义
    如果一个类中有 __iter__ 方法 且返回一个迭代器对象 则我们称这个类创建的对象为可迭代对象

for item in 可迭代对象  循环的内部机制
    首先执行 __iter__ 方法，获取其迭代器对象，然后再内部执行这个迭代器对象的next功能逐步取值
    




"""

# 通过for in 访问迭代器的时候 首先会经过__iter__方法 获取一个迭代器对象，如果不是则会报错
# 在使用next() 函数 不断的去访问p实例的 __next__方法 直到遇到停止条件
print('---------------第一遍使用for in---------------')
for i in p:
    print(i)
    pass

print('---------------第二遍使用for in---------------')
# 可以看到这一遍使用时 直接停止了循环 是因为p.age 已经是六了
# 第二次使用for in 访问迭代器是 一样会先经过__iter__方法 获取对应的迭代器对象
# 我们将 self.age初始化成1 解释器 再使用next() 函数 不断的去访问p时，进入  __next__方法中 就能正常返回数据 不会走if后面的语句了
for i in p:
    print(i)
    pass
# 在__iter__方法里加入语句 self.age=1 即可 正常遍历第二遍


# 可迭代对象只需要实现__getitem__方法，而迭代器 必须要实现__iter__ __next__ 两个方法
# 能通过next()访问的不一定是迭代器，迭代器一定能通过next() 访问
# next()函数 只能访问有 __next__方法的对象
# 一个可迭代对象一定可以通过 for in 进行访问 ，能通过for in进行访问的不一定是一个可迭代对象
# 因为这个实例对象 只要有__getitem__方法或__iter__ __next__两个方法 即可被 for in 访问  但它不一定有__iter__和__next__方法，也就不一定是可迭代对象和迭代器了


print('--------------- iter()函数 将对象转换为迭代器 ---------------')
# iter(可迭代对象)  才能生成迭代器
# iter(可调用对象，终止值)












