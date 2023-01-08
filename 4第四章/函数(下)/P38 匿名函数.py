# 用lambda关键字创建匿名函数
# 所谓匿名函数即这个函数没有名字不用def关键字创建标准的函数
# 语法:lambda 参数1,参数2,参数3..参数n:执行代码表达式
# 特点：用lambda关键字取创造函数
# 没有名字的函数
# 匿名函数冒号后面的表达式有且只有一个,注意:是表达式，而不是执行语句
# 匿名函数自带return，而return的结果就是表达式计算后d果
# 缺点：
# lambda 只能是单个表达式，不是一个代码块，lambda的设计就是为了满足简单函数的场景
# 仅仅能封装有限的逻辑，复杂逻辑实现不了，必须用def来处理
# 一般适合只需要执行完就不用了的函数

# 普通函数
def test(x,y):
    return x+y
# 匿名函数
text=lambda x,y:x+y
text(1,3)

# lambda x,y:x+y
# 创建一个匿名函数，一般用一个变量来接收，通过变量取调用匿名函数
M=lambda x,y:x+y
# 调用
print(M(10,24))

resule=lambda a,b,c:a*b*c
print(resule(12,13,10))

# 或者不用变量直接接收参数
(lambda a,b:a+b)(3,2)
print((lambda a,b:a+b)(3,2))


# 三元运算
# result=值1 if条件 else 值2  双分支的简写
age=25
# 可以把传统的双分支用一行表达式替代
print('可以参军'if age>18 else '继续' )
# 如果符合条件，输出前面的，不符合输出后面的
# lambda x,y:x if x>y else y  跟上一个一样，如果x>y输出x，否则输出y
funcText=lambda x,y:x if x>y else y
print(funcText(12,2))


#直接的调用
rs=(lambda x,y:x if x>y else y)(16,12)
#前面一个（）相当于对函数对象的调用了，相当于上面的funcText对函数的调用
# 后面直接给他传参就行了
print(rs)

varRs=lambda x:(x**2)+890
print(varRs(10))

# 使用匿名函数 对列表里的每一个值进行*2操作
lst=[2,4,6,8,10]
new_lst=list(map(lambda x:x*2,lst))
print(new_lst)
