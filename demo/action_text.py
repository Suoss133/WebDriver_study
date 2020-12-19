from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver')
driver.maximize_window()
driver.get(url='https://map.baidu.com')
time.sleep(3)
map = driver.find_element_by_xpath('//div[@id="mask"]')
ActionChains(driver).move_to_element(map).context_click().perform()
time.sleep(2)
start_point = driver.find_element_by_xpath('//span[@id="cmitem_start"]')
ActionChains(driver).move_to_element(start_point).click().perform()
time.sleep(2)
for i in range(2):
    ActionChains(driver).drag_and_drop_by_offset(source=map, xoffset=100, yoffset=0).perform()
    time.sleep(2)

end_point = driver.find_element_by_xpath('//span[@id="cmitem_end"]')
ActionChains(driver).move_to_element(end_point).click().perform()

