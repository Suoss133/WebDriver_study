import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver.get('https://www.jd.com/')
driver.maximize_window()
# driver.find_element_by_xpath('//ul[@class="elevator_list"]/li[1]').click()
# right_slice = driver.find_element_by_xpath(
#     '//div[@class="slider"]//button[@class="slider_control slider_control_next"]')
#
# list_elements = []
# flag = True
# while flag:
#     elements = driver.find_elements_by_xpath('//h6[@class="seckill-item__name"]')
#     for ele in elements:
#         if ele.text != '' and ele.text not in list_elements:
#             list_elements.append(str(ele.text))
#         else list_elements[0] == ele.text:
#             flag = False
#     right_slice.click()
#     import time
#     time.sleep(2)
# print(list_elements)
# print(len(list_elements))

driver.find_element_by_xpath('//input[@aria-label="搜索"]').send_keys('iphone12')
driver.find_element_by_xpath('//button[@aria-label="搜索"]').click()

time.sleep(3)
flag = True
while flag:
    time.sleep(3)
    page = driver.find_element_by_xpath('//div[@class="page clearfix"]')
    page.location_once_scrolled_into_view
    elements = driver.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li')
    for ele in elements:
        source_str = str(ele.text)
        list_content = source_str.split('\n')
        str_context = ' '.join(list_content)
        print(str_context)
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//a[@class="pn-next"]').click()
    except selenium.common.exceptions.NoSuchElementException:
        flag = False
