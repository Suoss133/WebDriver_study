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

    @classmethod
    def tearDownClass(cls) -> None:
        print('所有的用例运行执行后执行')
        cls.driver.quit()

    def setUp(self) -> None:
        print('每个test执行之前打开首页')
        self.driver.get(url=homopage_url)

    def tearDown(self) -> None:
        print('每个用例执行之后添加截图')
        day = time.strftime('%Y-%m-%d')
        current_time = time.strftime('%H-%M-%s')
        screenshot_dir = os.path.join(os.path.dirname(__file__), f'screenshots/{day}')
        if not os.path.exists(screenshot_dir):
            os.mkdir(screenshot_dir)
        png_file = os.path.join(screenshot_dir,current_time+'.png')
        self.driver.save_screenshot(png_file)
        self.driver.delete_all_cookies()

    def test_01_login_success(self):
        print('用户登录成功场景')

    def test_02_login_fail(self):
        print('用户登录失败场景')


if __name__ == '__main__':
    unittest.main(verbosity=2)
