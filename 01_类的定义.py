# 命名规范 每个单词首字母大写
#经典类的定义
class Money:
    pass
# class Money():   #加括号表示继承的意思
#     pass

# 根据这个类创建（实例化）一个对象  类名+()
one = Money()
print(one)    #输入one.pri + tab键 可快速补全print(one)

# 打印结果<__main__.Money object at 0x00000231DA75AC10>  one Money这个类的实例化对象 在内存对应的地址
print(Money.__name__)
xxx=Money   #无论怎么赋值 类名都不会变
print(xxx.__name__)







