from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Test_window:

    def test_window():

      driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
      driver.get("http://demo.automationtesting.in/Windows.html")
      driver.find_element(By.XPATH, "//a[contains(text(),'Open New Tabbed Windows')]").click()
      driver.find_element(By.XPATH,"//div[@id='Tabbed']//a").click()
      time.sleep(2)
      driver.close()