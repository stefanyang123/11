# while使用：适用于未知的循环次数
# for使用：适用于已知的循环（可迭代对象遍历）
print('------for嵌套显示乘法表自己想的------')
count=1
for a in range(1,10):
    for b in range(1,10):
        if a>=b:
            print('%d*%d=%d'%(a,b,a*b),end=' ')
            pass
        pass
    print()
    pass
print('运行完毕！')


print('------for嵌套显示乘法表答案------')
for a in range(1,10):
    for b in range(1,a+1):    #或者for b in range(1,11-a):
        print('%d*%d=%d' % (a, b, a * b), end=' ')
        pass
    print()
    pass


print('------for else------')
print('当for里面没有出现中断，的情况下，完整正确循环从头到尾遍历完了，我才会执行else')
# for----else
for item in range(1,11):
    print(item,end=' ')
    if item>=5:
        print('发现异常')
        break
    pass
else:
    print('在上面循环中，只要是出现了break，那么else的代码将不再执行')


# print('------for else用户登录小程序------')
# UN='ybw'
# PD='123'
# for i in range(3):        #依次取0，1，2
#     un = input("请输入用户名")
#     pd = input("请输入密码")
#     if un=='ybw' and pd=='123':
#         print('登录成功！')
#         break             #循环体中如果没有出现break，else就会执行
#         pass
#     pass
# else:
#     print('您的账号已被锁定')

print('------while else------')
i=1
while i<=10:
    print(i)
    if i==6:
        break
        pass
    i+=1
    pass
else:
    print('else执行了吗？')

