from time import sleep
'''
# 在使用print打印字符串的时候会自动换行
# 这是因为 print函数中有一个参数 end 默认它就是一个换行字符
print('hello');print('world')
# hello
# world

print('hello',end='\n');print('world')
print('hello',end='-------');print('world')   #hello-------world

# 当使用 ,  进行多个字符串连接打印时 会以空格连接
# 因为 print中有一个默认参数sep 默认就是空格
print('hello','world')
print('hello','world',sep='____')   #hello____world
'''
# 简易版进度条
for i in range(20):
    print('#',end='')
    sleep(0.5)


