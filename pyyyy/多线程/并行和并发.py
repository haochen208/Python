# import time
# def sing():
#     for i in range(5):
#         time.sleep(0.5)
#         print('我在唱歌')
# def dance():
#     for i in range(5):
#         time.sleep(0.5)
#         print('我在跳舞')
# sing()
# dance()

# import threading
# import time
# def sing():
#     for i in range(5):
#         time.sleep(0.5)
#         print('我在唱歌')
# def dance():
#     for i in range(5):
#         time.sleep(0.5)
#         print('我在跳舞')
# t1=threading.Thread(target=sing)
# t1.start()
# t2=threading.Thread(target=dance)
# t2.start()

# import threading
# num=0
# def t():
#     global num
#     num+=1
#     print(num,end='')
# for i in range(0,8):
#     d=threading.Thread(target=t)
#     d.start()

# import threading
# import time
# def run():
#     time.sleep(2)
#     print('当前线程的名字是%s\n'%threading.current_thread().name)
#     time.sleep(2)
# if __name__=='__main__':
#     start_time=time.time()
#     print('这是主线程:',threading.current_thread().name)
#     thread_list=[]
#     for i in range(5):
#         t=threading.Thread(target=run)
#         thread_list.append(t)
#     for t in thread_list:
#         t.setDaemon(True)
#         t.start()
#     for t in thread_list:
#         t.join()
#     print('主线程结束了',threading.current_thread().name)
#     print('一共用时:',time.time()-start_time)

# import threading
# import time
# def work1(nums):
#     nums.append(44)
#     print('---in work1---',nums)
# def work2(nums):
#     time.sleep(1)
#     print('---in work2---',nums)
# g_nums=[11,22,33]
# t1=threading.Thread(target=work1,args=(g_nums,))
# t1.start()
#
# t2=threading.Thread(target=work2,args=(g_nums,))
# t2.start()

# import threading
# g_num = 0
# def work1():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#     print("----in work1, g_num is %d---" % g_num)
#
# def work2():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#     print("----in work2, g_num is %d---" % g_num)
#
# print("---线程创建之前g_num is %d---" % g_num)
#
# t1 = threading.Thread(target=work1)
# t2 = threading.Thread(target=work2)
# t1.start()
# t2.start()


# import threading
# my_num=0
# lock=threading.Lock()
#
# def work1():
#     lock.acquire()
#     global my_num
#     for i in range(1000000):
#         my_num += 1
#     print("work1:",my_num)
#     lock.release()
#
# def work2():
#     lock.acquire()
#     global my_num
#     for i in range(1000000):
#         my_num += 1
#     print("work2:",my_num)
#     lock.release()
#
# if __name__=='__main__':
#     t1 = threading.Thread(target=work1)
#     t2 = threading.Thread(target=work2)
#     t1.start()
#     t2.start()

def AAA():
    print('hello world')
from tkinter import *
tk=Tk()
btn=Button(tk,text='click me',command=AAA)
btn.pack()








