class Person:
    def __run(self):
        print('run')
        pass

    def _Person__run(self):
        """
        会覆盖上边的 私有方法,不能这样命名
        :return:
        """
        print('xxx')

    pass

p=Person()
# p.__run() #AttributeError: 'Person' object has no attribute '__run'

# 类的外部之所以访问不了，是因为 方法的名字 被重整为 _Person__run










