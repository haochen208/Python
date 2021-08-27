# 编写一个collatz函数，他有一个叫number的参数，
# 如果该参数是偶数，那么collatz()打印并返回number//2;
# 如果该参数是奇数，那么collatz()打印并返回number*3+1;
# 然后编写一个程序，让用户输入一个整数，并不断对这个数字调用collatz()函数，直到函数返回值为1停止。
# 【现象是：无论输入的整数是什么，最后都会得到1】
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1

num = int(input("请输入一个整数："))
i = 0
while i != 1:
    i = collatz(num)
    num = i