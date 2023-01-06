print('------单分支------') #

#单分支
# if 条件表达式: 可以是比较/逻辑/复合表达式
#     代码指令
score=60
if score<=60:
    print('成绩不是太理想')  #满足条件就会执行语句块的内容
    pass #pass空语句 表示结束跳过这个代码块，填补这个结构，我想就执行print('成绩不是太理想')后，就结束单分支。不用也行，按完回车手动点回顶格缩进

print('语句运行结束')

print('------双分支------') #
# 双分支
# if 条件表达式: 可以是比较/逻辑/复合表达式
#     代码指令
# else:
#     代码指令
# 必定会执行其中一个分支

if score>=60:
    print ('你的成绩合格')   #score>=60结果为True执行
    pass
else:
    print('你的成绩不合格')   #score>=60结果为False执行
    pass

print('------多分支------')
# 多分支
# if 条件表达式: 可以是比较/逻辑/复合表达式
#     代码指令
# elif 条件表达式:
#     代码指令
# ....
# else 条件表达式:
# 1.只要满足其中一个分支，就会退出本层if语句结构(必定会执行其中一个分支)
# 2.至少有两种情况可以选择
# 3.elif 后面必须写上条件和语句（凡是看到if，elif后面肯定跟条件）
# 4.else是选配，根据实际情况来选择

# score=int(input("请输入你的分数"))
# print(type(score))
# if score>=90:
#     print('您的成绩是A')
#     pass
# elif score>=80:
#     print('您的成绩是B')
#     pass
# elif score >= 70:
#     print('您的成绩是C')
#     pass
# elif score>=60:
#     print('您的成绩是D')
#     pass
# else: #选配
#     print('您的成绩是不合格')
#     pass


print('------跟电脑猜拳吧------')
# 多条件（猜拳）
# 0:石头 1:剪刀 2:布

# import random #导入产生随机数的模块
# # 计算机  人
# per=int(input('请出拳[0:石头 1:剪刀 2:布]'))
# com=random.randint(0,2)  #产生0到2的随机数
# # 先写打赢的情况 三种
# if per==0 and com==1:
#     print('你赢了，电脑出的是{}'.format(com))
#     pass
# elif per==1 and com==2:
#     print('你赢了，电脑出的是{}'.format(com))
#     pass
# elif per==2 and com==0:
#     print('你赢了，电脑出的是{}'.format(com))
#     pass
# # 再写打平的情况
# elif per==com:
#     print('打平了，电脑出的也是{}'.format(com))
#     pass
# # 没有赢，也没有打平，剩下的情况就是输了
# else:
#     print('你输了，电脑出的是{}'.format(com))
#     pass

print('------if-else嵌套------')
# if-else嵌套
# 一个场景需要分阶段或者层次，做出不同的处理
# 要执行内部if的语句，一定要外部的if语句满足条件才可以


# xuefen=int(input("请输入你的学分："))
# if xuefen>10:            #程序中要想升学 学分必须大于10，成绩大于八十
#     grade = int(input("请输入你的成绩："))     #只有满足学分了，才有输入成绩的必要
#     if grade>=80:
#         print('可以升班了')
#         pass
#     else:
#         print('很遗憾虽然学分够了，成绩还没达到')
#         pass
#     pass
# else:
#     print('您的表现也太不好了')


