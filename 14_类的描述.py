'''
类的描述
方便理清逻辑思路 方便多人开发时的沟通  方便生成项目文档

'''
class Person:
    """
    关于这个类的描述，类的作用
    类的构造函数
    类属性的描述
    Attributes:
        count: int 它的含义
    """
    count=1

    def run(self,distance,step):
        """
        这个方法的作用效果
        :param distance: 参数的含义，参数的类型（python是动态语言，类型是不确定的），是否有默认值
        :param step:  参数的含义，参数的类型，是否有默认值
        :return:  返回的结果的含义 返回的数据类型
        """
        print('人在跑')
        pass
    pass

# 查看类的描述
help(Person)










