def level_3():
    print ('���� level_3')
    a = [0]
    b = a[1]    #��ȷ����  b = a[0]
    print ('�뿪 level_3')

def level_2():
    print ('���� level_2')
    level_3()
    print ('�뿪 level_2')

def level_1():
    print ('���� level_1')
    level_2()
    print ('�뿪 level_1')


level_1()

print('���������˳�')

'''
����������±���


���� level_1
���� level_2
���� level_3
Traceback (most recent call last):
  File "D:\pythonProject7\��������ջ.py", line 18, in <module>
    level_1()
  File "D:\pythonProject7\��������ջ.py", line 14, in level_1
    level_2()
  File "D:\pythonProject7\��������ջ.py", line 9, in level_2
    level_3()
  File "D:\pythonProject7\��������ջ.py", line 4, in level_3
    b = a[1]
IndexError: list index out of range

�ȵ��� level_1 ִ��line 18  û������ִ��
�ٵ��� level_2 ִ��line 14  û������ִ��
�ٵ��� level_3 ִ��line 9   û�����½���ִ��
��ִ�� line 4  ִ�е�ʱ����� IndexError: list index out of range����

���������� level_3 �� ���� 
���level_3      û�в����쳣  ��������ִ��
�ͻ᷵��level_2   û�в����쳣  ��������ִ��
�ͻ᷵��level_1   û�в����쳣  ��������ִ��
�ͻ᷵��line18 ����  ��û�в����쳣 ��������ִ�� �ᱨ��

���ǿ��Գ����ٲ�ͬ�������ò� �����쳣
������㲶���쳣 ���ܽ����к����������������е�

'''