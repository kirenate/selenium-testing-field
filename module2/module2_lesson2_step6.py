from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x:str) -> str:
  return str(math.log(abs(12*math.sin(int(x)))))

#print (calc(921))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x_element= (browser.find_element(By.CSS_SELECTOR, 'span#input_value'))
    x = x_element.text
    res = calc(x)
    
    answer = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer.send_keys(res)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script('return arguments[0].scrollIntoView(true)', robot_checkbox)
    robot_checkbox.click()

    robots_radiobutton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true)', robots_radiobutton)
    robots_radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script('document.querySelector("footer").remove()')
    submit.click()
finally:
    time.sleep(20)
    #browser.quit()