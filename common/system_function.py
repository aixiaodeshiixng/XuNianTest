from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


def login(driver:WebDriver,username,password):
    for a in range(2):
        driver.find_element_by_xpath('//input[@placeholder="账号"]').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        driver.find_element_by_xpath('//input[@placeholder="账号"]').send_keys(username)
        driver.find_element_by_xpath('//input[@placeholder="密码"]').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        driver.find_element_by_xpath('//input[@placeholder="密码"]').send_keys(password)
        driver.find_element_by_xpath('//span[contains(text(),"登录")]').click()
        if a<=0:
            driver.refresh()
        else:
            continue

def xunian_login(driver: WebDriver, username, password):
    driver.find_element(By.LINK_TEXT,'登录').click()
    driver.find_element_by_xpath('//input[@placeholder="手机号"]').send_keys(username)
    driver.find_element_by_xpath('//input[@placeholder="密码"]').send_keys(password)
    driver.find_element_by_xpath('//span[contains(text(),"登录")]').click()


def exit(driver):
    pass