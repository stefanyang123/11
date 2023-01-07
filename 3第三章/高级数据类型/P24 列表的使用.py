# list列表是一种有序的集合，可以随时添加和删除其中的元素
# 特点：
# 1.支持增删改查
# 2.列表中的数据是可以变化的[数据项是可以变化的，列表的内存地址不会改变]
# 3.用中括号来表示列表类型，数据项之间用逗号来分割，数据项可以是任何类型的数据！
# 4.支持索引和切片

# append   在列表后追加元素
# count    统计元素出现的次数
# extend   扩展，相当于批量添加
# index    获取指定数据索引号（下标）
# insert   在指定位置插入
# pop      删除最后一个元素
# remove   移除指定元素
# reverse  反转列表
# sort     列表排序 reverse=ture倒序



print('---列表---')
# li=[]       #定义一个空列表
li=[1,2,3,"你好"]
print(len(li))       #len()对于字符串，返回字符串长度，对于列表，返回列表元素的个数
strA='我喜欢python'
print(len(strA))
print(type(li))


print('---查找列表---')
# 查找列表
listA=['abc',758,13.1,'你好',True]
print(listA)    #序列是支持索引的，列表也是序列，支持索引就能切片
print(listA[0])    #输出第一个元素
print(listA[1:3])    #输出第二个元素（索引是1），到第三个元素(索引是2)
                     # 之所以是3，是因为不包括索引3对应的第四个元素
print(listA[2:])
print(listA[::-1])
print(listA*2)   #输出多次列表中的数据复制
#查找元素的索引
print(listA.index(758))  #获取指定元素索引号 返回的是一个索引下标

# 指定查找范围，查找特定元素
# print(listA.index(13.1,0,2))  #查找13.1是否在列表的第一位和第三位之间（不包括第三位）
#                               查不到会报异常



print('---常用的函数---')

print('---追加操作---')
# 追加操作
listA=['abc',758,13.1,'你好',True]
print(listA)
listA.append(['yy','bb','ww'])   #列表中可以有列表，列表中可以有任何数据
print('追加之后',listA)
listA.append(8888)   #追加单个数据8888
print('追加之后',listA)



print('---插入操作---')
# 插入操作
listA.insert(1,'我插入的数据')   #insert(位置，插入的内容)  在指定位置插入数据，其他数据往后移动
print(listA)



print('---批量加入操作---')
#批量加入（扩展）  把一个列表批量加入另一个列表中
data=range(10)  #生成10个序列 赋值给data
print(type(data))
data=list(range(10))     #list()强制转换成list对象
print(type(data))

listA.extend(range(10))         #它的参数是个可迭代对象
print(listA)

data=list(range(5))
listA.extend(data)
print(listA)

listA.extend(['j','k'])
print(listA)


print('-------修改操作-------')
listB=['ybw',666,52.1,'你好啊',True,77,88,5,6]
print('修改之前',listB)
listB[0]='yang'        #把第一个数据修改成yang
print('修改之后',listB)


print('-------删除操作-------')
print('删除之前',listB)
del listB[0]        #删除列表里第一个元素
print('删除之后',listB)
del listB[1:3]      #批量删除第二到第三之间的数据
print('批量删除之后',listB)


listB.remove(True)   #移除指定的元素   True元素
print('删除指定元素',listB)

listB.pop(0)        #移除指定位置（索引）的元素  第一位
print('删除指定位置元素',listB)





