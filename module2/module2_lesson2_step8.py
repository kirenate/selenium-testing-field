from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")


    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    input1.send_keys('firstname')

    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    input2.send_keys('lastname')

    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    input3.send_keys('email@gmail.com')
    
    upload_button = browser.find_element(By.CSS_SELECTOR, 'input#file')
    upload_button.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()
finally:
    time.sleep(20)
    browser.quit()