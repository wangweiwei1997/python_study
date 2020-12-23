# -*-coding:UTF-8 -*-
from xlwt.Workbook import Workbook

wb=Workbook
sheet = wb.add_sheet('测试')
sheet.write(2,2,'客户无忧')
wb.save(r'd:\测试.xls')
