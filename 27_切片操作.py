class Person:

    def __init__(self):
        self.item=[1,2,3,4,5,6]

    def __setitem__(self, key, value):
        """

        :param key:一个切片对象 slice 有 开始 结束 步长
        :param value:
        :return:
        """
        print(key.start)
        print(key.stop)
        print(key.step)
        print(value)
        if isinstance(key,slice):  #前面一个实例是否是后面某一个类型  判断key是否是slice
            self.item[key.start:key.stop:key.step]=value
        pass

    def __getitem__(self, item):
        print('getitem',item)
        pass

    # 删除的方法
    def __delitem__(self, key):
        print('delitem',key)
        pass

    pass
p=Person()
p[0:4:2]=['a','b']
print(p.item)