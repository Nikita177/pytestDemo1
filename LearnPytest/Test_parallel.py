'''
pip install pytest
pip install selenium
pip install webdriver-manager
pip install pytest-xdist

 pytest -v .\LearnPytest\Test_parallel.py -n 2

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_automation():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.find_element(By.XPATH,"//button[contains(text(),'Click Me')]").click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    driver.close()
    assert driver.title=='Automation Testing Practice'


def test_google():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    driver.close()
    assert driver.title=='Google'