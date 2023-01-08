# # 求任意组连续自然数的和1-10 20-30 35-45
# def anySun(a,b):
#     result = 0
#     for i in range(a,b+1):
#         result+=i
#         pass
#     print(result)
#
# def anySun1(a,b):
#     result=sum(range(a,b+1))
#     return result
#
# print(anySun1(20,30))
#
#
# # 100和尚吃100个馒头，大和尚1人3个，小和尚3人一个，大小和尚一共几个人？
# def count():
#     for a in range(1,100):
#         if a*3+(100-a)*1/3==100:
#             return (a,100-a)
#         pass
#     pass
# result=count()
# print('大和尚{}人，小和尚{}人'.format(result[0],result[1]))


# 指定一个列表，列表里由一个唯一不重复的元素，找它出来
li1=[1,2,3,4,2,3,4,6,5,5,6,5,6]
set1=set(li1)      #去重
li2=list(set1)
for i in li2:
    li1.remove(i)  #将li1里面的 li2全部去掉
    pass
set2=set(li1)      #去重，剩下li1里，重复出现的数字
for i in set1:
    if i not in set2:
        print(i)
        pass
    pass

# print(set1-set2)        #这样代码更简洁,但是返回的是集合











