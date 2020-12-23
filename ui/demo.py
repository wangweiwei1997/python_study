# -*-coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#找到网址，跟踪进去
driver=webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

#在网址上写入账户和密码
#点击右键-检查可看到name('username')
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
#不用键盘登录
# driver.find_element_by_class_name('btn-a').click()
#键盘登录(ENTER)
driver.find_element_by_class_name('btn-a').send_keys(Keys.ENTER)



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
#输入要搜索的物品
driver.find_element_by_name('keyword').send_keys('车')
driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()

driver.find_elements_by_css_selector('.caichang')




