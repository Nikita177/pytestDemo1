from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

def test_actions():

    driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    a= driver.find_element_by_xpath("//div[@id='draggable']")
    b=driver.find_element_by_xpath("//div[@id='droppable']")
    double_click=driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")

    action= ActionChains(driver)
    action.drag_and_drop(a,b).perform()
    time.sleep(5)
    action.double_click(double_click).perform()
    time.sleep(5)

    driver.quit()

