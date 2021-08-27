# 获取用户输入想吃的水果，如果在列表里面，则输出；不在列表里面，则添加到水果列表里面。
fruits = ["苹果", "桃子", "西瓜", "香蕉", "橘子"]
fruit = input("请输入您想吃的水果：")
if fruit in fruits:
    print(fruit)
else:
    fruits.append(fruit)

print(fruits)
