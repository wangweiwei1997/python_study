# -*-coding:UTF-8 -*-
from xlwt.Workbook import Workbook
from xlwt.Style import XFStyle
from importlib.resources import contents

Workbook

wb=Workbook('utf-8')
sheet=wb.add_sheet('测试')

title = ['编号', '姓名', '职业', '上级', '入职日期']

title_style = XFStyle()

for i in range(len(title)):
    sheet.write(4,i + 4,title[i],title_style)
    
content = [7369,'SMITH','CLERK',7902,12/17/1980]  ,[7499,'ALLEN','SALESMAN',7698,2/20/1981] 
for i in range(len(content)):
    for j in range(len(content[i])):