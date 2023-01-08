# 接收n个数字，求这些参数数字的和
# def SUM(*args):   #*args传进来是元组
#     result = 0
#     for answer in args:
#         result += answer
#         pass
#     return result
# SUM(1,2,3,4,5)
# print(SUM(1,2,3,4,5))
#
#
#
#
#
# # 找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
# list1=['00',11,22,33,44,55,66,77,88,99,12]
# tupleA=('00',22,33,44,55,66,88,99,12)
#
#
# # 自己的方法
# def ji(num):
#     '''
#     num等于列表元素总数偶数除以2，奇数减一除以2
#     :param num:
#     :return:
#     '''
#     list2=[]
#     for i in range(num):
#         a=2*i+1
#         # list2.append(list1[a])
#         list2.append(tupleA[a])
#         pass
#     return list2
# print(ji(4))

# 老师的方法
def jishu(num):    #没有*是列表类型，*arge 元组 **kwarge 字典
    """
    处理列表
    :param num:  接入一个元组或列表都没问题
    :return: 返回新的列表对象
    """
    listNew=[]
    index=1
    for i in num:
        if index%2==1:
            listNew.append(i)
            pass
        index+=1
        pass
    return listNew

rs3=jishu(['d',1,2,3,4,5,6])
print(rs3)


olddata=tuple(range(10,30))
print('原始数据',olddata)
rs4=jishu(range(10,30))   #动态生成一个range类型
rs4=jishu(tuple(range(10,30)))   #tuple(range(10,30))强制转换为元组类型
print('处理后的数据',rs4)




# 检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容
# 并将新的内容返回给调用者。字典里的value只能是字符串或列表

# # 定义一个判断字符长短函数
# def serh(val):
#     '''
#     检查每个字符串的长度，大于二返回前两个
#     :param val:
#     :return:
#     '''
#     long = len(val)
#     if long>2:
#         val=val[:2]
#         pass
#     return val
# # 规范书写0函数
# def decision(want):
#     '''
#     规范书写Y/N
#     :param want:
#     :return:
#     '''
#     if want=='Y'or want=='y':
#         return want
#     elif want=='N'or want=='n':
#         return want
#     else:
#         while want != 'Y' or want != 'y' or want != 'N' or want != 'n':
#             want = input('请输入Y/y继续，N/n退出')
#             if want == 'Y' or want == 'y':
#                 break
#                 pass
#             elif want == 'N' or want == 'n':
#                 break
#                 pass
#             pass
#         return want
# # 规范书写1函数
# def decision1(want):
#     '''
#     规范书写Y/N
#     :param want:
#     :return:
#     '''
#     if want=='Y'or want=='y':
#         return want
#     elif want=='N'or want=='n':
#         return want
#     else:
#         while want != 'Y' or want != 'y' or want != 'N' or want != 'n':
#             want = input('请输入Y/y继续新建，N/n输入字典里的键')
#             if want == 'Y' or want == 'y':
#                 break
#                 pass
#             elif want == 'N' or want == 'n':
#                 break
#                 pass
#             pass
#         return want
#
# # 新建一个字典
# dictA={}
# dictA['name']='杨博文'
# dictA['age']='18'
# dictA['pos']='学生'
# dictA['don']='hhh'
#
# # 用户输入要修改数据项的key，判断key是否存在
# key=input('请输入键....')
# if key not in dictA.keys():
#     want = input('字典里没有这个键，是否新建？[Y/N]...')
#     dec2 = decision1(want)    #规范书写1
#     if dec2 == 'Y' or dec2 == 'y':
#         val=input('请输入新的键....')
#         key=serh(val)
#         dictA[key] = 'none'
#         pass
#     else:
#         while key not in dictA.keys():
#          key=input('请输入字典里的键...')
# print('---------好的---------')
#
# #读取一下字典，给用户显示修改前的键值对，以确认
# value=dictA[key]
# print('当前键为{}，值为{}'.format(key,value))
#
# # 用户输入要修改的内容
# print('------不超过两字符-------')
# val=input('请问{}要修改成什么？'.format(key))
# print('---------完成！---------')
# dictA[key]=serh(val)
#
# # 是否要查看
# want=input('是否查看字典或退出？[Y/N]')
# dec=decision(want)             #调用函数赋值给新变量，容易发现问题
# if dec == 'Y' or dec == 'y':
#     print('呐！\n{}'.format(dictA))
#     print('-----谢谢使用，已退出----')
#     pass
# elif dec =='N'or dec =='n':
#     print('-----谢谢使用，已退出----')
#     pass




# if want=='Y'or want=='y':
#     print('呐！\n{}'.format(dictA))  #换行？\n对  /n错
#     print('-----谢谢使用，已退出----')
#     pass
# elif want=='N'or want=='n':
#     print('-----谢谢使用，已退出----')
#     pass
# else:
#     want = input('请输入Y/y继续，N/n退出')
#     while want != 'Y' or want != 'y' or want != 'N' or want != 'n':
#         want = input('请输入Y/y继续，N/n退出')
#         if want == 'Y' or want == 'y':
#             print('呐！\n{}'.format(dictA))
#             print('-----谢谢使用，已退出----')
#             break
#             pass
#         elif want == 'N' or want == 'n':
#             print('-----谢谢使用，已退出----')
#             break
#             pass
#         pass

# 老师的代码
def dictFunc(dic):  # **kwargs  可以直接写个变量，也可以写一个可变关键字参数
    """
    处理字典类型的数据
    :param dic:字典
    :return:
    """
    result={}     #空字典
    for key,value in dic.items():  #对传进来的字典遍历 key-value,传进来两项，自然能用两个变量接收
        if len(value)>2:
            result[key]=value[:2]   #向字典里添加数据
            pass
        else:
            result[key]=value
            pass
    return result
    pass

dictobj={'name':'杨博文','hobby':['唱歌','跳舞','rap'],'pro':'中国艺术'}
print(dictFunc(dictobj))

"""
总结

1.
for XXX in 可迭代对象：（可以是所有序列，包括字符串，列表，元组）
for XXX,XXX in 可迭代对象：（这里一般是字典，因为字典是键值对）


2.
def sunFunc(num)    num 可以导入任何东西 数字，字符串，列表，元组，字典
                    具体要看处理什么，怎么处理
                    *num   导入元组   
                    **num  导入字典
 3.                   
字符串，列表，元组，都是序列，都可通过切片操作
"""


