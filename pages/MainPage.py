from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class MainPage(PageObject):

    url = 'https://demo.testfire.net/bank/main.jsp'

    def __init__(self, driver):
        super(MainPage, self).__init__(driver=driver)
        self.driver.implicitly_wait(2)

    def is_main_url(self):
        return self.is_url(self.url)

    def login_failed_message_displayed(self):
        expected_message = 'Login Failed: We\'re sorry, but this username or password was not found in our system. Please try again.'
        real_message = self.driver.find_element(By.ID, '_ctl0__ctl0_Content_Main_message').text
        return expected_message == real_message
