from PageObjects import HomePage
from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from tests.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        first_page = HomePage(self.driver)
        first_page.get_shop().click()
        log.info('Getting all the card titles')
        checkout_page = CheckOutPage(self.driver)
        products = checkout_page.get_card_titles()
        i = 0
        for product in products:
            product_name = product.text
            log.info(product.text)
            if product_name == "Blackberry":
                log.info(i)
                log.info('Getting iteam to list')
                checkout_page.get_footer_buttons()[i].click()

            i += 1
        checkout_page = CheckOutPage(self.driver)
        checkout_page.get_checkout_button().click()
        confirm_page = checkout_page.get_button()
        log.info('Entering country name Ind')
        confirm_page.get_input_form().send_keys('Ind')
        self.verify_link_presence('India')
        confirm_page.get_drop_option().click()
        confirm_page.get_checkbox().click()
        confirm_page.get_submit().click()
        success_text = confirm_page.get_success_message().text
        log.info('Text received from finish message')

        assert "Success! Thank you!" in success_text
        self.driver.get_screenshot_as_file("screen.png")
