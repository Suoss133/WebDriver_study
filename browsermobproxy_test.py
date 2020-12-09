from selenium import webdriver
import json

# driver = webdriver.Chrome(executable_path='./driver/chromedriver')
# driver = webdriver.Firefox(executable_path='./driver/geckodriver')
# driver.get(url='http://www.baidu.com')

from browsermobproxy import Server

server = Server('/Users/dzj/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat')
server.start()
proxy = server.create_proxy()

profile = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(executable_path='./driver/geckodriver', firefox_profile=profile)
proxy.new_har("baidu",
              options={'captureContent': True, 'captureHeaders': True, 'captureBinaryContent': True})
driver.get("https://www.baidu.com")
print(json.dumps(proxy.har))
server.stop()
driver.quit()