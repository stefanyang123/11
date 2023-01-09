"""
英雄   西门吹雪  叶孤城
属性：
name 玩家的名字
blood  玩家的血量

方法：
tong() 捅对方一刀，对方掉血10
kanren() 砍对方一刀 对方掉血15
chiyao() 吃一颗药丸，补10血
__str__ 打印玩家状态
"""

import time #导入第三方时间的包(库)

# 第一步 需要先去定义一个类[角色]
class Role:
    def __init__(self,name,boold):
        """
        初始化函数
        :param name:角色名字
        :param boold:角色血量
        """
        self.name=name
        self.boold=boold
        pass
    def tong(self,enemy):   #捅谁  谁.boold就减少10
        """
        捅人-10
        :param enemy:敌人
        :return:
        """
        enemy.boold-=10
        info ='%s捅了%s一刀'%(self.name,enemy.name)
        print(info)
        pass
    def kanren(self,enemy):  #砍谁  谁.boold就减少15
        """
        砍人-15
        :param enemy: 敌人
        :return:
        """
        enemy.boold -= 15
        info = '%s砍了%s一刀'%(self.name, enemy.name)
        print(info)
        pass
    def chiyao(self):
        """
        吃药补血+10
        :return: 敌人
        """
        self.boold -= 10
        info = '%s吃了补血药增加了10血' % (self.name)
        print(info)
        pass
    def __str__(self):
        """

        :return:
        """
        return '%s还有%d血'%(self.name,self.boold)
        pass

# 第二部 创建游戏角色
xmcx=Role('西门吹雪',100)
ygc=Role('叶孤城',100)

while True:    #默认循环  条件一直True 里面没有条件判断，会变成死循环，用break
      if xmcx.boold<=0 or ygc.boold<=0:
        break
      else:
        # xmcx捅ygc 一刀
        xmcx.tong(ygc)
        print(xmcx)
        print(ygc)
        print('--------------')

        # ygc砍xmcx 一刀
        ygc.kanren(xmcx)
        print(xmcx)
        print(ygc)
        print('--------------')


        # xmcx吃药
        xmcx.chiyao()
        print(xmcx)
        print(ygc)
        print('--------------')

        time.sleep(1)    #休眠暂停一秒钟
        pass
print('对战结束')


















