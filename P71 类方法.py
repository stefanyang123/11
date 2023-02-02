# 类方法
# 类对象所拥有的方法，需要用装饰器 @classmethod 来标识其为类方法
# 对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数，类方法，可以通过类对象，实例对象调用
class People:
    country='中国'
    # 类方法 用@classmethod方法
    @classmethod  #加上这个修饰器后，方法的所有权归类对象所有，实例对象仍有使用权，但无修改权
    def get_country(cls):
        return cls.country  #通过类对象访问这个类属性
        pass

    @classmethod
    def change_country(cls,data):
        cls.country=data
        pass
    pass
print(People.get_country()) #通过类对象调用get_country类方法
p=People()
print('实例对象访问类方法',p.get_country())   #通过实例对象调用get_country类方法
print('--------类方法修改类对象---------')
print('修改前',People.country)
People.change_country('chinaa')
print('修改后',People.country)