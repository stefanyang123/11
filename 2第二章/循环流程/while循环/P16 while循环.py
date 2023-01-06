#循环的分类
# while 语法结构
#    while 条件表达式:
#        代码指令
# 语法特点
# 循环必须有一个初始值
# 条件表达式
# 变量（循环体内计数变量）的自增或自减，没有它会造成死循环
# 使用条件：循环的次数不确定，是依靠循环条件来结束
# 目的：为了将相似或相同的代码操作变得更加简洁，使代码可以重复利用

print('------while的使用 输出 1-100之间的数据------')
#while的使用 输出 1-100之间的数据
# i=1 #定义个变量
# while i<=100:
#     print(i)
#     i += 1
#     pass

# a=1 #定义个变量
# while a<=100:  #代码如果这样写会出现 2-101
#     a += 1
#     print(a)
#     pass

print('------使用while循环，对猜拳游戏的改进------')
wantCount=int(input("你想玩几局？"))
count=1
print('那咱们就玩{}局吧！'.format(wantCount))
while count<=wantCount:
    import random                  #游戏核心逻辑不变，在外层加一个循环
    per = int(input('请出拳[0:石头 1:剪刀 2:布]'))
    com = random.randint(0, 2)
    if per == 0 and com == 1:
        print('你赢了，电脑出的是{}'.format(com))
        pass
    elif per == 1 and com == 2:
        print('你赢了，电脑出的是{}'.format(com))
        pass
    elif per == 2 and com == 0:
        print('你赢了，电脑出的是{}'.format(com))
        pass
    elif per == com:
        print('打平了，电脑出的也是{}'.format(com))
        pass
    else:
        print('你输了，电脑出的是{}'.format(com))
        pass
    count += 1
    pass
print('游戏结束了！')




# for