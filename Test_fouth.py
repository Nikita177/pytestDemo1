from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_newtour():


    driver = webdriver.Chrome(ChromeDriverManager().install())
   # driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.find_element(By.XPATH,"//button[contains(text(),'Click Me')]").click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    driver.close()
