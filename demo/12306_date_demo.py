from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities['pageLoadStrategy'] = 'none'


driver = webdriver.Chrome(executable_path='../driver/chromedriver', desired_capabilities=desired_capabilities)

driver.get(url='https://www.12306.cn/index/')
# driver.maximize_window()
# time.sleep(2)
js_script = 'document.getElementById("train_date").value="2020-01-20"'
driver.execute_script(js_script)
