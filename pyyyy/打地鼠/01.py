# #定义函数，用于判断是否打地鼠成功
# import random
# def forereach():   #胜过,追到
#     mouse=random.randint(1,5)
#     human=int(input('Please guess which one:'))
#     return mouse==human
# print('Pocket Mole Start!')
# # for...each 如果for循环不是通过break退出，就会执行else语句
# for i in range(5):
#     catch=forereach()
#     if catch==True:
#         print('You Win')
#         break
#     else:
#         print('fail,please continue')
# else:
#     print('game over!')

# def hello():
#     print('hello')
# from tkinter import*
# tk=Tk()
# btn=Button(tk,text='click me',command=hello)
# btn.pack()

from tkinter import *
def GetInputValue(ShowNumEntry, Value):  # 用来显示值
    ShowNumEntry.insert(END, Value)

def GetNumOne():  # 按钮1并显示
    GetInputValue(ShowNumEntry, "1")


def GetNumTwo():  # 按钮2并显示
    GetInputValue(ShowNumEntry, "2")


def GetNumThree():  # 按钮3并显示
    GetInputValue(ShowNumEntry, "3")

def GetNumFour():#按钮4并显示
    GetInputValue(ShowNumEntry,"4")
def GetNumFive():#按钮5并显示
    GetInputValue(ShowNumEntry,"5")
def GetNumSix():#按钮6并显示
    GetInputValue(ShowNumEntry,"6")
def GetNumSeven():#按钮7并显示
    GetInputValue(ShowNumEntry,"7")
def GetNumEight():#按钮8并显示
    GetInputValue(ShowNumEntry,"8")
def GetNumNine():#按钮9并显示
    GetInputValue(ShowNumEntry,"9")
def GetNumZero():#按钮0并显示
    GetInputValue(ShowNumEntry,"0")
def GetDot():#按钮.并显示
    GetInputValue(ShowNumEntry,".")
def GetPlus():#按钮+并显示
    GetInputValue(ShowNumEntry,"+")
def GetMinus():#按钮-并显示
    GetInputValue(ShowNumEntry,"-")
def GetClean():#清除
    ShowNumEntry.delete(0,END)
def GetMultiply():#按钮*并显示
    GetInputValue(ShowNumEntry,"*")
def GetDivision():#按钮/并显示
    GetInputValue(ShowNumEntry,"/")
def GetResult():#计算结果并显示
    result = eval(ShowNumEntry.get())
    GetClean()
    ShowNumEntry.insert(0,str(result))
root = Tk()
root.wm_minsize(400,160)#设置窗口大小
ShowNumEntry = Entry(root, width=8, justify="right", font=12 )
ShowNumEntry.grid(row=0, column=5)
NumOneBtn = Button(root,text = "1", width = 8,height = 2,command = GetNumOne)
NumOneBtn.grid(row=1, column=0)
NumTwoBtn = Button(root,text = "2", width = 8,height = 2,command = GetNumTwo)
NumTwoBtn.grid(row=1, column=1)
NumThreeBtn = Button(root,text = "3", width = 8,height = 2,command = GetNumThree)
NumThreeBtn.grid(row=1, column=2)
PlusBtn = Button(root,text = "+", width = 8,height = 2,command = GetPlus)
PlusBtn.grid(row=1, column=3)
MinusBtn = Button(root,text = "-", width = 8,height = 2,command = GetMinus)
MinusBtn.grid(row=1, column=4)
CleanBtn = Button(root,text = "C", width = 8,height = 2,command = GetClean)
CleanBtn.grid(row=1, column=5)
NumFourBtn = Button(root,text = "4", width = 8,height = 2,command = GetNumFour)
NumFourBtn.grid(row=2, column=0)
NumFiveBtn = Button(root,text = "5", width = 8,height = 2,command = GetNumFive)
NumFiveBtn.grid(row=2, column=1)
NumSixBtn = Button(root,text = "6", width = 8,height = 2,command = GetNumSix)
NumSixBtn.grid(row=2, column=2)
MultiplyBtn = Button(root,text = "*", width = 8,height = 2,command = GetMultiply)
MultiplyBtn.grid(row=2, column=4)
ResultBtn = Button(root,text = "=", width = 8, height = 2,background = "green",command=GetResult)
ResultBtn.grid(row=2, column=5)
NumSevenBtn = Button(root,text = "7",width = 8, height = 2, command = GetNumSeven)
NumSevenBtn.grid(row=3, column=0)
NumEightBtn = Button(root,text = "8", width = 8, height = 2, command = GetNumEight)
NumEightBtn.grid(row=3, column=1)
NumNineBtn = Button(root,text = "9", width = 8, height = 2, command = GetNumNine)
NumNineBtn.grid(row=3, column=2)
NumZeroBtn = Button(root,text = "0", width = 8, height = 2, command = GetNumZero)
NumZeroBtn.grid(row=3, column=3)
DivisionBtn = Button(root,text = "/", width = 8, height = 2, command = GetDivision)
DivisionBtn.grid(row=3, column=4)
root.mainloop()


