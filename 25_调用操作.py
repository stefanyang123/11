class Person:
    def __call__(self, *args, **kwargs):
        print('执行了__call__方法')
        print(args,kwargs)
        pass

    pass

p=Person()
# 我们现在想让 实例对象 也具备像函数一样 被调用的能力 p()

p(123,456,name='ybw')  #解释器会自动的去 找类中的 __call__方法,如果没有实现该方法 就会报错

print('-'*20,'__call__方法的应用','-'*20)
# ----------------------具体应用-------------------------
class PenFactory:

    def __init__(self,p_type):
        self.p_type=p_type
        pass

    def __call__(self,p_color):
        print('创建了一个%s，它的颜色是%s'%(self.p_type,p_color))
        pass

    pass

gangbi=PenFactory('钢笔')  #创建一个实例 gangbi
gangbi('red')
gangbi('yellow')
gangbi('blue')

qianbi=PenFactory('铅笔')  #创建一个实例  qianbi
qianbi('red')
qianbi('green')
qianbi('bluck')
