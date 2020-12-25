# -*-coding:UTF-8 -*-
from selenium import webdriver
from time import sleep

# 业务（谷歌）
driver = webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
# 退出一个界面，进另外一个界面(菜单-管理中心）
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')
sleep(2)
#  //*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span（找出图片），点击商品名称下面的内容，右键点击检查，右键点击copy--copy xpath，把复制的内容粘贴到下面↓
goods_name = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
#  //*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img  点击上架（√）的内容，右键点击检查，右键点击copy--copy xpath，把复制的内容粘贴到下面↓
img_type = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img').get_attribute('src').split('/')

#↓假设img_type是否上架（用if）
if img_type[-1]=='no.gif':
    is_on_sale = 1
else:
    is_on_sale = 0
 #点上架：[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img 这个（click：点）   
driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img').click()
#进入数据库的网址:'192.168.1.4', 'root', 'root', 'ecshop', 3306
conn = connect('192.168.1.4', 'root', 'root', 'ecshop', 3306)
#用connect点击去查找到cursor和execute
cursor=conn.cursor()
cursor.execute("select is_on_sale from ecs_goods where goods_name='%s'" %goods_name)
result = cursor.fetchone()
#print(result[0])
if result[0] == is_on_sale:
    print('测试通过')
else:
    print('测试不通过')







