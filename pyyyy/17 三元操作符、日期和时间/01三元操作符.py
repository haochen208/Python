# if 条件1:
#     要做的事情1
# else:
#     要做的事情2

# if 3 > 2:
#     print("成立")
# else:
#     print("不成立")

# 三元操作符：条件为真的结果 if 条件 else 条件为假的结果
# print("成立" if 3 > 2 else "不成立")
# print("成立") if 3 > 2 else print("不成立")

# 满100打8折
import time
start = time.time()

money = int(input("请输入您的购买金额："))
print(money * 0.8 if money > 100 else money)

end = time.time()
print(end - start)
