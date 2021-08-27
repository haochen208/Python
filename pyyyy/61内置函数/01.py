# # # s='this if is you not are a reading very this good then way'
# # # print(dir(s))
# # # help(s.split)
# # # words=s.split()
# # # print(words)
# # # for i in range(0,len(words)):
# # #     print(words[i])
# # #
# # #
# # # class A:
# # #     def add(self,x):
# # #         y=x+1
# # #         print(y)
# # #
# # # class B(A):
# # #     def add(self,x):
# # #         super().add(x)
# # # b=B()
# # # b.add(2)
# # #
# #
# # # class Father(object):
# # #     def act(self):
# # #         print('Father Height passed on to son...')
# # #
# # # class Mother(object):
# # #     def act(self):
# # #         print('Mother Height passed on to son...')
# # #
# # # class Son(Father,Mother):
# # #     def act(self):
# # #         super().act()
# # # s=Son()
# # # s.act()
# # #
# # # class C(object):
# # #     def __init__(self):
# # #         self._x=None
# # #     def getx(self):
# # #         return self._x
# # #     def setx(self,value):
# # #         self._x=value
# # #     def delx(self):
# # #         del self._x
# # #     x=property(getx,setx,delx,"I am the 'x' property.")
# # # c=C()
# # # print(c.x)
# # #
# # # c.x=100
# # # print(c.x)
# #
# #
# # class Parrot(object):
# #     def __init__(self):
# #         self._voltage=10000
# #     @property
# #     def voltage(self):
# #         return self._voltage
# # p=Parrot()
# # print(p.voltage)
# #
# # class Parrot(object):
# #     def __init__(self):
# #         self._voltage=10000
# #     @property
# #     def voltage(self):
# #         return self._voltage
# #     @voltage.setter
# #     def voltage(self,value):
# #         self._voltage=value
# #     @voltage.deleter
# #     def voltage(self,value):
# #         del self._voltage
# # p=Parrot()
# # print(p.voltage)
# # p.voltage=999
# # print(p.voltage)
# #
# # def foo(arg,a):
# #     x=100
# #     y='hello python!'
# #     for i in range(10):
# #         j=1
# #         k=i
# #     print(locals())
# # foo(1,2)
# #
# # def foo(arg,a):
# #     x=100
# #     y='hello python!'
# #     for i in range(10):
# #         j=1
# #         k=i
# #     print(locals())
# # foo(1,2)
# # def runoob(arg):
# #     z=1
# #     print(locals())
# # runoob(4)
#
# # class A(object):
# #     def __init__(self):
# #         print('这是init方法')
# #     def __new__(cls):
# #         print('这是new方法')
# #         return object.__new__(cls)
# # A()
# #
# class MagicDemo(object):
#     def __init__(self):
#         print('call me second')
#         self.value=[1,2,3]
#     def __new__(cls,*args,**kwargs):
#         print('call me first')
#         return super(MagicDemo,cls).__new__(cls,*args,**kwargs)
#     def __del__(self):
#         print('call__del__')
#         del self
#     def __str__(self):
#         return "call __str__"
# mag=MagicDemo()
# #print(mag.value)
# #print(str(mag))
#
#
# class singleton(object):
#     __instance=None
#     def __new__(cls,age,name):
#         if not cls.__instance:
#             cls.__instance=object.__new__(cls)
#         return cls.__instance
# a=singleton(18,'dongGe')
# b=singleton(8,'dongGe')
# print(id(a))
# print(id(b))
# a.age=19
# print(b.age)
#
# class singleton(object):
#     __instance=None
#     __is_first=True
#     def __new__(cls,age,name):
#         if not cls.__instance:
#             cls.__instance=object.__new__(cls)
#         return cls.__instance
#     def __init__(self,age,name):
#         if singleton.__is_first:
#             self.age=age
#             self.name=name
#             singleton.__is_first=False
# a=singleton(68,'习大大')
# b=singleton(28,'习大大')
# print(id(a))
# print(id(b))
#
# print(a.age)
# print(b.age)
# a.age=19
# print(b.age)

# class Animal(object):
#     def __init__(self,name,life_value,aggressivity):
#         self.name=name
#         self.life_value=life_value
#         self.aggressivity=aggressivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggressivity
# class People(Animal):
#     camp='home'
#     def attack(self,enemy):
#         super().attack(enemy)
#         print('from people')
# class Dog(Animal):
#     camp='wo'
#     def attack(self,enemy):
#         super().attack(enemy)
#         print('from dog')
# p1=People('alice',80,30)
# p2=People('alex',80,30)
# d1=Dog('w1',100,50)
# d2=Dog('w2',90,50)
# d3=Dog('w3',90,50)
# print(p1.life_value)
# d1.attack(p1)
# print(p1.life_value)
#
# print(d1.life_value)
# p1.attack(d1)
# print(d1.life_value)

# def passwdLen(passwd):
#     if len(passwd)>8:
#         return True
#     else:
#         return False
# def passwdType(passwd):
#     passwd_upper,passwd_lower,passwd_digit,passwd_char=0,0,0,0
#     for i in passwd:
#         if i.isupper():
#             passwd_upper=1
#         elif i.islower():
#             passwd_lower=1
#         elif i.isdigit():
#             passwd_digit=1
#         else:
#             passwd_char=1
#     if (passwd_upper+passwd_lower+passwd_digit)>=3:
#         return True
#     else:
#         return False
#
# def passwdRepetition(passwd):
#     for i in range(len(passwd)-3):
#         if passwd.count(passwd[i:i+3])>1:
#             return False
#     return True
#
# while True:
#     passwd=input('请输入密码:\n')
#     if passwdLen(passwd) and passwdRepetition(passwd) and passwdType(passwd):
#         print('ok')
#     elif passwd=='quit':
#         break
#     else:
#         print('NG')


# import random
# rewardDict={'一等奖':(0,0.08),'二等奖':(0.08,0.3),'三等奖':(0.3,1)}
# def rewardFun():
#     number=random.random()
#     for k,v in rewardDict.items():
#         if v[0]<=number<=v[1]:
#             return k
# resultDict={}
# for i in range(10000):
#     res=rewardFun()
#     resultDict[res]=resultDict.get(res,0)+1
# for k,v in resultDict.items():
#     print('%s需要准备的奖品数量为:%d'%(k,v))
class A(object):
    def __init__(self):
        print('A')
        super(A, self).__init__()

class B(object):
    def __init__(self):
        print('B')
        super(B, self).__init__()

class C(A):
    def __init__(self):
        print('C')
        super(C, self).__init__()

class D(A):
    def __init__(self):
        print('D')
        super(D, self).__init__()

class E(B, C):
    def __init__(self):
        print('E')
        super(E, self).__init__()

class F(C, B, D):
    def __init__(self):
        print('F')
        super(F, self).__init__()

class G(D, B):
    def __init__(self):
        print('G')
        super(G, self).__init__()
if __name__ == '__main__':
    g = G()
    f = F()

