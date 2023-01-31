# 没有装饰器的写法
# def sign(func):
#     '''
#     传入一个函数，给这个函数增强一些功能，并返回增强后的函数 improve_func
#     :param func:原来的函数
#     :return:improve_func 增强后的函数
#     '''
#     print('进入装饰器')
#     print('传入的函数',func)
#     def improve_func(*args):
#         print('传入的参数:',*args)
#         if func(*args):
#             print('注册成功！')
#         else:
#             print('失败')
#     return improve_func
#     pass
#
# def len_name(username):
#     if len(username)<6:
#         return True
#     else:
#         return False
#     pass
#
# 需要显示的去调用，主功能是len_name的实现  附加功能是 sign显示注册成功与否
# len_name=sign(len_name)
# len_name('ybw')

print('------------------有装饰器的写法-------------------')
def sign(func):
    '''
    传入一个函数，给这个函数增强一些功能，并返回增强后的函数 improve_func
    sign被称为闭包函数 传入传出都是函数
    :param func:原来的函数
    :return:improve_func 增强后的函数
    '''
    print('进入装饰器')
    print('传入的函数',func)

    def improve_func(*args,**kwargs):
        '''
        对func功能进行增强扩展
        :param args: 任意参数
        :param kwargs: 任意键值对
        :return: 无返回值
        '''
        print('传入的参数:',*args,**kwargs)
        if func(*args,**kwargs):
            print('注册成功！')
        else:
            print('失败')
        pass

    return improve_func
    pass

@sign
def len_name(username):
    if len(username)<6:
        return True
    else:
        return False
    pass

# @sign
# def passward(word):
#     word=str(word)
#     if len(word)>10:
#         return True
#     else:
#         return False

# len_name('ybw')
# passward(1234567897897)
