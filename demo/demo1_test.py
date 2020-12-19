from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load = 'eager'
driver = webdriver.Chrome(executable_path='../driver/chromedriver', options=options)
driver.get('https://www.jd.com/')
driver.maximize_window()

driver.find_element_by_xpath('//input[@aria-label="搜索"]').send_keys('iphone12')
driver.find_element_by_xpath('//button[@aria-label="搜索"]').click()
