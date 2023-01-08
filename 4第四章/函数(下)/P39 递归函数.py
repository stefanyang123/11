# 递归函数 如果一个函数在其内部调用自身，这个函数就是递归函数
# 递归函数必须有一个结束条件，否则递归无法结束会一直递归下去，达到递归最大深度报错
# 优点：逻辑简单，定义简单
# 缺点：容易导致栈溢出，进入的层次太多，而资源又得不到释放，又没有返回，导致内存资源紧张


def jie(n):
    result=1
    for item in range(1,n+1):
        result*=item
        pass
    return result
print('5的阶乘',jie(5))
# 自己调自己，必须有一个明确的结束条件
# 用递归求阶乘
def digui(n):
    if n==1:          #如果n等于1，结果为1
        return 1
    else:             #如果n不等于1，结果为n*digui(n-1)
        return n*digui(n-1)
    pass
print('用递归实现5的阶乘{}'.format(digui(5)))

# 递归案例  模拟实现 树形结构的遍历


import os   #导入python自带的文件操作模块os模块
def findFile(file_Path):   #file_Path自己命名的一个存文件路径的参数
    listRs=os.listdir(file_Path)#得到该路径下所有的文件夹，赋值给listRs
    for fileItem in listRs:    #遍历得到的文件夹 得到文件或文件夹
        full_Path=os.path.join(file_Path,fileItem) #获取完整的文件路径
        if os.path.isdir(full_Path):     #判断是否是文件夹
            findFile(full_Path)  #如果是一个文件夹，再次去递归
            pass
        else:
            print(fileItem)      #如果是一个文件夹，再次去递归
            pass
        pass
    else:  #for循环执行完了，如果循环体没出现break else回去执行
        return      #如果什么也没找到，打开一堆文件夹后发现是空的就返回
    pass
#调用搜索文件路径
findFile('D:\\adobe')   #这里要用\转义   就可以将指定路径下的所有文件打印出来了






#如果得到的是文件，就直接输出，如果是文件夹就再次引用自己






















