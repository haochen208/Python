# # class person(object):
# #     def __init__(self,age,weight):
# #         self.age=age
# #         self.weight=weight
# #     def eat(self):
# #         pass
#
# class Car:
#     def __init__(self, name, cartstore):
#         self.name = name
#         self.carstore = carstore
#     def move(self):
#         pass
# class CarStore:
#     def __init__(self,name):
#         self.name =name
#     def chucun(self):
#         pass
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def buy(self):
#         pass
#
# person = Person('Joker')
# carstore = CarStore('suvstore')
# car = Car('suv', carstore)


# class hero(object):
#     def move(self):
#         print("正在前往事发地点")
#     def attack(self):
#         print("发出了一招强力的普通攻击..")
#     def info(self):
#         print("英雄%s的生命值:%d "%(self.name,self.hp))
#         print("英雄%s的攻击力:%d"%(self.name,self.atk))
#         print("英雄%s的护甲值:%d"%(self.name,self.armor))
# taidamier=hero()
# taidamier.name="泰达米尔"
# taidamier.hp=2600
# taidamier.atk=450
# taidamier.armor=200
# taidamier.info()
# taidamier.move()

# class Student:
#     def __init__(self):
#         self.name="张三"
#         self.age=15
#         self.sex="男"
#         self.classnum="123456"
#         self.sno=18
#     def displayInfo(self):
#         print("姓名:%s,年龄%s,性别%s，班级号%s，座位号%s"%(self.name,self.age,self.sex,self.classnum,self.sno))
# self=Student()
# self.displayInfo()

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_course(self):
#         return max(self.grade)
# zhangsan = Student("张三", 20, [69,88,100])
# print(zhangsan.get_name())
# print(zhangsan.get_age())
# print(zhangsan.get_course())

# class peoeple(object):
#     address="山东" #类属性
#     def __init__(self):
#         self.name="xiaowang"#实例属性
#         self.age=20
# p=peoeple
# p.age=12
# print(p.address)
# print(p.name)
# print(p.age)
# print(peoeple.address)
# print(peoeple.name)
# print(peoeple.age)

# class people(object):
#     country="china"
# print(people.country)
# p=people()
# print(p.country)
# p.country="japan"
# print(p.country)
# print(people.country)
# del p.country
# print(p.country)

class mixdata:
    data="spam"
    def __init__(self,value):
        self.data=value
    def display(self):
        print(self.data,mixdata.data)
if __name__=="__main__"
    x=mixdata(1024)
    x.display()