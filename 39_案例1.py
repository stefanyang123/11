# 计算器
# 实现一些基本的操作，加减乘除，及打印结果
# --------------------代码1-----------------------

# def plus(a,b):
#     return a+b
#     pass
#
# def minus(a,b):
#     return a - b
#     pass
#
# def multiply(a,b):
#     return a * b
#     pass
#
# def divide(a,b):
#     return a / b
#     pass

# # (2+6-4)*5
# r1=plus(2,6)
# r2=minus(r1,4)
# r3=multiply(r2,5)

# --------------------代码2-----------------------
# result=0
#
# def first_value(v):
#     global result
#     result = v
#     pass
#
# def plus(n):
#     global result
#     result+=n
#     pass
#
# def minus(n):
#     global result
#     result -= n
#     pass
#
# def multiply(n):
#     global result
#     result *= n
#     pass
#
# def divide(n):
#     global result
#     result /= n
#     pass
#
# # (2+6-4)*5
# first_value(2)
# plus(6)
# minus(4)
# multiply(5)
# print(result)

# --------------------代码3-----------------------
# class Caculator:
#
#     __result=0
#
#     @classmethod
#     def first_value(cls,v):
#         cls.__result = v
#         pass
#
#     @classmethod
#     def plus(cls,n):
#         cls.__result += n
#         pass
#
#     @classmethod
#     def minus(cls,n):
#         cls.__result -= n
#         pass
#
#     @classmethod
#     def multiply(cls,n):
#         cls.__result *= n
#         pass
#
#     @classmethod
#     def divide(cls,n):
#         cls.__result /= n
#         pass
#
#     @classmethod
#     def show(cls):
#         print('计算的结果是:%d'%(cls.__result))
#     pass
#
# # (2+6-4)*5
# Caculator.first_value(2)
# Caculator.plus(6)
# Caculator.minus(4)
# Caculator.multiply(5)
# Caculator.show()

# --------------------代码4-----------------------
# class Caculator:
#
#     def __init__(self,num):
#         self.__result=num
#
#     def plus(slef, n):
#         slef.__result += n
#
#     def minus(self,n):
#         self.__result -= n
#
#     def multiply(self,n):
#         self.__result *= n
#
#     def divide(self,n):
#         self.__result /= n
#
#     def show(self):
#         print('计算的结果是:%d'%(self.__result))
#
#     pass
#
# # (2+6-4)*5
# res=Caculator(2)
# res.plus(6)
# res.minus(4)
# res.multiply(5)
# res.show()

# --------------------代码5-----------------------

# class Caculator:
#
#     def check_num(self,num):
#         if not isinstance(num,int):
#             raise TypeError('当前这个数据的类型有问题')
#
#     def __init__(self,num):
#         self.check_num(num)
#         self.__result=num
#
#     def plus(self, n):
#         self.check_num(n)
#         self.__result += n
#
#     def minus(self,n):
#         self.check_num(n)
#         self.__result -= n
#
#     def multiply(self,n):
#         self.check_num(n)
#         self.__result *= n
#
#     def divide(self,n):
#         self.check_num(n)
#         self.__result /= n
#
#     def show(self):
#         print('计算的结果是:%d'%(self.__result))
#
#     pass
#
# # (2+6-4)*5
# res=Caculator(2)
# res.plus(6)
# res.minus(4)
# res.multiply(5)
# res.show()

# --------------------代码6-----------------------
# class Caculator:
#
#     def check_num_zsq(func):
#         def inner(self,n):
#             if not isinstance(n, int):
#                 raise TypeError('当前这个数据的类型有问题')
#             return func(self,n)   #返回传入函数的执行结果
#         return inner
#
#     @check_num_zsq
#     def __init__(self,n):
#         self.__result=n
#
#     @check_num_zsq
#     def plus(self, n):
#         self.__result += n
#
#     @check_num_zsq
#     def minus(self,n):
#         self.__result -= n
#
#     @check_num_zsq
#     def multiply(self,n):
#         self.__result *= n
#
#     @check_num_zsq
#     def divide(self,n):
#         self.__result /= n
#
#     def show(self):
#         print('计算的结果是:%d'%(self.__result))
#
#     pass
#
# # (2+6-4)*5
# res=Caculator(2)
# res.plus(6)
# res.minus(4)
# res.multiply(5)
# res.show()

