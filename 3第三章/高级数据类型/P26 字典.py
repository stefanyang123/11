# 字典(不是序列，不支持切片，没有索引)
# 字典是由 键值对 组成的集合，通常使用键来访问数据，跟list一样支持数据的添加，修改和删除操作
# 特点：
# 1.不是一个序列类型，没有下标概念，是一个无序的 键值集合，是python内置的高级数据类型
# 2.用{}来表示字典对象，每个键值对用逗号来分隔
# 3.字典的键(key)不能重复是唯一的，如果存在重复的键后者会覆盖前者，且只能是不可变类型(如数字，字符串，元组)
# 4.值(value)可以重复

# 可以储存任意对象，是以键值对的形式创建的{'key':'value'}利用大括号包裹
# 字典中，通过键来查找，字典的每个元素由2部分组成, 键:值
# 访问值用get方法,在我们不确定字典是否存在某个键而又想访问其值时使用


print('------------字典的创建---------------')
dictA={}
print(type(dictA))      #创建一个空字典
#给字典添加数据
dictA['name']='杨博文'   #给字典加一个键值对
dictA['age']='18'
dictA['pos']='学生'
# 结束添加
print(dictA)
dictB={'pro':'艺术','school':'北京'}  #以逗号分割为一个项，有两项
print(len(dictB))

print('------------字典的获取（查找）---------------')
print(dictA['name'])      #dictA['name']  'name'是一个键，打印键对应的值


print('------------字典的修改---------------')
dictA['name']='张国荣'     #修改键对应的值
print(dictA['name'])

dictA.update({'name':'我'})   #.update(新增数据项/修改的数据项)
print(dictA)

print('------------获取所有的键---------------')
print(dictA.keys())    #.keys() 获取所有的键

print('------------获取所有的值---------------')
print(dictA.values())  #.values()获取所有的值

print('------------获取所有的数据项（键值对）---------------')
print(dictA.items())   #.items()获取所有的数据项（键值对）

print('------------遍历所有数据项---------------')
for item in dictA.items():
    print(item)
    print(type(item))   #item是一个元组

print('------------遍历所有数据项1---------------')
for a,b in dictA.items():   #将字典中的 键 取出赋值给a 值赋值给b
    print('%s==%s'%(a,b))

print('------------删除数据项---------------')
del dictA['name']     #指定键名，用del 删除
print(dictA)

dictA.pop('age')      #用.pop()指定键名删除


print('------------对字典进行排序---------------')
dictA={}
dictA['name']='杨博文'
dictA['age']='18'
dictA['pos']='学生'
dictA['don']='hhh'
# sorted()    python内置的排序函数key如果是数字，按数字排。是字符串，按ASCLL码排

#d:d[0]代表按字典的key排序，d:d[1]代表按value排序，key=lambda d:d[]是固定用法
# key是sorted内的一个参数，用来指定排序方式key=lambda d:d[]是一个排序方法
sorted(dictA.items(),key=lambda d:d[1])  #如果value里有int又有str，不能比较排序会报错，统一value类型就好了
# 按字典的key排序
sorted(dictA.items(),key=lambda d:d[0])







