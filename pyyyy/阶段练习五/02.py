# 使用给定的整数n,编写程序以生成包含（i:i*i）的字典，并且是1和n之间的所有整数（包括两者），打印出一个字典
# 假设为程序提供了整数：8
# 输出结果：{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}
n=input("n=")
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)