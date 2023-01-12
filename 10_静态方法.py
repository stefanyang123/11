class Person:
    @staticmethod
    def jingtai():
        print('这是一个静态方法')
        pass
    pass
# 标准调用
Person.jingtai()

# 通过实例调用
p=Person()
p.jingtai()

# 间接调用
func=Person.jingtai
func()