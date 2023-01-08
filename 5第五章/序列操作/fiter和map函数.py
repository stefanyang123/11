print('-'*10,'fiter()函数','-'*10)
'''
fiter(function,iterable)
function:用来筛选的函数 在filter中会自动的把iterable中的元素
传递给function 然后根据function返回的True 或False 来判断是否保留此项数据
iterable:可迭代对象
'''
lst=[x for x in range(10)]  #列表推导式 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def func(i):   #判断奇数
    return i % 2 == 1
    pass
l1=filter(func,lst)   #l1是迭代器
print(l1)  #<filter object at 0x00000220CF5DBFA0>
print(list(l1))

print('-'*10,'map()函数','-'*10)
'''
map(function,iterable)
会根据提供的函数对制定序列列做映射
把可迭代对象iterable中的每一个元素传递给前面的函数function进行处理
处理的结果会返回成迭代器
'''
def func1(i):
    i*=2
    return i
    pass
it=map(func1,lst)  #<map object at 0x00000220CF5DBEB0>
print(it)
print(list(it))