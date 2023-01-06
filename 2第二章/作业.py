#猜年龄
"""
1.允许用户最多尝试三次
2.三次用完没猜对，问是否想继续玩？
如果回答Y或y,就继续让其猜三次，以此往复
如果回答N或n,就退出程序
如果回答除了Y或y，N或n，以外的，让其规范书写，并能按照操作者的意愿继续运行或者关闭程序
3.猜对了就退出
"""




# 第一次实现功能
age=3
chance=1
for a in range(3):
    ipage=int(input("请输入数字"))
    if ipage==age:
        print('猜对了！')
        break
        pass
    print('猜错了哦只有三次机会')
    pass
else:
    me=input("是否要继续？[Y/y是，N/n不]")
    while me=='y'or'Y':
        for a in range(3):
            ipage = int(input("请输入数字"))
            if ipage == age:
                print('猜对了！')
                break
                pass
            print('猜错了哦只有三次机会')
            pass
        else:
            me = input("是否要继续？[Y/y是，N/n不]")
            if me == 'n'or'N':
                print('游戏结束！')
                break
                pass
            pass
        pass





#答案
times=0
count=3
while times<=3:
    age=int(input('请输入您要的年龄...'))
    if age==25:
        print('恭喜您猜对啦')
        break
        pass
    elif age>25:
        print('大了')
        pass
    else:
        print('小了')
        pass
    times+=1
    if times==3:
        choose=input('想不想继续猜？Y/N?')
        if choose=='Y' or choose=='y':
           times==0
           pass
        elif choose=='N' or choose=='n':
           times==4
           pass
        else:
            print('请输入正确的标记')
            pass

    pass




# 想通后的解答
i=1
while i<=3:
    ipt=int(input('请输入一个数'))
    if ipt>=10:
        print('够了！')
        break
        pass
    else:
        print('还不够！')
        pass
    i+=1
    #对i是否大于三判断一下，大于则进如语句块，否则接着循环
    if i>3:
        want=input('是否继续？Y/N')
        #对用户的输入进行判断Y
        if want=='Y':
            print('请继续！')
            i=1
            pass
        elif want=='N':
            i=4
print('结束！')




# 代码量少了，但是不是无线次数的需要调节参数
for i in range(100):                #i=0,1,2....99   i=0运行一遍，i=1运行一遍..... 这个100控制最终次数
    ipt = int(input('请输入一个数'))
    if ipt>=10:
        print('够了！')
        break
        pass
    else:
        print('还不够！')
        pass
    if (i+1)%3==0:                   #当i=2,5,8....执行if下面的操作
        want = input('是否继续？Y/N')
        if want == 'Y':
            print('请继续！')
            pass
        elif want == 'N':
            break                    #只要在循环体内有break 就会退出所在循环体的循环
            pass
        pass
    elif i+1 ==100:                    #如果i达到了99,会提示
        want = input('休息休息再继续吧，是否继续？Y/N')
        if want == 'Y':
            print('请继续！')
            pass
        elif want == 'N':
            break  # 只要在循环体内有break 就会退出所在循环体的循环
            pass
        pass



# 改进想通后的解答
i=1
while i%4!=0:
    ipt=int(input('请输入一个数'))
    if ipt>=10:
        print('够了！')
        break
        pass
    else:
        print('还不够！')
        pass
    i+=1
    if i%4==0:          #对i是否大于三判断一下，大于则进如语句块，否则接着循环
        want=input('是否继续？Y/N')
        if want=='Y' or want=='y':   #对用户的输入进行判断Y
            print('请继续！')
            i+=1
            pass
        elif want=='N'or want == 'n':
            i=0
            pass
        else:
            while want != 'Y' or want != 'N' or want != 'n'or want != 'y':
                want = input('只能输入 [Y/N,y/n]')
                if want=='Y' or want=='y':
                    i=1
                    break
                    pass
                elif want=='N'or want == 'n':
                    i=0
                    break
                    pass
print('结束！')





























#