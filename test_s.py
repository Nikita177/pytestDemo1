import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def test_sec():

    driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
   # driver = webdriver.Chrome(ChromeDriverManager.install())
    driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
    driver.maximize_window()
    driver.find_element(By.ID,'firstName').send_keys("Nikita")
    name=driver.title
    print(driver.current_url)
    driver.close()
    assert name in "Create your Google Account"
