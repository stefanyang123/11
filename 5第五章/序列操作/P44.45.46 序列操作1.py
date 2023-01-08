# all(i)函数用于判断给定的可迭代参数i(元组或列表)，中所有的元素是否为True
# 如果是，返回True 否则返回False（可迭代参数对象里的元素至少有一项为0 空 False）
# 类似与逻辑运算符and的判断，只要有一个为False,结果为False
# 元素除了0 空 False 外都算True  对象i如果是个空列表，空元组也为True
print('--------all()------------')
li=[]
print(all(li))
li=[1,2,3,[]]
print(all(li))
li=[1,2,3,0]
print(all(li))


print('--------any()------------')
# any()函数用于判断给定的可迭代参数i(元组或列表),中所有的元素是否为False
# 如果是，返回False 否则返回True （可迭代参数对象里的元素至少有一项不为0 空 False）
# 类似与逻辑运算符or的判断，只要有一个为True,结果为True
# 元素除了0 空 False 外都算True
li1=[]
print(any(li1))
li1=[1,2,3,[]]
print(any(li1))
li1=[(),{},0,[]]
print(any(li1))



print('--------sort(list)与sorted(可迭代对象)------------')
# sort()应用在列表上的方法，返回对已存在的列表进行操作
# sorted()可以对所有的可迭代对象进行排序,返回一个全新的list
# sorted(iterable[,cmp[,key[,reverse]]])
# iterable--可迭代对象
#cmp--比较的函数，具有两个参数，参数的值从可迭代对象中取出
# 此函数遵守的规则为，大于则返回1，等于返回0，小于返回-1
# reverse(反向的意思)--排序规则  reverse=True 降序 False 升序(默认)
# 返回从新排序的列表
print('--------sorted(可迭代对象)------------')
lis=[5,6,8,1,2,4]
varList=sorted(lis,reverse=True)
print('降序前{}'.format(lis))
print('降序后{}'.format(varList))
lis=sorted([5,6,8,1,2,4],reverse=True)
print(lis)

print('--------列表.sort()------------')
lis1=[1,2,55,46,87,3]
lis1.sort()   #sort排序方法,直接修改的是原始对象
print(lis1)


print('--------列表.reverse()------------')
# 对列表对象里的元素进行反向排序


print('--------range()------------')
# range(start,stop[,step])
# start--默认从0开始 如range(5)  0,1,2,3,4 等价于range(0,5)
# stop--到stop结束，不包括stop
# step--默认1，range(0,5) 等价于 range(0,5,1)


print('--------zip()------------')
# 用来打包的,会把序列中对应的索引位置的元素存储为一个元组
# zip(iterable,.....)  一个或多个迭代器
# 用于将对象中对用的元素打包成一个个元组，返回由这些元组组成的列表
s1=['a','b','c','d']
s2=['你','我','他','她']
print(list(zip(s1)))
a=zip(s1,s2)
print(type(a))  #它是一个zip类型的，也是可迭代对象 <zip object at 0x0000024C0EACEF40>结果是个zip对象，内存地址在后面那一串16进制
print(a)
print(list(a))

# 如果可迭代对象的元素个数不一样，按照最少的那个迭代对象，压缩其中的元素
a=zip(['a','b','c','d'],['1','2'],s2)
print(list(a))

# print('--------zip()例子------------')
# def zipFunc():
#     books=[]  #存储所有的图书信息
#
#     id=input('请输入编号，每个项以空格分割..')#str
#     bookName=input('请输入书名，每个项以空格分割..')#str
#     bookPos=input('请输入书的位置，每个项以空格分割..')#str
#
#     idList=id.split(' ')   #生成序列可迭代对象
#     nameList=bookName.split(' ')  #以空格分割
#     posList=bookPos.split(' ')
#
#     item=zip(idList,nameList,posList)#进行打包处理
#     for bookItem in item:
#         """
#         遍历图书信息进行存储
#         """
#         dicInfo={'编号':bookItem[0],'书名':bookItem[1],'位置':bookItem[2]}
#         books.append(dicInfo)    #将字典对象加到list中
#         pass
#     for item in books:
#         print(item)
# zipFunc()

print('--------enumerate()遍历列表------------')
# 用于将一个可遍历的数据对象（列表元组字符串）组合为一个索引序列，同时列出数据和数据下标
# 一般用作for循环里  返回一个enumerate(枚举)对象
# enumerate(sequence[,start=])
# sequence--一个序列，迭代器或其他支持迭代的对象
# start--下标起始位置，默认从零开始

list1=['a','b','c','d']
for item in enumerate(list1):
    print(item)  #item是元组类型
for index,item in enumerate(list1):
    print(item)    #单独把索引值用index接收了

print('--------enumerate()遍历字典------------')
dictA={}
dictA['name']='杨博文'
dictA['age']='18'
dictA['pos']='学生'
dictA['don']='hhh'
print(dictA)
for index1,item1 in enumerate(dictA):  #用index1接收索引值
    print(item1,end=' ')       #用item1获取key值
    print(dictA[item1])        #用key访问字典


