
# 一些重要的方法不允许外部调用，防止子类意外重写，把普通方法设置为私有化方法
# 在方法名前面加两个下划线即可私有化方法
# 跟私有化属性一样，一般是类内部调用，子类不能继承，外部不能调用
# 在类的外部调用就会报错

class Animal:
    def __init__(self,name):
        self.name=name
    def __eat(self):
        print('吃东西')
        return '吃东西'
        pass
    def run(self):
        print('跑起来了')
        pass
    def __str__(self):
        return '{}会{}'.format(self.name,self.__eat()) #在这调用私有化方法
class Bird(Animal):
    pass

bird1=Bird('鸟')
# bird1.eat()  发现调用不了了，说明eat方法已经私有化了
bird1.run()
print(bird1)

# _XXX前面加一个下划线，以但下划线开头的表示的是protected 类型的变量，即保护类型
# 只能允许其本身于子类进行访问，不能使用from XXX import * 的方式导入

# __XXX__前后两个下划线，是魔术方法，一般是python自有的，我们不要创建这类型的方法

# XXX_ 后面单下划线，避免属性名于python关键字冲突

