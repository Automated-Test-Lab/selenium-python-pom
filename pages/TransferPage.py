from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class TransferPage(PageObject):
    url = 'https://demo.testfire.net/bank/transfer.jsp'

    def __init__(self, driver):
        super(TransferPage, self).__init__(driver=driver)
        self.driver.implicitly_wait(2)

    def go_to_transfer_url(self):
        self.driver.get(self.url)

    def is_transfer_url(self):
        return self.is_url(self.url)

    def select_from_account(self, from_account):
        self.driver.find_element(By.ID, 'fromAccount').send_keys(from_account)

    def select_to_account(self, to_account):
        self.driver.find_element(By.ID, 'toAccount').send_keys(to_account)

    def fill_amount_to_transfer(self, amount):
        self.driver.find_element(By.ID, 'transferAmount').send_keys(amount)

    def click_to_transfer(self):
        self.driver.find_element(By.ID, 'transfer').click()

    def successfully_transferred_message_displayed(self):
        expected_message = 'was successfully transferred'
        real_message = self.driver.find_element(By.ID, '_ctl0__ctl0_Content_Main_postResp').text
        return expected_message == real_message

    def failed_transferred_message_displayed(self, driver):
        expected_message = 'From Account and To Account fields cannot be the same.'
        alert = Alert(driver)
        real_message = alert.text
        return expected_message == real_message
