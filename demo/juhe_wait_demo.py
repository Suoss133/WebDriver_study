from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='../driver/chromedriver')
driver.maximize_window()
driver.get(url='https://www.juhe.cn/')
start = time.process_time()

iframe  = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//iframe[@id="layui-layer-iframe1"]')))
driver.switch_to.frame(iframe)

driver.find_element_by_xpath('//input[@id="mobilephone"]').send_keys('13365854568')

driver.quit()
end = time.process_time()
print(f'总运行时间:{end - start}')
