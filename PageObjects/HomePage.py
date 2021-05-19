import pytest
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "//form/div[1]/input")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.ID, "exampleInputPassword1")
    checkbox_ice_cream = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit_button = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CSS_SELECTOR, "div[class*='alert-success']")
    gender_female = (By.XPATH, "//option[contains(text(),'Female')]")

    def get_shop(self):
       return self.driver.find_element(*HomePage.shop)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox_ice_cream)

    def get_gender_option(self):
        return self.driver.find_element(*HomePage.gender)

    def get_female(self):
        return self.driver.find_element(*HomePage.gender_female)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit_button)

    def get_message_text(self):
        return self.driver.find_element(*HomePage.success_message).text

