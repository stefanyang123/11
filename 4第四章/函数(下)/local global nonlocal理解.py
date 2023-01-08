# 定义在方法外的变量叫全局变量
b='全局变量 global variable'

def foo():
    # 定义在方法内的 叫局部变量
    # 局部变量 只能在方法内被访问
    a='局部变量 local variable'
    print(b) #全局变量可以在方法内被访问 但不可以被操作
    '''
    强行对全局变量b进行修改 会报错
    因为在局部方法这里 找不到全局变量b的声明 
    因此需要在方法里使用关键字global
    像这样子定义就能在方法里去操作全局变量了
    '''
    global b
    b=b+'!'
    pass

foo()
print(b) #全局变量也可以在方法外被访问

'''
如果在方法里在定义一个方法 也就是定义一个内部方法
想要在这个内部方法里操作全局变量 同样用global 关键字

但如果想在内部方法去操作外部方法定义的变量
也就是说 现在想 在内部方法里去 操作这个c
就要用nonlocal关键字
'''
def foo1():
    c = '局部变量 local variable'
    def foo2():
        nonlocal c
        c=c+'!'
        pass
    foo2()
    pass
