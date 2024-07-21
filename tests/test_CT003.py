from pages.MainPage import MainPage
from pages.TransferPage import TransferPage


class TestCT003:
    def testtransfersuccessfully(self, open_browser):
        login_p = open_browser
        login_p.fill_username('admin')
        login_p.fill_password('admin')
        login_p.click_to_login()

        main_p = MainPage(login_p.driver)
        assert main_p.is_main_url(), 'Main page not found!'

        transfer_p = TransferPage(login_p.driver)
        transfer_p.go_to_transfer_url()
        assert transfer_p.is_transfer_url(), 'Transfer page not found!'
        transfer_p.select_from_account('800000 Corporate')
        transfer_p.select_to_account('800001 Checking')
        transfer_p.fill_amount_to_transfer('200')
        transfer_p.click_to_transfer()
        transfer_p.successfully_transferred_message_displayed()
