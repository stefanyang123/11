class Person:
    # 实例方法
    def run(self):
        pass

    # 类方法  需要装饰器 @classmethod
    @classmethod
    def leifangfa(cls):
        print('这是一个类方法','cls传递的是类',cls)
        pass




    pass

# 通过类调用
Person.leifangfa()

# 通过一个实例进行调用
p=Person()
p.leifangfa()  #传递的是 p实例所对应的类 而不是p实例

# 间接调用
func=p.leifangfa
func()
