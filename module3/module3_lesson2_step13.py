import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test_registration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element(By.CSS_SELECTOR, "[required].first")
        input1.send_keys("Firstname")
        input2 = browser.find_element(By.CSS_SELECTOR, "[required].second")
        input2.send_keys("Lastname")
        input3 = browser.find_element(By.CSS_SELECTOR, "[required].third")
        input3.send_keys("email@gmail.com")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        time.sleep(10)
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайтаx
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Something went wrong...")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element(By.CSS_SELECTOR, "[required].first")
        input1.send_keys("Firstname")
        input2 = browser.find_element(By.CSS_SELECTOR, "[required].second")
        input2.send_keys("Lastname")
        input3 = browser.find_element(By.CSS_SELECTOR, "[required].third")
        input3.send_keys("email@gmail.com")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        time.sleep(10)
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайтаx
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Something went wrong...")


if __name__ == "__main__":
    unittest.main()
