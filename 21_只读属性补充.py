# class Person:
#     # __setatter__是系统内置的，当我们通过实例.属性 = 值 给一个实例增加一个属性或者修改属性值的时候
#     # 都会调用这个函数，在这个方法内部，才会真正的把，这个属性，以及对应的数据，给储存到__dict__字典里面
#     def __setattr__(self, key, value):
#         print(key,value)
#
#     pass
# p1=Person()
# p1.age=18
#
# # 因为我们在这个类中，相当于重写了__setattr__方法，现在通过p1.age=18
# # 只会执行print(key,value) 而不会去给对象添加属性了
#
# print(p1.__dict__)  #{}

class Person:
    # __setatter__是系统内置的，当我们通过实例.属性 = 值 给一个实例增加一个属性或者修改属性值的时候
    # 都会调用这个函数，在这个方法内部，才会真正的把，这个属性，以及对应的数据，给储存到__dict__字典里面
    def __setattr__(self, key, value):
        print(key,value)
        #我们要真正的实现只读属性 age
        #1.判断 key 是否是 age， 且 age 在__dict__字典里的所有键中 是的话 啥也不干
        # 允许第一次添加，后续修改就不能了 因为第一次添加age age不在__dict__字典中 所以会执行else后面的添加操作
        if key == 'age' and key in self.__dict__.keys():
            print('这个属性是只读属性不能设置数值')
        #2.如果不是只读属性的名称，真正的给它添加到这个实例里面去
        else:
            # 本意是想给实例添加属性 如果这样写
            # self.key=value 会得到一个死循环调用
            # self.key=value -> 自动调用__setattr__方法 -> 方法里执行self.key=value -> 自动调用__setattr__方法->...
            #这样也能给实例添加属性
            self.__dict__[key]=value
    pass

p1=Person()
p1.age=18

print(p1.__dict__)  #{}
# 尝试修改age属性 发现不行
p1.age=999
print(p1.age)

# 尝试添加其他属性
p1.name='ybw'
print(p1.__dict__)
# 这样才真正实现了只读属性的功能， 而 __age 是伪私有 通过修改后的属性名 _Person__age 一样可以修改