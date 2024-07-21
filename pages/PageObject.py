from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageObject:
    class_title_page = 'title'

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
        self.driver.implicitly_wait(2)

    def is_url(self, url):
        WebDriverWait(self.driver, timeout=5).until(expected_conditions.url_to_be(url))
        return self.driver.current_url == url

    def wait_visible_element(self, by, value, timeout):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            return False
        return element.is_displayed()

    def is_title(self, title_text):
        title_element_text = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        return title_element_text == title_text

    def is_page(self, url, title_text):
        return self.is_title(title_text) and self.is_url(url)

    def wait_visible_alert_selected(self, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.alert_is_present())
        except TimeoutException:
            return False
        return element

    def close(self):
        self.driver.quit()
