# -*-coding:UTF-8 -*-
from selenium import webdriver
from time import sleep
from ui.demo import driver

#业务（谷歌）
wb=webdriver.Chrome
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_elements_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()
sleep(1)
driver.switch_to.frame('menu-frame')
