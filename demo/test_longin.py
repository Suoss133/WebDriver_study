import unittest
import os
import time
from selenium import webdriver

chromedirver = os.path.join(os.path.dirname(__file__), '../driver/chromedriver')
driver = webdriver.Chrome(executable_path=chromedirver)
homopage_url = 'http://49.233.108.117:3000/'


class TestLogin(unittest.TestCase):
    driver = driver

    @classmethod
    def setUpClass(cls) -> None:
        print('所有的用例运行之前打开浏览器')
        cls.driver = driver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(url=homopage_url)

    @classmethod
    def tearDownClass(cls) -> None:
        print('所有的用例运行执行后执行')
        cls.driver.quit()

    def setUp(self) -> None:
        print('每个test执行之前打开登录页面')
        self.driver.find_element_by_xpath('//ul[@class="nav pull-right"]/li[last()]/a').click()

    def tearDown(self) -> None:
        print('每个用例执行之后添加截图')
        day = time.strftime('%Y-%m-%d')
        current_time = time.strftime('%H-%M-%s')
        screenshot_dir = os.path.join(os.path.dirname(__file__), f'screenshots/{day}')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        png_file = os.path.join(screenshot_dir, current_time + '.png')
        self.driver.save_screenshot(png_file)
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def login_with_username_password(self, username, password):
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@type="submit"]').click()

    def should_login_success(self):
        '''断言，判断登录成功是否跳转到首页'''
        url = self.driver.current_url
        self.assertEqual(url, homopage_url)

    def shoule_login_fail_with_erro_msg(self, erro_msg):
        result_erro_text = self.driver.find_element_by_xpath('//div[@class="alert alert-error"]/strong').text
        self.assertEqual(result_erro_text, erro_msg)

    def test_01_login_success(self):
        self.login_with_username_password('fanmao1', '123456')
        self.should_login_success()

    def test_02_login_fail(self):
        self.login_with_username_password('helloword', '123456')
        self.shoule_login_fail_with_erro_msg('用户名或密码错误')

    def test_03_login_fail(self):
        self.login_with_username_password('helloword', '')
        self.shoule_login_fail_with_erro_msg('信息不完整。')


if __name__ == '__main__':
    unittest.main(verbosity=2)
