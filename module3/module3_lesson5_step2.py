from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

#доделать!!


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

@pytest.fixture(scope=function)
def browser():
    browser = webdriver.Chrome()
    browser.get(link1)
    yield browser
    browser.quit()


class testRegistration():
    
    @pytest.mark.reqfield
    def test_send_first_name(self, browser):
        firstname = browser.find_element(By.CSS_SELECTOR, "[required].first")
        firstname.send_keys("Firstname")

    @pytest.mark.reqfield
    def test_send_last_name(self, browser):
        lastname = browser.find_element(By.CSS_SELECTOR, "[required].second")
        lastname.send_keys("Lastname")

    @pytest.mark.reqfield
    def test_send_email(self, browser):
        email = browser.find_element(By.CSS_SELECTOR, "[required].third")
        email.send_keys("email@gmail.com")

    @pytest.mark.smoke
    def test_submit_button_pressed(self, browser):
        testRegistration.test_send_first_name()
        testRegistration.test_send_last_name()
        testRegistration.test_send_email()
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text, "Something went wrong..."

    @pytest.mark.regression
    def test_submit_button_not_pressed(self, browser):
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text, "Something went wrong..."
