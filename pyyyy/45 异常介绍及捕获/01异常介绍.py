# # try:
# #     s=int(input("请输入一个数字："))
# #     print(450 / s)
# # except:
# #     print("请输入一个大于不等于0的数")
# #
# try:
#     s=int(input("请输入一个整数："))
#     m=int(input("请再输入一个整数："))
#     print(s/m)
# except ZeroDivisionError:
#     print("请输入正确的数字")

# try:
#     s=int(input("请输入一个整数："))
#     print(450/s)
# except Exception:
#     print("请输入正确的数字")

try:
    h=int(input("请输入一个整数："))
    print(450/h)
except Exception as e:
    print(e)