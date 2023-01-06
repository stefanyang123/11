print('------使用while嵌套循环，打印乘法表1------')
#打印九九乘法表 row行 col列
row=1
while row<=9:
    col=1   #现有行，才有列
    while col<=row:   #每当列小于等于行时，会执行循环内的语句
        print('%d*%d=%d'%(row,col,row*col),end=" ")
        # print()每执行一次就会换行后面加上,end=" "就会不让它换行
        col+=1
        pass
    print()            #每当列大于行时，会跳出循环执行print()，应该在这里换行
    row+=1
    pass

print('------使用while嵌套循环，打印乘法表2------')

row=9
while row>=1:
    col=1   #现有行，才有列
    while col<=row:   #每当列小于等于行时，会执行循环内的语句
        print('%d*%d=%d'%(row,col,row*col),end=" ")
        col+=1
        pass
    print()            #执行print()，在这里换行
    row-=1             #每当列大于行时，会跳出循环,并让行数减一
    pass

print('------打印直角三角形------')
row=7           #设定一个初始的行数，默认值为1
while row>=1:   #要打印7行，因为一旦超过七就终止循环了
    j=1         #控制在每一行上面打印字符的数量
    while j<=row:
        print('*',end=' ')    #每次打印完*，用空格隔开，并阻止换行
        j+=1                  #每次打印完内层的j发生变化
        pass                  #把内层循环给退出来
    print()                   #每打完一行，接着第二行时我们需要换行
    row-=1                    #行的变量也要发生变化
    pass

print('------打印等腰三角形------')
row=1
while row<=10:
    j=1                       #在每一行要控制空格的输出和*的输出
    while j<=10-row:           #控制打印空格的数量
        print('.',end='')      #把.改成空格即可，这里为了方便理解
        j+=1
        pass           #先打印完.再打印*
    k=1
    while k<=2*row-1:         #控制打印*号
        print('*', end='')
        k+=1
        pass
    print()
    row+=1
    pass


"""
print('*',end='')       
能打印一个* 并且不换行
                    
while j<=10-row:          
    print('*',end='')      
    j+=1
    pass  
给它外面加上一个循环语句就能让它一直打印*
加上条件语句以及变量，来控制限制它循环的次数

打印是从左到右打印，对应代码是从上往下运行
因此位于同一缩进的 上面的循环体先被打印，而下面的循环体后被打印
同样位于同一缩进的 上面的语法先被执行，下面的后被执行
"""

print('------打印等腰三角形升级版------')
row=1
while row<=10:

    j=1                   #打印.
    while j<=10-row:
        print('.',end='')
        j+=1
        pass

    print('  ', end='')    #打印空格

    k=1                    #打印*
    while k<=2*row-1:
        print('*', end='')
        k+=1
        pass

    print('  ', end='')    #打印空格

    i= 1                   #打印.
    while i<= 10 - row:
        print('.', end='')
        i += 1
        pass

    print() #到这里每一行该做什么的逻辑已经结束，用它换行接着打印下一行
    row+=1
    pass


