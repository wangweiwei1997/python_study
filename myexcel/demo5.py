# -*-coding:UTF-8 -*-
from pymysql import connect
#引包：connect
conn = connect(host='192.168.1.4', user='root', password="root", database='cms', port=3306)
#打开游标cursor
cursor = conn.cursor()
#在mysql找到这个表格
cursor.execute('select * from _cai_student_cai')

result=cursor.fetchall()
print(result)
cursor.close()
conn.close()


