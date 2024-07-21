from pages.MainPage import MainPage


class TestCT001:
    def testloginfailed(self, open_browser):
        login_p = open_browser
        login_p.fill_username('admin')
        login_p.fill_password('admin333')
        login_p.click_to_login()

        main_p = MainPage(login_p.driver)
        main_p.login_failed_message_displayed()
