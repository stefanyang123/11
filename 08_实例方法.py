class Person:
    def eat(self,food):
        print('在吃',food)
        pass

    def eat2(xxx):
        print('把形参名称self改成xxx，也能传递实例',xxx)
        pass

    def eat3():
        print('直接把self删掉')

# 标准调用
p=Person()
p.eat('菠萝')   #前面的对象 p 会自动传入self中


'''
其他调用方式  本质就是直接找到函数本身来调用 

# 使用类调用
Person.eat(123,'apple')    #本例 123会被传入self中

# 赋值给变量通过变量 间接调用
func=Person.eat    #把Person类中的实例方法 eat拿出来赋值给func变量
func(123,'apple')

'''

print('-'*60)
p.eat2()

print('-'*60)
try:
    p.eat3()
except Exception as e:
    print(e,'\n说明p.eat 拿实例调用实例方法的时候'
            '\n解释器会自动的给这个方法传递第一个参数为实例对象'
            '\n而eat2没有形参来接收，就会报错')

















