class Money:
    pass
one=Money()
one.age=10
print(one.__dict__,'one的属性和属性值 是以键值对的形式存储在内存中 是个字典')

print('-' * 10,'直接将字典类型赋值给one.__dict__','-' * 10)
one.__dict__={'name':'ybw'}
one.__dict__['age']=999
print(one.age)
print(one.name)

print('-' * 10,'类的__dict__属性是不能被修改的','-' * 10)
try:
    Money.__dict__={'姓名':'ybw'}
except Exception as e:
    print(e)

print('\n一般情况下，属性存储在__dict__ 的字典当中 有些内置对象没有这个__dict__属性\n',
       '一般对象可以直接修改__dict__属性\n',
       '但对类象的__dict__为只读，默认无法修改 可以通过setattr方法修改')

print('\n类属性被各个对象共享')
two=Money()
Money.size=12
print(one.size)
print(two.size)

print('\n如下代码会不会报错')
p=Money()
p.size += 2  #p.size(新建实例属性) = p.size(访问类属性)+2
print(p.size)
print(Money.size)