import os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common import browser, system_function
from common.config import local_config



class TesttLoginSucess(unittest.TestCase):

    def setUp(self):
        self.driver = browser.get_chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_login(self):
        self._testMethodName = 'xnwx-dl-01'
        self._testMethodDoc = '正确的用户名和密码能否登录'
        self.driver.get(local_config.URL+local_config.PORT)
        system_function.xunian_login(self.driver,'17673297546','1234567')
        time.sleep(2)
        print('111111111')

        b = self.driver.find_elements_by_xpath('//li[contains(text(),"注销")]')
        print(len(b))
        if len(b) ==0:
            a = False
        elif len(b)==1:
            a = True
        else:
            a = False
        print(a)












if __name__=='__main__':
    unittest.main()
