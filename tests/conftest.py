import time

import pytest

from pages.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help='Select browser')


@pytest.fixture()
def open_browser(request):
    select_browser = request.config.getoption("--browser_selenium").lower()
    if select_browser not in ['chrome', 'safari', 'firefox']:
        raise Exception('Browser not supported')
    login_p = LoginPage(browser=select_browser)
    login_p.open_page()
    yield login_p
    time.sleep(2)
    login_p.close()


@pytest.fixture()
def run_all_browser(all_browsers):
    login_p = LoginPage(browser=all_browsers)
    login_p.open_page()
    yield login_p
    time.sleep(5)
    login_p.close()


@pytest.fixture()
def login_saucedemo(open_browser):
    login_p = open_browser
    # login_p.enter_login()
    yield login_p
