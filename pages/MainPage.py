from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class MainPage(PageObject):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver=driver)
        self.driver.implicitly_wait(2)

    def welcome_to_page_message_displayed(self):
        expected_message = 'Welcome to Altoro Mutual Online.'
        real_message = self.driver.find_element(By.CSS_SELECTOR, '[class="fl"]').text
        return expected_message == real_message