# # --------------------代码7-----------------------
# class Caculator:
#
#     def __check_num_zsq(func):
#         def inner(self,n):
#             if not isinstance(n, int):
#                 raise TypeError('当前这个数据的类型有问题')
#             return func(self,n)   #返回传入函数的执行结果
#         return inner
#
#     @__check_num_zsq
#     def __init__(self,n):
#         self.__result=n
#
#     @__check_num_zsq
#     def plus(self, n):
#         self.__result += n
#
#     @__check_num_zsq
#     def minus(self,n):
#         self.__result -= n
#
#     @__check_num_zsq
#     def multiply(self,n):
#         self.__result *= n
#
#     @__check_num_zsq
#     def divide(self,n):
#         self.__result /= n
#
#     def show(self):
#         print('计算的结果是:%d'%(self.__result))
#
#     pass
#
# # (2+6-4)*5
# res=Caculator(2)
# res.plus(6)
# res.minus(4)
# res.multiply(5)
# res.show()

# --------------------代码8 方法一-----------------------
# # 选用python3.8解释器  安装pywin32库
# import win32com.client
#
# # # 1.创建一个播报器对象
# # speaker=win32com.client.Dispatch("SAPI.SpVoice")
# # # 通过这个播报对象，直接，播放相对于的字符串就可以
# # speaker.Speak('hei hei')
#
# class Caculator:
#
#     # def __say_any(func):
#     #     def inner(self):
#     #         func(self)
#     #         # 1.创建一个播报器对象
#     #         speaker1 = win32com.client.Dispatch("SAPI.SpVoice")
#     #         # 通过这个播报对象，直接，播放相对于的字符串就可以
#     #         speaker1.Speak(self.speak)
#     #     return inner
#
#     def __say(func):
#         def inner(self,n):
#             res=func(self, n)
#             # 1.创建一个播报器对象
#             speaker = win32com.client.Dispatch("SAPI.SpVoice")
#             # 通过这个播报对象，直接，播放相对于的字符串就可以
#             speaker.Speak(self.speak)
#
#             return res   #返回传入函数的执行结果
#         return inner
#
#     def __check_num_zsq(func):
#         def inner(self,n):
#             if not isinstance(n, int):
#                 raise TypeError('当前这个数据的类型有问题')
#             return func(self,n)   #返回传入函数的执行结果
#         return inner
#
#     @__check_num_zsq
#     @__say
#     def __init__(self,n):
#         self.speak = f'{n}'
#         self.__result=n
#
#     @__check_num_zsq
#     @__say
#     def plus(self, n):
#         self.speak = f'加上{n}'
#         self.__result += n
#
#     @__check_num_zsq
#     @__say
#     def minus(self,n):
#         self.speak = f'减去{n}'
#         self.__result -= n
#
#     @__check_num_zsq
#     @__say
#     def multiply(self,n):
#         self.speak = f'乘以{n}'
#         self.__result *= n
#
#     @__check_num_zsq
#     @__say
#     def divide(self,n):
#         self.speak = f'除以{n}'
#         self.__result /= n
#
#     @__say_any
#     def show(self):
#         self.speak = f'等于{self.__result}'
#         print('计算的结果是:%d'%(self.__result))
#
#     pass
#
# # (2+6-4)*5
# res=Caculator(2)
# print(res.speak)
# res.plus(6)
# print(res.speak)
# res.minus(4)
# print(res.speak)
# res.multiply(5)
# print(res.speak)
# res.show()


