# 1.类就是个模板，模板里可以包含多个函数，函数里实现一些功能，
# 2.是一系列相似对象的组合，对象是根据模板创建的实例，通过实例对象可以执行类中的函数
# 3.定义在类的里面，方法的外面，叫类属性，定义在方法里面使用self引用的属性称为 实例属性
class Fl():
    def __init__(self,name,col,hp):
        self.name=name
        self.col=col
        self.hp=hp
        pass
    def ip(self):
        print('self的id是',id(self))
    def tong(self,shei):
        """
        同shei谁的hp就减去10
        :param shei:
        :return:
        """
        shei.hp-=10
        print('{}捅了{}一刀，{}掉了10血'.format(self.name,shei.name,shei.name))
        pass
    def __str__(self):
        return '%s的颜色是%s的,血量为%d'%(self.name,self.col,self.hp)

pg=Fl('苹果','红',100)
pg.zj=10  #通过对象添加属性，类里面是一些共性的属性，这里一般是对象特定的属性
print('苹果的直径是',pg.zj)

jz=Fl('橘子','橙',100)
print(pg,jz)


print('----self就是实例本身----')
pg.ip()
print('{}的id是'.format(pg.name),id(pg))

pg.tong(jz)
print(jz)





















