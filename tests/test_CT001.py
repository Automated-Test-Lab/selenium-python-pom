
class TestCT001:
    def testlogin(self, open_browser):
        login_p = open_browser
        assert login_p.is_login_url(), 'Login page not found!'
