import pytest
import allure


def test_sec():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome(r"C:\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.find_element_by_name("q").send_keys("LinkedIn login")
    driver.find_element_by_name("btnK").click()
    driver.find_element_by_partial_link_text("LinkedIn Login").click()
    driver.find_element_by_id("username").send_keys("nikita")
    driver.find_element_by_id("password").send_keys("p")
    driver.find_element_by_tag_name("button").click()
    print(driver.title)
    print(driver.current_url)
    driver.close()
# assert name in title
