from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://demo.testfire.net/login.jsp'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.driver.implicitly_wait(2)

    def open_page(self):
        self.driver.get(self.url)
