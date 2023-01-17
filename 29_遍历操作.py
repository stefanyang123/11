# 怎样让我们自己创建的对象可以使用 for in 进行遍历
# 1.实现__getitem__方法
# class Person:
#     def __init__(self):
#         self.result = 1
#
#     def __getitem__(self, item):
#         self.result += 1
#         if self.result >=6:
#             # 判断result大于等于6 抛出一个停止遍历的异常
#             raise StopIteration('写一些异常信息')
#
#         return self.result
#     pass
#
# p=Person()
#
# """
# 当我们通过 for in 去访问一个实例的时候，解释器会首先去找有没有实现getitem方法
# 不断地去访问__getitem__，并获取返回的值，直到遇到停止条件(抛出StopIteration异常)，否则就是无限循环
# """
# for i in p:
#     print(i)
#     pass

# 2.实现
class Person:
    def __init__(self):
        self.result = 1

    def __getitem__(self, item):
        print('getitem')
        self.result += 1
        if self.result >=6:
            # 判断result大于等于6 抛出一个停止遍历的异常
            raise StopIteration('写一些异常信息')

        return self.result

    def __iter__(self):
        """
        iter优先级高于 getitem
        :return:
        """
        print('iter')

        # iter() 返回一个迭代器  列表可迭代 但不是迭代器
        # 迭代器必须要有一个实例方法 __next__
        # return iter([1,2,3,4,5])
        return self
        pass

    def __next__(self):
        """
        迭代器必须要有的方法
        要把上面self 变成迭代器  必须要有这个方法
        :return:
        """
        self.result += 1
        if self.result >= 6:
            # 判断result大于等于6 抛出一个停止遍历的异常
            raise StopIteration('停止遍历')

        return self.result
    pass

p=Person()

"""
当我们通过 for in 去访问一个实例的时候，解释器会首先去找有没有实现getitem方法

当我们通过 for in 去访问 p实例时
如果你实现了 __iter__方法 ，解释器就会通过该方法来操作这个p实例
也就是间接的调用了p实例里这个__iter__方法  这里我们让它返回的是self  也就是p实例本身
但是 返回的得是个迭代器 (p实例在实现 __next__方法后 才是个迭代器)
前面我们 return 的 iter([1,2,3,4,5])  [1,2,3,4,5]是个可迭代对象
iter()函数 会调用对象的__iter__ 方法而且要有返回值

"""
# for i in p:
#     print(i)
#     pass

# 怎样让我们自己创建的对象可以使用 next() 访问   实现next方法
print(next(p))
print(next(p))
print(next(p))
print(next(p))
try:
    print(next(p))
    pass
except Exception as e:
    print(e)























