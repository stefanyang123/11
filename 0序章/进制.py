# 0xf2 表示十六进制数f2  对于十进制242
# 0 1 2 3 4 5 6 7 8 9 A B C D E F
# 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F


# def oxx(n):
#     """
#     十进制转换十六进制Demo限制65535以内
#     :param n:
#     :return:
#     """
#     x = '0123456789ABCDEF'
#     listNew=[]
#     for i in x:
#         for j in x:
#             ox = i + j
#             listNew.append(ox)
#             pass
#         pass
#     return listNew[n]
# print(oxx(242))



# 进制十进制与十六进制转换
def oxx(n):
    """
    十进制转换十六进制Demo限制
    :param n:
    :return:以字符串形式返回十六进制数
    """
    x = '0123456789ABCDEF'
    listNew=[]
    for a in x:
        for b in x:
            for c in x:
                for d in x:
                    ox =a+b+c+d
                    listNew.append(ox)
                pass
            pass
        pass
    pass
    return listNew[n]
def xxo(n):
    """
    十六进制转十进制限制FFFF以内
    :param n:
    :return:以数字形式返回十进制数
    """
    x = '0123456789ABCDEF'
    i=4-len(n)
    user=('0'*i)+n
    # 生成一个16进制表
    listNew = []
    for a in x:
        for b in x:
            for c in x:
                for d in x:
                    ox = a + b + c + d
                    listNew.append(ox)
                pass
            pass
        pass
    pass
    return listNew.index(user)
def will():
    """
    运作逻辑
    :return: none
    """
    want=input('是要10转16进制[y]还是16转10进制数[任意键]...')
    print('---------好的---------')
    if want=='y':
        num = input('请输入你要转换的十进制数...')
        finNum=int(num)
        print('{}转换为十六进制为{}'.format(num,oxx(finNum)))
        pass
    else:
        num = input('请输入你要转换的十六进制数...')
        print('{}转换为十进制为{}'.format(num, xxo(num)))
        pass
will()
want1='g'   #初始化以进入循环体
while want1=='g':
    want1 = input('是否继续[g]或按任意键退出...')
    if want1 != 'g':
        want2= input('确认退出？[按f取消，按任意键退出]...')
        if want2=='f':
            want1='g'
        else:
            break
        pass
    will()
print('------------已退出---------------')
