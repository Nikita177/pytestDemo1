from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_window():

    driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.webelements.com/")
    rows=len(driver.find_elements(By.XPATH,"//tbody/tr"))
    #ols=len(driver.find_elements(By.XPATH,"//tbody/tr[2]/td"))
    print(f"No of rows{rows}")

    for row in range(2,rows+1):
      for col in range(1,len(driver.find_elements(By.XPATH,"//tbody/tr["+str(row)+"]/td"))+1):
       value=driver.find_element(By.XPATH, "//tbody/tr[" + str(row) + "]/td[" + str(col) + "]").text
       print(value+"\n",end=' ')
       print(' ')







