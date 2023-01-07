# 合并操作+
# 两个对象相加操作，会合并两个对象（适用于字符串，列表，元组）
# 复制*
# 对自身按指定次数进行+操作（适用于字符串，列表，元组）
# in判断元素是否存在与对象里（适用于字符串，列表，元组，字典）

print('--------字符串合并操作--------')
strA='我很开心'
strB='我用python'
print(strA+strB)

print('--------列表合并操作--------')
listA=list(range(10))
listB=list(range(11,20))
print(listA+listB)

print('--------复制操作--------')
# 复制*
print(strA*3)      #让strA复制三次
print(listA*3)      #让listA复制三次

print('--------对象是否存在--------')
print('我' in strA)       #结果是个布尔类型的值
print('我' not in strA)
print(22 in listA)
dictA={'name':'peter'}
print('age' in dictA)      #判断键'age'是否在字典中






