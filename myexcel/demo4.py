# -*-coding:UTF-8 -*-
from xlrd import open_workbook
from xlutils.copy import copy


yuanshi_excel=open_workbook(r'd:/原始表.xls')
new_sheet = copy(yuanshi_excel)
sheet = new_sheet.get_sheet(0)

sheet.write(2, 5, 14)
sheet.write(2, 8, '王苇')
new_sheet.save(r'd:/新表.xls')



