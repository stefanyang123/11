# 将实例化的对象 也以操作字典或者操作列表那样 来进行操作
class Person:

    def __init__(self):
        self.cache={}

    # 修改的方法
    def __setitem__(self, key, value):
        print('setitem',key,value)
        self.cache[key]=value
        pass

    # 查询的方法
    def __getitem__(self, item):
        print('getitem', item)
        return self.cache[item]
        pass

    # 删除的方法
    def __delitem__(self, key):
        print('delitem', key)
        del self.cache[key]
        pass

    pass

p=Person()

# 像操作字典一样 操作实例
# 往实例p 的cache属性（字典） 添加一键值对
p['name']='ybw'
print(p.cache)    # {'name': 'ybw'}

# 查询
print(p['name'])    #ybw

# 删除
del p['name']

