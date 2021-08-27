import xlrd,json
data=xlrd.open_workbook('d:\student.xls')
table=data.sheets()[0]
nrows=table.nrows
stu_score_list=[]
for i in range(nrows):
    if i==0:
        continue
    print(table.row_values(i))

stu_score_list.append(table.row_values(i))
json_data=json.dumps(stu_score_list)

with open('d:\student.xls','w') as f:
    f.write(json_data)
with open('d:\student.xls','r') as f:
    data=json.load(f)

avg_score_dict={}
for i in stu_score_list:
    stu_name=i[0]
    avg_score=sum(i[1::])/len(i[1::])
    print('%s的平均成绩为:%.2f分'%(stu_name,avg_score))
    if i[4]>=80:
        print("%s的python成绩为:%d分"%(i[0],i[4]))
    avg_score_dict[stu_name]=avg_score

subject_list=['语文','数学','英语','科学','python']

for stu_score in stu_score_list:
    for score in stu_score[1::]:
        if score==100:
            student_name=stu_score[0]
            score_index=stu_score[1:].index(100)
            subject=subject_list[score_index]
            print("有满分科目的学生是%s,对应得满分科目是%s"%(student_name,subject))
