# -*-coding:UTF-8 -*-
from pymysql import connect
from xlwt.Workbook import Workbook

# 链接MySQL数据库
conn = connect(host='192.168.1.4', user='root', password="root", database='cms', port=3306)
# 游标
cursor = conn.cursor()
# 引出表格
cursor.execute('select * from wang_student')
result = cursor.fetchall()

print(result)
cursor.close()
conn.close()



wb=Workbook('utf-8')


