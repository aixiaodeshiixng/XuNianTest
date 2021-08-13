import os
from selenium import webdriver

def get_chrome():
    driver_path = os.path.dirname(__file__)+'/../webdriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    return driver



