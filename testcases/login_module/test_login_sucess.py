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
        self._testMethodName = 'qrs-ht-dl-01'
        self._testMethodDoc = '柒芮斯为每个商品添加规格和价格'
        self.driver.get(local_config.URL+local_config.PORT)
        system_function.login(self.driver,'administrator','macro123')
        self.driver.find_element_by_xpath('//span[contains(text(),"商品管理")]').click()
        self.driver.find_element_by_xpath('//span[contains(text(),"商品列表")]').click()
        for k in range(14):
            self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[6]/span[3]/div/input').click()
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
            self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[6]/span[3]/div/input').send_keys('%d'%(k+7))
            ActionChains(self.driver).key_down(Keys.ENTER).perform()
            time.sleep(1)
            for l in range(10):
                print(l)
                list1 = self.driver.find_elements_by_xpath('//div[contains(text(),"出售价：")]')
                # del list1[0]
                a = list1[l].text
                time.sleep(1)
                list2 = self.driver.find_elements_by_xpath('//span[contains(text(),"规格编辑")]')
                list2[l+1].click()
                time.sleep(3)
                self.driver.find_element_by_xpath('//span[contains(text(),"新增")]').click()
                self.driver.find_element_by_xpath('//input[@placeholder="请输入规格名称"]').send_keys('50分H色VSI')
                self.driver.find_element_by_xpath('//input[@placeholder="请输入规格编码"]').send_keys('23521')
                b = self.driver.find_elements_by_xpath('//input[@placeholder="请输入价格"]')
                for i in b :
                    i.send_keys(a[4:])
                self.driver.find_element_by_xpath('//input[@placeholder="请输入库存"]').send_keys(999)
                c = self.driver.find_elements_by_xpath('//input[@placeholder="请输入"]')
                c[0].send_keys(12)
                c[1].send_keys(12)
                self.driver.find_element_by_xpath('//span[contains(text(),"保存")]').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('//span[contains(text(),"商品管理")]').click()
                self.driver.find_element_by_xpath('//span[contains(text(),"商品列表")]').click()
                self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[6]/span[3]/div/input').click()
                ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[6]/span[3]/div/input').send_keys('%d'%(k+7))
                ActionChains(self.driver).key_down(Keys.ENTER).perform()
                time.sleep(2)
                print(k+7)





        # self.driver.find_element_by_xpath('//span[contains(text(),"出入库管理")]').click()
        # self.driver.find_element_by_xpath('//span[contains(text(),"新建采购单")]').click()
        # self.driver.find_element_by_xpath('//span[contains(text(),"导入钻石")]').click()
        # os.system('C:\\Users\\dn\\Documents\\aaa.exe')
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//span[contains(text(),"确认导入")]').click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath('//span[contains(text(),"出入库管理")]').click()
        # actual_result = self.driver.find_element_by_xpath()



if __name__=='__main__':
    unittest.main()
