# 自定义对象 比较大小 相等 以及真假的规则
# 数字10再python里本质上是int类 的实例
# 现在自己定义好一个类 通过类创建两个实例 比较大小
class A:

    def __eq__(self, other):
        """
        等号两边一个是self 一个是other
        :param other:
        :return:
        """
        print(other)
        pass


    pass

a1=A()
a2=A()

# # 如果类中没有实现对应的方法 在python3中会报错
# # TypeError: '>' not supported between instances实例 of 'A' and 'A'
# print(a1 > a2)

print(a1==a2)

print()

class Person:

    def __init__(self,age,height):
        self.age=age
        self.height=height
        pass

    def __eq__(self, other):
        """
        这里是相等，相等和不相等是一个方向的操作，实现了一个会自动推导另一个
        :param other:
        :return:
        """
        print('进入__eq__方法')
        return self.age==other.age
        pass

    def __ne__(self, other):
        """
        这是不等于方法，也可以单独实现 不相等方法
        :param other:
        :return:
        """
        print('进入__ne__方法')
        return self.age!=other.age
        pass

    # 其他方法
    def __gt__(self, other):
        # 大于
        pass

    def __ge__(self, other):
        #大于等于  g大于 e等于
        pass

    def __lt__(self, other):
        #小于
        pass

    def __le__(self, other):
        #小于等于
        pass

    pass

p1=Person(18,180)
p2=Person(19,190)

# 在等于方法中 如果self.age==other.age 返回True
# 在没有单独实现不等于方法时
# 那么在不等于方法中 内容相反
print(p1 == p2)  #False

# 单独实现后 会进入不等于方法
print(p1 != p2)   #p1会传给self p2会传给other

# 如果对于反向操作的比较符，只定义了其中一个方法但使用的是另外一种比较运算符
# 那么解释器会采用调换参数的方式进行调用该方法 把p1给other 把p2给self 即可
# 不支持叠加 即 >=  <=  等  如果非要实现这操作

# 就要用到装饰器 @functools.total_ordering 装饰这个类
# 先引入 functools 模块

# import functools
# @functools.total_ordering
# class Person:
#   pass

# 会自补全  >=  <= 这些对应方法
# 小于等于  实际上是 小于或等于 因此 如果小于满足True，则不会继续执行等于了。小于不满足，才会都执行


print('上下文环境的布尔值')
# ----------------------------- 上下文环境的布尔值-----------------------------
# 非0及真 非空及真
class Person:

    # def __init__(self):
    #     self.age=18
    #     pass

    def __bool__(self):
        """
        方法返回什么，实例就是什么
        :return:
        """
        return False
        # return self.age>=18
        pass

    pass
p=Person()

if p:   #实例p的 __bool__方法 返回的是False，所以这里不会执行
    print('hhhh')
    pass

if 8:
    print('xxx')
    pass

if 'abc':
    print('123')
    pass

