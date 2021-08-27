# product_list=[("iphone",5800),
#               ("mac pro",9800),
#               ("bike",800),
#               ("watch",10600),
#               ("coffee",31),
#               ("python",120)]
# shopping_list=[]
# money=input("请输入你的钱数:")
# if money.isdigit():
#     money=int(money)
# else:
#     print("该输入包含其他字符")
# while True:
#     for index,item in enumerate(product_list):
#         print(index,item)
#     print("按q退出")
#     user_choise=input("请输入你要买的商品编号：")
#     if user_choise.isdigit():
#         user_choise=int(user_choise)
#         if user_choise < len(product_list) and user_choise>=0:
#             p_item=product_list[user_choise]
#             if p_item[1]<=money:
#                 shopping_list.append(p_item)
#                 money-=p_item[1]
#                 print("added %s into shoppingcart,your current balance is %d"%(p_item,money))
#             else:
#                 print("你的余额只有[%s],无法购买"% money)
#         else:
#             print("product code[%s] is not exist"%user_choise)
#     elif user_choise=="q":
#             print("-------shopping list--------")
#             for p in shopping_list:
#                 print(p)
#             print("your current balance:",money)
#             exit()
#     else:
#         print("invalid option")




