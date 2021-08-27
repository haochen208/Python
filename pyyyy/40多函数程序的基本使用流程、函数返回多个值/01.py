# num=1
# def f1():
#     global num
#     num =100
# def f2():
#     print(num)
# f1(f2())

# def f3():
#     return "恭喜"
# def f4(num):
#     print(num+"发财")
# f4(f3())

def f5():
    return "恭喜"
def f6():
    return f5()+"发财"
print(f6())