import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

def test_first():

        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.maximize_window()
        driver.find_element_by_name("q").send_keys("LinkedIn login")
        time.sleep(2)
        driver.find_element_by_name("btnK").click()
        driver.find_element(By.PARTIAL_LINK_TEXT,'LinkedIn Login').click()
        name = driver.title
        print(driver.current_url)
        driver.close()
        assert name in "LinkedIn Login, Sign in | LinkedIn"




