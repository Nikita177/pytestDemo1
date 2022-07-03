from selenium import webdriver
from selenium.webdriver.common.by import By


def test_newtour():

    driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://demo.guru99.com/test/newtours/")
    links=driver.find_elements(By.TAG_NAME,"a")
    print("Number of links present ",len(links))
    driver.close()