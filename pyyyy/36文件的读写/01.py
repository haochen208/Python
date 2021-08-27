# # f=open("小说.txt","r",encoding="utf-8")
# # print(f.read())
# # print(f.read(15))
# # f.close()
#
# f=open("小说.txt","r",encoding="utf-8")
# # content=f.readlines()
# # j=1
# # for i in content:
# #     print(j,i)
# #     j += 1
# c=f.readline()
# print(c)
# c1=f.readline()
# print(c1)
# f.close()

oldname=input("请输入您要要拷贝的文件名：")
index=oldname.find(".")
newname=oldname[:ibdex]+"-副本"+oldname[index:]
oldfile=open(oldname,"r",encoding="utf-8")
content=oldfire.readlines()
newfire=open(newname,"w",encoding="utf-8")
for i in content:
    newfile.write(i)
oldfile.close()
newfile.close()