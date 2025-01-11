from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import pyperclip

def calc(x:str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    submit1 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit1.click()

    confirm1 = browser.switch_to.alert
    confirm1.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    res = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer.send_keys(res)

    submit2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit2.click()

    confirm2 = browser.switch_to.alert
    temp = confirm2.text.split(': ')
    stepik_answer = temp[1]
    pyperclip.copy(stepik_answer)
    confirm2.accept()
finally:
    time.sleep(5)
    browser.quit()