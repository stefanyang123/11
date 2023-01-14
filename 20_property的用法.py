# #property 的第一种使用方式
# class Person(object):
#     def __init__(self):
#         self.__age=18
#         pass
#
#     def get_age(self):
#         print('------ get')
#         return self.__age
#         pass
#
#     def set_age(self, value):
#         print('------ set')
#         self.__age=value
#         pass
#
#     age = property(get_age, set_age)
#
# p=Person()
# print(p.age)
#
# # 没有设置property的情况下  p.age=90是在给实例增加实例属性age
# p.age=90
# print(p.age)
#
# print(p.__dict__)  #实例没有新增属性

# 第二种使用方式
# 这种方式，不用把读取和修改都写出来，只用写其中之一即可
# class Person(object):
#     def __init__(self):
#         self.__age = 18
#         pass
#
#     @property
#     def age(self):
#         print('---------get!')
#         return self.__age
#         pass
#
#     @age.setter
#     def age(self,value):
#         print('---------setted!')
#         self.__age=value
#
#     pass
#
# p=Person()
# print(p.age)
#
# p.age=10
# print(p.age)






