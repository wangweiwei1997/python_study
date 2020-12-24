# -*-coding:UTF-8 -*-
from selenium import webdriver



#业务（谷歌）
wb=webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_elements_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

driver.switch_to.frame('menu-frame')
driver.find_elements_by_link_text('商品列表').click()
#退出，进另外一个
driver.switch_to_default_content()
driver.switch_to.frame('main-frame')

good_names = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
img_type = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').get_attribute('src').split('/')


