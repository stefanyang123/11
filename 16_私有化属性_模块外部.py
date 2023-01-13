# 以这种形式导入 三种属性都能访问到不会报错 顶多会有警告
# import 私有化属性
# print(私有化属性.num)
# print(私有化属性._num)  Access to a protected member _shou of a class
# print(私有化属性.__num)

# 以这种形式导入 就只能访问公有变量 但能导入被__all__指明的属性 无论公私
from 私有化属性 import *
print(num)

# 凡是通过这种方式导入的 带一个_的变量 不能在当前模块被访问
try:
    print(_num)
except Exception as e:
    print(e)

# 访问私有属性一样不可以
try:
    print(__num)
except Exception as e:
    print(e)
