# 函数返回值
# 函数执行完以后会返回一个对象，如果在函数的内部有return就可以返回实际的值，如果没有返回空None
# 类型：可以返回任意类型，返回值类型应该取决与return后面的类型
# 用途：给调用方返回数据
# 在一个函数体内可以出现多个return值，不一定都执行，但肯定只能返回一个return值
# 如果在一个函数体内 执行了return，意味着函数就执行完成退出了，return后面的代码语句将不会执行

print('-------没有return的函数------')
def Sum(a,b):
    sum=a+b
    pass
Sum(10,20)
print(Sum(10,20))


print('------有return的函数，返回一个数据------')
def Sum(a,b):
    sum=a+b
    return sum   #将计算的结果返回,在哪里调用就返回到哪里
    pass

print(Sum(10,20))   #函数的返回值返回到调用的地方
rs=Sum(10,20)       #还可以将返回值赋值给变量


print('------有return的函数，返回一个列表类型的数据------')
# 定义函数
def cal(num):
    li=[]            #创建一个空列表
    result=0         #定义一个整形变量resul 和i
    i=1

    while i<=num:     #循环体
        result+=i     #i是控制循环的，当大于num时会退出循环
        i+=1          #resul是计算结果
        pass          #循环体  退出循环时i大于num，且resul=0+...+num

    li.append(result)   #将计算的结果追加到列表里
    return li
# 调用函数
cal(50)
print(cal(50))
print(type(cal(50)))

print('------有return的函数，返回一个元组类型的数据------')
def returnTuple():
    '''
    返回元组类型的数据
    :return:
    '''
    # return 1,2,3            返回元组类型数据
    # return {'name':'测试'}   返回字典类型数据
    # 你要返回什么数据，根据你的需要在return后写就行了
    pass

A=returnTuple()
print(type(A))



























