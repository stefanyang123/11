def foo(name,age=18):
    print(f'位置参数{name}')
    print('-'*40)
    print(f'Keyword参数{age}')
    print('-' * 40)
    pass

foo('我',19)  #可以按顺序传递参数
foo(age=19,name='我')  #也可以以键值的形式 不按顺序传递参数

'''
#如果在形参中添加一个 /
# /前面的形参只能通过位置直接传递参数的值  不可以使用键值的方式进行传递
def foo(name,/,age=18):   
    print(f'位置参数{name}')
    print('-' * 40)
    print(f'Keyword参数{age}')
    print('-' * 40)
    pass
foo('wo',18)    

#如果在形参中添加一个 *
# *后面的形参只能通过键值的方式传递参数的值  不可以使用参数的值直接传递参数的值
def foo(name,*,age=18):   
    print(f'位置参数{name}')
    print('-' * 40)
    print(f'Keyword参数{age}')
    print('-' * 40)
    pass
foo('wo',age=18)

# 在/和*中间的形参
# 既可以直接使用参数值进行传递 又可以使用键值的方式传递
def foo(name,/,sex,*,age=18):   
    print(f'位置参数{name}')
    print('-' * 40)
    print(f'Keyword参数{age}')
    print('-' * 40)
    pass
foo('wo',sex=1,age=18)
foo('wo',0,age=18)
'''

# 另外两个常用参数的定义
'''
在参数前面加一个* 那么这个参数就可以接受多个参数值 并以元组的形式获取
在参数前面加两个* 那么这个参数就可以接受多个以键值形式的参数值 并以字典的形式获取

'''
def foo1(*args,**kwds):
    print(args)
    print('-' * 40)
    print(kwds)
    print('-' * 40)
    pass



