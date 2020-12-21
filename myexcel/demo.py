# -*-coding:UTF-8 -*-


# 读多少行
from xlrd import open_workbook
bk=open_workbook(r'd:\emp.xls')
sheet=bk.sheet_by_name('empinfo')
print(sheet.nrows)

# 读多少列
print(sheet.ncols)

#读某单元格（ANALYST）
cell_value = sheet.cell_value(12,6) #下标从0开始
print(cell_value)

#读整个第X（7）行数据
row_values = sheet.row_values(6,4)#4代表切割到哪里
print(row_values)

#读某列（姓名）数据
col_values = sheet.col_values(5,5)
print(col_values)


#读整个列表数据


#分装整个列表
class MyExcel():

    def __init__(self, workbook_name, sheet_name):
        self.workbook_name = workbook_name
        self.sheet_name = sheet_name

    def __sheet(self):
        bk = open_workbook(self.workbook_name) 
        sheet = bk.sheet_by_name(self.sheet_name)
        return sheet