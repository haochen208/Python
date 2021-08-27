# 从键盘输入一段字符串，将小写字母全部转换成大写字母，然后输出到一个"test.txt"文件中进行保存
s=input("请输入一段字符串：")
a=open("text.txt","w",encoding="UTF-8")
a.write(s.upper())
a.close()
f=open("text.txt","r",encoding="UTF-8")
print(f.read())
f.close()