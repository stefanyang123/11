# 强制类型转换
# int()    转换为整形
# float()  转换为浮点型
# str()    转换为字符串,返回对象的string格式
# 函数将对象(列表 元组 数字等)转化为字符串

print('----------str()---------')
lis=str(1)
print(lis)
print(type(lis))



print('--------list()-----------')
# list()   将元组转换为列表  将元组！
tup=(1,2,3,4)
print(type(tup))
li=list(tup)
print(type(li))
li.append('强制转换成功')
print(li)


print('---------tuple()----------')
# tuple()  转换为元组 只要是序列都能转！
tupList=tuple(li)
print(type(tupList))


print('---------dict()----------')
# dict()   创建一个字典
dic1=dict()
print(type(dic1))
# dic1=dict(a=1,b='hello',c=[1,2,3])  这种添加方式也可以
dic1['name']='小明'
dic1['age']=18
print(dic1)


print('----------bytes()---------')
# bytes()   转换字节类型的数组
print(bytes('我 喜 欢 python',encoding='utf-8'))


print('---------bin()----------')
# bin()    十进制转二进制
print(bin(10))  #转换二进制 0b开头是二进制


print('--------hex()-----------')
# hex()     十进制转十六进制 0x开头是16进制
print(hex(242))


# oct()     十进制转八进制



# bool()   转换为True 和 False
# 如果没有参数返回False
# bool(x)  x=[],(),{},0,0.0,None  都返回False


print('--------ord-----------')
# chr(i)    数字转字符 用一个range(256)内的(0-255)整数做参数，返回一个对于的字符
# i 可以是十进制也可以是十六进制形式的数字
# 返回值是当前整数对应的ASCII字符
# ord(长度为1的字符串)       字符转换数字

# print(ord('py'))  报异常
print(ord('p'))     #正确方法















