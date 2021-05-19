import pytest

from PageObjects.HomePage import HomePage
from TestData.HomePageTestData import HomePageData
from tests.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form(self, get_data):
        log = self.get_logger()
        log.info('test_home_page is started')
        home_page = HomePage(self.driver)
        log.info('First name is ' + get_data['firstname'])
        home_page.get_name().send_keys(get_data['firstname'])
        log.info('Email is ' + get_data['email'])
        home_page.get_email().send_keys(get_data['email'])
        home_page.get_password().send_keys('Wer436Jm*p]UYT')
        home_page.get_checkbox().click()
        self.select_option_by_text(home_page.get_gender_option(), get_data['gender'])
        home_page.get_submit().click()
        message = home_page.get_message_text()
        assert 'success' in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data_excel('test_data1'))
    def get_data(self, request):
        return request.param
