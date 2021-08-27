# import re
# # 根据正则表达式查找数据，提示：只查找一次
# # 1.pattern: 正则表达式
# # 2.string: 要匹配的字符串
# match_obj = re.search("\d+", "水果有20个 其中苹果10个")
# if match_obj:
#     # 获取匹配结果数据
#     print(match_obj.group())
# else:
#     print("匹配失败")
#
#
# #需求：匹配出多种水果的个数
# import re
# # 根据正则表达式查找数据，提示：可以查找多次，返回一个列表，如果没找到返回一个空列表
# # 1.pattern: 正则表达式
# # 2.string: 要匹配的字符串
# result = re.findall("\d+", "苹果10个 鸭梨5个 总共15个水果")
# print(result)
#
#
# import re
# res=re.sub('\d+','22','评论数:10 赞数:20',count=1)
# print(res)
#
# import re
# res=re.sub('\d+','22','评论数:10 赞数:20',count=1)
# print(res)
# import re
# def add(match_obj):
#     value=match_obj.group()
#     result=int(value)+1
#     return str(result)
# result=re.sub('\d+',add,'阅读数:10')
# print(result)
#
# import re
# mystr='貂蝉,杨玉环,西施,王昭君'
# result=re.split(',|:',mystr,maxsplit=2)
# print(result)

# import re
# pattern=r'[?|&]'
# url="http://www.baidu.com/login.jsp?username='xiaoming'\
# &pwd='mmmmmm'"
# res=re.split(pattern,url)
# print(res)

import tkinter as tkr
import re

QQstr="""
群成员人数: 12/500  添加成员  设置管理员  删除成员 
搜索关键词
更多筛选
		成员	群名片	QQ号	性别	
Q龄	
入群时间	
最后发言	
1	
暖阳	
杨某某
785844930	男	10年	2012年5月以前	2016/04/29	
	2	
绿野	
孟某某
453984879	未知	13年	2012年5月以前	2016/04/29	
	3	
 小孤山 	
王某某
592124209	男	10年	2012年5月以前	2015/03/05	
	4	
曹小军	
曹某某
893107577	女	8年	2012年5月以前	2016/04/18	
	5	
小蚂蚁	
关某某
1486337721	女	7年	2012年5月以前	2012/04/06	
	6	
妍化山石	
段某某
1654784261	女	7年	2012年5月以前	2016/04/17	
	7	
云淡风轻	
孙某某
1327227541	女	6年	2013/03/17	2016/04/17	
	8	
孙叶子	
孙某霞
84007476	女	17年	2013/03/17	2016/04/17	
	9	
桃李不言	
王某伟
529530247	男	13年	2013/03/17	2015/07/16	
	10	
咕噜熊	
谢某某
29363055	男	17年	2016/04/17	2016/04/17	
	11	
峰	
齐某某
27931865	男	17年	2016/04/17	2016/04/17	
	12	
明月	
关某某
304919428	女	14年	2016/04/17	2016/04/17	
友情链接：QQ官方网站 | 腾讯开放平台 | 在线教育介绍 | QQ商家 | QQ会员 | 腾讯文档
"""

#全局变量
baklist=[]
#提取QQ号，加上邮箱号，插入列表
def extract():
    global baklist #引用全局变量
    mylist=re.findall(r"[1-9][0-9]{4,10}",text.get("0.0","end"))
    print("提取到的QQ号是：")
    print(mylist)
    for qq in mylist:
        qq+="@qq.com"
        list.insert(tkr.END,qq)
        baklist.append(qq)

#保存提取的信息到files文件夹
def save():
    file=open("qqmail.txt","wb")
    if baklist!=None:
        for qq in baklist:
            file.write((qq+"\r\n").encode("utf-8"))
    file.close()

win=tkr.Tk()
button=tkr.Button(win,text="提取",command=extract)
button.pack()

buttonSave=tkr.Button(win,text="保存",command=save)
buttonSave.pack()

text=tkr.Text(win)
text.insert(tkr.INSERT,QQstr)
text.pack()

list=tkr.Listbox(win)
list.pack()

win.mainloop()