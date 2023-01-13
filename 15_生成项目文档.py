'''
生成项目文档

方式一： 使用内置模块 pydoc

步骤
1.打开cmd
2.在pycharm 找到要提取文档的文件所在的文件夹  右键->copy->copy path
3.默认路径是C盘，不在C盘要切换盘,
    键入 D: 切换到D盘   键入cls  清屏   按一次上键（可以按多次） 回到上一次输入的名令
4.键入 cd 路径   右键->粘贴  因为没有ctrl+v
    键入python3 --help                  查看python3里的帮助文档
    键入python3 -m pydoc -h             查看如何使用
    键入python3 -m pydoc 模块的名称       生成模块中类的描述
    键入python3 -m pydoc -k 关键字       按关键字找到含有关键字的目录

5.键入python3 -m pydoc -p 端口号（随意输入数字）
    (推荐)键入python3 -m pydoc -b  端口号不需要去写，自动给你用没用过的

6.键入b  会打开一个网页，会看到所有相关模块的注释文档
    Built in Modules 系统内置模块
    ValueError:could not find object 模块名改成英文即可正常显示
7.键入q  关闭服务

8.键入python3 -m pydoc -w (模块名称或目录）
    把文档内容写入html文件里，如果给定的名字是目录的话，这个文档会包含目录里所有的内容

----------------------------------------------------------------------------------

方式二：
其他第三方模块 sphinx epydoc doxygen












'''