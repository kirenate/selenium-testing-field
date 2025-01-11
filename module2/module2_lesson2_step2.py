from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

def calc(a:int, b:int) -> int:
  return a+b

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    a = int(browser.find_element(By.CSS_SELECTOR, 'span#num1').text)
    b = int(browser.find_element(By.CSS_SELECTOR, 'span#num2').text)
    res = str(calc(a,b))
    select = Select(browser.find_element(By.CSS_SELECTOR, 'select#dropdown'))
    select.select_by_value(res)

    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()
finally:
    time.sleep(20)
    browser.quit()