from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://demo.testfire.net/login.jsp'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.driver.implicitly_wait(2)

    def open_page(self):
        self.driver.get(self.url)

    def fill_username(self, username):
        self.driver.find_element(By.ID, 'uid').send_keys(username)

    def fill_password(self, password):
        self.driver.find_element(By.ID, 'passw').send_keys(password)

    def click_to_login(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="btnSubmit"]').click()
