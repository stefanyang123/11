# 简易装饰器
def func_improve(func):
    def innerfun():
        print('func扩展1')
        func()
        print('func扩展2')
    return innerfun

@func_improve
def funca():
    print('123')
    pass

funca()

