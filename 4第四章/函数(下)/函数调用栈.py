def level_3():
    print ('进入 level_3')
    a = [0]
    b = a[1]    #正确代码  b = a[0]
    print ('离开 level_3')

def level_2():
    print ('进入 level_2')
    level_3()
    print ('离开 level_2')

def level_1():
    print ('进入 level_1')
    level_2()
    print ('离开 level_1')


level_1()

print('程序正常退出')

'''
程序会有如下报错


进入 level_1
进入 level_2
进入 level_3
Traceback (most recent call last):
  File "D:\pythonProject7\函数调用栈.py", line 18, in <module>
    level_1()
  File "D:\pythonProject7\函数调用栈.py", line 14, in level_1
    level_2()
  File "D:\pythonProject7\函数调用栈.py", line 9, in level_2
    level_3()
  File "D:\pythonProject7\函数调用栈.py", line 4, in level_3
    b = a[1]
IndexError: list index out of range

先调用 level_1 执行line 18  没有往下执行
再调用 level_2 执行line 14  没有往下执行
再调用 level_3 执行line 9   没有往下接着执行
再执行 line 4  执行的时候会有 IndexError: list index out of range报错

这个错误会在 level_3 中 发出 
如果level_3      没有捕获异常  不会往下执行
就会返回level_2   没有捕获异常  不会往下执行
就会返回level_1   没有捕获异常  不会往下执行
就会返回line18 那行  再没有捕获异常 不会往下执行 会报错

我们可以尝试再不同函数调用层 捕获异常
在最里层捕获异常 是能将所有函数的内容正常运行的

'''