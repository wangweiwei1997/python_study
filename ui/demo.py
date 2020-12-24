# -*-coding:UTF-8 -*-

#数据库连接表内容

from time import sleep

from pymysql import connect
from pymysql.cursors import Cursor
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 一、先  webdriver：引出包，再进行下一步操作
#   ..\drivers\chromedriver.exe：返回到drivers包下的chromedriver.exe
#找到网址，跟踪进去
driver=webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
#最大化这个网址
driver.maximize_window()

#二、登录谷歌----在网址上写入账户和密码
#点击右键-检查可看到name=username
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
#不用键盘登录
driver.find_element_by_class_name('btn-a').click()
#键盘登录(ENTER)
# driver.find_element_by_class_name('btn-a').send_keys(Keys.ENTER)

sleep(1)
#在商品列表点击-----检查------找到menu-frame
#switch_to_frame：进
#find_element_by：输入
#.click：点一下（相当于鼠标点击）
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
#出去重新进一个
driver.switch_to.default_content()
#在搜索点击-----检查------找到menu-frame
#进入到查询
driver.switch_to.frame('main-frame')
sleep(2)
#输入要搜索的商品（车）
driver.find_element_by_name('keyword').send_keys('车')
#' 搜索 '需去   检查  复制过来，因为你不知道他有多少空格存在
driver.find_element_by_xpath("/html/body/div[3]/form/input[2]").click()


#  //*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span---- 在平衡车处 点击检查，右键点击copy（copy xpath)
#复制到下面
sleep(1)
  
search_text = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
search_total = driver.find_element_by_id('totalRecords').text  

#三、打开MySQL数据库内容
conn = connect('192.168.1.4','root','root','ecshop',3306)
#游标
cursor = conn.cursor()
#打开MySQL:ecs_goods的表格:显示：goods_name
cursor.execute("select goods_name from ecs_goods where goods_name like '%车%'")


#fetchall（光标执行所有内容）
#fetchone（光标执行一个内容）
#抓取上面：（select goods_name from ecs_goods where goods_name like '%车%）的值
#用rs定义
rs = cursor.fetchall()
# print(rs)

#打开MySQL:ecs_goods的表格，count(*)：统计表格的数据
cursor.execute("select count(*) from ecs_goods where goods_name like '%车%'")
#抓取上面：（select count(*) from ecs_goods where goods_name like '%车%）的值
#用total来定义
total=cursor.fetchone()
#谷歌的search_text和数据库的goods_name；谷歌的search_total和数据库的count(*)---相对比
if search_text==rs[0][0] and int(search_total) ==total[0] :
    print('测试通过')
else:
    print("测试不通过")
cursor.close()
conn.close()












