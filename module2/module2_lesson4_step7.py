from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math
import pyperclip

def calc(x:str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    book = browser.find_element(By.ID, 'book')
    book.click()

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    browser.execute_script('return arguments[0].scrollIntoView(true)', x_element)
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