# --------------------代码8 方法二-----------------------
# # 选用python3.8解释器  安装pywin32库
# import win32com.client
#
# class Caculator:
#
#     def __said(self,word):
#         # 1.创建一个播报器对象
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         # 通过这个播报对象，直接，播放相对于的字符串就可以
#         speaker.Speak(word)
#
#     def __creat_say_zsq(word=''):
#         def __say(func):
#             def inner(self,n):
#                 self.__said(word + str(n))
#                 return func(self, n)   #返回传入函数的执行结果
#             return inner
#
#         return __say
#
#     def __check_num_zsq(func):
#         def inner(self,n):
#             if not isinstance(n, int):
#                 raise TypeError('当前这个数据的类型有问题')
#             return func(self,n)   #返回传入函数的执行结果
#         return inner
#
#     @__check_num_zsq
#     @__creat_say_zsq()   #调用creat_say_zsq方法 返回一个装饰器
#     def __init__(self,n):
#         self.__result=n
#
#     @__check_num_zsq
#     @__creat_say_zsq('加上')
#     def plus(self, n):
#         self.__result += n
#
#     @__check_num_zsq
#     @__creat_say_zsq('减去')
#     def minus(self,n):
#         self.__result -= n
#
#     @__check_num_zsq
#     @__creat_say_zsq('乘以')
#     def multiply(self,n):
#         self.__result *= n
#
#     @__check_num_zsq
#     @__creat_say_zsq('除以')
#     def divide(self,n):
#         self.__result /= n
#
#     def show(self):
#         print('计算的结果是:%d'%(self.__result))
#         self.__said('计算的结果是' + str(self.__result))
#
#     @property
#     def result(self):
#         return self.__result
#     pass
#
# # (2+6-4)*5
# res=Caculator(2)
# res.plus(6)
# res.minus(4)
# res.multiply(5)
# res.show()
# print(res.result)

# --------------------代码9-----------------------
# 选用python3.8解释器  安装pywin32库
import win32com.client

class Caculator:

    def __said(self,word):
        # 1.创建一个播报器对象
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        # 通过这个播报对象，直接，播放相对于的字符串就可以
        speaker.Speak(word)

    def __creat_say_zsq(word=''):
        def __say(func):
            def inner(self,n):
                self.__said(word + str(n))
                return func(self, n)   #返回传入函数的执行结果
            return inner
        return __say

    def __check_num_zsq(func):
        #传入一个函数func，返回给外界一个func的增强函数inner
        def inner(self,n):
            """
            inner 有func的功能，并且还有扩展的一些功能，可以看成是func的增强函数
            :param self:实例
            :param n: 用户输入 参与运算的数字
            :return: func函数的执行结果
            """
            if not isinstance(n, int):
                raise TypeError('当前这个数据的类型有问题')
            return func(self,n)   #运行func并且返回给外界
        return inner

    @__check_num_zsq
    @__creat_say_zsq()   #调用creat_say_zsq方法 返回一个装饰器
    def __init__(self,n):
        self.__result=n

    @__check_num_zsq
    @__creat_say_zsq('加上')
    def plus(self, n):
        self.__result += n
        return self

    @__check_num_zsq
    @__creat_say_zsq('减去')
    def minus(self,n):
        self.__result -= n
        return self

    @__check_num_zsq
    @__creat_say_zsq('乘以')
    def multiply(self,n):
        self.__result *= n
        return self

    @__check_num_zsq
    @__creat_say_zsq('除以')
    def divide(self,n):
        self.__result /= n
        return self

    def show(self):
        print('计算的结果是:%d'%(self.__result))
        self.__said('计算的结果是' + str(self.__result))

    def clear(self):
        self.__result=0
        self.__said('归零')
        return self

    @property
    def result(self):
        return self.__result
    pass

# (2+6-4)*5
res=Caculator(2)
# 链式编程
res.plus(6).minus(4).multiply(5).divide(10).clear().plus(10)
res.show()
print(res.result)






