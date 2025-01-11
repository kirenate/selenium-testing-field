from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "label span#input_value")
    x = x_element.text
    res = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, 'div input#answer')
    answer.send_keys(res)
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    robot_radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="Submit"]')
    submit.click()
finally:
    time.sleep(20)
    browser.quit()