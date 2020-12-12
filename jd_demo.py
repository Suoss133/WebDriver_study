from selenium import webdriver

driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver.get('https://www.jd.com/')
driver.maximize_window()
# driver.find_element_by_xpath('//ul[@class="elevator_list"]/li[1]').click()
# right_slice = driver.find_element_by_xpath(
#     '//div[@class="slider"]//button[@class="slider_control slider_control_next"]')
#
# list_eles = []
# flag = True
# while flag:
#     eles = driver.find_elements_by_xpath('//h6[@class="seckill-item__name"]')
#     for ele in eles:
#         if ele.text != '' and ele.text not in list_eles:
#             list_eles.append(str(ele.text))
#         else list_eles[0] == ele.text:
#             flag = False
#     right_slice.click()
#     import time
#     time.sleep(2)
# print(list_eles)
# print(len(list_eles))

driver.find_element_by_xpath('//input[@aria-label="搜索"]').send_keys('iphone12')
driver.find_element_by_xpath('//button[@aria-label="搜索"]').click()

import time
import re

time.sleep(3)
page = driver.find_element_by_xpath('//div[@class="page clearfix"]')
page.location_once_scrolled_into_view
eles = driver.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li')
for ele in eles:
    partter = re.compile('[^\s].+?')
    partter_text = partter.findall(ele.text)
    str_context = ''.join(partter_text)
    print(str_context)

