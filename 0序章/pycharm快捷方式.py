# 单行注释ctrl + / 快速添加快捷键
# 例如这里是注释
# 多行注释使用'''注释'''或"""注释""" 都行
"""
例如
这里
是
注释
"""
# 注释的作用
# 1.提高代码可读性，提高开发效率，尤其对大型项目或者团队项目有重要意义
# 2.进行代码调试，将一部分代码注释掉，对问题进行排查，进行代码完善
# ctrl+shift+F10 快速执行
# Ctrl+s  快速保存
# ctrl+d  快速复制选中行代码
# tab 缩进  shift+tab 回缩
# shift+ F6  快速重命名
# ctrl+x  剪切
# ctrl+鼠标滚轮  对代码放缩
# 按着ctrl点击自定义的函数，会跳到定义的位置
# 按着ctrl点击python内置的函数，会跳到说明书
# 代码没有提示的解决方法 file-> power save mode 取消勾选 即可
# 'hello word'.pri + tab键   快速打出print('hello word')
# i.pri + tab键              快速打出print(i)
# alt+shift+ctrl+左键选中     快速编辑多行 内容相同的连续多行
# 右键变量名-> refactor        批量更改某一个变量名

#这个红点是断点，用来Debug的，程序运行到这会停下，显示参数状态，F8用来逐行运行
# 不点run 点Debug以启动
def digui(n):
    if n==1:
        return 1
    else:
        return n*digui(n-1)
    pass
print('用递归实现5的阶乘{}'.format(digui(5)))

# 双击加引号 要英文输入法
# File -> settings -> 搜索 Smark Keys -> 勾选surround selection on typing quote or brace

# 右键顶上的文件->split Vertically/split Horizontally 可以左右 上下分屏


