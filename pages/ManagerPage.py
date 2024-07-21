from pages.PageObject import PageObject


class ManagerPage(PageObject):
    url = 'https://demo.testfire.net/index.jsp'

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)
        self.driver.implicitly_wait(5)

    def is_manager_page(self):
        return self.is_url(self.url)

