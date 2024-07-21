from pages.MainPage import MainPage


class TestCT001:
    def testloginsuccessfully(self, open_browser):
        login_p = open_browser
        login_p.fill_username('admin')
        login_p.fill_password('admin')
        login_p.click_to_login()

        main_p = MainPage(login_p.driver)
        main_p.welcome_to_page_message_displayed()
