### 获取身高
height = float(input("请输入你的身高(m)："))
### 获取体重
num2 = float(input("请输入你的体重(kg)："))
### 计算BMI值
bmi = num2 / (height * height)
print("你的BMI指数是：%.2f" % bmi)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")