print('算数运算符，结果是数值类型的数据')  #运行结果分行，方便复习看
# 算术运算符
a,b,c,d=-2,3,5,8  #定义多个变量
#    **求指数
print(a**b)
#    %取余 a除以b的余数
print(a%b)
#    //地板除  忽略小数位，保留整数位
print(d//c)
#    /除法     结果包含小数点后的数
print(a/b)

print('比较运算符,结果是bool类型的数据')  #运行结果分行，方便复习看

# 比较运算符
#     ==等于     x==y       如果x恰好等于y，则为真
#     !=不等于   x!=y        以此类推
#     >大于      x>y
#     <小于      x<y
#     >=大于或等于      x>=y
#     <=小于或等于      x<=y
a,b=5,6  #尽管上面a,b=-2,3，这里从新给5,6贴上了变量a,b的标签，不影响上面，也不影响这里使用
print(a==b)
print(a>b)
print(a<b)

print('逻辑运算符,参与运算的是bool类型，结果也是bool类型的数据')  #运行结果分行，方便复习看
c,d=True,False#注意是首字母大写的True 和  False,小写会报错
#    and      c and d    c,d同为真 结果为真，其中一个为假，结果为假(一假便假)
#    or       c or  d    c,d有一个为真，结果为真，全部为假，结果为假(一真便真)
#    not      not c      取反，如果c为真，结果为假  如果c为假，结果为真(真假相反)
print(c and d)
print(c or d)
print(not c)
print(c and not c)
print(c and not c or c)  #True and True or True
print(a+b>b and a>b)   #True and False
# 优先级 相同从左往右
# () -> not -> and -> or

print('赋值运算符')  #运行结果分行，方便复习看
#  = 赋值运算符       c+=a等效于 c=c+a 先把c+a算完再赋值给c,这是两步运算
#  +=加法赋值运算符    以此类推
#  -=减法赋值运算符
#  *=乘法赋值运算符
#  /=除法赋值运算符
#  %=取模赋值运算符
#  **=幂赋值运算符
#  //=取整赋值运算符
a,b,c,d=-2,3,5,8
print(a,'用a+=1前，a的值')
a+=1  #a+=1是一个复合表达式，即将a+1算完再赋值给a,不能用于直接输出，故不能直接print(a+=c)
print(a,'用a+=1后，a的值')
a+=c
print(a,'用a+=c后，a的值')

# x=3,y=4   会报错
# 要么写成 x,y=3,4 要么写成 x=y=4


