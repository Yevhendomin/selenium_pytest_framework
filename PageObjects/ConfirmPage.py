from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    input_form = (By.ID, "country")
    drop_option = (By.LINK_TEXT, 'India')
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")


    def get_input_form(self):
        return self.driver.find_element(*ConfirmPage.input_form)

    def get_drop_option(self):
        return self.driver.find_element(*ConfirmPage.drop_option)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def get_submit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def get_success_message(self):
        return self.driver.find_element(*ConfirmPage.success_message)


