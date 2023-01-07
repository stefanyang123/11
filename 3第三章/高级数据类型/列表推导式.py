# 简单模式模式：只包含循环，不包含判断筛选

# 常规写法
list_1 = []
for x in range(1,10):
    list_1.append(x)
    pass
print(list_1)

# 列表推导式
# list_1里放x x哪里来的 从 for x in range(1,10) 这个for 循环里
list_1 = [x for x in range(1,10)]
print(list_1)


# 常规写法2
list_2 = []
for x in range(1,10):
    list_2.append(x*x)
    pass
print(list_2)
# 列表推导式
list_2 = [x*x for x in range(1,10)]
print(list_2)


# 一般模式：包含判断和筛选
# 一个等于号是赋值 把右边赋值给左边  两个等于号是 判断两边是否相等

# 常规写法
list_3 = []
for x in range(1,10):
    if x % 2 == 0:  #  取余  筛选出偶数
        list_3.append(x)
    pass
print(list_3)
# 列表推导式
# 从左到右一次递进 语句之间是嵌套关系 最左边在最外层
# 首先是循环 判断 符合条件的再放入到列表中
list_3 = [x for x in range(1,10) if x % 2 == 0]


# 变态模式：包含循环嵌套和判断筛选
# 常规写法5：
# 取列表5中每一个列表里的偶数 放到新的列表6中
list_5 = [[1,2,3],[4,5,6],[7,8,9]]
list_6 = []
for list in list_5:
    for x in list:
        if x % 2 ==0:
            list_6.append(x)
            pass
        pass
    pass
print(list_6)

# 列表推导式
list_6 = [x for list in list_5 for x in list if x % 2 ==0]
print(list_6)

lst=[[1]*3]*3 #[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(lst)




