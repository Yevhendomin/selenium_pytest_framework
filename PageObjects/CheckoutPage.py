from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    card_titles = (By.CSS_SELECTOR, ".card-title a")
    cards = (By.XPATH, "//div[@class='card h-100']")
    footer_buttons = (By.CSS_SELECTOR, ".card-footer button")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    button = (By.XPATH, "//button[@class='btn btn-success']")

    def get_cards(self):
        return self.driver.find_elements(*CheckOutPage.cards)

    def get_card_titles(self):
        return self.driver.find_elements(*CheckOutPage.card_titles)

    def get_footer_buttons(self):
        return self.driver.find_elements(*CheckOutPage.footer_buttons)

    def get_checkout_button(self):
        return self.driver.find_element(*CheckOutPage.checkout_button)

    def get_button(self):
        self.driver.find_element(*CheckOutPage.button).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
