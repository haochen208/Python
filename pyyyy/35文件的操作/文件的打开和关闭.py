# f=open("haochen.txt","w",encoding="UTF-8")
# f.write("我叫昊宸 \n")
# f.write("今年十二岁了 \n")
# f.close()

# f=open("haochen.txt","r",encoding="UTF-8")
# print(f.read())
# f.close()

# f=open("haochen.txt","a",encoding="UTF-8")
# f.write("my name is haochen.")
# f.close()

# f=open("text.py","w",encoding="UTF-8")
# f.close()
#
# f=open("text.py","w",encoding="UTF-8")
# f.write("""year = int(input("请输入一个年份："))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("%d是闰年" % year)
# else:
#     print("%d不是闰年" % year)
# """)


import random

f = open("ip.txt", "w")
for i in range(120):
    f.write(
        str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "\n")

f.close()