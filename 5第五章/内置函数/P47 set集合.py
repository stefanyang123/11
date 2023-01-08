# set(集合)是python中的一种数据类型，是一个无序的且不重复的元素集合
# 由于元素间无序不重复，可以转换为集合来做去重的操作，不支持索引，切片，更像是一个只有key的字典
print('--------集合的创建------')
# 创建一个字典
dic1={1:3}
dic2={}    #这个是空字典！
print(type(dic1))
print(type(dic2))

# 集合的创建，类似于字典，但是只有key没有value
set1={'1','2'}
set2={1,2,3}
print(type(set2))
# 或者
list1=[1,2,3,4]
set3=set(list1)   #强制转换为集合形式

print('--------添加操作add()------')
set1.add('python')
print(set1)

print('--------清空操作clear()------')
set1.clear()
print(set1)

print('------取两个集合的差集difference()------')
a={1,2,3,4,}
b={3,4,5,6}
print(a.difference(b))   #可以理解为a与b不同的地方
print(b.difference(a))   #b与a不同的地方
print(a-b)


print('------取两个集合的交集intersection()------')
print(a.intersection(b))
print(a&b)   #&与

print('------取两个集合的并集union()------')
print(a.union(b))
print(a|b)

print('------随机移除集合里的某个元素pop()------')
# 从集合中拿数据且同时删除
print('pop前',a)
print(a.pop())
print('pop后',a)

print('------移除集合里指定的元素discard()------')
print('discard前',b)
print('移除6')
b.discard(6)   #不返回值，打印不出来
print('discard后',b)


print('------更新集合update()------')
a={1,2,3,4,}
b={3,4,5,6}  #往a里添加集合b，会去掉把重复的去掉
a.update(b)
print(a)
# 并集会造出新的集合，而update只是对a的修改，没有新的集合产生

