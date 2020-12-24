# -*-coding:UTF-8 -*-
from selenium import webdriver
from ui.demo import driver


wb=webdriver.Chrome()
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_element_by_class_name('btn-a').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()