# a=2
# print(isinstance(a,int))
# print(isinstance(a,str))
# print(isinstance(a,(str,int,list))) #是元组中的一个返回True

# print(isinstance(False,bool))
# print(isinstance(False,int))
# print(isinstance(True,bool))
# print(isinstance(True,int))
#
# print(isinstance(a,int))
# print(isinstance(a,str))
# print(isinstance(a,(str,int,list))) #是元组中的一个返回True
# print(isinstance(False,bool))
# print(isinstance(False,int))print(callable(0))
# print(callable('runoob'))
#
# def add(a,b):
#     return a+b
# print(callable(add))


# class A:
#     def method(self):
#       return 0
# print(callable(A))
# a=A()
# print(callable(a))  #没有实现__call__,返回False
#
# class B:
#   def __call__(self):
#     return 0
# print(callable(B))
# b=B()
# print(callable(b))  #实现__call__,返回True

# print(help(sys))

# a='runoob'
# print(id(a))
# b=19
# print(id(b))
#
#
# class Runoob:
#   a=1
# print(vars(Runoob))
# runoob=Runoob()
# print(vars(runoob))

# a=4
# b=a
# c=4
# print(id(a),id(b),id(c))

# class Hero(object):
#     def __init__(self,name,skill,hp,atk,armor):
#         self.name=name
#         self.skill=skill
#         self.hp=hp
#         self.atk=atk
#         self.armor=armor
#     def __str__(self):
#         return "英雄<%s>数据:生命值%d,攻击力%d,护甲值%d"%(self.name,self.hp,self.atk,self.armor)
# taidamier=Hero('泰达米尔','旋风斩',2600,450,200)
# gailun=Hero('盖伦','大宝剑',4200,260,400)
# print(taidamier)
# print(gailun)
# class Hero(object):
#     def __init__(self,name):
#         print('__init__方法被调用')
#         self.name=name
#     def __del__(self):
#         print('%s被删除...'%self.name)
#
# taidamier=Hero('泰达米尔')
# print('%d被删除1次'%id(taidamier))
# del(taidamier)
# print('-'*20)
# gailun=Hero('盖伦')
# gailun1=gailun
# gailun2=gailun
# print('%d被删除1次'%id(gailun))
# del(gailun)
# print('%d被删除1次'%id(gailun1))
# del(gailun1)
# print('%d被删除1次'%id(gailun2))
# del(gailun2)


# class Home:
#     def __init__(self,area):
#         self.area=area
#         self.containsItem=[]
#     def __str__(self):
#         msg='当前房间可用面积为:'+str(self.area)
#         if len(self.containsItem)>0:
#             msg=msg+'容纳物品有:'
#             for temp in self.containsItem:
#                 msg=msg+temp.getName()+','
#             msg=msg.strip(',')
#         return msg
#     def accommodateItem(self,item):
#         needArea=item.getUsedArea()
#         if self.area>needArea:
#             self.containsItem.append(item)
#             self.area-=needArea
#             print('ok:已经存放到房间中')
#         else:
#             print('err:房间可用面积为:%d,但是但是当前要存放的物品需要的面积为:%d'%(self.area,needArea))
# class Bed:
#     def __init__(self,area,name='床'):
#         self.name=name
#         self.area=area
#     def __str__(self):
#         msg='床的面积为:'+str(self.area)
#         return msg
#     def getUsedArea(self):
#         return self.area
#     def getName(self):
#         return self.name
# newHome=Home(100)
# print(newHome)
# newBed=Bed(20)
# print(newBed)
# newHome.accommodateItem(newBed)
# print(newHome)
# newBed2=Bed(30,'席梦思')
# print(newBed2)
# newHome.accommodateItem(newBed2)
# print(newHome)

# class A(object):
#     def __init__(self):
#         self.num=10
#     def print_num(self):
#         print(self.num+10)
# class B(A):
#     pass
# b=B()
# print(b.num)
#
# class Master(object):
#     def __init__(self):
#         self.kongfu='古法煎饼果子配方'
#     def make_cake(self):
#         print('按照<%s>制作了一份煎饼果子...'%self.kongfu)
# class Prentice(Master):
#     pass
# daomao=Prentice()
# print(daomao.kongfu)
# daomao.make_cake()
#
#
# class Master(object):
#     def __init__(self):
#         self.kongfu='古法煎饼果子配方'
#     def make_cake(self):
#         print('[古法]按照<%s>制作了一份煎饼果子...'%self.kongfu)
#     def dayandai(self):
#         print('师傅的大烟袋...')
# class School(object):
#     def __init__(self):
#         self.kongfu='现代煎饼果子配方'
#     def make_cake(self):
#         print('[现代]按照<%s>制作了一份煎饼果子...'%self.kongfu)
#     def xiaoyandai(self):
#         print('学校的小烟袋...')
#
# class Prentice(School,Master):
#     pass
#
# damao=Prentice()
# print(damao.kongfu)
# damao.make_cake()
# damao.dayandai()
# damao.xiaoyandai()
