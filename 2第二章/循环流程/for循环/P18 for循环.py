# for循环和while循环一样也可以完成循环
# 在python中for循环可以遍历任何序列的项目，如一个列表或者一个字符串

print('------for循环------')
# for循环
# 便立操作依次取集合容器中的每个值
#    for 临时变量 in 容器:
#         执行代码块

tags='我是个帅哥'     #字符串类型本身就是一个字符类型的集合
for item in tags:   #item是变量可以随意取名，在tags中取，赋值给item
    print(item)
    pass

# range 此函数可以生成一个数据集合列表
# range(起始,结束:步长)  步长不能为0,默认1
# range(1,100) 生成1-99，左包含右不包含
# print(type(range(1,100)))
for data in range(1,101):
    print(data,end='')
    pass


print()
print('------计算1加到100------')
sum=0
for data in range(1,101):
    sum+=data
    # print(sum, end='')
    pass
print(sum, end='')

print()
print('------找出50-200之间的奇数偶数------')
# for data in  range(50,201):
#     if data%2==0:
#         print('%d是偶数'%data)
#         pass
#     else:
#         print('%d是奇数'%data)
#         pass
#     pass



print('------break关键字------')
# break       代表中断结束，满足条件直接的结束本层循环
# continue    结束本次循环继续进行下次循环
# 当continue的条件满足的时候，本次循环剩下的语句将不再执行后面的循环继续
# 这两个关键字只能用在循环中
# sum=0
# for item in range(1,51):
#     if sum>100:
#         print('循环执行到%d就退出来了' %item)
#         break #退出循环体，不再循环了
#         pass
#     sum+=item
#     pass
# print('sum=%d'%sum)
#
# print('------continue关键字------')
# for item in range(1,51):
#     if item%2==0:                  #奇数不进入循环，偶数进入循环，但是不执行continue后的语句
#          print('%d是偶数'%item)
#          continue
#          print('在continue后')
#          pass
#     print(item)
#     pass
#
print('------加深理解------')
for item in 'i love you':
    if item=='e':
        break             #彻底中断循环
    print(item,end='')
    pass
print()
for item in 'i love you':
    if item=='o':          #只把o跳过循环，不执行
        continue
        print('这里不会执行')
    print(item,end='')
    pass

# while中也能用break 和 continue

# for if continue 跳出不符合if条件的本次循环 其他循环接着执行
# for if break  跳出整个循环